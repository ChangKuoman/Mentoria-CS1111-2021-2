
# crear una matriz n x n y realizar la suma de la diagonal principal

import random

matriz = [
  #  0  1  2
    [1, 2, 3], # 0
    [4, 5, 6], # 1
    [7, 8, 9]  # 2
] # 0,0  1,1  2,2 ...... i,i

mat = [
    [1, 4],
    [9, 6]
]

def suma_diagonal_principal(matriz):
    suma = 0
    for i in range(0, len(matriz)):
        suma += matriz[i][i]
    return suma

# n x n
def generar_matriz_cuadrada(n):
    matriz = []
    # while / for ?
    for i in range(n):
        matriz.append([])
        for j in range(n):
            matriz[i].append(random.randint(1, 9))

    return matriz


matriz2 = generar_matriz_cuadrada(7)

for i in matriz2:
    print(i)

print(suma_diagonal_principal(matriz2))
