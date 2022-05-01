
### EJERCICIO DE PC ###

"""
Escribe aqui el enunciado de tu pregunta: Disenie e implemente un programa,
que permita registrar: el nombre, edad, peso y talla de ”n” personas. Estos datos se
registrarán en una lista de listas (matriz), para luego realizar los siguiente:
• Imprimir la lista (matriz)
• Imprimir el nombre de la persona mas joven
• Imprimir el nombre de la persona mas alta
• Hallar e imprimir el peso de todos las personas en conjunto.
"""
# [
#   [nombre, edad, peso, talla],
#   [nombre, edad, peso, talla],
#   [nombre, edad, peso, talla],
#   [nombre, edad, peso, talla]
#
# ]

import funciones as f

n = int(input("n: "))
matriz = []

for i in range(n):
    nombre = str(input("nombre: "))
    edad = int(input("edad: "))
    peso = float(input("peso: "))
    talla = int(input("talla: "))
    matriz.append( [ nombre, edad, peso, talla ] )

print("MATRIZ:")
f.imprimir_matriz(matriz)

edad_menor = matriz[0][1]
indice = 0
for i in range(n):
    if edad_menor > matriz[i][1]:
        edad_menor = matriz[i][1]
        indice = i
print(matriz[indice][0])

talla_alta = matriz[0][3]
indice = 0
for i in range(n):
    if talla_alta < matriz[i][3]:
        talla_alta = matriz[i][3]
        indice = i
print(matriz[indice][0])

suma_pesos = 0
for i in range(n):
    suma_pesos += matriz[i][2]
print(suma_pesos)

print(f"El promedio de los pesos es {suma_pesos/n}.")
print("El promedio de los pesos es {}.".format(suma_pesos/n))
