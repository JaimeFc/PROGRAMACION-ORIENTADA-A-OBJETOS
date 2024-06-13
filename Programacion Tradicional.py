def ingresar_temperaturas():
    temperaturas = []
    for i in range(7):
        temp = float(input(f"Ingresa la temperatura del día {i+1}: "))
        temperaturas.append(temp)
    return temperaturas

def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

def main():
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"El promedio semanal de la temperatura es: {promedio:.2f}")

if __name__ == "__main__":
    main()
