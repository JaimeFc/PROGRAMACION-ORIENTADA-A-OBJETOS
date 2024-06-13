# Clase que representa el clima diario
class ClimaDiario:
    def __init__(self):
        self.temperaturas = []  # Inicializar una lista para almacenar las temperaturas diarias

    # Método para ingresar las temperaturas diarias
    def ingresar_temperaturas(self):
        for i in range(7):  # Iterar sobre los 7 días de la semana
            temp = float(input(f"Ingresa la temperatura del día {i+1}: "))  # Solicitar la temperatura del día
            self.temperaturas.append(temp)  # Agregar la temperatura a la lista de la instancia

    # Método para calcular el promedio de las temperaturas
    def calcular_promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)  # Calcular y retornar el promedio

# Función principal que coordina el ingreso de datos y el cálculo del promedio
def main():
    clima = ClimaDiario()  # Crear una instancia de ClimaDiario
    clima.ingresar_temperaturas()  # Llamar al método para ingresar las temperaturas
    promedio = clima.calcular_promedio()  # Llamar al método para calcular el promedio
    print(f"El promedio semanal de la temperatura es: {promedio:.2f}")  # Mostrar el promedio

# Verificar si el script se está ejecutando directamente
if __name__ == "__main__":
    main()  # Llamar a la función principal

