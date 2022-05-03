
### EJERCICIO DE PC ###

# PC3 2021-1 1
dic = {}

while True:
    dni = int(input("Ingrese dni: "))
    if dni == 0:
        break
    apellido = str(input("Ingrese apellido paterno: "))
    nombre = str(input("Ingrese nombre: "))
    edad = int(input("Ingrese edad: "))

    dic[dni] = [apellido, nombre, edad]

print("***********************")
print("Realizar busqueda")

numero = int(input("Ingrese dni: "))
apellido_b = str(input("Ingrese apellido paterno: "))

print(f"Pasajero(a): {dic[numero][1]} {dic[numero][0]} con dni: ({numero}) y edad {dic[numero][2]}")
