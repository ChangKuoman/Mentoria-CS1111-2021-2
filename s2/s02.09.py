
### EJERCICIO DE PC ###

"""
Un numero es perfecto si la suma de sus divisores (excepto el mismo numero) es igual al mismo numero. Ejemplo, 6 es perfecto, porque la suma de sus divisores (1, 2, 3) es igual al mismo numero es decir igual a 6. Determinar si un numero ingresado del teclado es perfecto.
"""

num = int(input("Numero: "))

divisores = 0
for x in range(1, num+1):
    if num == x:
        continue
    elif num % x == 0:
        divisores += x

if num == divisores:
    print("es perfecto")
else:
    print("no es perfecto")
