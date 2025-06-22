import requests

URL = "http://servidor:5000/"

response = requests.get(URL)

print("Respuesta del servidor:", response.json())