
# enunciado: img2

matriz = [
    ['pais', 'oro', 'plata', 'bronce'],
    ['estados unidos', 40, 35, 29],
    ['rusia', 39, 32, 28],
    ['inglaterra', 26, 33, 27],
    ['china', 23, 30, 26],
    ['alemania', 22, 31, 27]
]

# output esperado:
# oro: 150
# plata: 161
# bronce: 137
# la medalla mas repartida fue: plata

oro = 0
plata = 0
bronce = 0

for i in range(1, len(matriz)):
    oro += matriz[i][1]
    plata += matriz[i][2]
    bronce += matriz[i][3]

print(oro)
print(plata)
print(bronce)

if oro > plata and oro > bronce:
    print("oro")
elif plata > oro and plata > bronce:
    print("plata")
else:
    print("bronce")
