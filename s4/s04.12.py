
### INTRODUCCION ###

# functions
from math import pi

def hallar_area_circulo(radio):
    area = pi* (radio**2)
    return area

r = int(input("RADIO: "))
print(round(hallar_area_circulo(r), 2))
n = 7
print(round(hallar_area_circulo(n), 2))
