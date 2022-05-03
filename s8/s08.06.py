
### EJERCICIO ###

# USANDO LIST COMPREHENSION

cadena1 = str(input("Cadena1: ")) # "Maria,Pepe,Juan,Luis"
cadena2 = str(input("Cadena2: ")) # "Luisa,Maria,Mariana,Ellie" delimitador ','

lista1 = [i for i in cadena1.split(',')]
lista2 = [i for i in cadena2.split(',')]

print(lista1)
print(lista2)

# Uniendo las 2 listas sin repetirse:

# Manera 1
lista3 = []
for i in lista1:
    if i not in lista3: lista3.append(i)
for i in lista2:
    if i not in lista3: lista3.append(i)
print(lista3)

# Manera 2
lista4 = list(set(lista1+lista2))
print(lista4)
