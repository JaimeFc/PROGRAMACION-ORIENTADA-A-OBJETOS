import tkinter as tk
from tkinter import messagebox, ttk


class TaskApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("600x600")
        self.root.configure(background="silver")

        # Campo de entrada
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        # Botón para añadir tarea
        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(pady=5)

        # Lista de tareas (TreeView)
        self.tasks = ttk.Treeview(root, columns=('Tarea', 'Estado'), show='headings')
        self.tasks.heading('Tarea', text='Descripción')
        self.tasks.heading('Estado', text='Estado')
        self.tasks.pack(fill=tk.BOTH, expand=True, pady=10)

        # Configurar el evento de doble clic en una tarea
        self.tasks.bind('<Double-1>', self.toggle_task_completion)

        # Botones para marcar como completada, desmarcar y eliminar tarea
        self.complete_button = tk.Button(root, text="Marcar como Completada",
                                         command=lambda: self.toggle_task_completion(complete=True))
        self.complete_button.pack(side=tk.LEFT, padx=(20, 0), pady=5)

        self.uncomplete_button = tk.Button(root, text="Desmarcar Tarea",
                                           command=lambda: self.toggle_task_completion(complete=False))
        self.uncomplete_button.pack(side=tk.LEFT, padx=(10, 20), pady=5)

        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(side=tk.RIGHT, padx=(0, 20), pady=5)

        # Evento para añadir tarea con Enter
        self.task_entry.bind('<Return>', lambda event: self.add_task())

        # Evento para cerrar la aplicación con Escape
        self.root.bind('<Escape>', lambda event: self.root.destroy())

    def add_task(self):
        """Añadir una nueva tarea a la lista."""
        task = self.task_entry.get()
        if task:
            # Añadir tarea con el estado 'Pendiente'
            self.tasks.insert('', tk.END, values=(task, 'Pendiente'))
            self.task_entry.delete(0, tk.END)  # Limpiar el campo de entrada
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingresa una tarea.")

    def toggle_task_completion(self, event=None, complete=True):
        """Marcar o desmarcar una tarea como completada."""
        selected_item = self.tasks.selection()
        if selected_item:
            # Obtener los valores de la tarea seleccionada
            task_desc = self.tasks.item(selected_item, 'values')[0]
            if complete:
                # Cambiar el estado a 'Tarea realizada' y el color de fondo
                self.tasks.item(selected_item, values=(task_desc, 'Tarea realizada'), tags=('completed',))
                self.tasks.tag_configure('completed', background='light green')
            else:
                # Cambiar el estado a 'Pendiente' y restaurar el color de fondo
                self.tasks.item(selected_item, values=(task_desc, 'Pendiente'), tags=('uncompleted',))
                self.tasks.tag_configure('uncompleted', background='white')
        else:
            messagebox.showinfo("Información", "Selecciona una tarea para cambiar su estado.")

    def delete_task(self):
        """Eliminar la tarea seleccionada."""
        selected_item = self.tasks.selection()
        if selected_item:
            self.tasks.delete(selected_item)
        else:
            messagebox.showinfo("Información", "Selecciona una tarea para eliminar.")


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskApp(root)
    root.mainloop()
