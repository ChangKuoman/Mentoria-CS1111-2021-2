
### INTRODUCCION ###

# strings

# .split()
frase = "TRES TRISTES TIGRES TRAGAN TRIGO EN UN TRIGAL"

nueva= ""
for palabra in frase.split():

    for letra in range(len(palabra)):
        if letra+1 == len(palabra):
            nueva += palabra[letra].upper() # mayuscula
        else:
            nueva += palabra[letra].lower() # minuscula
    nueva += " "

print(nueva)

# UPPER --> MAYUSCULAS
# LOWER --> minusculas
# CAPITALIZE --> Capitalize

# .capitalize()
nueva2 = frase.capitalize()
print(nueva2)

mayusc = ""
for palabra in frase.split():
    mayusc += palabra.capitalize() + " "

print(mayusc)

palabra = str(input("Ingrese palabra: "))
print(palabra.upper())
