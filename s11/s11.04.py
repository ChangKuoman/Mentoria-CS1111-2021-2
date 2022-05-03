
### EJERCICIO ###

# crear una matriz de n x n y tenga en la diagonal principal un caracter y lo demas un asterisco

n = int(input("Ingrese tamanio: "))
char = str(input("Ingrese caracter: "))

matriz = []
for i in range(n):
    matriz.append([])
    for j in range(n):
        if i == j:
            matriz[i].append(char)
        else:
            matriz[i].append("*")

for i in range(n):
    for j in range(n):
        print(matriz[i][j], end=" ")
    print()
