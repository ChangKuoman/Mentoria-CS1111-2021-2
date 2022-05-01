
### EJERCICIO ###

# Escribir un programa que solicite al usuario una frase e ingrese las vocales a una una lista y las consonantes a otra, sin repetirse.

cadena = str(input("cadena: "))
vocales = []
consonantes = []

for i in cadena:
    if i in "aeiouAEIOU":
        if i not in vocales:
            vocales.append(i)
    elif i == " ":
        continue
    else:
        if i not in consonantes:
            consonantes.append(i)

print(vocales)
print(consonantes)

lista = ["a", "a", "a"]
print(lista.count("a"))
