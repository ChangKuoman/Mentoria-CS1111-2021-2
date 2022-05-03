
### EJERCICIO ###

# archivos
from random import randint

n = int(input("Num: "))
while n<1:
    n = int(input("Num: "))

numeros={
    0:"cero ",
    1:"uno ",
    2:"dos ",
    3:"tres ",
    4:"cuatro ",
    5:"cinco ",
    6:"seis ",
    7:"siete ",
    8:"ocho ",
    9:"nueve "
}

with open("numeros.txt", "w") as file:

    for i in range(n):
        num = randint(100, 999)
        file.write(str(num))
        file.write(" ")

        for i in str(num):
            file.write(numeros[int(i)])

        file.write("\n")

print("Se genero el archivo numeros.txt")
