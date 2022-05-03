
### INTRODUCCION ###

# recursividad
# 9
# 9 x 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1
n = int(input("N: "))

# iterativa
def fact_iter(n):
    total = 1
    for i in range(1, n+1):
        total *= i
    return total

print(fact_iter(n))

# recursiva
def fact_recur(n):
    if n == 1:
        return 1
        if n == 0:
            return 1
    else:
        return n * fact_recur(n-1)

print(fact_recur(n))
