
### INTRODUCCION ###

# referencia a listas
lista = [1, 2, 3, 4, 5]

print(lista[1])

referencia = lista
otra_lista = lista[::]
otra_lista2 = lista.copy()

referencia[1] = 15
otra_lista[1] = 10
otra_lista2[1] = 50

print(lista)
print(referencia)
print(otra_lista)
print(otra_lista2)
