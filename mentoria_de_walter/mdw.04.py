
# input:
# kaYaK
# kayal
# level
# EOF

# output:
# 2_1,2
# numeroDePalindromes_ubicacion1,ubicacion1, etc...

lista = []
contador = 0
while True:
    cadena = str(input("")).lower()

    cadena_reves=""
    for char in cadena:
        if char == " ":
            continue
        else:
            cadena_reves = char + cadena_reves

    if cadena == cadena_reves:
        contador += 1
        lista.append(contador)

    if cadena == "eof":
        break

nueva_cadena = str(contador) + "_"
nueva_cadena += ",".join([str(i) for i in lista])
print(nueva_cadena)
