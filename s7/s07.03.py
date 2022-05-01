
### EJERCICIO DE PC ###

def analizar(lista1, lista2):
    nueva_lista = []
    for i in range(len(lista1)):
        suma = 0
        for j in range(i + 1):
            suma += lista2[j]
        nueva_lista.append(lista1[i] * suma)
    return nueva_lista


lista1 = [2, 3, 4, 5, 6]
lista2 = [5, 6, 7, 8, 9]
# 2 * 5 = 10
# 3 * (5+6) = 33
# 4 * (5+6+7) = 72
# 5 * (5+6+7+8) = 130
# 6 * (5+6+7+8+9) = 210
print(analizar(lista1, lista2))
