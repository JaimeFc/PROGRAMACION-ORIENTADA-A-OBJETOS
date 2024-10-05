import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
root = tk.Tk()
root.title("Gestión de Tareas")
root.geometry("400x400")

# Campo de entrada para nuevas tareas
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Lista de tareas
task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50, height=15)
task_listbox.pack(pady=10)

# Botones de acción
add_button = tk.Button(root, text="Añadir Tarea", command=lambda: add_task())
add_button.pack(pady=5)

complete_button = tk.Button(root, text="Marcar como Completada", command=lambda: mark_completed())
complete_button.pack(pady=5)

delete_button = tk.Button(root, text="Eliminar Tarea", command=lambda: delete_task())
delete_button.pack(pady=5)

# Funciones para la gestión de tareas
def add_task():
    task = entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada vacía", "Por favor ingresa una tarea.")

def mark_completed():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task = task_listbox.get(selected_task_index)
        task_listbox.delete(selected_task_index)
        completed_task = f"[Completada] {task}"
        task_listbox.insert(tk.END, completed_task)
        task_listbox.itemconfig(tk.END, {'fg': 'green'})  # Cambia el color a verde
    else:
        messagebox.showwarning("Selección vacía", "Por favor selecciona una tarea.")

def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Selección vacía", "Por favor selecciona una tarea.")

# Iniciar el bucle principal de la aplicación
root.mainloop()

