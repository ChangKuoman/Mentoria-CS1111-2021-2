
### EJERCICIO ###

# ingrese dos listas, primero pregunte la cantidad de elementos y luego ingresarlos manualmente para ambas listas
# imprima listas para:
# * la interseccion de ambas listas sin elementos que se repitan
# * la diferencia (lista1 - lista2) sin elementos que se repitan
# * los numeros pares de ambas listas sin elementos que se repitan

valores_lista1 = int(input("Ingrese numero de elementos lista1: "))
lista1 = []
for i in range(valores_lista1):
    lista1.append(int(input(f"Ingrese valor {i+1}: ")))

valores_lista2 = int(input("Ingrese numero de elementos lista2: "))
lista2 = []
for i in range(valores_lista2):
    lista2.append(int(input(f"Ingrese valor {i+1}: ")))

print(f"Lista 1 = {lista1}")
print(f"Lista 2 = {lista2}")

lista_interseccion = []
for elemento_lista1 in lista1:
    for elemento_lista2 in lista2:
        if elemento_lista1 == elemento_lista2 and elemento_lista1 not in lista_interseccion:
            lista_interseccion.append(elemento_lista2)

print(f"Resultado 1 (interseccion) = {lista_interseccion}")

lista_diferencia = []
for elemento in lista1:
    if elemento not in lista_interseccion:
        lista_diferencia.append(elemento)

print(f"Resultado 2 (diferencia lista1 - lista2) = {lista_diferencia}")

lista_pares = []
for elemento in lista1:
    if elemento % 2 == 0 and elemento not in lista_pares:
        lista_pares.append(elemento)
for elemento in lista2:
    if elemento % 2 == 0 and elemento not in lista_pares:
        lista_pares.append(elemento)

print(f"Resultado 3 (pares en listas) = {lista_pares}")
