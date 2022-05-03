
### INTRODUCCION ###

# busqueda
import matplotlib.pyplot as plt
from random import randint as rd

def busqueda_lineal(lista, elemento):
    iter = 0
    for i in lista:
        iter += 1
        if i == elemento:
            break
    return iter

x = []
y = []
for i in range(50):
    lista = [rd(1, 100) for x in range(i)]
    iter = busqueda_lineal(lista, rd(1, 100))
    x.append(i)
    y.append(iter)

def busqueda_binaria_recursiva(lista, x, iter=1):
    #caso base
    if len(lista) == 1:
        return lista[0] == x, iter
    n = len(lista)
    i_mitad = n//2
    if lista[i_mitad] == x:
        return True, iter
    #llamada recursiva
    elif lista[i_mitad] < x:
        return busqueda_binaria_recursiva(lista[i_mitad:], x, iter+1)
    elif lista[i_mitad] > x:
        return busqueda_binaria_recursiva(lista[:i_mitad], x, iter+1)

def busqueda_binaria_iterativa(lista, x):
    low = 0
    high = len(lista) - 1
    resultado = False
    while low <= high:
        mid = low + (high-low)//2

        if lista[mid] == x:
            resultado = True
            break
        elif x < lista[mid]:
            high = mid - 1
        elif x > lista[mid]:
            low = mid + 1

    return resultado

x2 = []
y2 = []
for i in range(1, 50):
    lista = [rd(1, 100) for x in range(i)]
    estado, iter = busqueda_binaria_recursiva(lista, rd(1, 100))
    x2.append(i)
    y2.append(iter)

plt.plot(x, y, 'r.', x2, y2, 'b.')
plt.show()
