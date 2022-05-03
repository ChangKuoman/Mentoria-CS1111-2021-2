
### EJERCICIO ###

# Escribir un programa que pida un numero (1-12) y muestre el mes

meses = {
    1:"Enero",
    2:"Febrero",
    3:"Marzo",
    4:"Abril",
    5:"Mayo",
    6:"Junio",
    7:"Julio",
    8:"Agosto",
    9:"Septiembre",
    10:"Octubre",
    11:"Noviembre",
    12:"Diciembre"
}

n = int(input("Ingrese numero (1-12): "))

print(f"El mes es {meses[n]}")
