class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def obtener_id(self):
        return self.id_producto

    def obtener_nombre(self):
        return self.nombre

    def establecer_cantidad(self, cantidad):
        self.cantidad = cantidad

    def obtener_cantidad(self):
        return self.cantidad

    def establecer_precio(self, precio):
        self.precio = precio

    def obtener_precio(self):
        return self.precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"
import json

class Inventario:
    def __init__(self):
        self.productos = {}

    def añadir_producto(self, producto):
        self.productos[producto.obtener_id()] = producto

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print(f"Producto {id_producto} eliminado.")
        else:
            print(f"Producto con ID {id_producto} no encontrado.")

    def actualizar_cantidad(self, id_producto, cantidad):
        if id_producto in self.productos:
            self.productos[id_producto].establecer_cantidad(cantidad)
            print(f"Cantidad del producto {id_producto} actualizada a {cantidad}.")
        else:
            print(f"Producto con ID {id_producto} no encontrado.")

    def actualizar_precio(self, id_producto, precio):
        if id_producto in self.productos:
            self.productos[id_producto].establecer_precio(precio)
            print(f"Precio del producto {id_producto} actualizado a ${precio:.2f}.")
        else:
            print(f"Producto con ID {id_producto} no encontrado.")

    def buscar_producto(self, nombre):
        resultados = [producto for producto in self.productos.values() if producto.obtener_nombre() == nombre]
        if resultados:
            for producto in resultados:
                print(producto)
        else:
            print(f"No se encontraron productos con el nombre '{nombre}'.")

    def mostrar_productos(self):
        if self.productos:
            for producto in self.productos.values():
                print(producto)
        else:
            print("El inventario está vacío.")

    def guardar_en_archivo(self, filename):
        with open(filename, 'w') as file:
            json.dump({id: vars(prod) for id, prod in self.productos.items()}, file)
        print(f"Inventario guardado en {filename}.")

    def cargar_desde_archivo(self, filename):
        try:
            with open(filename, 'r') as file:
                productos = json.load(file)
                self.productos = {id: Producto(**prod) for id, prod in productos.items()}
            print(f"Inventario cargado desde {filename}.")
        except FileNotFoundError:
            print(f"El archivo {filename} no se encontró.")
def menu():
    inventario = Inventario()

    while True:
        print("\n--- Sistema de Gestión de Inventario ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar cantidad")
        print("4. Actualizar precio")
        print("5. Buscar producto por nombre")
        print("6. Mostrar todos los productos")
        print("7. Guardar inventario en archivo")
        print("8. Cargar inventario desde archivo")
        print("9. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)
        elif opcion == "2":
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == "3":
            id_producto = input("Ingrese el ID del producto para actualizar cantidad: ")
            cantidad = int(input("Ingrese la nueva cantidad: "))
            inventario.actualizar_cantidad(id_producto, cantidad)
        elif opcion == "4":
            id_producto = input("Ingrese el ID del producto para actualizar precio: ")
            precio = float(input("Ingrese el nuevo precio: "))
            inventario.actualizar_precio(id_producto, precio)
        elif opcion == "5":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)
        elif opcion == "6":
            inventario.mostrar_productos()
        elif opcion == "7":
            filename = input("Ingrese el nombre del archivo para guardar el inventario: ")
            inventario.guardar_en_archivo(filename)
        elif opcion == "8":
            filename = input("Ingrese el nombre del archivo para cargar el inventario: ")
            inventario.cargar_desde_archivo(filename)
        elif opcion == "9":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    menu()
