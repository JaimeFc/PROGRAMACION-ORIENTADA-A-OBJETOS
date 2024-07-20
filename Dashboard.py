import os # Importa el módulo os para interactuar con el sistema operativo

def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        # Verifica si el archivo existe en la ruta absoluta
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            # Imprime el contenido del archivo
            print(archivo.read())
    except FileNotFoundError:
        # Mensaje si el archivo no se encuentra
        print("El archivo no se encontró.")
    except Exception as e:
        # Mensaje para cualquier otro error
        print(f"Ocurrió un error al leer el archivo: {e}")

def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)
    # Diccionario con las opciones del menú y las rutas relativas de los scripts
    opciones = {
        '1': 'Unidad 1/Semana 2/EJEMPLO DE ABSTRACCION.py',
        '2': 'Unidad 1/Semana 2/EJEMPLO DE ENCAPSULACION.py',
        '3': 'Unidad 1/Semana 2/EJEMPLO DE HERENCIA.py',
        '4': 'Unidad 1/Semana 2/EJEMPLO DE POLIMORFISMO.py',
        '5': 'Unidad 1/Semana 3/Programacion Tradicional.py',
        '6': 'Unidad 1/Semana 4/Sistema de reserva modificado con vista de numero de habitacion.py',
        '7': 'Unidad 2/Semana 5/PROGRAMA PARA CALCULAR AREA DE UN TRIANGULO.py',
        '8': 'Unidad 2/Semana 6/SemClase Objetos clases Herencia Encapsulamiento Polimorfismo.py',
        '9': 'Unidad 2/Semana 7/Constructores y Destructores.py',
        # Agrega aquí el resto de las rutas de los scripts
    }
    # Bucle infinito para mostrar el menú hasta que el usuario elija salir
    while True:
        print("\nMenu Principal - Dashboard")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            print(f"Ruta del archivo: {ruta_script}")  # Imprime la ruta para depuración
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

# Ejecutar el menú principal si este script se ejecuta directamente
if __name__ == "__main__":
    mostrar_menu()
