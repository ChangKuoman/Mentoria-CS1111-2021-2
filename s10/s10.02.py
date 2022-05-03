
### INTRODUCCION ###

# archivos
# a -> aniadir
# w -> sobreescribir


file = open("escribir.txt", "a")
cadena = str(input("Escribir algo: "))
file.write(cadena)
file.close()


with open("nombre.txt", "w") as f:
    while True:
        cadena = str(input("Escribir algo: "))
        if cadena == "fin":
            break
        f.write(cadena)
