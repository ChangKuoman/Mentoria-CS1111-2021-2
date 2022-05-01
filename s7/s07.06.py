
### EJERCICIO DE PC ###

def SplitList(lista, sep):
    result = []
    sub_lista = []
    for i in lista:
        if i == sep:
            result.append(sub_lista)
            sub_lista = []
            continue
        sub_lista.append(i)
    result.append(sub_lista)
    return result


lista = [5, 2, 0, 1, 3, 6, 0, 4, 6]
separador = 0
print(SplitList(lista, separador))

lista = [8, 3, -1, 4, 3, 10]
separador = -1
print(SplitList(lista, separador))

lista = [8, 3, 4, 3, 10]
separador = -1
print(SplitList(lista, separador))
