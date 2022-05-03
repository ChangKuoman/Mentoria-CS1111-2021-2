
### EJERCICIO ###

# reemplazar la a por 1 la e por 2 la i por 3 la o por 4 la u por 5 la A por 6 la E por 7 la I por 8 la O por 9 y la U por 0

cadena = str(input("CADENA: ")) #inmutable
cadena = cadena.replace("a", "1")
cadena = cadena.replace("e", "2")
cadena = cadena.replace("i", "3")
cadena = cadena.replace("o", "4")
cadena = cadena.replace("u", "5")
cadena = cadena.replace("A", "6")
cadena = cadena.replace("E", "7")
cadena = cadena.replace("I", "8")
cadena = cadena.replace("O", "9")
cadena = cadena.replace("U", "0")
print(cadena)

cadena = str(input("CADENA: ")) #inmutable
cadena2 = ""
for i in cadena:
    if i == "a":
        cadena2 += "1"
    elif i == "e":
        cadena2 += "2"
    elif i == "i":
        cadena2 += "3"
    elif i == "o":
        cadena2 += "4"
    elif i == "u":
        cadena2 += "5"
    elif i == "A":
        cadena2 += "6"
    elif i == "E":
        cadena2 += "7"
    elif i == "I":
        cadena2 += "8"
    elif i == "O":
        cadena2 += "9"
    elif i == "U":
        cadena2 += "0"
    else:
        cadena2 += i
print(cadena2)
