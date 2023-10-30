class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []

def find_lca(root, node1, node2, required_ancestor=None):
    if root is None:
        return None

    if root.name == node1 or root.name == node2:
        return root

    found_nodes = []
    for child in root.children:
        lca = find_lca(child, node1, node2, required_ancestor)
        if lca is not None:
            found_nodes.append(lca)

    if len(found_nodes) == 2:
        return root
    elif len(found_nodes) == 1:
        return found_nodes[0]
    elif root.name == required_ancestor:
        return root
    else:
        return None

# Ejemplo de uso
if __name__ == "__main__":
    raiz = TreeNode("Uziel")
    e2 = TreeNode("Jesus")
    e3 = TreeNode("Graciela")
    e4 = TreeNode("José")
    e5 = TreeNode("Luis Miguel")
    e6 = TreeNode("Valentina")
    e7 = TreeNode("Alfredo")
    e8 = TreeNode("Christina")
    e9 = TreeNode("Xavier")
    e10 = TreeNode("Lionel")
    e11 = TreeNode("Cristiano R")
    e12 = TreeNode("Michael")
    e13 = TreeNode("Michelle")
    e14 = TreeNode("Barak")
    e15 = TreeNode("Ronaldinho")
    e16 = TreeNode("Dana")
    e17 = TreeNode("Christian N")
    e18 = TreeNode("Diego")
    e19 = TreeNode('Magi')
    e20 = TreeNode('Bart')
    e21 = TreeNode('Joaquin')
    e22 = TreeNode('Juan')
    e23 = TreeNode('George')
    e24 = TreeNode('Caleb')
    e25 = TreeNode('Goku')
    e26 = TreeNode('Benito')
    e27 = TreeNode('Brayan')
    e28 = TreeNode('Valentina II')
    e29= TreeNode("Arturo")
    e30 = TreeNode('Melchor')
    e31 = TreeNode('Gohan')
    e32 = TreeNode('Goten')
    e33 = TreeNode('Daniel')
    e34 = TreeNode('Kevin')
    e35 = TreeNode('Kimberly')
    e36 = TreeNode('Britani')
    e37 = TreeNode('Obidio')
    e38 = TreeNode('Gaspar')
    e39 = TreeNode('Baltazar')
    e40 = TreeNode('Pan')
    e41 = TreeNode('Ian')
    e42 = TreeNode('Alex')
    e43 = TreeNode('Pennelope')
    e44 = TreeNode('Eliel')
    e45 = TreeNode('Omar')
    e46 = TreeNode('Goku II')
    e47 = TreeNode('Yandel')
    e48 = TreeNode('Alexander')

    raiz.children = [e2, e3]
    e2.children = [e4, e5]
    e3.children = [e6, e7]
    e4.children = [e8, e9]
    e5.children = [e10, e11]
    e6.children = [e19, e20]
    e7.children = [e21, e22]
    e8.children = [e12, e13]
    e9.children = [e14]
    e10.children = [e15, e16]
    e11.children = [e17]
    e14.children = [e23, e24]
    e16.children = [e25]
    e17.children = [e26]
    e19.children = [e27, e28]
    e21.children = [e29]
    e22.children = [e30]
    e25.children = [e31, e32]
    e26.children = [e33, e34]
    e27.children = [e35, e36]
    e28.children = [e42, e43]
    e29.children = [e37]
    e30.children = [e38, e39]
    e31.children = [e40]
    e35.children = [e41]
    e38.children = [e44]
    e39.children = [e45]
    e40.children = [e46]
    e41.children = [e47, e48]

    node1 = "Yandel"
    node2 = "Valentina"
    required_ancestor = "Graciela"  # Establecer el ancestro requerido

    lca = find_lca(raiz, node1, node2, required_ancestor)
    if lca:
        print(f"El ancestro común más bajo de {node1} y {node2} es {lca.name}")
    else:
        print(f"No se encontró un ancestro común para {node1} y {node2} que sea {required_ancestor}")
