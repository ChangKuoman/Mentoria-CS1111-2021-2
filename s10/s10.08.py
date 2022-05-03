
### EJERCICIO DE PC ###

"""
Disenie e implemente un programa que pida como dato un numero entero n,
y luego realice lo siguiente:
• Cree un archivo llamado numeros.txt, donde se graben n numeros aleatorios un
por linea. Los numeros generados podran ser desde el 1 al 99.
• Luego, cree un segundo archivo llamado filtrados.txt, en donde se grabe uni-
camente aquellos numeros que figuran en el primer archivo y que son numeros
primos.
Note, que en la pantalla no se imprimira nada, ya que la informacion queda guardada
en los archivos: numeros.txt y filtrados.txt
Recuerde, que esta trabajando con archivos texto, por lo cual todo lo que se graba o
lee son cadenas.
"""
from random import randint

n = int(input("N= "))

file = open("numeros.txt", "w")

for i in range(n):
    file.write(str(randint(1, 99)))
    file.write("\n")

file.close()

file_entrada = open("numeros.txt", "r")
file_salida = open("filtrados.txt", "w")

def es_primo(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

for i in file_entrada:
    i = i.rstrip()
    i = int(i)
    if es_primo(i):
        file_salida.write(str(i))
        file_salida.write("\n")

file_entrada.close()
file_salida.close()
