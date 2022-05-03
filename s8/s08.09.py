
### EJERCICIO ###

# revertir una frase sin el uso de slices ni .reverse()
# INPUT= buenas tardes joven
# OUTPUT= joven tardes buenas

cadena = str(input("INPUT= "))

def reversa(cadena):
    cadena += " "
    oracion = ""
    palabra = ""

    for i in cadena:
        if i != " ":
            palabra += i
        else:
            oracion = palabra + " " + oracion
            palabra = ""

    return oracion

print(reversa(cadena))
