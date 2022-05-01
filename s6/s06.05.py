
### EJERCICIO ###

# Escribir un programa que genere dos matrices de 5x5 con número al azar entre 1 y 10, luego cree una nueva matriz con la multiplicación de las dos matrices. Imprimir las 3 matrices.

# random.randint
import funciones as f

mat1 = f.crear_matriz()
mat2 = f.crear_matriz()

f.imprimir_matriz(mat1)
print()
f.imprimir_matriz(mat2)

matriz_resultado = f.crear_matriz()

for i in range(5):
    for j in range(5):
        matriz_resultado[i][j] = mat1[i][j] * mat2[i][j]

print()
f.imprimir_matriz(matriz_resultado)
