import tkinter as tk
from tkinter import simpledialog, messagebox

# Clase para representar un conjunto de elementos disjuntos
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))

    # Encontrar la raíz del conjunto al que pertenece un elemento k
    def find(self, k):
        if self.parent[k] == k:
            return k
        return self.find(self.parent[k])

    # Unir dos conjuntos disjuntos
    def union(self, a, b):
        x = self.find(a)
        y = self.find(b)
        if x != y:
            self.parent[x] = y

# Función para construir el árbol de expansión mínima usando el algoritmo de Kruskal
def runKruskalAlgorithm(edges, n):
    MST = []
    ds = DisjointSet(n)
    index = 0
    edges.sort(key=lambda x: x[2])

    while len(MST) != n - 1:
        src, dest, weight = edges[index]
        index += 1
        x = ds.find(src)
        y = ds.find(dest)

        if x != y:
            MST.append((src, dest, weight))
            ds.union(x, y)

    return MST

def generate_graph():
    num_edges = simpledialog.askinteger("Número de Aristas", "¿Cuántas aristas desea ingresar?")
    if num_edges is None:
        return

    edges = []
    for i in range(num_edges):
        edge = simpledialog.askstring(f"Arista #{i + 1}", "Ingrese la arista en el formato 'a b w', donde 'a' y 'b' son los vértices y 'w' es el peso:")
        if edge is not None:
            parts = edge.split()
            if len(parts) == 3:
                src, dest, weight = parts
                edges.append((vertex_mapping[src], vertex_mapping[dest], int(weight)))

    n = len(vertex_mapping)
    e = runKruskalAlgorithm(edges, n)
    result_text = "\n".join([f'({src}, {dest}, {weight})' for src, dest, weight in e])
    messagebox.showinfo("Resultado", f"Árbol de expansión mínima:\n{result_text}")

# Crear una ventana gráfica
root = tk.Tk()
root.title("Algoritmo de Kruskal")

# Crear un botón para generar el grafo
generate_button = tk.Button(root, text="Generar Grafo", command=generate_graph)
generate_button.pack()

# Mapeo de vértices
vertex_mapping = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6,
    'h': 7
}

root.mainloop()
