import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry


class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AGENDA PERSONAL")
        self.root.geometry("700x600")
        self.root.configure(background="silver")

        # Variable para rastrear el evento que se está editando
        self.editing_event = None

        # Inicializa el frame donde se pondrá el contenido
        self.entry_frame = tk.Frame(self.root)
        self.entry_frame.grid(column=0, row=0, padx=10, pady=20)

        # Campo de entrada de Fecha
        self.date_label = tk.Label(self.entry_frame, text="Fecha del Evento")
        self.date_label.grid(column=0, row=1, padx=10, pady=10, sticky='e')  # Alinear a la derecha
        self.date_entry = DateEntry(self.entry_frame, width=20, background='darkblue',
                                    foreground='white', borderwidth=2, date_pattern='y-mm-dd')
        self.date_entry.grid(column=1, row=1, padx=10, pady=10, sticky='w')  # Alinear a la izquierda

        # Campo de entrada de Descripción
        self.description_label = tk.Label(self.entry_frame, text="Descripción del Evento")
        self.description_label.grid(column=0, row=0, padx=10, pady=10, sticky='e')  # Alinear a la derecha
        self.description_entry = ttk.Entry(self.entry_frame, width=40)
        self.description_entry.grid(column=1, row=0, padx=10, pady=10, sticky='w')  # Alinear a la izquierda

        # Campo de entrada de Hora
        self.time_label = tk.Label(self.entry_frame, text="Hora del Evento")
        self.time_label.grid(column=0, row=2, padx=10, pady=10, sticky='e')  # Alinear a la derecha
        self.time_entry = ttk.Entry(self.entry_frame, width=20)
        self.time_entry.grid(column=1, row=2, padx=10, pady=10, sticky='w')  # Alinear a la izquierda

        # Botones para agregar, eliminar, editar y guardar cambios de eventos
        self.add_button = ttk.Button(self.entry_frame, text="Agregar Evento", command=self.add_event)
        self.add_button.grid(column=0, row=3, padx=10, pady=10, sticky='w')

        self.delete_button = ttk.Button(self.entry_frame, text="Eliminar Evento Seleccionado",
                                        command=self.delete_event)
        self.delete_button.grid(column=2, row=3, padx=10, pady=10, sticky='w')

        self.quit_button = ttk.Button(self.entry_frame, text="Salir", command=self.root.quit)
        self.quit_button.grid(column=3, row=3, padx=10, pady=10, sticky='w')

        self.editar_button = ttk.Button(self.entry_frame, text="Editar Evento Seleccionado", command=self.editar_evento)
        self.editar_button.grid(column=1, row=3, padx=10, pady=10, sticky='w')

        self.save_button = ttk.Button(self.entry_frame, text="Guardar Cambios", command=self.guardar_cambios_evento,
                                      state='disabled')
        self.save_button.grid(column=1, row=4, padx=10, pady=10, sticky='w')

        # Frame para mostrar los eventos en una lista
        self.tree_frame = tk.Frame(self.root)
        self.tree_frame.grid(column=0, row=1, padx=10, pady=20)

        # TreeView para mostrar los eventos
        self.tree = ttk.Treeview(self.tree_frame, columns=("Fecha", "Hora", "Descripción"), show='headings', height=10)
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.column("Fecha", width=100)
        self.tree.column("Hora", width=100)
        self.tree.column("Descripción", width=300)
        self.tree.grid(column=0, row=0, padx=10, pady=10)

        # Barra de desplazamiento para el TreeView
        self.scrollbar = ttk.Scrollbar(self.tree_frame, orient="vertical", command=self.tree.yview)
        self.scrollbar.grid(column=1, row=0, sticky='ns')
        self.tree.configure(yscrollcommand=self.scrollbar.set)

        # Lista para almacenar los eventos
        self.events = []

    def add_event(self):
        """Agregar un nuevo evento a la lista."""
        date = self.date_entry.get()
        time = self.time_entry.get()
        description = self.description_entry.get()

        if date and time and description:
            # Agregar el evento a la lista de eventos y al TreeView
            self.events.append((date, time, description))
            self.tree.insert("", "end", values=(date, time, description))

            # Limpiar los campos de entrada
            self.clear_entries()
        else:
            messagebox.showwarning("Campos incompletos", "Por favor complete todos los campos para agregar el evento.")

    def delete_event(self):
        """Eliminar el evento seleccionado de la lista."""
        selected_item = self.tree.selection()
        if selected_item:
            confirm = messagebox.askyesno("Confirmación", "¿Está seguro de que desea eliminar el evento seleccionado?")
            if confirm:
                # Obtener el índice del elemento seleccionado en el TreeView
                index = self.tree.index(selected_item)

                # Eliminar el evento de la lista y el TreeView usando el índice
                del self.events[index]
                self.tree.delete(selected_item)
        else:
            messagebox.showwarning("No seleccionado", "Por favor seleccione un evento para eliminar.")

    def editar_evento(self):
        """Permitir editar el evento seleccionado en el TreeView."""
        selected_item = self.tree.selection()

        if selected_item:
            # Obtener los valores del evento seleccionado
            item = self.tree.item(selected_item)
            event = item['values']

            # Colocar los valores actuales en los campos de entrada para permitir la edición
            self.date_entry.set_date(event[0])
            self.time_entry.delete(0, 'end')
            self.time_entry.insert(0, event[1])
            self.description_entry.delete(0, 'end')
            self.description_entry.insert(0, event[2])

            # Guardar referencia del evento que se está editando
            self.editing_event = selected_item
            self.save_button.config(state='normal')  # Habilitar el botón de guardar cambios
        else:
            messagebox.showwarning("No seleccionado", "Por favor seleccione un evento para editar.")

    def guardar_cambios_evento(self):
        """Guardar los cambios en el evento editado."""
        if self.editing_event:
            date = self.date_entry.get()
            time = self.time_entry.get()
            description = self.description_entry.get()

            if date and time and description:
                # Actualizar el evento en el TreeView
                self.tree.item(self.editing_event, values=(date, time, description))

                # Actualizar el evento en la lista interna
                index = self.tree.index(self.editing_event)
                self.events[index] = (date, time, description)

                # Limpiar los campos de entrada y desactivar el botón de guardar cambios
                self.clear_entries()
                self.editing_event = None
                self.save_button.config(state='disabled')  # Deshabilitar el botón después de guardar
            else:
                messagebox.showwarning("Campos incompletos",
                                       "Por favor complete todos los campos para guardar los cambios.")
        else:
            messagebox.showwarning("No seleccionado", "No hay evento seleccionado para guardar cambios.")

    def clear_entries(self):
        """Limpiar los campos de entrada."""
        self.date_entry.set_date(
            self.date_entry.cget("mindate"))  # Establecer la fecha mínima permitida o la fecha actual
        self.time_entry.delete(0, 'end')
        self.description_entry.delete(0, 'end')


# Inicializa root antes de crear una instancia de AgendaApp
root = tk.Tk()
app = AgendaApp(root)
root.mainloop()
