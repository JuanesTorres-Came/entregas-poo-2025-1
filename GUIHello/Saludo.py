import tkinter as tk
from tkinter import messagebox

class AplicacionSaludo:
    def __init__(self, master):
        self.master = master
        master.title("tk")
        
        # Etiqueta
        self.label = tk.Label(master, text="Como te llamas?")
        self.label.grid(row=0, column=0, padx=5, pady=5)
        
        # Entrada de texto
        self.entry = tk.Entry(master)
        self.entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Botón de saludo
        self.saludo_button = tk.Button(master, text="Saludo", command=self.saludar)
        self.saludo_button.grid(row=1, column=0, padx=10, pady=10)
        
        # Botón de salir
        self.salir_button = tk.Button(master, text="Salir", command=master.quit)
        self.salir_button.grid(row=1, column=1, padx=10, pady=10)

    def saludar(self):
        nombre = self.entry.get()
        if nombre.strip() == "":
            messagebox.showwarning("Atención", "Por favor ingresa tu nombre.")
        else:
            messagebox.showinfo("...", f"Hola {nombre}!")

# Crear ventana principal
if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionSaludo(root)
    root.mainloop()
