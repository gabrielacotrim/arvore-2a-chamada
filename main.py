import json

# Definição de um nó da árvore
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Classe para construir e manipular a árvore binária de busca
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, current_node, key):
        if key < current_node.key:
            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self._insert(current_node.left, key)
        else:
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._insert(current_node.right, key)

    # Percurso em pré-ordem
    def pre_order_traversal(self, node, result):
        if node:
            result.append(node.key)
            self.pre_order_traversal(node.left, result)
            self.pre_order_traversal(node.right, result)

    # Percurso em pós-ordem
    def post_order_traversal(self, node, result):
        if node:
            self.post_order_traversal(node.left, result)
            self.post_order_traversal(node.right, result)
            result.append(node.key)

# Leitura do arquivo JSON
with open('arvore.json', 'r') as file:
    data = json.load(file)

values = data['values']

# Construção da árvore binária de busca
bst = BinarySearchTree()
for value in values:
    bst.insert(value)

# Realizar os percursos
pre_order_result = []
post_order_result = []

bst.pre_order_traversal(bst.root, pre_order_result)
bst.post_order_traversal(bst.root, post_order_result)

# Exibir os resultados
print("Valores na ordem pré-ordem:", pre_order_result)
print("Valores na ordem pós-ordem:", post_order_result)
