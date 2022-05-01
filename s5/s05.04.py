
### INTRODUCCION ###

# functions
n = int(input("n: "))
m = int(input("m: "))

def suma(x=3, y=8.5):
    # instrucciones
    n = x + y
    return n

# print(suma(n, m))
print(suma(5, 9))

b = 5
c = 10

a = suma(y=b, x=c)
print(a)

print(suma(10, 15))
