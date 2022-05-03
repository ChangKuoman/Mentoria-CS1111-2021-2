
### EJERCICIO ###

# mezclando archivos in.txt e in2.txt intercalando las lineas y escribiendolas en out.txt
with open("in1.txt", "r") as file:
    texto1 = file.readlines()

with open("in2.txt", "r") as file:
    texto2 = file.readlines()

if len(texto1) > len(texto2):
    mayor = len(texto1)
else:
    mayor = len(texto2)

with open("out.txt", "w") as file:
    for i in range(mayor):
        if i < len(texto1):
            file.write(texto1[i])
            if i == len(texto1) - 1:
                file.write("\n")
        if i < len(texto2):
            file.write(texto2[i])
            if i == len(texto2) - 1:
                file.write("\n")
