
### INTRODUCCION ###

# strins
palabra = str(input(""))

# "Hola"
#  0123
#  -4 -3 -2 -1

for letra in range(len(palabra)):
    if letra == 2:
        continue
    print(palabra[letra])
