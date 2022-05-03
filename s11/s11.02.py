
### INTRODUCCION ###

# archivos
import json

with open("data.json", "r") as archivo:
    informacion = json.load(archivo)

print(informacion)

informacion["Maria"]["carrera"] = "cs"

print(informacion["Maria"])

print(json.dumps(informacion, indent=3))

dic = {
    1:{
        2:3,
        4:5
    },
    2:{
        3:4,
        5:6
    }
}

print(json.dumps(dic, indent=3))
