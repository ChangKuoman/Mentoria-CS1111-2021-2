
### INTRODUCCION ###

# matrix
import funciones as f

# ¿Qué es una matriz? --> lista de listas
# Ejemplo --> [ [12, 6], [17, 96], [4, 6] ]

matriz = [
    [41, 8], #0
    [5, 8], #1
    [7, 9, 5, 6] #2
]

def imprimir_2(matriz):

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print()

f.imprimir_matriz(matriz)
imprimir_2(matriz)
