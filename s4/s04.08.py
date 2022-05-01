
### EJERCICIO ###

# Escribir un programa en el cual se ingrese una palabra e imprimir la palabra pero con las vocales en mayúsculas y las consonantes en minúsculas, no considere números.

frase = str(input("Ingrese frase: "))

frase2 = ""
for letra in frase:
    if letra in "aeiouAEIOU":
        frase2 += letra.upper()
    else:
        frase2 += letra.lower()

print(frase2)
