
### EJERCICIO DE PC ###

# PC3 2020-1 2
def imprimir_matriz(mat):
    for i in mat:
        for j in i:
            print(j, end=" ")
        print()

linea = str(input("INPUT (a b n)= "))

lista = [int(i) for i in linea.split()]

# lista2 = [i for i in range(a, b) if i%2==0]
# print(lista2)

a, b, n = lista

aux = a
matriz = []
for i in range(n):
    matriz.append([])
    for j in range(n):
        matriz[i].append(aux)
        aux += 1
        if aux == b+1:
            aux = a

imprimir_matriz(matriz)

columna = int(input("Ingrese columna: "))
while columna < 0 or columna >=n:
    columna = int(input("Ingrese columna: "))

suma = 0
for i in range(n):
    suma += matriz[i][columna]
print(f"Promedio: {suma/n}")
