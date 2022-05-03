
### EJERCICIO ###

# USANDO LIST COMPREHENSION

# Crear un matriz de nxn numeros al azar del 10 al 99. Generar otra matriz con los numeros que sean mayores a 50 y si no cumple reemplazar por “O”. Imprimir ambas matrices
from random import randint as rd
n = int(input("N: "))

matriz = [[rd(10, 99) for i in range(n)] for j in range(n)]

matriz2 = [[matriz[j][i] if matriz[j][i]<50 else -1 for i in range(n)] for j in range(n)]

for i in matriz:
    print(i)
print()
for i in matriz2:
    print(i)
