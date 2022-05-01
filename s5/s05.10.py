
### EJERCICIO ###

# Escribir un programa que solicite al usuario una palabra y use una función para verificar si contiene las letras de “p”, “a” y “n”, la función debe retornar un booleano.

cadena = str(input("palabra: "))

def letra(abc):
    p = False
    a = False
    n = False
    for i in abc:
        #i = p, i = a
        if i == "p":
            p = True
        elif i == "a":
            a = True
        elif i == "n":
            n = True
    return p and a and n

print(letra(cadena))
