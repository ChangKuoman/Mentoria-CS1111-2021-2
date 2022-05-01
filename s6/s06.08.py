
### EJERCICIO DE PC ###

"""
Deberas crear una funcion que se llame maravilla. Esta funcion recibira 3
parametros, y tendra las siguientes caracteristicas:
• El primer parametro sera un caracter, el cual puede ser alguno de estos simbolos:
”+” (mas) ”-” (menos) ”*” (por) ”/” (entre) .
• El segundo y el tecer parametros seran dos numeros enteros .
• La funcion devolvera el resultado de la operacion enviada.
• Si el primer parametro fuera ”entre” y el segundo numero un cero, debera imprimir
un mensaje de error y no devolvera nada.
"""

def maravilla(caracter, n, m):

    if caracter == "+":
        resultado = n+m
    elif caracter == "-":
        resultado = n-m
    elif caracter == "*":
        resultado = n*m
    elif caracter == "/":
        if m == 0:
            resultado = "ERROR NO SE PUEDE DIVIDIR POR 0"
        else:
            resultado = n/m
    else:
        resultado = "CARACTER INCORRECTO"

    return resultado

char = str(input("caracter: "))
n = int(input("n: "))
m = int(input("m: "))
print(maravilla(char, n, m))
