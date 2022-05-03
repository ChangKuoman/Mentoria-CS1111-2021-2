
### EJERCICIO ###

# dictionary
dic = {}

n = int(input("input (n): "))

for i in range(n):
    equipo = str(input("voto: "))

    if equipo not in dic.keys():
        dic[equipo] = 1
    else:
        dic[equipo] += 1

print("Output:")
for i in dic.keys():
    print(f"{i} = {dic[i]} votaciones")
