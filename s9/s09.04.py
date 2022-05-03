
### EJERCICIO ###

# Escribir un programa que pida una cadena de texto y cuente la cantidad de vocales, consonantes, numeros y espacios y los agregue a un diccionario.

vocales = {"a":0, "e":0, "i":0, "o":0, "u":0}

cadena = str(input("Ingrese cadena: "))

for letra in cadena:
    if letra == "a":
        vocales["a"] += 1
    elif letra == "e":
        vocales["e"] += 1
    elif letra == "i":
        vocales["i"] += 1
    elif letra == "o":
        vocales["o"] += 1
    elif letra == "u":
        vocales["u"] += 1

print(vocales)

cantidades = {"vocales":0, "consonantes":0, "numeros":0, "espacios":0}

for letra in cadena:
    if letra in "aeiouAEIOU":
        cantidades["vocales"] += 1
    elif letra == " ":
        cantidades["espacios"] += 1
    elif letra in "0123456789":
        cantidades["numeros"] += 1
    elif letra == ".":
        continue
    else:
        cantidades["consonantes"] += 1

print(cantidades)
