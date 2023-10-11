import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from random import randrange

def crear_lista(num_elementos):
    lista_valores = []
    for i in range(num_elementos):
        valor = simpledialog.askstring("Ingresar Valor", f"Ingrese el valor #{i + 1}:")
        if valor is None:
            return None
        lista_valores.append(valor)
    return lista_valores

def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def shuffle(A):
    for i in range(len(A)):
        j = randrange(i, len(A))
        swap(A, i, j)

def main():
    num_elementos = simpledialog.askinteger("Número de Elementos", "Número de elementos que tendrá su arreglo:")
    if num_elementos is None:
        return
    if num_elementos <= 0:
        messagebox.showerror("Error", "El número de elementos debe ser mayor que cero.")
        return

    lista_valores = crear_lista(num_elementos)
    if lista_valores is None:
        return

    messagebox.showinfo("Resultado", "La lista es: " + str(lista_valores))
    shuffle(lista_valores)
    messagebox.showinfo("Resultado", "La lista aleatorizada es: " + str(lista_valores))

if __name__ == "__main__":
    VentanaMain = tk.Tk()
    VentanaMain.title("Algoritmo de Fisher-Yates número de elementos")
    VentanaMain.geometry("300x150")

    btnCrear = tk.Button(text="Continuar", command=main)
    btnCrear.pack()

    VentanaMain.mainloop()
