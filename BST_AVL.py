class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._insert(val, self.root)

    def _insert(self, val, current_node):
        if val < current_node.val:
            if current_node.left is None:
                current_node.left = Node(val)
            else:
                self._insert(val, current_node.left)
        elif val > current_node.val:
            if current_node.right is None:
                current_node.right = Node(val)
            else:
                current_node.right = self._insert(val, current_node.right)

        else:
            print("Value already in tree.")

# Crear un nuevo árbol BST
bst = BST()

# Insertar valores en el árbol
bst.insert(5)
bst.insert(3)
bst.insert(7)

class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.height = 1

class AVL:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self.root = self._insert(val, self.root)

    def _insert(self, val, current_node):
        if current_node is None:
            return Node(val)
        elif val < current_node.val:
            current_node.left = self._insert(val, current_node.left)
        else:
            current_node.right = self._insert(val, current_node.right)

        current_node.height = 1 + max(self._get_height(current_node.left), self._get_height(current_node.right))
        balance = self._get_balance(current_node)

        # Si el nodo está desbalanceado, aplicamos las rotaciones necesarias
        if balance > 1 and val < current_node.left.val:
            return self._rotate_right(current_node)

        if balance > 1 and val > current_node.left.val:
            current_node.left = self._rotate_left(current_node.left)
            return self._rotate_right(current_node)

        if balance < -1 and val > current_node.right.val:
            return self._rotate_left(current_node)

        if balance < -1 and val < current_node.right.val:
            current_node.right = self._rotate_right(current_node.right)
            return self._rotate_left(current_node)

        return current_node

    def _get_height(self, current_node):
        if current_node is None:
            return 0
        return current_node.height

    def _get_balance(self, current_node):
        if current_node is None:
            return 0
        return self._get_height(current_node.left) - self._get_height(current_node.right)

    def _rotate_left(self, current_node):
        new_node = current_node.right
        current_node.right = new_node.left
        new_node.left = current_node
        current_node.height = 1 + max(self._get_height(current_node.left), self._get_height(current_node.right))
        new_node.height = 1 + max(self._get_height(new_node.left), self._get_height(new_node.right))
        return new_node

    def _rotate_right(self, current_node):
        new_node = current_node.left
        current_node.left = new_node.right
        new_node.right = current_node
        current_node.height = 1 + max(self._get_height(current_node.left), self._get_height(current_node.right))
        new_node.height = 1 + max(self._get_height(new_node.left), self._get_height(new_node.right))
        return new_node
            
import random

arbol_bst = BST()

valores = set(random.sample(range(1, 10000001), 10000000))

for valor in valores:
    arbol_bst.insert(valor)


arbol_avl = AVL()

valores = set(random.sample(range(1, 10000001), 10000000))

for valor in valores:
    arbol_avl.insert(valor)

import time

# Tomar el tiempo de ejecución del árbol BST
inicio_bst = time.time()
for valor in valores:
    arbol_bst.insert(valor)
fin_bst = time.time()
tiempo_bst = fin_bst - inicio_bst
print("Tiempo de ejecución del árbol BST: ", tiempo_bst)

# Tomar el tiempo de ejecución del árbol AVL
inicio_avl = time.time()
for valor in valores:
    arbol_avl.insert(valor)
fin_avl = time.time()
tiempo_avl = fin_avl - inicio_avl
print("Tiempo de ejecución del árbol AVL: ", tiempo_avl)
