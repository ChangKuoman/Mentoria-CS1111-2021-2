
### EJERCICIO ###

# hallar recursivamente el promedio de los numeros pares de una lista
def promedio_lista_pares(lista, cantidad):
    # caso base
    if lista == []:
        return None
    elif len(lista) == 1:
        if lista[0] % 2 == 0:
            return lista[0]/cantidad
        else:
            return 0
    # llamada recursiva
    else:
        if lista[0] % 2 == 0:
            return lista[0]/cantidad + promedio_lista_pares(lista[1:], cantidad)
        else:
            return 0 + promedio_lista_pares(lista[1:], cantidad)

def hallar_cantidad_pares(lista):
    # caso base
    if lista == []:
        return None
    elif len(lista) == 1:
        return not lista[0] % 2
    # llamada recursiva
    else:
        if lista[0] % 2 == 0:
            return 1 + hallar_cantidad_pares(lista[1::])
        else:
            return 0 + hallar_cantidad_pares(lista[1::])

lista = [10, 7, 13, 20, 9, 7, 5]
print(promedio_lista_pares(lista, hallar_cantidad_pares(lista)))
lista = [2, 4, 6, 8, 10, 11, 12]
print(promedio_lista_pares(lista, hallar_cantidad_pares(lista)))
