
### EJERCICIO ###

# Escribir un programa que reciba un número de DNI y usando una función verifique e imprima si es válido (tener una longitud de 8 dígitos) o no.

dni = int(input("Ingrese DNI: "))

def verificar_dni(dni):
    n = len(str(dni))
    if n == 8:
        print("VALIDO")
    else:
        print("NO VALIDO")

    if dni < 100000000 and dni > 9999999:
        print("VALIDO")
    else:
        print("NO VALIDO")

verificar_dni(dni)
