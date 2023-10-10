import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from random import randrange

def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def shuffle(A):
    for i in range(len(A)):
        j = randrange(i, len(A))
        swap(A, i, j)

def crear_ventana_valor(num_elementos):
    ventana_valor = tk.Toplevel()
    ventana_valor.title(f"Ingrese el valor #{num_elementos + 1}")
    
    varValor = tk.StringVar()
    lblValor = tk.Label(ventana_valor, text=f"Valor #{num_elementos + 1}: ")
    lblValor.pack()
    
    txtValor = tk.Entry(ventana_valor, textvariable=varValor)
    txtValor.pack()
    
    btnGuardar = tk.Button(ventana_valor, text="Guardar", command=lambda: guardar_valor(varValor.get(), num_elementos, ventana_valor))
    btnGuardar.pack()
    
    return ventana_valor

def guardar_valor(valor, num_elementos, ventana):
    A.append(valor)
    ventana.destroy()
    
    if len(A) < num_elementos:
        mostrar_siguiente_ventana()

def mostrar_siguiente_ventana():
    if ventanas_A:
        ventana = ventanas_A.pop(0)
        ventana.wait_window(ventana)
    else:
        # Si se han ingresado todos los valores, cierra las ventanas de ingreso
        for ventana in ventanas_A:
            ventana.destroy()
def parametro():
    if varNumeros.get() == "":
        return messagebox.showerror("Error", "El campo de texto no puede estar vacío")  
    num_elementos = int(varNumeros.get())
    global ventanas_A
    ventanas_A = []
    global A
    A = []
    
    for i in range(num_elementos):
        ventana = crear_ventana_valor(i)
        ventanas_A.append(ventana)
        
        if i < num_elementos:
            mostrar_siguiente_ventana()
    
    # After all values have been entered, shuffle and show the messagebox
    messagebox.showinfo("Resultado", "La lista es: " + str(A))
    shuffle(A)
    messagebox.showinfo("Resultado", "La lista aleatorizada es: " + str(A))
    
VentanaMain = tk.Tk()
VentanaMain.title("Algoritmo de Fisher-Yates número de elementos")
VentanaMain.geometry("300x150")

varNumeros = tk.StringVar()
lblNum = tk.Label(text="Número de datos que tendrá su arreglo: ")
lblNum.pack()
txtNum = tk.Entry(textvariable=varNumeros)
txtNum.pack()

btnCrear = tk.Button(text="Continuar", command=parametro)
btnCrear.pack()


VentanaMain.mainloop()
