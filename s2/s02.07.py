
### EJERCICIO ###

# Generar un programa que pida un numero del 1 al 12 y no se encuentra en el rango, volver a pedir el numero, luego imprimira la tabla de multiplicar de aquel numero.
# 8 x 1 = 8
# 8 x 2 = 16
# 8 x 3 = 24
# 8 x 4 = 32
# 8 x 5 = 40
# 8 x 6 = 48
# 8 x 7 = 56
# 8 x 8 = 64
# 8 x 9 = 72
# 8 x 10 = 80
# 8 x 11 = 88
# 8 x 12 = 96

n = int(input("n: "))
while (n < 0 or n > 12):
    n = int(input("n: "))

for num in range(1, 13):
    print(n, "x", num, "=", n*num)
