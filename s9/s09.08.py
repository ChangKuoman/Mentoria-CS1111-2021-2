
### EJERCICIO DE PC ###

"""
Escribir un programa en Python que cree un diccionario de traducci ́on INGLES-
ESPANOL.  ̃
• Ingresar datos desde teclado [clave:valor]y almacenarlos en un diccionario (obliga-
torio).
• Si ingresa una palabra que existe debe agregar un sin ́onimo.
• Mostrar las palabras que tienen 2 o mas sin ́onimos en ingles.
• Ingresar ”salir” para terminar de ingresar
Input : mirar , look
Input : perro , dog
Input : mirar , watch
Output :
mirar :[ look , watch ]
"""

diccionario_ingles = {}

while True:

    cadena = str(input("Input (espanol, ingles): ")).lower()

    if cadena == "salir":
        break

    palabras = cadena.split(',')

    espaniol = palabras[0] # espaniol
    ingles = palabras[1] # inglés

    if espaniol not in diccionario_ingles.keys():
        diccionario_ingles[espaniol] = [ingles]
    else:
        diccionario_ingles[espaniol].append(ingles)

print("Diccionario completo:")
print(diccionario_ingles)

print("\nValores con 2 sinónimos:")
for i,j in diccionario_ingles.items():
    if len(j) >= 2:
        print(i, j)
