class NodoBST:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBST:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        nuevo_nodo = NodoBST(valor)
        if self.raiz is None:
            self.raiz = nuevo_nodo
        else:
            self._insertar_recursivo(self.raiz, nuevo_nodo)

    def _insertar_recursivo(self, nodo_actual, nuevo_nodo):
        if nuevo_nodo.valor < nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = nuevo_nodo
            else:
                self._insertar_recursivo(nodo_actual.izquierda, nuevo_nodo)
        else:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = nuevo_nodo
            else:
                self._insertar_recursivo(nodo_actual.derecha, nuevo_nodo)


class NodoAVL:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
        self.altura = 1

class ArbolAVL:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        nuevo_nodo = NodoAVL(valor)
        if self.raiz is None:
            self.raiz = nuevo_nodo
        else:
            self.raiz = self._insertar_recursivo(self.raiz, nuevo_nodo)

    def _insertar_recursivo(self, nodo_actual, nuevo_nodo):
        if nuevo_nodo.valor < nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = nuevo_nodo
            else:
                nodo_actual.izquierda = self._insertar_recursivo(nodo_actual.izquierda, nuevo_nodo)
        else:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = nuevo_nodo
            else:
                nodo_actual.derecha = self._insertar_recursivo(nodo_actual.derecha, nuevo_nodo)
        
        nodo_actual.altura = 1 + max(self._altura(nodo_actual.izquierda), self._altura(nodo_actual.derecha))
        balance = self._calcular_balance(nodo_actual)
        
        # Rotación simple a la derecha
        if balance > 1 and nuevo_nodo.valor < nodo_actual.izquierda.valor:
            return self._rotacion_derecha(nodo_actual)
        
        # Rotación simple a la izquierda
        if balance < -1 and nuevo_nodo.valor > nodo_actual.derecha.valor:
            return self._rotacion_izquierda(nodo_actual)
        
        # Rotación doble a la izquierda
        if balance > 1 and nuevo_nodo.valor > nodo_actual.izquierda.valor:
            nodo_actual.izquierda = self._rotacion_izquierda(nodo_actual.izquierda)
            return self._rotacion_derecha(nodo_actual)
        
        # Rotación doble a la derecha
        if balance < -1 and nuevo_nodo.valor < nodo_actual.derecha.valor:
            nodo_actual.derecha = self._rotacion_derecha(nodo_actual.derecha)
            return self._rotacion_izquierda(nodo_actual)
        
        return nodo_actual

    def _altura(self, nodo):
        if nodo is None:
            return 0
        return nodo.altura

    def _calcular_balance(self, nodo):
        if nodo is None:
            return 0
        return self._altura(nodo.izquierda) - self._altura(nodo.derecha)

            
import random

arbol_bst = ArbolBST()

# Generar un conjunto de 10 millones de valores aleatorios
valores = set(random.sample(range(1, 10000001), 10000000))

# Insertar cada valor en el árbol BST
for valor in valores:
    arbol_bst.insertar(valor)


arbol_avl = ArbolAVL()

# Generar un conjunto de 10 millones de valores aleatorios
valores = set(random.sample(range(1, 10000001), 10000000))

# Insertar cada valor en el árbol AVL
for valor in valores:
    arbol_avl.insertar(valor)

import time

# Tomar el tiempo de ejecución del árbol BST
inicio_bst = time.time()
for valor in valores:
    arbol_bst.insertar(valor)
fin_bst = time.time()
tiempo_bst = fin_bst - inicio_bst
print("Tiempo de ejecución del árbol BST: ", tiempo_bst)

# Tomar el tiempo de ejecución del árbol AVL
inicio_avl = time.time()
for valor in valores:
    arbol_avl.insertar(valor)
fin_avl = time.time()
tiempo_avl = fin_avl - inicio_avl
print("Tiempo de ejecución del árbol AVL: ", tiempo_avl)
