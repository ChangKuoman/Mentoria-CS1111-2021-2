
### EJERCICIO ###

# X
# X X
# X X X
# X X X X
# X X X X X

# manera 1
n = int(input("n: "))

for i in range(n):
    for j in range(n):
        if j<=i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# manera 2
n = int(input("N: "))

for i in range(n):
    for j in range(i+1):
        print("X", end=" ")
    print()
