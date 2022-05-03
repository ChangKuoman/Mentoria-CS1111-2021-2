
### EJERCICIO ###

# USANDO LIST COMPREHENSION

# Teniendo la siguiente cadena, separar cada palabra en un elemento de una lista.
cadena = '5,8,6,7,8,6,7'

lista = [int(i) for i in cadena.split(',')]
print(lista)
