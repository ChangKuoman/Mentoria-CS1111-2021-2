
### EJERCICIO ###

# ingresar n numeros que se generaran aleatoriamente de 4 digitos. si el segundo y tercer digito son pares escribirlo en pares.txt si el primer y cuarto digito son impares escribirlo en impares.txt. Notese que puede cumplir ambas condicionales
import random
n = int (input("INPUT: "))

# pares.txt si 2 o 3 digito es par
# impares.txt si 1 o 4 digito es impar
pares = open("pares.txt", "w")
impares = open("impares.txt", "w")

for i in range(n):
    numero = str(random.randint(1000, 9999))
    if numero[1] in "02468" or numero[2] in "02468":
        pares.write(numero)
        pares.write("\n")
    if numero[0] in "13579" or numero[3] in "13579":
        impares.write(numero)
        impares.write("\n")

pares.close()
impares.close()
