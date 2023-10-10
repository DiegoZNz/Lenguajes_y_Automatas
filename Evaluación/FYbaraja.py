import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import random

# Crear una lista que represente la baraja inglesa
baraja = ["2 de Corazones", "3 de Corazones", "4 de Corazones", "5 de Corazones", "6 de Corazones",
          "7 de Corazones", "8 de Corazones", "9 de Corazones", "10 de Corazones", "J de Corazones",
          "Q de Corazones", "K de Corazones", "A de Corazones",
          "2 de Diamantes", "3 de Diamantes", "4 de Diamantes", "5 de Diamantes", "6 de Diamantes",
          "7 de Diamantes", "8 de Diamantes", "9 de Diamantes", "10 de Diamantes", "J de Diamantes",
          "Q de Diamantes", "K de Diamantes", "A de Diamantes",
          "2 de Tréboles", "3 de Tréboles", "4 de Tréboles", "5 de Tréboles", "6 de Tréboles",
          "7 de Tréboles", "8 de Tréboles", "9 de Tréboles", "10 de Tréboles", "J de Tréboles",
          "Q de Tréboles", "K de Tréboles", "A de Tréboles",
          "2 de Picas", "3 de Picas", "4 de Picas", "5 de Picas", "6 de Picas",
          "7 de Picas", "8 de Picas", "9 de Picas", "10 de Picas", "J de Picas",
          "Q de Picas", "K de Picas", "A de Picas"]

def repartir_cartas(baraja, num_jugadores):
    random.shuffle(baraja)
    jugadores = [[] for _ in range(num_jugadores)]  # Crear listas para cada jugador
    
    for _ in range(7):  # Repartir 7 cartas a cada jugador
        for jugador in jugadores:
            carta = baraja.pop()
            jugador.append(carta)
    
    return jugadores

def main():
    num_jugadores = simpledialog.askinteger("Número de Jugadores", "Número de jugadores:")
    if num_jugadores is None:
        return
    if num_jugadores <= 1:
        messagebox.showerror("Error", "El número de jugadores debe ser mayor que 1.")
        return
    if num_jugadores > 4:
        messagebox.showerror("Error", "El número de jugadores no puede ser mayor que 4.")
        return
    
    
    jugadores = repartir_cartas(baraja, num_jugadores)
    
    # Mostrar las manos de los jugadores
    for i, mano in enumerate(jugadores):
        messagebox.showinfo(f"Jugador {i + 1}", f"Mano del Jugador {i + 1}: {', '.join(mano)}")

    # Mostrar las cartas restantes
    if baraja:
        messagebox.showinfo("Cartas Restantes", f"Cartas restantes: {', '.join(baraja)}")
    else:
        messagebox.showinfo("Cartas Restantes", "No quedan cartas en la baraja.")

if __name__ == "__main__":
    VentanaMain = tk.Tk()
    VentanaMain.title("Distribución de Cartas")
    VentanaMain.geometry("300x150")

    btnCrear = tk.Button(text="Comenzar Juego", command=main)
    btnCrear.pack()

    VentanaMain.mainloop()
