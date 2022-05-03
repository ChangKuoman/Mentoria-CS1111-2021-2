
# enunciado: img7

test1 = [5, 4, 1, 2, 8, 3, 2, 9]
# output esperado: 2

test2 = [4, 1, 9, 3, 10, 6, 4, 3]
# output esperado: 3

test3 = [8, 3, 4, 8, 2, 1, 6, 7]
# output esperado: 2

def ordenar_hallar_elemento(lista):
    for i in range(len(lista) - 1):
        for j in range(len(lista) - 1):

            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

    elemento = lista[2]
    return elemento

print(ordenar_hallar_elemento(test1))
print(ordenar_hallar_elemento(test2))
print(ordenar_hallar_elemento(test3))
