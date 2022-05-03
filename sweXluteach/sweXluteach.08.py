
# enunciado: img8

# L = T**4 * R**2
# L = R**2 * T**4
tabla = [
    ['UY-Scutti', 1.71, 3365],
    ['Canis Mayoris', 1.42, 3490],
    ['KY Cyg', 1.42, 3500],
    ['Mu Cephei', 1.26, 3750],
    ['S Persei', 1.20, 3000],
    ['VX Sagittarii', 1.12, 3000]
]

for i in range(len(tabla)-1):
    for j in range(len(tabla)-1):

        L1 = tabla[j][2]**4 * tabla[j][1]**2
        L2 = tabla[j+1][2]**4 * tabla[j+1][1]**2
        if L1 > L2:
            tabla[j], tabla[j+1] = tabla[j+1], tabla[j]

for i in range(len(tabla)):
    print(tabla[i][0])
