
# API

import requests

pais = "pe"
dic = requests.get("https://restcountries.com/v3/alpha/" + pais).json()

print(dic[0]['name']['official'])
