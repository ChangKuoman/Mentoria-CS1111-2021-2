
# enunciado: img3

from random import randint

numeros = {
    '0':'Chusaq',
    '1':'Huk',
    '2':'Iskay',
    '3':'Kinsa',
    '4':'Tawa',
    '5':'Pisqa',
    '6':'Soqta',
    '7':'Qanchis',
    '8':'Pusaq',
    '9':'Esqon'
}

n = int(input("N: "))

dic = {}

for i in range(n):
    numero = randint(100, 999)

    numero_q = ""
    for digito in str(numero):
        numero_q += numeros[digito] + " "

    dic[numero] = numero_q

for i in dic:
    print(i, dic[i])
