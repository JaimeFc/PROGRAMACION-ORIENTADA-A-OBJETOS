# Programa para calcular el área de un triángulo
# Este programa solicita al usuario que ingrese la base y la altura de un triángulo
# y calcula el área del mismo utilizando la fórmula: (base * altura) / 2

print("CALCULA EL AREA DE UN  TRIANGULO")

def calcular_area_triangulo(base: float, altura: float) -> float:
    """
    Calcula el área de un triángulo dado su base y altura.

    :para base: Base del triángulo.
    :para altura: Altura del triángulo.
    :return: Área del triángulo.
    """
    area = (base * altura) / 2
    return area


def main():
    # Solicitar la base del triángulo al usuario
    base = float(input("Ingrese la base del triángulo en unidades: "))

    # Solicitar la altura del triángulo al usuario
    altura = float(input("Ingrese la altura del triángulo en unidades: "))

    # Calcular el área del triángulo
    area = calcular_area_triangulo(base, altura)

    # Mostrar el resultado al usuario
    print(f"El área del triángulo con base {base} unidades y altura {altura} unidades es {area} unidades cuadradas.")

# Verificar si el script se está ejecutando como el programa principal
if __name__ == "__main__":
    main()
