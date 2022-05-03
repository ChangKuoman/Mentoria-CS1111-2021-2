
# enunciado: img4

n = int(input("N: "))

def calcular_cuadrados(n):
    if n == 1:
        return 1
    else:
        return n**2 + calcular_cuadrados(n-1)

print(calcular_cuadrados(n))
