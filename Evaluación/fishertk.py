import tkinter as tk
from tkinter import simpledialog, ttk, messagebox
from random import randrange

def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def shuffle(A):
    for i in range(len(A)):
        j = randrange(i, len(A))
        swap(A, i, j)

def parametro():
    num_elementos = varNumeros.get()
    
    if not num_elementos:
        messagebox.showerror("Error", "El campo de texto no puede estar vacío")
        return
    
    num_elementos = int(num_elementos)
    
    valores = []
    
    for i in range(num_elementos):
        valor = simpledialog.askstring(f"Valor #{i + 1}", f"Ingrese el valor #{i + 1}")
        
        if valor is not None:
            valores.append(valor)
    
    if valores:
        messagebox.showinfo("Resultado", f"La lista es: {valores}")
        shuffle(valores)
        messagebox.showinfo("Resultado", f"La lista aleatorizada es: {valores}")

# Crear la ventana principal
VentanaMain = tk.Tk()
VentanaMain.title("Algoritmo de Fisher-Yates número de elementos")
VentanaMain.geometry("300x150")

# Crear widgets
varNumeros = tk.StringVar()
lblNum = tk.Label(text="Número de datos que tendrá su arreglo: ")
lblNum.pack()
txtNum = tk.Entry(textvariable=varNumeros)
txtNum.pack()
btnCrear = tk.Button(text="Continuar", command=parametro)
btnCrear.pack()

# Iniciar la aplicación
VentanaMain.mainloop()
