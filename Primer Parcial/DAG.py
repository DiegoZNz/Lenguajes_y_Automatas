import sys

# Una clase para representar un grafo dirigido ponderado
class Graph:
    # Constructor
    def __init__(self, edges, N):
        # Lista de adyacencia
        self.adjList = [[] for _ in range(N)]
        
        # Agregar bordes a la lista de adyacencia
        for (source, dest, weight) in edges:
            self.adjList[source].append((dest, weight))

def DFS(graph, v, discovered, departure, time):
    discovered[v] = True
    for (u, w) in graph.adjList[v]:
        if not discovered[u]:
            time = DFS(graph, u, discovered, departure, time)
    departure[time] = v
    time = time + 1
    return time

def findLongestDistance(graph, source, N):
    # Inicializar departure, discovered y time
    departure = [-1] * N
    discovered = [False] * N
    time = 0
    
    # Realizar DFS en todos los vértices del grafo
    for i in range(N):
        if not discovered[i]:
            time = DFS(graph, i, discovered, departure, time)

    # Inicializar cost y parent
    cost = [sys.maxsize] * N
    parent = [-1] * N
    cost[source] = 0

    # Relaxar las aristas N-1 veces para encontrar la distancia más larga
    for _ in range(N - 1):
        for u in range(N):
            for (v, w) in graph.adjList[u]:
                w = -w  # Hace que el peso sea negativo
                if cost[u] != sys.maxsize and cost[u] + w < cost[v]:
                    cost[v] = cost[u] + w
                    parent[v] = u

    # Imprimir las distancias más largas
    for i in range(N):
        print(f'dist ({source}, {i}) = {-cost[i]}')

if __name__ == '__main__':
    edges = [
        (0, 6, 2), (1, 2, -4), (1, 4, 1), (1, 6, 8), (3, 0, 3),
        (3, 4, 5), (5, 1, 2), (7, 0, 6), (7, 1, -1), (7, 3, 4), (7, 5, -4)
    ]
    N = 8
    graph = Graph(edges, N)
    source = 7
    findLongestDistance(graph, source, N)
