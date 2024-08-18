class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        """
        Constructor para inicializar un objeto de la clase Producto.
        :param id_producto: ID único del producto.
        :param nombre: Nombre del producto.
        :param cantidad: Cantidad disponible en el inventario.
        :param precio: Precio del producto.
        """
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        """
        Método para representar el producto como una cadena de texto.
        :return: Representación en formato ID | Nombre | Cantidad | Precio.
        """
        return f"ID: {self.id_producto} | {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio:.2f}"

    # Getters y Setters para cada atributo
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
    def __init__(self):
        """
        Constructor para inicializar el inventario como una lista vacía.
        """
        self.productos = []

    def agregar_producto(self, producto):
        """
        Método para agregar un producto al inventario.
        Se asegura de que el ID del producto sea único.
        :param producto: Objeto de la clase Producto a agregar.
        """
        if any(p.get_id_producto() == producto.get_id_producto() for p in self.productos):
            print("Error: Ya existe un producto con ese ID.")
        else:
            self.productos.append(producto)
            print("Producto añadido exitosamente.")

    def eliminar_producto(self, id_producto):
        """
        Método para eliminar un producto del inventario por su ID.
        :param id_producto: ID del producto a eliminar.
        """
        producto_encontrado = next((p for p in self.productos if p.get_id_producto() == id_producto), None)
        if producto_encontrado:
            self.productos.remove(producto_encontrado)
            print(f"Producto con ID {id_producto} eliminado.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """
        Método para actualizar la cantidad y/o precio de un producto por su ID.
        :param id_producto: ID del producto a actualizar.
        :param cantidad: Nueva cantidad (opcional).
        :param precio: Nuevo precio (opcional).
        """
        producto_encontrado = next((p for p in self.productos if p.get_id_producto() == id_producto), None)
        if producto_encontrado:
            if cantidad is not None:
                producto_encontrado.set_cantidad(cantidad)
            if precio is not None:
                producto_encontrado.set_precio(precio)
            print(f"Producto con ID {id_producto} actualizado.")
        else:
            print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        """
        Método para buscar productos por nombre.
        Permite coincidencias parciales, mostrando todos los productos que coinciden.
        :param nombre: Nombre o parte del nombre a buscar.
        """
        productos_encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if productos_encontrados:
            for producto in productos_encontrados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_inventario(self):
        """
        Método para mostrar todos los productos en el inventario.
        """
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos:
                print(producto)


# Interfaz de usuario en la consola
def menu():
    """
    Función principal que muestra un menú interactivo para el usuario.
    Permite agregar, eliminar, actualizar, buscar y mostrar productos.
    """
    inventario = Inventario()
    while True:
        print("\n1. Agregar Producto\n2. Eliminar Producto\n3. Actualizar Producto\n4. Buscar Producto\n5. Mostrar Inventario\n6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '6':
            break  # Sale del ciclo y termina el programa
        elif opcion == '1':
            # Solicita datos al usuario para crear un nuevo producto
            id_producto = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad: "))
            precio = float(input("Ingrese el precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
        elif opcion == '2':
            # Solicita el ID del producto a eliminar
            id_producto = input("Ingrese el ID del producto que desea eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == '3':
            # Solicita el ID del producto a actualizar y permite actualizar cantidad y/o precio
            id_producto = input("Ingrese el ID del producto que desea actualizar: ")
            cantidad = input("Ingrese la nueva cantidad (deje en blanco si no desea cambiarla): ")
            precio = input("Ingrese el nuevo precio (deje en blanco si no desea cambiarlo): ")

            # Convierte las entradas a los tipos adecuados si no están en blanco
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None

            inventario.actualizar_producto(id_producto, cantidad, precio)
        elif opcion == '4':
            # Solicita el nombre o parte del nombre para buscar productos
            nombre = input("Ingrese el nombre del producto que desea buscar: ")
            inventario.buscar_producto(nombre)
        elif opcion == '5':
            # Muestra todos los productos en el inventario
            inventario.mostrar_inventario()
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()


