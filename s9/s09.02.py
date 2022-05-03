
### EJERCICIO ###

# Escribir un programa que pida un numero (1-7) y muestre el dia de la semana

dias = {
    1:"Lunes",
    2:"Martes",
    3:"Miercoles",
    4:"Jueves",
    5:"Viernes",
    6:"Sabado",
    7:"Domingo"
}

n = int(input("Ingrese un numero (1-7): "))

print(f"El dia es {dias[n]}")
