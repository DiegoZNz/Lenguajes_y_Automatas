#Una clase para representar un objeto graph

class Graph:
    #Constructor
    def __init__(self,edges,n):
        self.adjList = [ [] for _ in range(n) ]
        for (src,dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)
    #función para comprobar si es seguro asignar el color 'c' al vértice 'v'
def isSafe(graph,color,v,c):
    #verifica el color de cada vértice adyacente de 'v'
    for u in graph.adjList[v]:
        if color[u]==c:
            return False
    return True

def kColorable (g, color, k, v, n):
    #si todos los colores están asignados, imprima la solución
    if v==n:
        print([COLORS[color[v]]for v in range(n)])
        return
    #prueba todas las combinaciones posibles de colores disponibles
    for c in range(1, k+1):
        #si es seguro asignar el color 'c' al vértice 'v'
        if isSafe(g, color, v, c):
            #asignar color 'c' al vértice 'v'
            color[v]=c
            #recorre para el siguiente vertice
            kColorable(g, color, k, v+1, n)
            #retractare
            color[v]=0

if __name__ == '__main__':
    #Lista de aristas de graph según el diagrama anterior
    edges=[(0,1), (0,4), (0,5), (4,5), (1,4), (1,3), (2,3), (2,4)]

    #Una lista para almacenar colores (puede manejar 10 graph coloreables)
    COLORS=['BLUE', 'GREEN', 'RED', 'YELLOW', 'ORANGE', 'PINK', 'BLACK', 'BROWN', 'WHITE', 'PURPLE']

    n=6
    
    g=Graph(edges, n)

    k=3

    color= [None] * n

    #imprime todas las k-configuraciones coloreables del graph

    kColorable(g, color, k, 0, n)
