
### EJERCICIO ###

# crear una lista que tenga los elementos de una matriz siendo por columnas de arriba a abajo y luego de abajo a arriba y asi sucesivamente

matriz = [
# 0      2
# arriba a abajo
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
#     1
# abajo a arriba
]

lista = []

for i in range(len(matriz)):
  for j in range(len(matriz)):
    if i%2 == 0:
      lista.append(matriz[j][i])
    else:
      lista.append(matriz[len(matriz)-1-j][i])

print(lista)
