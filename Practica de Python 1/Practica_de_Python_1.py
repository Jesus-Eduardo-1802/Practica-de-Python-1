import tkinter as tk
from tkinter import messagebox

def mensaje():
    print("Diste click")
    nombre = tbNombre.get()
    messagebox.showinfo("Nombre de Usuario", "Bienvenido : " + nombre)

ventana = tk.Tk()
ventana.geometry("300x200")
ventana.configure(bg="Lightblue")
ventana.title("Actividad 02 - Pantalla en Blanco")


lbNombre = tk.Label(text="Nombre : ")
lbNombre.place(x=50,y=70)


tbNombre = tk.Entry()
tbNombre.place(x=150, y=70)


btnAceptar = tk.Button(ventana, text="Aceptar", command=mensaje)
btnAceptar.place(x=50,y=100)

btnCancelar = tk.Button(ventana, text="Cancelar", command=ventana.quit)
btnCancelar.place(x=150,y=100)


ventana.mainloop()
