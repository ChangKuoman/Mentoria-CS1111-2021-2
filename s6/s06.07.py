
### EJERCICIO DE PC ###

"""
Implemente una funcion que reciba dos parametros, el primer parametro es
obligatorio y el segundo es opcional, con un valor por defecto de 20, la funcion realiza
los siguientes calculos:
• Si el primer parametro es multiplo de 3 entonces se debe calcular y retornar la suma
de todos los numeros multiplos de 3 desde el primer hasta el segundo parametro.
• Si el primer parametro es diferente de multiplo de 3 entonces se debe calcular y
retornar la suma de todos los numeros desde el primer hasta el segundo parametro.
Luego implemente un programa que solicite ingresar dos n ́umeros, llame a la funcion
implementada e imprima el resultado.
"""

import funciones as f

n = int(input("n: "))
m = int(input("m: "))
resultado = f.ejercicio(n, m)
print(resultado)
