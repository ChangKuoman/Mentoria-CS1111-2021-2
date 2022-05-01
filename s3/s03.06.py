
### EJERCICIO DE PC ###

"""
Desarrolle un programa que permita dibujar un rectangulo, segun la cantidad
de filas y columnas.
• El numero de las filas debe ser mayor a 2. El programa debera verificar el ingreso
del dato.
• El numero de las columnas debe ser mayor a 4. El programa debera verificar el
ingreso del dato.
• El rectangulo se construye imprimiendo un ”*” en los bordes del rectangulo y ”o”
al medio, tal y como se muestra en los ejemplos:
Filas [ mayor a 2] :7
Columnas [ mayor a 4] : 9
* * * * * * * * *
* o o o o o o o *
* o o o o o o o *
* o o o o o o o *
* o o o o o o o *
* o o o o o o o *
* * * * * * * * *
"""

fila = int(input("Fila: "))
while fila<2:
    fila = int(input("Fila: "))

columna = int(input("Columna: "))
while columna<4:
    columna = int(input("Columna: "))

for i in range(fila):
    for j in range(columna):
        if i==0 or i==fila-1 or j==0 or j==columna-1:
            print("*", end=" ")
        else:
            print("o", end=" ")
    print()
