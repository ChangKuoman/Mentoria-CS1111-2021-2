
### EJERCICIO DE PC ###

"""
Desarrollar un programa en Python que permita ingresar 5 cursos y sus notas,
nota1 y nota2, recoger informacion desde teclado e indicar los siguientes resultados
 Mostrar la cantidad de aprobados y desaprobados por NOTA
"""

aprobado = 0
desaprobado = 0
for curso in range(5):
    nombre = str(input("Nombre del curso: "))
    nota1 = float(input("Nota1: "))
    nota2 = float(input("Nota2: "))
    promedio = (nota1 + nota2)/2
    if promedio >= 10.5:
        aprobado += 1
    else:
        desaprobado += 1

print("Cantidad de cursos aprobados: {}".format(aprobado))
print(f"Cantidad de cursos desaprobados: {desaprobado}")
