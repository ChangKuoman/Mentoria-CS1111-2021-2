
### EJERCICIO ###

# Escribir un programa que genere una lista de 10 números al azar del 1 al 20 y genere una segunda lista en la cual si el número es mayor a 5 se eleva al cuadrado. Imprimir ambas listas.

from random import randint

lista = []
potencia = []
for i in range(10):
    n = randint(1, 20)
    lista.append(n)
    if n > 5:
        potencia.append(n ** 2)

print(lista)
print(potencia)
