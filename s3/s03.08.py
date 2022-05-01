
### EJERCICIO DE PC ###

"""
(5 points) Desarrolle un programa usando ciclos anidados, que pida al usuario ingresar
un numero positivo n e imprima con las siguientes condiciones:
• Al inicio de cada fila imprima el n ́umero de la fila
• Imprimir un cuadrado de asteriscos nxn y dentro una cruz de asteriscos.
• Para poner la cruz del medio, considerar la mitad de n, si n es impar redondear al
entero mayor, por ejemplo n = 5 usar la columna 3
Ingrese un numero : 5
  0 1 2 3 n
0 * * * * *
1 *   *   *
2 * * * * *
3 *   *   *
n * * * * *
"""

n = int(input("n: "))
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or i == n//2 or j ==0 or j==n-1 or j== n//2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
