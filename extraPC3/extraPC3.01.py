
### EJERCICIO ###

# list comprehension
def funcion1(lista):
    nueva_lista = [i**2 for i in lista if i%2==0 and i%6!=0]
    return nueva_lista


print(funcion1([1, 2, 3, 4, 5, 6, 7, 8]))


def funcion2(filas, columnas, valor):
    matriz = [[valor for j in range(columnas)] for i in range(filas)]
    return matriz


print(funcion2(3, 2, 1))


def funcion3(lista):
    pares = [i for i in lista if i%2 == 0]
    impares = [i for i in lista if i%2 != 0]
    return pares, impares

# a, b = funcion3([1, 2, 3, 4, 5, 6, 7, 8])
# print(a)
# print(b)
#
# c = funcion3([1, 2, 3, 4, 5, 6, 7, 8])
# print(c)


print(funcion3([1, 2, 3, 4, 5, 6, 7, 8]))


def funcion4(matriz):
    matriz2 = [y for x in matriz for y in x]
    return matriz2


print(funcion4([[1, 2, 3], [4, 5, 6]]))

tupla = (14, 15)
lista = [14, 15]

print(tupla)
print(lista)

print(funcion1([2, 6, 12, 14]))
print(funcion2(3, 4, 0))
print(funcion3([2, 6, 12, 14]))
print(funcion4([[1, 2], [3, 4], [5, 6]]))
