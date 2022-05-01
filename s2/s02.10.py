
### EJERCICIO ###

# Determinar la cantidad de cifras que tiene un numero entero ingresado del teclado.

n = int(input("n: "))

cantidad = 0
for num in str(n):
    cantidad += 1

print(cantidad)
