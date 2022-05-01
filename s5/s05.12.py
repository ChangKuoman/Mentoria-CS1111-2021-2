
### EJERCICIO ###

# Escribir un programa que pida numeros positivos al usuario. Mostrar el numero cuya sumatoria de digitos fue mayor y la cantidad de numeros cuya sumatoria de digitos fue menor que 10. Utilizar una o mas funciones, segun sea necesario.

lista = []
for i in range(3):
    lista.append(int(input("n: ")))

def sumatoria_digitos(lista): # 89 -> 8 + 9 = 17
    lista_suma = []
    for i in lista:
        suma = 0
        for digito in str(i):
            suma += int(digito)

        suma2 = 0
        # 895 -> 895%10
        # suma + 5
        # 895 // 10
        # 89
        # 89 -> 89 % 10
        # suma + 9
        # 89//10 -> 8
        # 8 % 10 -> 8
        # suma + 8
        # 8 // 10 -> 0

        while i > 0:
            n = i % 10
            suma2 += n
            i = i // 10

        # print(suma)
        # print(suma2)
        lista_suma.append(suma)
    return lista_suma
sumass = sumatoria_digitos(lista)

numero_max = max(sumass)

print(lista)

print(numero_max)
print(sumass)

for i in range(len(sumass)):
    if sumass[i] == numero_max:
        print(lista[i])
