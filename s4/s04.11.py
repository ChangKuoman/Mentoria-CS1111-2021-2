
### EJERCICIO DE PC ###

"""
Este programa debera leera una frase y luego generara e imprimira tres frases
con las siguientes caracteristicas:
• La primera frase tendra todas las palabras pares de la frase. (longitud par)
• La segunda frase tendra todas las palabras de la frase con menos de cinco letras.
• La tercera frase tendra todas las palabras que empiecen con letras desde la A a la
M, sin importar si es en minuscula o mayuscula.
Ingrese un texto : Me dejo por un pan con queso
Me dejo un
Me dejo por un pan con
Me dejo con
"""

frase = "Me dejo por un pan con queso"
pares = ""
cinco = ""
letraam = ""
abc = "abcdefghijklm"
for palabra in frase.split():
    if len(palabra) % 2 == 0:
        pares += palabra +" "
    if len(palabra) < 5:
        cinco += palabra +" "
    if palabra[0].lower() in abc:
        letraam += palabra +" "

print(pares)
print(cinco)
print(letraam)
