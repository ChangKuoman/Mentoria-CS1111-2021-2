
### EJERCICIO ###

# Escribir una funcion recursiva que multiplique a x b

def mult_recur(a, b):
  if b == 0 or a == 0:
    return 0
  if b == 1:
    return a
  else:
    return a + mult_recur(a, b-1)

print(mult_recur(10, 8))
