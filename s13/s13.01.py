
### EJERCICIO DE PC ###

"""
Escribe una funcion recursiva que calcule la multiplicacion de una lista que contiene otras listas.
Usar: if type(element) is list:
output = 960
"""
lista = [2 ,3 ,4 ,[2 ,4 ,5]]

def multiplicar_lista(lista):
    if len(lista) == 1:
        if type(lista[0]) is list:
            return multiplicar_lista(lista[0])
        else:
            return lista[0]
    else:
        if type(lista[0]) is list:
            return multiplicar_lista(lista[0]) * multiplicar_lista(lista[1:])
        else:
            return lista[0] * multiplicar_lista(lista[1:])

print(multiplicar_lista(lista))
