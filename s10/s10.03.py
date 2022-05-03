
### EJERCICIO ###

# Escribir un programa que lea un archivo .txt e imprima solo las lineas pares, siendo la primera 1.

# range(0, n)
# [0, 1, 2, 3]
#
# 1 -> 0
# 2 -> 1
# 3 -> 2
# 4 -> 3

file = open("archivo.txt", "r")

print(file)
texto = file.readlines()

for i in range(len(texto)):
    if i%2==0:
        print(texto[i+1])
    if i%2!=0:
        print(texto[i])

file.close()
