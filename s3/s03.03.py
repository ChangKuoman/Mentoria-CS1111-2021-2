
### EJERCICIO ###

"""
UPCH lab5.2
La siguiente se llama la conjetura de Ulam en honor del matematico S. Ulam:
a) Comience con cualquier entero positivo
b) Si es par, dividalo entre 2; si es impar, multipliquelo por tres y sumele 1
c) Obtenga enteros sucesivamente repitiendo el proceso
Al final, obtendra el numero 1, independientemente del numero inicial. Por ejemplo, cuando el entero inicial es 26, la secuencia sera: 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1.
Leer un entero positivo del teclado, determinar e imprimir la sucesion de Ulam. Hallar la suma de dicha sucesion.
"""

n = int(input("n: "))
while n<=0:
    n = int(input("n: "))

while n > 1:
    if n % 2 == 0:
        n = n//2
    else:
        n = (n * 3) + 1
    print(n, end=" ")
