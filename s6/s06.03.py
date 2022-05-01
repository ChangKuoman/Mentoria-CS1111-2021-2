
### EJERCICIO ###

# Teniendo en cuenta la siguiente matriz, imprimir la suma de la columna 2020 y la fila 'abr'.

meses = [
    ['mes', 2019, 2020, 2021],
    ['ene', 50,   16, 49],
    ['feb', 13,   47, 61],
    ['mar', 15,   82, 46],
    ['abr', 20,   17, 95] # 4
]

suma = 0

for i in range(1, len(meses)):
    suma += meses[i][2]
print(suma)

abril = 0
for i in range(1, len(meses[4])):
    abril += meses[4][i]
print(abril)

suma_total=0
for i in range(1, len(meses)):
    for j in range(1, len(meses[i])):
        suma_total += meses[i][j]

print(suma_total)
