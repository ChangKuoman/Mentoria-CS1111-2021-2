
### EJERCICIO ###

# Escribir un programa que permita al usuario ingresar palabras hasta poner “F” y se escriba en un archivo .txt

doc = open("nuevo.txt", "w")

palabra = " "

while True:
    palabra = str(input("Ingrese algo: "))
    if palabra == "F":
        break
    doc.write(palabra)
    doc.write("\n")

doc.close()

# a -> add
# w -> write
# r -> read

doc = open("nuevo.txt", "r")

for i in doc:
    print(i)

doc.close()
