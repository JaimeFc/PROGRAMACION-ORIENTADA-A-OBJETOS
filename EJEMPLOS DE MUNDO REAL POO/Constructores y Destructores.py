class Moto:
    # El método __unit__ es el constructor de la clase
    def __init__(self ,marca, modelo):
        self.marca = marca # Inicia el atributo marca
        self.modelo = modelo # Inicia el atributo modelo
        print(f"Moto {self.marca}{self.modelo} ha sido creada") # Mensaje que indica
        # que el Objeto a sido creado

        # el método __del__ es el destructor de la clase. Se llama automaticamente
        #cuando el objeto esta a punto de ser destruido (cuando se libera la memoria).
    def __del__(self):
        print(f"Moto {self.marca}{self.modelo} ha sido destruida") # Mensaje que indica que el objeto
        # esta siendo destruido

mi_moto = Moto("Honda", "CB190R") # Elimina el metodo explicitamente
# esto activa el metodo __del__, mostrando el mensaje de destrucción.

del mi_moto












