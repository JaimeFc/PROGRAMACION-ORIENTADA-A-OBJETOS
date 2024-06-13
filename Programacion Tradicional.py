# Función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []  # Lista para almacenar las temperaturas diarias
    for i in range(7):  # Iterar sobre los 7 días de la semana
        temp = float(input(f"Ingresa la temperatura del día {i+1}: "))  # Solicitar la temperatura del día
        temperaturas.append(temp)  # Agregar la temperatura a la lista
    return temperaturas  # Retornar la lista de temperaturas

# Función para calcular el promedio de las temperaturas
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)  # Calcular y retornar el promedio

# Función principal que coordina el ingreso de datos y el cálculo del promedio
def main():
    temperaturas = ingresar_temperaturas()  # Llamar a la función para ingresar las temperaturas
    promedio = calcular_promedio(temperaturas)  # Llamar a la función para calcular el promedio
    print(f"El promedio semanal de la temperatura es: {promedio:.2f}")  # Mostrar el promedio

# Verificar si el script se está ejecutando directamente
if __name__ == "__main__":
    main()  # Llamar a la función principal
