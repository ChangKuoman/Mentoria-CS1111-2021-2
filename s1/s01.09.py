
### EJERCICIO DE PC ###

"""
Desarrolle un programa que permita tener como datos:
• La fecha en que una persona nacio, en el formato: dia, mes, anio
• La fecha actual, en el formato: dia, mes, anio
Y el programa indique: la edad y a que generacion pertenece, considerando los datos de la siguiente tabla:
13 - 20 Generacion Z
21 - 35 Generacion Y
36 - 59 Generacion X
60 a mas Generacion Baby Boomers
"""

dia1 = int(input("Dia de nacimiento: "))
mes1 = int(input("Mes de nacimiento: "))
anio1 = int(input("Anio de nacimiento: "))

dia2 = int(input("Dia de hoy: "))
mes2 = int(input("Mes de hoy: "))
anio2 = int(input("Anio de hoy: "))

edad = anio2 - anio1

if edad >= 13 and edad <= 20:
    print("Generacion Z")
elif edad in range(21,36):
    print("Generacion Y")
elif edad in range(36,60):
    print("Generacion X")
elif edad >= 60:
    print("Baby Boomer")
