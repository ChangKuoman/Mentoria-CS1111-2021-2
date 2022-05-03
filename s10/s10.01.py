
### INTRODUCCION ###

# archivos
archivo = open("archivo.txt", "r")
for cadena in archivo:
    print(cadena)
archivo.close()


# .split()
# .strip()
# .rstrip()
archivo = open("archivo.txt", "r")
texto = archivo.readlines()
print(texto)
for i in texto:
    print(i.rstrip())
archivo.close()


letra = "HOLA\n"
print(letra)

f=open('archivo.txt', 'r')
cad= f.readline()
while cad != '':
    print(cad,end='')
    cad = f.readline()

# a -> aniadir
# w -> sobreescribir
