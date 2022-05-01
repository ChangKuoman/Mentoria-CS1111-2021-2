
### EJERCICIO ###

# BMI = peso(kg) / altura(m)^2

peso = float(input("Ingrese peso en kg: "))
altura = float(input("Ingrese altura en m: "))

indice = peso / (altura ** 2)
indice = round(indice, 5)
print(f"Su indice de masa corporal es {indice}.")
