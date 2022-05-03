
### EJERCICIO DE PC ###

# obtener los nombres de los estudiantes que les gusta x comida e imprimirlo si hay 2 o mas a quienes les guste la misma comida
import json

alumnos = {
    "Alejandro":  ["ceviche", "lomo saltado", "pollo a la brasa"],
    "Roberto":    ["lomo saltado"],
    "Jesus":      ["lomo saltado", "lasagna"],
    "Carlos":     ["lasagna"],
    "Melina":     ["ceviche", "arroz con pollo"]
}

comida = {}

for clave,valor in alumnos.items():
  for elemento in valor:
    if elemento not in comida.keys():
      comida[elemento] = [clave]
    else:
      comida[elemento].append(clave)

# print(comida)
print(json.dumps(comida, indent=5))

for valor in comida.values():
    if len(valor) >= 2:
        print(valor)

# diccionario = {
#  llave : valor,
#  key : value
# }
