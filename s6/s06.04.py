
### EJERCICIO ###

# Teniendo en cuenta la siguiente matriz, imprimir la suma del total de medallas y el total de cada país.

tokyo2020 = [
    ['País', 'Oro', 'Plata', 'Bronce'], #0
    ['EEUU', 39, 41, 33], # 1
    ['China', 38, 32, 18], # 2
    ['Japón', 27, 14, 17] #3
]

# cual es mas legible: todo en una linea o en varias?
# tokyo2020 = [ ['País', 'Oro', 'Plata', 'Bronce'], ['EEUU', 39, 41, 33], ['China', 38, 32, 18], ['Japón', 27, 14, 17] ]
# matriz_chiquita = [[1, 4], [5, 8]]

# {} llave    --> diccionarios
# [] corchete --> listas

eeuu = 0
china = 0
japon = 0
for i in range(1, len(tokyo2020[1])):
    eeuu += tokyo2020[1][i]
    china += tokyo2020[2][i]
    japon += tokyo2020[3][i]

print(eeuu)
print(china)
print(japon)

suma_total = 0
for i in range(1, len(tokyo2020)):
    for j in range(1, len(tokyo2020[i])):
        suma_total += tokyo2020[i][j]

print(suma_total)
