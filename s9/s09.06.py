
### EJERCICIO ###

# Crear un quiosco que tenga las siguientes opciones:
#
# Quiosco Pan con Palta
#
# Elija una opcion
# 1. Ingresar un nuevo producto
# 2. Averiguar el costo de un producto
# 3. Imprimir todos los productos con su precio
# 4. Salir
#
# y en el diccionario de productos cuente al principio:

productos = {'Pan':1.5, 'Palta':5}

while True:
    print("""
    Elija una opcion
    1. Ingresar un nuevo producto
    2. Averiguar el costo de un producto
    3. Imprimir todos los productos con su precio
    4. Salir
    """)

    n = int(input("Ingrese opcion: "))

    if n == 1:

        nombre = str(input("Ingrese nombre de producto: "))
        precio = float(input("Ingrese precio: "))

        productos[nombre] = precio

    elif n == 2:

        nombre = str(input("Ingrese producto a saber el precio: "))
        print("El precio del producto es:")
        print("S/.", productos[nombre])

    elif n == 3:

        for i,j in productos.items():
            print(f"Producto: {i}")
            print(f"Precio: S/.{j}")

    elif n == 4:
        break
