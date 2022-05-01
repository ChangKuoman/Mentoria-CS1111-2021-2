
### EJERCICIO DE PC ###

"""
Este programa debera leer una frase y luego generara e imprimira tres cadenas
de caracteres con las siguientes caracteristicas:
• La primera cadena tendra todas las palabras de la frase que empiecen con vocal.
En caso no haya, imprimira el mensaje: No hay palabras con vocales.
• La segunda cadena tendra todas las palabras de la frase que empiecen con conso-
nante. En caso no haya, imprimira el mensaje: No hay palabras con consonantes.
• La tercera cadena tendra todas las palabras con mas de cuatro letras. En caso
ninguna palabra cumpla esto, imprimira un texto que diga: No hay palabras de
mas de cuatro letras.
"""

frase = "pan Queso tamal Agua Eco uso panecillo"
        #012
vocales = ""
consonantes= ""
cuatro = ""

for palabra in frase.split():
    if palabra[0] in "AEIOUaeiou":
        vocales += palabra +" "
    else:
        consonantes += palabra +" "
    if len(palabra) > 4:
        cuatro += palabra+" "

print(vocales)
print(consonantes)
print(cuatro)
