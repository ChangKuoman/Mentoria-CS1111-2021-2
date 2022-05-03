
"""
Uno de los juegos mas populares de azar es el juego de dados conocido como “craps”,
el cual se juega en casinos y callejones en ttodo el mundo. Las reglas del juego son simples:
Un jugador tira dos dados.
El valor del tiro del jugador, se calcula mediante la suma del resultado de los dos dados.
Si la suma es 7 u 11 en el primer tiro, el jugador gana.
Si la suma es 2, 3 o 12 en el primer tiro, el jugador pierde (es decir, la casa gana).
Si la suma es 4, 5, 6, 8, 9 o 10 en el primer tiro, esa suma se convierte en el punto del jugador;
para ganar el jugador debe seguir tirando los dados hasta que salga otra vez su punto; el jugador
pierde si tira un 7 antes de obtener su punto.
Escriba un programa en Python que simule el juego de “craps” entre un jugador y el computador.
El programa debe permitir jugar cuantas veces desee el usuario. Si el usuario no desea seguir jugando,
el programa termina mostrando para cada jugada el numero de tiros realizados, si gano o perdio el usuario,
y ademas, el numero total de jugadas, el numero de jugadas ganadas, numero de jugadas perdidas, porcentaje
de jugadas ganadas y porcentaje de jugadas perdidas.
"""

import random

def juego():
    perdidas = 0
    ganadas = 0
    seguir = "SI"
    while seguir == "SI":
        #                      1-6
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        suma = dado1 + dado2
        tiradas = 1

        print("DADO 1: ", dado1)
        print("DADO 2: ", dado2)
        print("SUMA: ", suma)

        if suma == 7 or suma == 11:
            print("GANo: ", suma)
            ganadas += 1
        elif suma == 2 or suma == 3 or suma == 12:
            print("PERDIo: ", suma)
            perdidas += 1
        else:
            punto = suma  # Guardar este dato

            while True:
                dado1 = random.randint(1, 6)
                dado2 = random.randint(1, 6)
                suma = dado1 + dado2
                tiradas += 1

                print("DADO 1: ", dado1)
                print("DADO 2: ", dado2)
                print("SUMA: ", suma)
                if suma == 7:
                    print("PERDIO: 7")
                    perdidas += 1
                    break
                elif suma == punto:
                    print("GANo: ", suma)
                    ganadas += 1
                    break

        print("CANTIDAD DE TIRADAS: ", tiradas)
        seguir = str(input("DESEA SEGUIR JUGANDO? (SI/NO): "))

    print("GRACIAS POR JUGAR :D")
    print("CANTIDAD DE PARTIDAS GANADAS: ", ganadas)
    print("CANTIDAD DE PARTIDAS PERDIDAS: ", perdidas)
    print("TOTAL DE PARTIDAS JUGADAS: ", ganadas + perdidas)
    print("PORCENTAJE DE PARTIDAS GANADAS: ", ganadas / (ganadas + perdidas) * 100)  # ganadas / total * 100
    print("PORCENTAJE DE PARTIDAS PERDIDAS: ", perdidas / (ganadas + perdidas) * 100)  # perdidas / total * 100

juego()
