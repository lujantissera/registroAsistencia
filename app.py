import tkinter as tk
from tkinter import messagebox
from database import crear_base_de_datos, guardar_datos
import sqlite3


def crear_formulario():
    ventana = tk.Tk()
    ventana.title("Registro de Asistencia")

    tk.Label(ventana, text="Nombre").grid(row=0, column=0)
    tk.Label(ventana, text="Apellido").grid(row=1, column=0)
    tk.Label(ventana, text="Fecha (DD/MM/AAAA)").grid(row=2, column=0)
    tk.Label(ventana, text="PC").grid(row=3, column=0)

    nombre_entry = tk.Entry(ventana)
    apellido_entry = tk.Entry(ventana)
    fecha_entry = tk.Entry(ventana)
    pc_entry = tk.Entry(ventana)

    nombre_entry.grid(row=0, column=1)
    apellido_entry.grid(row=1, column=1)
    fecha_entry.grid(row=2, column=1)
    pc_entry.grid(row=3, column=1)

    guardar_button = tk.Button(ventana, text="Guardar", 
                               command=lambda: guardar_datos(nombre_entry, apellido_entry, fecha_entry, pc_entry, ventana))
    guardar_button.grid(row=4, column=1)

    ventana.mainloop()

if __name__ == "__main__":
    crear_base_de_datos()
    crear_formulario()
