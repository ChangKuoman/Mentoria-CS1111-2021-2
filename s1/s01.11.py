
### EJERCICIO DE PC ###

"""
En el planeta Gorinki, los gorinkianos son mayores de edad a partir de los 15.
Al ser mayor de edad, si son pretinos reciben un bono de 500 estufares, si son torientes
un bono de 600 estufares, y si son foluntas un bono de 700 estufares. El programa
debera preguntar al gorinkiano su edad y su clan, e indicarle cuantos estufares recibira.
Recuerda que si no es mayor de edad no recibira nada. Finalmente, si tiene mas de 120
anios se le duplica el bono.
"""

edad = int(input("Ingrese edad: "))
clan = input("Ingrese clan: ")

if edad >= 120 and clan == "pretino":
    print("1000 estufares")
elif edad >= 15 and clan == "pretino":
    print("500 estufares")
elif edad >= 120 and clan == "toriente":
    print("1200 estufares")
elif edad >= 15 and clan == "toriente":
    print("600 estufares")
elif edad >= 120 and clan == "folunta":
    print("1400 estufares")
elif edad >= 15 and clan == "folunta":
    print("700 estufares")
else:
    print("No recibes bono")
