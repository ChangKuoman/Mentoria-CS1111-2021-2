
### EJERCICIO ###

# matrix
def imprimir_matriz(mat):
    for i in mat:
        for j in i:
            print(j, end=" ")
        print()

def crear_matriz_vacia(matriz):
    mat = []
    for i in range(len(matriz)):
        mat.append([])
        for j in range(len(matriz[0])):
            mat[i].append(0)
    return mat

matriz = [
    [5, 4, 2],
    [1, 2, 3],
    [0, 6, 7]
]
matriz2 = [
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [0, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 0]
]

print("INPUT:")
imprimir_matriz(matriz2)

print()

def rotar_matriz(matriz):
    matriz_rotada = crear_matriz_vacia(matriz)
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            matriz_rotada[i][j] = matriz[len(matriz)-1-j][i]
    return matriz_rotada

matriz_rotada = rotar_matriz(matriz2)
imprimir_matriz(matriz_rotada)
print()

matriz_rotada = rotar_matriz(matriz_rotada)
imprimir_matriz(matriz_rotada)
