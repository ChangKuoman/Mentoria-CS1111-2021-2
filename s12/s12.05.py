
### EJERCICIO DE PC ###

"""
Desarrollar una funci ́on recursiva que reciba 3 par ́ametros y devuelva como
resultado la suma o multiplicaci ́on de todos los n ́umetos desde el inicio y fin de rango
indicados. Utilizar RECURSIVIDAD. Obligatorio.
Inicio : 5
Fin : 10
Tipo : M
Resultado : 5*6*7*8*9*10 = 151200
Inicio : 5
Fin : 10
Tipo : S
Resultado : 5+6+7+8+9+10=45
"""

def funcion_s_m(inicio, fin, tipo):
    if tipo == 'S':
        # caso base
        if inicio == fin:
            return inicio
        # llamada recursiva
        else:
            return inicio + funcion_s_m(inicio + 1, fin, tipo)

    if tipo == 'M':
        # caso base
        if inicio == fin:
            return inicio
        # llamada recursiva
        else:
            return inicio * funcion_s_m(inicio + 1, fin, tipo)


n1 = int(input("INICIO: "))
n2 = int(input("FIN: "))
# tipo = str(input("TIPO: "))

print(funcion_s_m(n1, n2, 'S'))
print(funcion_s_m(n1, n2, 'M'))
