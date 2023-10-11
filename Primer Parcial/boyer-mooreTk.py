import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

def findMajoritaryElement(nums):
    d = {}
    #recorrer la lista y almacenar la frecuencia de cada elemento en un diccionario
    for i in nums:
        d[i] = d.get(i, 0) + 1
        
        #devolver el elemento si su cuenta es mayor que n/2
        
    for key, value in d.items():
        if value > len(nums)/2:
            return messagebox.showinfo("Resultado", "El elemento mayoritario es: " + str(key))
        #devolver mensaje si no hay un elemento mayoritario
    return messagebox.showinfo("Resultado", "No hay elemento mayoritario")


#creamos la ventana
Ventana= Tk()
Ventana.title("Algoritmo de Boyer-Moore")
Ventana.geometry("300x150")
panel=ttk.Notebook (Ventana)


varNumeros = tk.StringVar()
lblNum = Label(text="Numeros: ")
lblNum.pack()
txtNum = Entry(textvariable=varNumeros)
txtNum.pack()

#creamos el boton que jalara los numeros separados por comas para crear la lista

def crearLista():
    
    # Validamos que el campo de texto no esté vacío
    if varNumeros.get() == "":
        messagebox.showerror("Error", "El campo de texto no puede estar vacío")
        return
    
    
    # Validamos que el campo de texto solo acepte números y comas
    lista = varNumeros.get().split(",")
    for i in lista:
        if not i.isdigit() and i != ",":
            messagebox.showerror("Error", "El campo de texto solo debe contener números y comas")
            return
    lista = list(map(int, lista))
    findMajoritaryElement(lista)
    
btnCrear = Button(text="Crear lista", command=crearLista)
btnCrear.pack()

Ventana.mainloop()