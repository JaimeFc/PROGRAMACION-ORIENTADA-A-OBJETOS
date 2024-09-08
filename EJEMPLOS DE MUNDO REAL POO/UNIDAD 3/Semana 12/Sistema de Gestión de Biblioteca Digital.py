import pickle

# Clase Libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn
        self.datos_inmutables = (self.titulo, self.autor)

    def __str__(self):
        return f"'{self.titulo}' de {self.autor} (ISBN: {self.isbn}, Categoría: {self.categoria})"

# Clase Usuario
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        self.libros_prestados.remove(libro)

    def listar_libros_prestados(self):
        if self.libros_prestados:
            print(f"Libros prestados por {self.nombre}:")
            for libro in self.libros_prestados:
                print(f" - {libro}")
        else:
            print(f"{self.nombre} no tiene libros prestados.")

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}"

# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}
        self.usuarios_registrados = set()
        self.usuarios = {}

    # Función para guardar datos en un archivo binario
    def guardar_datos(self, archivo):
        with open(archivo, 'wb') as f:
            pickle.dump(self, f)
        print(f"Datos guardados en {archivo}.")

    # Función para cargar datos desde un archivo binario
    @staticmethod
    def cargar_datos(archivo):
        try:
            with open(archivo, 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            print("No se encontró un archivo de datos, iniciando biblioteca vacía.")
            return Biblioteca()

    def anadir_libro(self, libro):
        if libro.isbn not in self.libros_disponibles:
            self.libros_disponibles[libro.isbn] = libro
            print(f"Libro '{libro.titulo}' añadido correctamente.")
        else:
            print("El libro ya está en la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            libro = self.libros_disponibles.pop(isbn)
            print(f"Libro '{libro.titulo}' eliminado correctamente.")
        else:
            print("El libro no se encuentra en la biblioteca.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.usuarios_registrados:
            self.usuarios_registrados.add(usuario.id_usuario)
            self.usuarios[usuario.id_usuario] = usuario
            print(f"Usuario {usuario.nombre} registrado correctamente.")
        else:
            print("El usuario ya está registrado.")

    def dar_de_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios_registrados:
            usuario = self.usuarios.pop(id_usuario)
            self.usuarios_registrados.remove(id_usuario)
            print(f"Usuario {usuario.nombre} dado de baja correctamente.")
        else:
            print("El usuario no está registrado.")

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios_registrados and isbn in self.libros_disponibles:
            usuario = self.usuarios[id_usuario]
            libro = self.libros_disponibles.pop(isbn)
            usuario.prestar_libro(libro)
            print(f"Libro '{libro.titulo}' prestado a {usuario.nombre}.")
        else:
            print("Préstamo no disponible. Verifica si el usuario o el libro existen.")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios_registrados:
            usuario = self.usuarios[id_usuario]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.devolver_libro(libro)
                    self.libros_disponibles[isbn] = libro
                    print(f"Libro '{libro.titulo}' devuelto por {usuario.nombre}.")
                    return
            print("El usuario no tiene este libro prestado.")
        else:
            print("El usuario no está registrado.")

    def buscar_libro(self, criterio):
        resultados = []
        for libro in self.libros_disponibles.values():
            if criterio.lower() in libro.titulo.lower() or criterio.lower() in libro.autor.lower() or criterio.lower() in libro.categoria.lower():
                resultados.append(libro)
        if resultados:
            print("Resultados de la búsqueda:")
            for libro in resultados:
                print(libro)
        else:
            print("No se encontraron libros con ese criterio.")

    def listar_libros_prestados_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            usuario.listar_libros_prestados()
        else:
            print("El usuario no está registrado.")

# Menú interactivo
def menu():
    archivo_datos = 'biblioteca_digital.dat'
    biblioteca = Biblioteca.cargar_datos(archivo_datos)

    while True:
        print("\n--- Menú de Biblioteca Digital ---")
        print("1. Añadir libro")
        print("2. Eliminar libro")
        print("3. Registrar usuario")
        print("4. Dar de baja usuario")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Buscar libro")
        print("8. Listar libros prestados de un usuario")
        print("9. Guardar y salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            titulo = input("Título del libro: ")
            autor = input("Autor del libro: ")
            categoria = input("Categoría del libro: ")
            isbn = input("ISBN del libro: ")
            libro = Libro(titulo, autor, categoria, isbn)
            biblioteca.anadir_libro(libro)

        elif opcion == "2":
            isbn = input("ISBN del libro a eliminar: ")
            biblioteca.quitar_libro(isbn)

        elif opcion == "3":
            nombre = input("Nombre del usuario: ")
            id_usuario = input("ID del usuario: ")
            usuario = Usuario(nombre, id_usuario)
            biblioteca.registrar_usuario(usuario)

        elif opcion == "4":
            id_usuario = input("ID del usuario a dar de baja: ")
            biblioteca.dar_de_baja_usuario(id_usuario)

        elif opcion == "5":
            id_usuario = input("ID del usuario que pide el préstamo: ")
            isbn = input("ISBN del libro a prestar: ")
            biblioteca.prestar_libro(id_usuario, isbn)

        elif opcion == "6":
            id_usuario = input("ID del usuario que devuelve el libro: ")
            isbn = input("ISBN del libro a devolver: ")
            biblioteca.devolver_libro(id_usuario, isbn)

        elif opcion == "7":
            criterio = input("Introduce título, autor o categoría para buscar: ")
            biblioteca.buscar_libro(criterio)

        elif opcion == "8":
            id_usuario = input("ID del usuario: ")
            biblioteca.listar_libros_prestados_usuario(id_usuario)

        elif opcion == "9":
            biblioteca.guardar_datos(archivo_datos)
            print("Datos guardados. Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()


