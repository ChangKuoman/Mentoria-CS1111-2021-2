
### EJERCICIO DE PC ###

"""
Desarrollar e implentar un programa que permita formar dos listas de numeros
enteros con datos aleatorios del 0 al 50. El tamaño de cada lista sera ingresado como
dato. Cada lista representa a un conjunto por lo tanto no contendra elementos
repetidos. Con estas listas realice lo siguiente:
• Imprima cada lista
• Por medio de la una funcion Interseccion, halle la lista interseccion, es decir
aquella que contiene los elementos comunes a ambas listas. La funcion debe recibir
como parametros las dos listas y formar la lista interseccion de modo tal que no
contenga elementos repetidos.
"""

from random import randint
n = int(input("n: "))

lista1=[]
lista2=[]
for i in range(n):
    lista1.append(randint(0, 50))
    lista2.append(randint(0, 50))

[1, 86, 2]
[5, 7, 2]

def interseccion(lista1, lista2, n):
    lista_comunes = []

    for i in range(n):
        for j in range(n):
            if lista1[i] == lista2[j] and lista1[i] not in lista_comunes:
                lista_comunes.append(lista1[i])

    return lista_comunes

print(lista1)
print(lista2)
print(interseccion(lista1, lista2, n))
