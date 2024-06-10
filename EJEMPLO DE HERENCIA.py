class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        return f"{self.brand} {self.model} is starting."

class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

    def start(self):
        return f"{self.brand} {self.model} with {self.doors} doors is starting."

# Uso de la herencia
car = Car("Toyota", "Corolla", 4)
print(car.start())
