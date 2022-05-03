
### INTRODUCCION ###

# list comprehension
lista = []
for i in range(5):
    lista.append(i)

print(lista)

lista1 = [i for i in range(5)]

print(lista1)

lista2 = [i for i in range(20) if i%2==0]

print(lista2)

matriz = [[i for i in range(5)] for j in range(5)]

print(matriz)
