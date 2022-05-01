
### EJERCICIO ###

# Escribir un programa que reciba un numero inicial y otro final, luego imprima los numeros que sean divisibles entre 3 y 9

n1 = int(input("inicio: "))
n2 = int(input("final: "))

for i in range(n1, n2+1):
    if i % 3 == 0 and i % 9 == 0:
        print(i)
