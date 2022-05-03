
# si la suma de 2 numeros es 10 retornar es 10, si no es 10 retornar no es 10

def suma(n, m):
    if n + m == 10:
        dato = "ES 10"
    else:
        dato = "NO ES 10"
    return dato

print(suma(4, 6))
print(suma(4, 8))
