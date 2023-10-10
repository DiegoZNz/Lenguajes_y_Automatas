import tkinter as tk
from tkinter import simpledialog, ttk, messagebox

def findMajoritaryElement(nums):
    d = {}
    
    # Recorrer la lista y almacenar la frecuencia de cada elemento en un diccionario
    for i in nums:
        d[i] = d.get(i, 0) + 1
        
    # Devolver el elemento si su cuenta es mayor que n/2
    for key, value in d.items():
        if value > len(nums)/2:
            return messagebox.showinfo("Resultado", "El elemento mayoritario es: " + str(key))
    
    # Devolver mensaje si no hay un elemento mayoritario
    return messagebox.showinfo("Resultado", "No hay elemento mayoritario")

def crearLista():
    num_elementos = varNumeros.get()
    
    if not num_elementos:
        return
    
    try:
        num_elementos = int(num_elementos)
    except ValueError:
        messagebox.showerror("Error", "Ingrese un número válido")
        return
    
    lista = []
    
    # Solicitar al usuario los números según la cantidad especificada
    for i in range(num_elementos):
        numero = simpledialog.askinteger("Ingresar número", f"Ingrese el valor del elemento #{i + 1}:")
        
        if numero is not None:
            lista.append(numero)
    
    if lista:
        findMajoritaryElement(lista)

# Crear la ventana principal
Ventana = tk.Tk()
Ventana.title("Algoritmo de Boyer-Moore")
Ventana.geometry("300x150")

varNumeros = tk.StringVar()
lblNum = tk.Label(text="Número de elementos: ")
lblNum.pack()
txtNum = tk.Entry(textvariable=varNumeros)
txtNum.pack()

# Crear el botón que jalará los números separados por comas para crear la lista
btnCrear = tk.Button(text="Crear lista", command=crearLista)
btnCrear.pack()

# Iniciar la aplicación
Ventana.mainloop()
