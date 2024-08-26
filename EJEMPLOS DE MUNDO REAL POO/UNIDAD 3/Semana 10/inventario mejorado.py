import os

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto} | {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio:.2f}"

    def get_id_producto(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio


class Inventario:
    def __init__(self, archivo='inventario.txt'):
        self.archivo = archivo
        self.productos = []
        self.cargar_inventario()

    def cargar_inventario(self):
        """
        Carga el inventario desde el archivo al iniciar el programa.
        Si el archivo no existe, se crea uno nuevo.
        """
        try:
            if os.path.exists(self.archivo):
                with open(self.archivo, 'r') as f:
                    for linea in f:
                        id_producto, nombre, cantidad, precio = linea.strip().split(',')
                        producto = Producto(id_producto, nombre, int(cantidad), float(precio))
                        self.productos.append(producto)
            else:
                with open(self.archivo, 'w') as f:
                    pass  # Crea el archivo si no existe
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error al leer el archivo: {e}")

    def guardar_inventario(self):
        """
        Guarda el inventario en el archivo después de cada modificación.
        """
        try:
            with open(self.archivo, 'w') as f:
                for producto in self.productos:
                    f.write(f"{producto.get_id_producto()},{producto.get_nombre()},{producto.get_cantidad()},{producto.get_precio()}\n")
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error al escribir en el archivo: {e}")

    def agregar_producto(self, producto):
        if any(p.get_id_producto() == producto.get_id_producto() for p in self.productos):
            print("Error: Ya existe un producto con ese ID.")
        else:
            self.productos.append(producto)
            self.guardar_inventario()
            print("Producto añadido exitosamente.")

    def eliminar_producto(self, id_producto):
        producto_encontrado = next((p for p in self.productos if p.get_id_producto() == id_producto), None)
        if producto_encontrado:
            self.productos.remove(producto_encontrado)
            self.guardar_inventario()
            print(f"Producto con ID {id_producto} eliminado.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        producto_encontrado = next((p for p in self.productos if p.get_id_producto() == id_producto), None)
        if producto_encontrado:
            if cantidad is not None:
                producto_encontrado.set_cantidad(cantidad)
            if precio is not None:
                producto_encontrado.set_precio(precio)
            self.guardar_inventario()
            print(f"Producto con ID {id_producto} actualizado.")
        else:
            print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        productos_encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if productos_encontrados:
            for producto in productos_encontrados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos:
                print(producto)


def menu():
    inventario = Inventario()
    while True:
        print("\n1. Agregar Producto\n2. Eliminar Producto\n3. Actualizar Producto\n4. Buscar Producto\n5. Mostrar Inventario\n6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '6':
            break
        elif opcion == '1':
            id_producto = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad: "))
            precio = float(input("Ingrese el precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
        elif opcion == '2':
            id_producto = input("Ingrese el ID del producto que desea eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == '3':
            id_producto = input("Ingrese el ID del producto que desea actualizar: ")
            cantidad = input("Ingrese la nueva cantidad (deje en blanco si no desea cambiarla): ")
            precio = input("Ingrese el nuevo precio (deje en blanco si no desea cambiarlo): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)
        elif opcion == '4':
            nombre = input("Ingrese el nombre del producto que desea buscar: ")
            inventario.buscar_producto(nombre)
        elif opcion == '5':
            inventario.mostrar_inventario()
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
