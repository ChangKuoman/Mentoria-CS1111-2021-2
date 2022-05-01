
### EJERCICIO ###

# Escribir un programa que solicite al usuario una frase y esta se guarde letra por letra en una matriz cuadrada adecuada a la longitud de la frase y llene los espacios vacios con “*”.

# pan
# [
#  [p , a]
#  [n , *]
# ]

# atun
# [
#  [a , t]
#  [u , n]
# ]

import funciones as f
import math

frase = str(input("FRASE: "))
# 1. Hallar nxn
tamano = math.ceil(math.sqrt(len(frase))) #1.73 --> 2 | 5.77962 --> 6 | 1.1 --> 2

# 2. Crear una matriz de nxn
matriz = f.crear_matriz_2(tamano)

# print(tamano)
# f.imprimir_matriz(matriz)

# 3. Agregar los datos
# frase = pollito --> len(frase) = 7
#         0123456
contador = 0
for i in range(tamano):
    for j in range(tamano):
        if contador < len(frase):
            matriz[i][j] = frase[contador]
            contador += 1

f.imprimir_matriz(matriz)
