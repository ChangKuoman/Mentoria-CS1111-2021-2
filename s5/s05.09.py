
### EJERCICIO ###

# Pedir al usuario ingresar numeros hasta ingresar “fin”, imprimir los numeros mayores a 10.

lista = []

while True:
    n = str(input("n: "))
    if n == "fin": break
    if int(n) > 10:
        lista.append(int(n))

print(lista)
