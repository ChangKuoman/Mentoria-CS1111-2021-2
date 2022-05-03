
### EJERCICIO DE PC ###

"""
Utilizando diccionarios evaluar un texto y generar un diccionario con las letras
en min ́uscula como keys y como valor una lista con las posiciones donde aparece la letra
en el texto.
"""

# tener un diccionario
# key: string  |  value: lista
# input -> string
# ouput -> diccionario

dic = {}

# "a":[1, 5, 8] , "b": [7, 6, 10]

# hola dia
# "h":[0]
# "o":[1]
# "l":[2]
# "a":[3]

# "a":[7] X crear
# "a":[3, 7] si aniadir

cadena = str(input("Ingrese cadena= ")).lower()

for i in range(len(cadena)):
    letra = cadena[i]

    if letra not in dic.keys(): # no existe la clave
        dic[letra] = [i]

    else:                       # si existe
        dic[letra].append(i)
#       [1, 5, 8] <-- i

print(dic)
