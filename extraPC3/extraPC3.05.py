
### EJERCICIO ###

# si la suma de la diagonal principal es mayor a la suma de los demas valores, en este caso diremos que una amtriz es diagonal
def es_diagonal(matriz, f, c):
    suma_diagonal = 0
    suma_resto = 0
    for i in range(f):
        for j in range(c):
            if i==j:
                suma_diagonal += matriz[i][j]
            else:
                suma_resto += matriz[i][j]

    if suma_diagonal > suma_resto:
        return 1
    else:
        return -1

matriz = [
    [78, 97, 66, 49, 79],
    [53, 61, 84, 8, 26],
    [70, 78, 44, 9, 66],
    [83, 97, 38, 84, 49],
    [27, 85, 24, 32, 41]
]

print(es_diagonal(matriz, len(matriz), len(matriz[0])))

matriz2 = [
    [12, 43, 82, 4],
    [12, 17, 71, 94],
    [82, 73, 20, 4],
    [28, 2, 52, 59],
    [19, 46, 2 , 67],
    [94, 80, 64, 16],
    [14, 84, 61, 69]
]

print(es_diagonal(matriz2, len(matriz2), len(matriz2[0])))
