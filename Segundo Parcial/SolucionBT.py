class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)

def isSafe(graph, puerto, v, c):
    for u in graph.adjList[v]:
        if puerto[u] == c:
            return False
    return True

def kColoreable(g, puerto, k, v, n):
    if v == n:
        print([PUERTOS[puerto[v]] for v in range(n)])
        return
            
    for c in range (1, k+1):
        if isSafe(g, puerto, v, c):
            puerto[v] = c
            kColoreable(g, puerto, k, v+1, n)
            puerto[v] = 0

def edge():
    print("Ingrese la arista en el formato x, y: ")
    x, y = map(int, input().split(','))
    return (x, y)

if __name__ =='__main__':
    edges = []
    print("Cuantos puertos quiere?: ")
    k = int(input())
    print("Cuantos nodos tiene el grafo: ")
    n = int(input())
    print("Cuantas aristas tiene el grafo: ")
    v = int(input())
    edges = []
    for i in range(v):
        edges.append(edge())
    PUERTOS = ['ensanada', 'baja california' ,'caboSanLucas', 'guaymas', 'topo', 'mazatlan', 'puertoVallarta', 'manzanillo']
    g = Graph(edges, n) 
    puerto = [None] * n
    print("Matriz de puertos: ")
    kColoreable(g, puerto, k, 0, n)


