
### EJERCICIO DE PC ###

"""
5. Implemente un programa que dada una secuencia de N numeros enteros (positivos,
negativos y ceros), determine con la ayuda de un solo bucle, el promedio de los numeros
negativos y el promedio de los numeros positivos.
a) Simule el ingreso de los datos con la funcion input()
b) Simule el ingreso de datos con la funcion random.randint()
"""

# import random
# from random import randint
from random import randint as rd

n = int(input("n: "))
inicio = int(input("inicio: "))
final = int(input("final: "))

cantidad2 = 0
cantidad = 0
positivos = 0
negativos = 0

for i in range(n):
    valor = rd(inicio, final)
    print(valor)
    if valor < 0:
        negativos = negativos + valor
        cantidad = cantidad + 1
    elif valor == 0:
        continue
    else:
        positivos = positivos + valor
        cantidad2 = cantidad2 + 1

print("Promedio negativos: ", negativos/cantidad)
print("Promedio positivos: ", positivos/cantidad2)
