from random import randint


def imprimir_matriz(matriz):

    for i in matriz:
        for j in i:
            print(j, end=" ")
        print()


def crear_matriz():
    mat = []
    for i in range(5):
        mat.append([])
        for j in range(5):
            mat[i].append(randint(1, 9))
    return mat


def ejercicio(num, num2=20): # valor por defeto num2=20

    suma = 0
    if num%3 == 0:
        for i in range(num, num2):
            if i%3==0: suma+=i
    else:
        for i in range(num, num2):
            suma += i

    return suma


def crear_matriz_2(n):
    mat = []
    for i in range(n):
        mat.append([])
        for j in range(n):
            mat[i].append("*")
    return mat
