
# ordenando una lista de strings

lista = ["Zach", "Maria", "Amelia", "Carlos", "Arian"]

for i in range(len(lista) - 1):
    for j in range(len(lista) - 1):

        if lista[j] > lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]

print(lista)
