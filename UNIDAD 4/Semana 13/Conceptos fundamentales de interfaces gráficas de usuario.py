import tkinter as tk

app = tk.Tk()
app.title("Software para calcular el IVA %")
app.geometry("500x500")
app.configure(bg="gray")


def calcular_resultado():
    try:
        # Obtiene el valor del campo de entrada y realiza un cálculo
        numero = float(entrada.get())
        porcentaje = 12
        resultado = numero * porcentaje / 100
        # Muestra el resultado en el área de texto
        area_texto.insert(tk.END, f"El 12% de {numero} es {resultado}\n")
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce un número válido.")

# Función para limpiar el área de texto
def limpiar_resultado():
    area_texto.delete(1.0, tk.END)

from tkinter import messagebox

# Crear un título
titulo = tk.Label(app, text="Calcula el IVA del 12% de un numero")
titulo.pack(pady=30)
titulo.config(bg=("yellow"))


# Crear una etiqueta
etiqueta = tk.Label(app, text="Introduce un número:")
etiqueta.pack()
etiqueta.config(bg="yellow")

# Crear un campo de entrada
entrada = tk.Entry(app)
entrada.pack()

# Crear un botón para calcular el resultado
boton_calcular = tk.Button(app, text="Calcular", command=calcular_resultado)
boton_calcular.pack(pady=5)
boton_calcular.config(bg="lightgreen")

# Crear un botón para limpiar el resultado
boton_limpiar = tk.Button(app, text="Limpiar", command=limpiar_resultado)
boton_limpiar.pack(pady=5)
boton_limpiar.config(bg="red")

# Crear un área de texto para mostrar el resultado
area_texto = tk.Text(app, height=10, width=50)
area_texto.pack()

# Ejecutar el bucle de eventos
app.mainloop()






