
### INTRODUCCION ###

# functions
def sumar(a, b):
    suma = a + b # variable local
    return suma

print(sumar(8, 6))
# print(suma)

v_global = 48 # variable global
print(v_global)

def suma_global(a):
    global v_global
    v_global += a
    v_global -= 50

suma_global(12)
print(v_global)
