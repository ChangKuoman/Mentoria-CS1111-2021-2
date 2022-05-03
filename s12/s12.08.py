
### EJERCICIO ###

# hallar recursivamente la suma de los numeros pares de una lista
def suma_lista_pares(lista):
    # caso base
    if lista == []:
        return None
    elif len(lista) == 1:
        if lista[0] % 2 == 0:
            return lista[0]
        else:
            return 0
    # llamada recursiva
    else:
        if lista[0] % 2 == 0:
            return lista[0] + suma_lista_pares(lista[1:])
        else:
            return 0 + suma_lista_pares(lista[1:])

lista = [10, 7, 13, 20, 9, 7, 5]
print(suma_lista_pares(lista))
