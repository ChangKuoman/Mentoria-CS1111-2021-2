
### EJERCICIO DE PC ###

"""
Realice un programa que permita generar ”n” n ́umeros al azar cuyos valores pueden
estar desde el 100 al 999, y el programa forme diccionario en donde el n ́umero sea la
clave y el valor asociado sea el n ́umero deletreado en quechua.
Note que al ser un diccionario no puede tener claves repetidas.
En la siguiente tabla se muestran la equivalencia de cada d ́ıgito en quechua.
"""

numeros = {
    0: "Chusaq",
    1: "Huk",
    2: "Iskay",
    3: "Kinsa",
    4: "Tawa",
    5: "Pisqa",
    6: "Soqta",
    7: "Qanchis",
    8: "Pusaq",
    9: "Esqon"
}

nuevo_dic = {}

from random import randint

n = randint(5, 10)

for i in range(n):
    numero = randint(100, 999)

    nueva_cadena =""
    for digito in str(numero):
        nueva_cadena += numeros[int(digito)]

    nuevo_dic[numero] = nueva_cadena

for i in nuevo_dic:
    print(i, nuevo_dic[i])

# 154
# "HukPisqaTawa"
# 986
# "EsqonPusaqSoqta"
