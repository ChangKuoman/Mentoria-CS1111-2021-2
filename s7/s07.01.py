
### INTRODUCCION ###

# pintar matrices
matriz = [
    [2, 0, 7, 1, 8],
    [6, 2, 7, 5, 9],
    [3, 0, 4, 8, 9],
    [0, 8, 5, 3, 9],
    [4, 3, 3, 2, 3],
    [3, 6, 3, 3, 1],
    [9, 3, 1, 4, 1],
    [0, 9, 3, 3, 6]
]

def imprimir_matriz(matriz):
    for i in matriz:
        for j in i:
            print(j, end=" ")
        print()

imprimir_matriz(matriz)

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if matriz[i][j] == 9:
            matriz[i][j] = 0

print()
print()
imprimir_matriz(matriz)
