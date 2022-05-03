
### INTRODUCCION ###

# complejidad algoritmica
import time

def timer():
    inicio = time.time()

    suma = 0
    for i in range(10000000):
        suma += i

    fin = time.time()
    total = fin - inicio
    print(total)

timer()
