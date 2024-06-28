# Programa para gestionar un registro de estudiantes
# Funcionalidad: Permite añadir estudiantes, mostrar la lista de estudiantes y buscar estudiantes por nombre.
# Utiliza diferentes tipos de datos como integer, float, string y boolean.

def mostrar_menu():
    """Muestra el menú principal con las opciones disponibles."""
    print(" Presiona 1. Añadir estudiante")
    print(" Presiona 2. Mostrar todos los estudiantes")
    print(" Presiona 3. Buscar estudiante por nombre")
    print(" Presiona 4. Salir")

def añadir_estudiante(registro):
    """Añade un nuevo estudiante al registro."""
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = int(input("Ingrese la edad del estudiante: "))
    nota_final = float(input("Ingrese la nota final del estudiante: "))
    # Se crea un diccionario con la información del estudiante
    estudiante = {
        "nombre": nombre,
        "edad": edad,
        "nota_final": nota_final,
        "aprobado": nota_final >= 7.0  # Calcula si el estudiante ha aprobado
    }
    registro.append(estudiante)  # Añade el diccionario al registro
    print("Estudiante añadido exitosamente.")

def mostrar_estudiantes(registro):
    """Muestra todos los estudiantes en el registro."""
    if not registro:
        print("No hay estudiantes en el registro.")
    else:
        for idx, estudiante in enumerate(registro, start=1):
            print(f"Estudiante {idx}:")
            print(f"  Nombre: {estudiante['nombre']}")
            print(f"  Edad: {estudiante['edad']}")
            print(f"  Nota Final: {estudiante['nota_final']}")
            print(f"  Aprobado: {'Sí' if estudiante['aprobado'] else 'No'}")

def buscar_estudiante(registro, nombre_buscar):
    """Busca un estudiante por nombre en el registro."""
    encontrado = False
    for estudiante in registro:
        if estudiante['nombre'].lower() == nombre_buscar.lower():  # Compara los nombres en minúsculas
            print("Estudiante encontrado:")
            print(f"  Nombre: {estudiante['nombre']}")
            print(f"  Edad: {estudiante['edad']}")
            print(f"  Nota Final: {estudiante['nota_final']}")
            print(f"  Aprobado: {'Sí' if estudiante['aprobado'] else 'No'}")
            encontrado = True
            break
    if not encontrado:
        print("Estudiante no encontrado.")

def main():
    """Función principal que gestiona el flujo del programa."""
    registro = []  # Lista que almacena los estudiantes
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            añadir_estudiante(registro)
        elif opcion == '2':
            mostrar_estudiantes(registro)
        elif opcion == '3':
            nombre_buscar = input("Ingrese el nombre del estudiante a buscar: ")
            buscar_estudiante(registro, nombre_buscar)
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
