
### EJERCICIO ###

matriz = [
    [14, 25, 72, 27],
    [16, 26, 52, 65],
    [24, 24, 45, 23],
    [26, 35, 51, 27],
    [17, 31, 72, 21],
    [18, 51, 23, 14]
]

# Numero: 3
# Suma de la columna 3: 177
# Mayor de la fila 3: 51

def ejercicio_matriz():
    numero = int(input("Número: "))

    suma = 0
    for i in range(len(matriz)):
        suma += matriz[i][numero]

    print(f"Suma de la columna {numero}: {suma}")

    mayor = matriz[numero][0]
    for i in matriz[numero]:
        if i > mayor:
            mayor = i
    print(f"El mayor de la fila {numero}: {mayor}")

ejercicio_matriz()
