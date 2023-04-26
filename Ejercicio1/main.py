from AVL_trees import AVLtree

print('\n*** Instantiate AVL ***\n')
tree = AVLtree()
print('AVL object: {}'.format(tree)) 
print('Current root: {}'.format(tree.root)) 

#test metodo insert
print('\n*** Inserting Nodes in Tree ***\n')


nodes_values = [33, 77, 4, 11, 16, 55, 5, 1, 14, 63]

for value in nodes_values:
    print('Inserting node with value: {}'.format(value))
    tree.insert(value)

print('Current root: {}'.format(tree.root)) # current root


#test metodo traverse
print('\n*** Traversing Tree ***\n')
print(tree._traverse(tree.root))


#test para buscar un nodo en especifico
print('\n*** Searching key in Tree ***\n')
test_keys = [33, 44, 2, 3, 4, 63, 1]

for key in test_keys:
    print('Searching for {}: {}'.format(key, tree.search(key)))


#testa para eliminar un nodo
print('\n*** Delete key in Tree ***\n')

print("Tree original")
print(tree._traverse(tree.root))

tree.delete(33)
tree.delete(77)
tree.delete(4)

print(tree._traverse(tree.root))

#test para hallar el valor minimo 

print('\n*** Minimum ***\n')

print(tree.min())

#test para hallar el valor maximo
print('\n*** Maximum ***\n')
print(tree.max())