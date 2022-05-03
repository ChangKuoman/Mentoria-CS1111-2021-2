
### EJERCICIO DE PC ###

"""
Implementar un programa que lea un archivo (por ejemplo datos.txt), dentro
del archivo tiene que estar una lista de alumnos y sus notas, el programa tiene que cal-
cular, la mayor nota, la menor nota, la nota promedio y esa informaci ́on debe guardarla
en otro archivo(por ejemplo datoscalculado.txt).
Ejemplo del contenido del archivo datos.txt
Carlos 16
Maria 18
Juan 14
Pedro 16
Ignacio 12
Luis 11
Mario 20
Fabian 13
Marcos 14
"""

documento = open("datos.txt", "r")

texto = documento.readlines()

lista_de_notas = []

for i in texto:
    i = i.rstrip()
    # \n \t
    i = i.split()
    lista_de_notas.append(i[1])

documento.close()

print(lista_de_notas)

lista_notas_enteros = [int(i) for i in lista_de_notas]

print(lista_notas_enteros)

maximo = max(lista_notas_enteros)
minimo = min(lista_notas_enteros)
promedio = sum(lista_notas_enteros)/len(lista_notas_enteros)

print(maximo)
print(minimo)
print(promedio)

archivo = open("datoscalculado.txt", "w")

archivo.write(str(maximo))
archivo.write("\n")
archivo.write(str(minimo))
archivo.write("\n")
archivo.write(str(promedio))

archivo.close()

"\n" "\t" "/n" "/t"
