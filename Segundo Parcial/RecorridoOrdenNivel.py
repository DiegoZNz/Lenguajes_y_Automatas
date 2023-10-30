from collections import deque
#una clase para almacenar un nodo de arbol binario

class Node:
    #constructor para crear un nuevo nodo
    def __init__(self, key = None, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right
        
    #funcion para imprimir el recorrido del orden de nivel de un arbol binario dado

def levelOrderTraversal(root):
    #caja base
    if not root:
        return
# crear una queue vacía y poner en queue el nodo raíz 
    queue = deque()
    queue.append(root)
    # bucle hasta que la queue esté vacía
    while queue:
        # procesa el nodo del frente y encolar sus hijos
        curr = queue.popleft()
        print(curr.key, end = ' ')
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
            
if __name__=='__main__':
    root = Node(15)
    root.left = Node(10)
    root.right = Node(20)
    root.left.left = Node(8)
    root.left.right = Node(12)
    root.right.left = Node(16)
    root.right.right = Node(25)
    
    levelOrderTraversal(root)