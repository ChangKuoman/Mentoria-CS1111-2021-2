
### EJERCICIO ###

# USANDO LIST COMPREHENSION

# Escribir un programa que genere una lista con n numeros al azar del 1 al 9.
import random

n = int(input("N: "))

lista_normal= []
for i in range(n):
    lista_normal.append(random.randint(1, 9))
print(lista_normal)

lista = [random.randint(1, 9) for i in range(n)]
print(lista)

lista_pares = [i for i in lista if i%2==0]
print(lista_pares)

lista_impares = [i for i in lista if i%2!=0]
print(lista_impares)

lista_varios = [i if i%2==0 else "O" for i in lista]
print(lista_varios)
