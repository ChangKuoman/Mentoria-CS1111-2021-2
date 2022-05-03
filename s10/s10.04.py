
### EJERCICIO ###

# Escribir un programa que lea un archivo .txt e imprima palabra por palabra.

archivo = open("data.txt", "r")

for linea in archivo:
    for palabra in linea.split(","):
        print(palabra)

archivo.close()
