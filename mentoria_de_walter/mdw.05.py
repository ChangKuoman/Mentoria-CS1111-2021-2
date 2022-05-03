
# hallar la suma de los digitos de un numero e indicar si la suma es par o no

n = int(input("N: "))

suma=0
for i in str(n):
    suma += int(i)
print(suma)
if suma%2 == 0:
    print("es par")
else:
    print("es impar")

# 12345
# 12345 % 10 = 5
# 12345 // 10 = 1234

# 1234 % 10 = 4
# 1234 // 10 = 123

# 123 % 10 = 3
# 123 // 10 = 12

# 12 % 10 = 2
# 12 // 10 = 1

# 1 % 10 = 1
# 1 // 10 = 0

suma = 0
while n > 0:
    suma += n % 10
    n = n // 10
print(suma)
