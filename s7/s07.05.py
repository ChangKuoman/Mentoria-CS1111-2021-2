
### EJERCICIO ###

numero1 = int(input("Numero 1: "))
numero2 = int(input("Numero 2: "))
while numero1 == numero2:
    numero1 = int(input("Numero 1: "))
    numero2 = int(input("Numero 2: "))


def sonAmigos(numero1, numero2):
    suma_divisores_numero1 = 0
    suma_divisores_numero2 = 0
    for i in range(1, numero1):
        if numero1 % i == 0:
            suma_divisores_numero1 += i

    for i in range(1, numero2):
        if numero2 % i == 0:
            suma_divisores_numero2 += i

    return suma_divisores_numero1 == numero2 and suma_divisores_numero2 == numero1


print(f"{numero1} y {numero2}", end=". ")
if sonAmigos(numero1, numero2):
    print("Son numeros amigos")
else:
    print("No son numeros amigos")
