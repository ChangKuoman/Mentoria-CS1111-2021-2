
### INTRODUCCION ###

# functions
def cuadrado(lado, contador):
    area = lado*lado
    contador += 1
    return area, contador

l = 5
cont = 0

area, cont = cuadrado(l, cont)
l = 8
area, cont = cuadrado(l, cont)
print(area)
print(cont)
print(l)
