
### EJERCICIO ###

# hallar recursivamente el promedio de una lista
def promedio_lista(lista, longitud):
    # caso base
    if lista == []:
        return None
    elif len(lista) == 1:
        return lista[0]/longitud
    # llamada recursiva
    else:
        return lista[0]/longitud + promedio_lista(lista[1:], longitud)

# lista = [15, 18, 16, 13, 14]
# print(promedio_lista(lista, len(lista)))
