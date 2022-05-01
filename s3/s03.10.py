
### EJERCICIO DE PC ###

"""
n = 5
1 2 3 4 5
      6
    7
  8
9 1 2 3 4

n = 6
1 2 3 4 5 6
        7
      8
    9
  1
2 3 4 5 6 7
"""

n = int(input("n: "))
contador = 1

for i in range(n):
    for j in range(n):
        if j+i==n-1 or i == 0 or i == n-1:
            print(contador, end=" ")
            contador += 1

            if contador >= 10: contador = 1

        else:
            print(" ", end=" ")
    print()
