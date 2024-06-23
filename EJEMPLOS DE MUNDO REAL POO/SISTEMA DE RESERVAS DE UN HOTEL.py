# Definición de la clase Cliente
class Cliente:
    def __init__(self, nombre, correo):
        self.nombre = nombre  # Atributo nombre
        self.correo = correo  # Atributo correo

    def __str__(self):
        return f"Cliente: {self.nombre}, Correo: {self.correo}"

# Definición de la clase Habitación
class Habitación:
    def __init__(self, número, tipo, precio):
        self.número = número  # Atributo número de habitación
        self.tipo = tipo  # Atributo tipo de habitación (simple, doble, suite)
        self.precio = precio  # Atributo precio por noche

    def __str__(self):
        return f"Habitación {self.número}, Tipo: {self.tipo}, Precio: ${self.precio} por noche"

# Definición de la clase Reserva
class Reserva:
    def __init__(self, cliente, habitación, días):
        self.cliente = cliente  # Atributo cliente que realiza la reserva
        self.habitación = habitación  # Atributo habitación reservada
        self.días = días  # Atributo número de días de la reserva

    def costo_total(self):
        return self.días * self.habitación.precio  # Método para calcular el costo total de la reserva

    def __str__(self):
        return (f"Reserva de {self.cliente.nombre} en la habitación {self.habitación.número} "
                f"por {self.días} días. Costo total: ${self.costo_total()}")

# Definición de la clase Hotel
class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre  # Atributo nombre del hotel
        self.habitaciones = []  # Atributo lista de habitaciones
        self.reservas = []  # Atributo lista de reservas

    def agregar_habitación(self, habitación):
        self.habitaciones.append(habitación)  # Método para agregar una habitación al hotel

    def realizar_reserva(self, cliente, número_habitación, días):
        # Buscar la habitación por número
        habitación = next((hab for hab in self.habitaciones if hab.número == número_habitación), None)
        if habitación:
            reserva = Reserva(cliente, habitación, días)  # Crear una nueva reserva
            self.reservas.append(reserva)  # Agregar la reserva a la lista de reservas
            return reserva
        else:
            return None

    def __str__(self):
        return f"Hotel: {self.nombre}"

# Ejemplo de uso del sistema
# Crear un hotel
hotel = Hotel("Gran Hotel")

# Crear algunas habitaciones
hab1 = Habitación(101, "simple", 50)
hab2 = Habitación(102, "doble", 80)
hab3 = Habitación(201, "suite", 150)

# Agregar habitaciones al hotel
hotel.agregar_habitación(hab1)
hotel.agregar_habitación(hab2)
hotel.agregar_habitación(hab3)

# Solicitar datos del cliente y reserva
nombre_cliente = input("Ingrese el nombre del cliente: ")
correo_cliente = input("Ingrese el correo del cliente: ")
número_habitación = int(input("Ingrese el número de habitación: "))
días = int(input("Ingrese el número de días de la reserva: "))

# Crear un cliente
cliente = Cliente(nombre_cliente, correo_cliente)

# Realizar una reserva
reserva = hotel.realizar_reserva(cliente, número_habitación, días)

# Imprimir detalles de la reserva
if reserva:
    print(reserva)
else:
    print("Habitación no disponible")

# Comentar la salida
# La salida variará según los datos ingresados por el usuario

