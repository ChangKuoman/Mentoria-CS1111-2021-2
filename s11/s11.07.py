
### EJERCICIO DE PC ###

# ingresar una cadena e imprimir las posiciones en las que se encuentran los caracteres en la cadena
import json
texto = str(input("INPUT= ")).lower()

# MANERA 1
dic = {}
for i in range(len(texto)):
    if texto[i] not in dic.keys():
        dic[texto[i]] = [i]
    else:
        dic[texto[i]].append(i)

print(json.dumps(dic, indent=3))

# MANERA 2
dic2= {}
contador=0

for i in texto:
    if i not in dic2.keys():
        dic2[i] = [contador]
    else:
        dic2[i].append(contador)
    contador += 1

print(json.dumps(dic2, indent=3))
