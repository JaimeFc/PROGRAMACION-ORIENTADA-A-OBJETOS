# Definición de la clase base
class Animal:
    def __init__(self, nombre, edad):
        self._nombre = nombre  # Atributo encapsulado
        self._edad = edad      # Atributo encapsulado

    def hacer_sonido(self):
        return "Sonido genérico de animal"

# Definición de la clase derivada
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self._raza = raza  # Atributo encapsulado

    # Método sobrescrito (Polimorfismo)
    def hacer_sonido(self):
        return "Ladrido"

    # Método específico de Perro
    def mostrar_info(self):
        return f"Nombre: {self._nombre}, Edad: {self._edad}, Raza: {self._raza}"

# Definición de otra clase derivada
class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self._color = color  # Atributo encapsulado

    # Método sobrescrito (Polimorfismo)
    def hacer_sonido(self):
        return "Maullido"

    # Método específico de Gato
    def mostrar_info(self):
        return f"Nombre: {self._nombre}, Edad: {self._edad}, Color: {self._color}"

# Crear instancias y demostrar la funcionalidad
def main():
    # Crear una instancia de Perro
    perro1 = Perro("Firulais", 5, "Labrador")
    print(perro1.mostrar_info())
    print(perro1.hacer_sonido())

    # Crear una instancia de Gato
    gato1 = Gato("Misu", 3, "Blanco")
    print(gato1.mostrar_info())
    print(gato1.hacer_sonido())

    # Demostrar polimorfismo con una lista de animales
    animales = [perro1, gato1]
    for animal in animales:
        print(f"{animal._nombre} hace: {animal.hacer_sonido()}")

if __name__ == "__main__":
    main()
