
### EJERCICIO ###

# AAA -> 3A

# AAAAAAAAAAAA -> NO 12A SINO 9A3A

# AAAAAAAAAAAABBCCCCDD -> 9A4A2B4C2D

cadena = str(input("CADENA: "))
nueva_cadena = ""

char = cadena[0]
contador = 0
for i in range(len(cadena)):
    if cadena[i] == char and contador < 10:
        contador += 1
        if contador == 9:
            nueva_cadena += "9" + char
            contador = 0
    else:
        if contador != 0:
            nueva_cadena += str(contador) + char
            char = cadena[i]
            contador = 1
        else:
            char = cadena[i]
            contador = 1
nueva_cadena += str(contador) + char

print(nueva_cadena)
