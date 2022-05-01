
### EJERCICIO ###

# Escribir un programa que calcule el numero armonico:
# f(n) = 1/1 + 1/2 + 1/3 + ... + 1/n

n = int(input("n: "))

cantidad = 0
for numero in range(1, n+1):
    cantidad += 1/numero

print(round(cantidad, 5))
