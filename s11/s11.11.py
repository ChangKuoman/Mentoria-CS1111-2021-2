
### EJERCICIO ###

# crear una matriz 5 x 5 con numeros al azar del 1 al 9
from random import randint as rd


# usando list comprehension
matriz = [[rd(0, 9) for i in range(5)] for i in range(5)]

for i in matriz:
    print(i)


# usando fors
matriz = []
for i in range(5):
    matriz.append([])
    for j in range(5):
        matriz[i].append(rd(0, 9))

print()
for i in matriz:
    print(i)
