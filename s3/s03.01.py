
### EJERCICIO ###

# Hallar la factorial de un número entero positivo.

n = int(input("n: "))
factorial = 1
for x in range(1, n+1):
    factorial *= x
print(factorial)
