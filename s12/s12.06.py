
### EJERCICIO ###

# sumar recursivamente los elementos de una lista
def suma_lista(lista):
    # caso base
    if lista == []:
        return None
    elif len(lista) == 1:
        return lista[0]
    # llamada recursiva
    else:
        return lista[0] + suma_lista(lista[1:])

# ITERATIVA:
# suma = 0
# for i in range(len(lista)):
#     suma += lista[i]

# lista = [45]
# lista = []
lista = [10.2, 20.45, 30.10]
print(suma_lista(lista))
