
### INTRODUCCION ###

# lists
lista = [15, 0.84, True, "hola", [15]]
#         0     1    2     3      4

for i in lista:
    print(i)

n = int(input("n: "))

lista.insert(0, n)

print(lista)
