'''
AVL Trees
'''

class Node:
    def __init__(self, data): 
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

    def __repr__(self):
         return '({})'.format(self.data)
    
'''
Funciones necesarias
'''

class AVLtree:
    def __init__(self):
        self.root = None

    # funcion para saber la altura de un nodo
    def height(self, node):
        if node is None:
            return 0
        return node.height

    #funcion para hacer una rotacion simple ala izquierda
    def rotate_left(self, node):
        right_child = node.right
        node.right = right_child.left
        right_child.left = node
        
        node.height = max(self.height(node.left), self.height(node.right)) + 1
        right_child.height = max(self.height(right_child.left), self.height(right_child.right)) + 1
        
        return right_child
    
    # funcion para hacer una rotacion simpel a la derecha
    def rotate_right(self, node):
        left_child = node.left
        node.left = left_child.right
        left_child.right = node
        
        node.height = max(self.height(node.left), self.height(node.right)) + 1
        left_child.height = max(self.height(left_child.left), self.height(left_child.right)) + 1
        
        return left_child
    
    #funcion para hacer una rotacion doble a la izquierda
    def rotate_left_right(self, node):
        node.left = self.rotate_left(node.left)
        return self.rotate_right(node)
    
    #funcion para realizar una rotacion doble a la derechs
    def rotate_right_left(self, node):
        node.right = self.rotate_right(node.right)
        return self.rotate_left(node)

    # funcion para obtener el balance factor de un nodo
    def balance(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right) #formula de balace de la lectura
    
       

    '''
    Metodos
    '''

    