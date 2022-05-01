
### EJERCICIO ###

# Escribir un programa que solicite al usuario su nombre y anio de nacimiento. Luego indicara su edad en el presente anio.

nombre = input("Ingrese su nombre: ")
anio_de_nacimiento = int(input("Ingrese su anio de nacimiento: "))
edad = 2021 - anio_de_nacimiento
print(f"Hola {nombre}, tu edad es {edad}")
