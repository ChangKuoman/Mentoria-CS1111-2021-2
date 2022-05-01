
### EJERCICIO ###

# X X X X X
# X X X X
# X X X
# X X
# X

n = int(input("n: "))

for i in range(n):
    for j in range(n-i):
        print("X", end=" ")
    print()
