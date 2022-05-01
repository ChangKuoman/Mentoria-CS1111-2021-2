
### INTRODUCCION ###

# string
cadena = "Cholotate"

# .count()
contador = 0
for i in range(len(cadena)):
    if cadena[i] == "o":
        contador += 1

print(contador)
print(cadena.count("o"))

# .find()
for i in range(len(cadena)):
    if cadena[i] == "o":
        print(i)
        break

print(cadena.find("o"))

# concatenando
cadena2 = ""
cadena2 += "H"
for i in range(1, len(cadena)):
    cadena2 += cadena[i]
print(cadena2)

# .replace()
nueva = cadena.replace("o", "i")
print(nueva)

nueva_cadena = ""
for i in range(len(cadena)):
    if cadena[i] == "o":
        nueva_cadena += "i"
    else:
        nueva_cadena += cadena[i]

print(nueva_cadena)
