
### EJERICICO DE PC ###

"""
Un valor es valido si pertenece al intervalo de 1 a 20 inclusive. Ingresar varios numeros emitiendo el mensaje correspondiente (“valido”, “no valido”) para cada uno y terminar cuando se hayan ingresado tres (3) numeros validos.
"""

validos = 0
while validos < 3:
    n = int(input("n: "))
    if n in range(1, 21):
        print("valido")
        validos += 1
    else:
        print("no valido")
