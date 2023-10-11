#Una clase para representar un objeto grafo
class Graph:
    #constructor
    def __init__(self, edges, n):
        #Una lista de listas para representar una lista de adyacencia
        self.adjList = [[] for _ in range(n)]
        #Agregar bordes al grafo no dirigido
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)

#Función para comprobar si es seguro asignar el colo 'c' al vertice 'v'
def isSafe(graph, color, v, c):
    #Verifica el color de cada vertice adyacente de 'v'
    for u in graph.adjList[v]:
        if color[u] == c:
            return False
    return True

def kColoreable(g, color, k, v, n):
    #Si todos los colores estan asignados, imprima la solucion
    if v == n:
        print([COLORS[color[v]] for v in range(n)])
        return
            
    # prueba todas las combinaciones posibles de colores disponibles
    for c in range (1, k+1):
        # si es seguro asignar el color c al vertice v
        if isSafe(g, color, v, c):
            color[v] = c
            # recursivamente asigna colores a los vertices restantes
            kColoreable(g, color, k, v+1, n)
            # backtrack: si la asignacion de color no lleva a una solucion
            color[v] = 0

def edge():
    print("Ingrese la arista en el formato x, y: ")
    x, y = map(int, input().split(','))
    return (x, y)

if __name__ =='__main__':
    edges = []
    print("Cuantos colores quiere?: ")
    k = int(input())
    print("Cuantos nodos tiene el grafo: ")
    n = int(input())
    print("Cuantas aristas tiene el grafo: ")
    v = int(input())
    edges = []
    for i in range(v):
        edges.append(edge())
    COLORS = ['BLUE', 'GREEN', 'RED', 'YELLOW', 'ORANGE', 'PINK', 'BLACK', 'BROWN', 'WHITE', 'PURPLE']
    g = Graph(edges, n) 
    color = [None] * n
    print("Matriz de colores: ")
    kColoreable(g, color, k, 0, n)


