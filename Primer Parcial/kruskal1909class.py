#clase para representar un conjunto de elementos disjuntos

class disjointSet:
    parent = {}
    #realizar la operacion make_set
    
    def make_set(self, n):
        #crear 'n' conjuntos disjuntos (uno por cada vertice)
        for i in range(n):
            self.parent[i] = i
    
    #encontrar la raiz del conjunto al que pertenece un elemento k
    
    def find(self, k):
        #si k es una raiz, devolver k
        
        if self.parent[k] == k:
            return k
        #sino, aplicar find al padre de k       
        return self.find(self.parent[k])
    
    #unir dos conjuntos disjuntos
    def union(self, a, b):
        #encontrar la raiz de a y b
        x = self.find(a)
        y = self.find(b)
        
        #unir los conjuntos
        self.parent[x] = y
    
    #funcion # para construir el arbol de expansion minima usando el algoritmo de kruskal
    
def runKruskalAlgorithm(edges,n):
    #almacena los bordes presentes en el MST
    MST = []
    #inicilizar la clase disjointSet
    #crea un conjunto singleton para cada elemento del universo
    ds = disjointSet()
    ds.make_set(n)
    index = 0
    
    #ordenar los bordes aumentando su peso
    edges.sort(key = lambda x: x[2])
    
    #mst contiene exactamente n-1 aristas
    
    while len(MST) != n-1:
        #considerar el borde sigiente con menor peso del grafo
        (src, dest, weight) = edges[index]
        index = index + 1
        
        #encontrar la raiz de los conjuntos a los que se unen los dos extremos 
        #vertices de la siguiente arista pertenecen
        x = ds.find(src)
        y = ds.find(dest)   
        
        #si ambos extremos tienen diferentes padres, pertenecen a diferentes componentes conectados y se pueden incluir en el MST
        
        if x != y:
            MST.append((src, dest, weight))
            ds.union(x, y)
            
    return MST

if __name__ == '__main__':
    #(u, v, w) representan una arista de u a v con peso w
    

    vertex_mapping = {
        'a': 0,
        'b': 1,
        'c': 2,
        'd': 3,
        'e': 4,
        'f': 5,
        'g': 6
    }
    
    edges = [
        ('a', 'b', 7), ('a', 'd', 5), ('b', 'c', 8), ('b', 'd', 9),
        ('b', 'e', 7), ('c', 'e', 5), ('d', 'e', 15), ('d', 'f', 6),
        ('e', 'f', 8), ('e', 'g', 9), ('f', 'g', 11)
    ]

    n = 7

    # Traducir los nombres de los vértices a números enteros
    edges = [(vertex_mapping[src], vertex_mapping[dest], weight) for src, dest, weight in edges]

    # Construir el árbol de expansión mínima
    e = runKruskalAlgorithm(edges, n)

    # Imprimir el resultado
    for edge in e:
        src, dest, weight = edge
        print(f'({src}, {dest}, {weight})')
