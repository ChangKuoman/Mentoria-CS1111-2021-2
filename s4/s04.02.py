
### EJERCICIO ###

#    1
#   121
#  12321
# 1234321

#    1
#   12 1
#  123 21
# 1234 321

m = int(input("m: "))

for i in range(1, m + 1):
    print(" " * (m - i), end="")  # espacios en blanco

    for j in range(1, i + 1):  # piramide izquierda
        print(j, end="")

    for f in range(i - 1, 0, -1):  # piramide derecha
        print(f, end="")

    print()  # salto de línea
