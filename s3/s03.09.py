
### EJERCICIO DE PC ###

"""
Escribe un programa que lea un n ́umero entero N como entrada y retorne
como salida una ’X’ dibujada en un cuadrado de N × N.
Input :
5
Output :
  0 1 2 3 4
0 *       *
1   *   *
2     *
3   *   *
4 *       *
"""

n = int(input("n: "))

for i in range(n):
    for j in range(n):
        if i==j or j+i == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
