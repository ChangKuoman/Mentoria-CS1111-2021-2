
### INTRODUCCION ###

def busqueda_binaria_recursiva(lista, x, indice=0):
    #caso base
    if len(lista) == 1:
        if lista[0] == x:
            return lista.index(x) + indice
        else:
            return -1

    n = len(lista)
    i_mitad = n//2
    if lista[i_mitad] == x:
        return lista.index(x) + indice

    #llamada recursiva
    elif lista[i_mitad] < x:
        return busqueda_binaria_recursiva(lista[i_mitad:], x, indice + i_mitad)
    elif lista[i_mitad] > x:
        return busqueda_binaria_recursiva(lista[:i_mitad], x, indice)

lista = [10, 45, 63, 80, 95]

print(busqueda_binaria_recursiva(lista, 95))

# sorted()
# .sort()
