
### INTRODUCCION ###

# lists
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("longitud", len(numeros))
print("suma", sum(numeros))
print("maximo", max(numeros))
print("minimo" , min(numeros))

corte = slice(0, 6, 2)
print(numeros[corte])

print(numeros[:8:3])

numeros.remove(1) # por valor
numeros.pop() # por 1 indice
numeros.clear()
del numeros[0:8:2] # por indice o cortes
del numeros
print(numeros) # va a salir error ya que eliminamos la lista
