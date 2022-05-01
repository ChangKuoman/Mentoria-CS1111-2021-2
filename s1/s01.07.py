
### EJERCICIO ###

# Escribir un programa genere un numero al azar entre 1 y 20, e indique si se encuentra entre el 7 y el 12.

from random import randint as rd

n = rd(1,20)

print(n)
if 7 <= n and n <= 12:
    print("Se encuentra en el rango")
else:
    print("No se encuentra en el rango")
