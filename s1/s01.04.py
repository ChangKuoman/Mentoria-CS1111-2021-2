
### EJERCICIO ###

# Escribir un programa que reciba una cantidad de segundos y calcule su equivalente en horas, minutos y segundos.

segundos = int(input("Ingrese segundos: "))

minutos = segundos // 60
horas = minutos // 60
minutos = minutos - 60 * horas
segundos = segundos - 60 * (minutos + (60 * horas))

print(minutos)
print(horas)
print(segundos)
