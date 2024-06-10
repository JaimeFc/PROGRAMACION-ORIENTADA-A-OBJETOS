class Bird:
    def fly(self):
        return "Bird is flying"

class Airplane:
    def fly(self):
        return "Airplane is flying"

# Uso del polimorfismo
def make_it_fly(flying_object):
    print(flying_object.fly())

# Diferentes objetos que comparten una interfaz común
bird = Bird()
airplane = Airplane()

make_it_fly(bird)
make_it_fly(airplane)
