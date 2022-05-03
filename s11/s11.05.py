
### EJERCICIO ###

# ingresar un nombre y obtener los datos de la api
import json
import requests

data = requests.get("https://reqres.in/api/users?page=1").json()
#print(json.dumps(data, indent=3))
#print(json.dumps(data["data"][2], indent=4))
nombre = str(input("Ingrese nombre: "))

for i in data["data"]:
    if i["first_name"] == nombre: # EJM: Emma
        print(json.dumps(i, indent=3))
