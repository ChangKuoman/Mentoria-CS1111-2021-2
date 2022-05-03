
### INTRODUCCION ###

# complejidad algoritmica
n = int(input("N: "))
suma = 0
iter = 0
for i in range(1, n+1):
    suma += i
    iter += 1
print("Suma" , suma)
print("ITERACIONES", iter)
# O (n)

suma2 = (n * (n + 1)) / 2
print(1)
# O (1)

print(suma2)

iter = 0
for i in range(n):
    for j in range(n):
        suma += j
        iter += 1

print("ITERACIONES", iter)
# O (n^2)

iter = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            iter += 1
print("ITERACIONES", iter)

# O (n^3)
