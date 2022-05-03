
# enunciado: img6

numeros = [10, 30, 110, 110.2, 20, 50, 2, 900, 2, 13]

for i in range(len(numeros)-1):
    for j in range(len(numeros)-1):

        if numeros[j] > numeros[j+1]:

            temp = numeros[j]
            numeros[j] = numeros[j+1]
            numeros[j + 1] = temp

            # numeros[j], numeros[j+1] = numeros[j+1], numeros[j]

print(numeros)
