
### EJERCICIO ###

# Hallar la suma de los terminos de la siguiente serie: 1 - 1/2 + 1/3 – 1/4 + ....+ 1/N.

n = int(input("n: "))

suma_pares = 0
suma_impares = 0

for impar in range(1, n+1, 2):
    suma_impares += 1/impar

for par in range(2, n+1, 2):
    suma_pares += 1/par

total = suma_impares - suma_pares
print(total)
