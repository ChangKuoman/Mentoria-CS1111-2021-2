
### EJERCICIO ###

# Pedir a usuario que ingrese una frase y si la palabra comienza por una vocal el programa imprime la palabra.

frase = str(input("Ingrese frase: "))

consonantes = 0
vocales = 0
for letra in frase:
    #if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    if letra in "aeiouAEIOU":
        vocales += 1
    elif letra in " .,*/-1234567890":
        continue
    else:
        consonantes += 1

print(vocales)
print(consonantes)
print(vocales + consonantes)
print(len(frase))
