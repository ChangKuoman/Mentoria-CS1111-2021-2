
### EJERCICIO DE PC ###

"""
Desarrolle un programa que pida al usuario ingresar una opcion (a, b, c) y
tambien le pida ingresar 5 numeros, y realize los siguientes calculos:
• Si escogio la opcion a entonces debe imprimir el promedio de los numeros
• Si escogio la opcion b entonces debe imprimir la cantidad de numeros pares
• Si escogio la opcion c entonces debe imprimir la cantidad numero que son de
multiplos de 4
"""

opcion = str(input("opcion (a,b,c): "))

if opcion == 'a':
    suma = 0
    for i in range(5):
        n = int(input(f"n{i}: "))
        suma += n
    print(suma/5)

elif opcion == 'b':
    contador = 0

    for i in range(5):
        n = int(input(f"n{i}: "))
        if n%2 == 0:
            contador += 1

    print(f"Contador: {contador}")
elif opcion == 'c':
    contador = 0
    for i in range(5):
        n = int(input(f"n{i}: "))
        if n % 4 == 0:
            contador += 1

    print(f"Contador: {contador}")
else:
    print("Opcion invalida")
