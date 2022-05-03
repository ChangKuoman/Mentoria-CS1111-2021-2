
# usando list comprehension generar 10 numeros decimales entre 10 y 20 (incluidos) redondeados a 2 decimales
import random

lista = [round(random.uniform(10, 20), 2) for i in range(10)]

print(lista)
