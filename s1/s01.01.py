
### INTRODUCCION ###

# concatenando con f-string
nombre = "Adrian"
edad = 19

print(f"Hola mi nombre es {nombre} y mi edad es {edad}")

# imprimiendo una expresion
print(5 * (10 + 5) > 55 and (True or False))

"""
este es comentario multininea en python que quiero comentar
linea
linea
"""

# if - elif - else
numero = int(input("Ingrese un numero: "))

if numero > 2:
    print("mayor")
elif numero < 2:
    print("menor")
else:
   print("igual")

# paridad de un numero
number = int(input("n: "))

if number % 2 == 0:
    print("Es multiplo de 2")

print(number%2)
