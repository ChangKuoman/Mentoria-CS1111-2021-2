
# enunciado: img1

def elimina_duplicados(lista):
    lista_unicos = []
    for i in lista:
        if i not in lista_unicos:
            lista_unicos.append(i)

    return lista_unicos

lista = [4, 5, 8, 6, 1, 4, 5]
# output esperado = [4, 5, 8, 6, 1]

print(elimina_duplicados(lista))
