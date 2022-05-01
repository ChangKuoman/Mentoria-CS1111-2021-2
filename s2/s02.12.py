
### INTRODUCCION FOR ANIDADO ###

# imprime numeros primos dentro de un rango
n1= int(input("inicio: "))
n2= int(input("final: "))

for i in range(n1, n2):
    for x in range(2, i):
        if i % x == 0:
            break
    else:
        print(i)

# verifica si el numero ingresado es primo
numero = int(input("numero: "))

for num in range(2, numero):
    if numero % num == 0:
        print("no es primo")
        break
else:
    print("es primo")
