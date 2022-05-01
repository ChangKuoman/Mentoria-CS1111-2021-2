
### EJERCICIO DE PC ###

"""
Dada la siguiente matriz de numeros:
14 25 72 27
16 26 52 65
24 24 45 23
26 35 51 27
17 31 72 21
18 51 23 14
Implemente un algoritmo que haga lo siguiente:
• Escriba la matriz de datos en el programa principal
• Solicite ingresar un numero y el programa debe mostrar en pantalla, lo siguiente:
La suma de la columna, considerando al numero como  ́ındice de la columna,
El mayor numero de la fila, considerando al numero como  ́ındice de la fila.
Numero : 3
Suma de la columna 3: 177
Mayor de la fila 3: 51
"""

numeros = [
    [14, 25, 72, 27],
    [16, 26, 52, 65],
    [24, 24, 45, 23],
    [26, 35, 51, 27], #3
    [17, 31, 72, 21],
    [18, 51, 23, 14]
]

n = int(input("Número: "))

suma=0
for i in range(6):
    suma += numeros[i][n]

mayor = numeros[n][0]
for i in range(4):
    if numeros[n][i] > mayor:
        mayor = numeros[n][i]

print(f"La suma de la columna {n}: es {suma}")
print(f"El numero mayor de la fila {n}: es {mayor}")
