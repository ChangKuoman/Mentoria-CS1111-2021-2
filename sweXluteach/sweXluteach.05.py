
# enunciado: img5

def H(n):

    if n == 1:
        return 0
    else:
        return n * (n-1) + H(n-1)

n = int(input("N: "))
print(H(n))
