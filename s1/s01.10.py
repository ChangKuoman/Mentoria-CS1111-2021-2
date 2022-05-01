
### EJERCICIO DE PC ###

"""
Escribir un programa en Python, que permita calcular el precio de una entrada al teatro, considerando lo siguiente:
 Si la persona es menor de edad pagara 20 soles.
 Si la persona tiene de 18 a 55 anios pagara 80 soles.
 Si la persona tiene m ́as de 55 anios pagara 40 soles.
 Los fines de semana hay descuento de 40 porciento
 Martes y jueves 30 porciento descuento
"""

edad = int(input("Ingrese edad: "))
dia = input("Ingrese día: ")

if edad <= 17:
    precio = 20
elif edad >= 18 and edad <= 50:
    precio = 80
else:
    precio = 40

if dia == "martes" or dia == "jueves":
    precio *= 0.7
    # precio = precio * 0.7
elif dia == "sabado" or dia == "domingo":
    precio *= 0.6

print(f"Pagas {precio}")
