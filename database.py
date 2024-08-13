import sqlite3

import sqlite3
from tkinter import messagebox

def crear_base_de_datos():
    conexion = sqlite3.connect('asistencia.db')
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS asistencia (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            fecha TEXT NOT NULL,
            pc TEXT NOT NULL
        )
    ''')
    conexion.commit()
    conexion.close()

def guardar_datos(nombre_entry, apellido_entry, fecha_entry, pc_entry, ventana):
 try:
    nombre = nombre_entry.get()
    apellido = apellido_entry.get()
    fecha = fecha_entry.get()
    pc = pc_entry.get()

    conexion = sqlite3.connect('asistencia.db')
    cursor = conexion.cursor()
    cursor.execute('''
        INSERT INTO asistencia (nombre, apellido, fecha, pc)
        VALUES (?, ?, ?, ?)
    ''', (nombre, apellido, fecha, pc))
    conexion.commit()
    conexion.close()
    
    messagebox.showinfo("Éxito", "Datos guardados con éxito! Ya puedes empezar a trabajar")
    
    nombre_entry.delete(0, 'end')
    apellido_entry.delete(0, 'end')
    fecha_entry.delete(0, 'end')
    pc_entry.delete(0, 'end')
    
    ventana.quit()
 except Exception as e:
        # Mostrar mensaje de error si algo falla
    messagebox.showerror("Error", f"No se pudieron guardar los datos: {str(e)}")

