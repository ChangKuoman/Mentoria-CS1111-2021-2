
### EJERCICIO ###

# Escribir un programa que solicite al usuario tres edades e imprima cual es mayor.

edad1 = int(input("Edad 1: "))
edad2 = int(input("Edad 2: "))
edad3 = int(input("Edad 3: "))

if edad1 > edad2 and edad1 > edad3:
    print(edad1)
elif edad2 > edad1 and edad2 > edad3:
    print(edad2)
elif edad3 > edad2 and edad3 > edad1:
    print(edad3)
