
### EJERCICIO DE PC ###

"""
Disenie e implemente un programa que permita leer una cadena de ADN y el
programa genere e imprima la cadena complementaria, respetando la correspondencia
entre las bases: (A - T, C - G).
Cadena de ADN : acgttgcaaaccggtt
Cadena de ADN : ACGTTGCAAACCGGTT
Cadena complementaria : TGCAACGTTTGGCCAA
"""
# a --> t
# t --> a
# c --> g
# g --> c

adn = str(input("adn: "))

complemento = ""
for letra in adn.lower():
    if letra == "a":
        complemento += "T"
    elif letra == "t":
        complemento += "A"
    elif letra == "c":
        complemento += "G"
    elif letra == "g":
        complemento += "C"

print("El complemento es: {}".format(complemento))
