from graphviz import Graph
import random

class AVLTree:
    def __init__(self):
        self.root = None

    class Node:
        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None
            self.height = 1

    def insert(self, key):
        def get_height(node):
            if node is None:
                return 0
            return node.height

        def get_balance(node):
            if node is None:
                return 0
            return get_height(node.left) - get_height(node.right)

        def right_rotate(node):
            new_root = node.left
            node.left = new_root.right
            new_root.right = node
            node.height = max(get_height(node.left), get_height(node.right)) + 1
            new_root.height = max(get_height(new_root.left), get_height(new_root.right)) + 1
            return new_root

        def left_rotate(node):
            new_root = node.right
            node.right = new_root.left
            new_root.left = node
            node.height = max(get_height(node.left), get_height(node.right)) + 1
            new_root.height = max(get_height(new_root.left), get_height(new_root.right)) + 1
            return new_root

        def insert_node(node, key):
            if node is None:
                return AVLTree.Node(key)
            if key < node.key:
                node.left = insert_node(node.left, key)
            else:
                node.right = insert_node(node.right, key)
            node.height = max(get_height(node.left), get_height(node.right)) + 1
            balance = get_balance(node)
            if balance > 1 and key < node.left.key:
                return right_rotate(node)
            if balance < -1 and key > node.right.key:
                return left_rotate(node)
            if balance > 1 and key > node.left.key:
                node.left = left_rotate(node.left)
                return right_rotate(node)
            if balance < -1 and key < node.right.key:
                node.right = right_rotate(node.right)
                return left_rotate(node)
            return node

        self.root = insert_node(self.root, key)

    def render(self):
        def render_node(node, dot):
            if node is not None:
                dot.node(str(node.key), str(node.key))
                if node.left is not None:
                    dot.edge(str(node.key), str(node.left.key))
                    render_node(node.left, dot)
                if node.right is not None:
                    dot.edge(str(node.key), str(node.right.key))
                    render_node(node.right, dot)

        dot = Digraph(comment='AVL Tree')
        render_node(self.root, dot)
        dot.render('avl_tree.gv', view=True)

tree = AVLTree()
for i in range(100):
    tree.insert(random.randint(1, 1000))

import os
os.environ["PATH"] += os.pathsep + 'ruta_de_instalación_de_graphviz'
