
### EJERCICIO ###

def merge(lista, left, right):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i]['nombre'] < right[j]['nombre']:
              lista[k] = left[i]
              i+=1
              k+=1
        else:
            lista[k] = right[j]
            j+=1
            k+=1
    while i < len(left):
        lista[k] = left[i]
        i += 1
        k +=1
    while j < len(right):
        lista[k] = right[j]
        j += 1
        k +=1

def merge_sort(lista):
    if len(lista) > 1:
        mid = len(lista) // 2
        left = lista[:mid]
        right = lista[mid:]
        merge_sort(left)
        merge_sort(right)
        merge(lista, left, right)

# Implementar un codigo que ordene por nombre la siguiente lista y luego pida ingresar el nombre de un postre e imprima la informacion del postre (usando cualquier algoritmo de ordenamiento y busqueda binaria)

comidas = [
  {'nombre':'Pie de Limon', 'pais':'Francia', 'ingrediente':'Limon'},
  {'nombre':'Mazamorra Morada', 'pais':'Peru', 'ingrediente':'Maiz Morado'},
  {'nombre':'Jericalla', 'pais':'Mexico', 'ingrediente':'Leche'},
  {'nombre':'Pastel de Luna', 'pais':'China', 'ingrediente':'Manteca'}
]

merge_sort(comidas)
for i in comidas:
    print(i)

def busqueda_binaria_recursiva(lista, x, indice=0):
    #caso base
    if len(lista) == 1:
        if lista[0]['nombre'] == x:
            return indice
        else:
            return -1

    n = len(lista)
    i_mitad = n//2
    if lista[i_mitad]['nombre'] == x:
        return lista.index(lista[i_mitad]) + indice

    #llamada recursiva
    elif lista[i_mitad]['nombre'] < x:
        return busqueda_binaria_recursiva(lista[i_mitad:], x, indice + i_mitad)
    elif lista[i_mitad]['nombre'] > x:
        return busqueda_binaria_recursiva(lista[:i_mitad], x, indice)

nombre = str(input("POSTRE: "))
indice = busqueda_binaria_recursiva(comidas, nombre, indice=0)
if indice != -1:
    print(comidas[indice])
else:
    print("no se encontro el postre")
