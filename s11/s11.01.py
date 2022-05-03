
### INTRODUCCION ###

# archivos
import json

diccionario = {
    "Maria":{
        "edad": 18,
        "carrera":"mecanica"
    },

    "Jose":{
        "edad": 21,
        "carrera":"bio"
    }
}

print(diccionario["Maria"]["carrera"])

diccionario["Jose"]["edad"] = 20

print(diccionario["Jose"]["edad"])

diccionario["Jose"] = {
    "cursos": 7,
    "color_favorito":"rojo"
}

print(diccionario["Jose"])

with open("data.json", "w") as file:
    json.dump(diccionario, file, indent=2)
