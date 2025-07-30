import requests

def buscar_moeda(par):
    url = f"https://economia.awesomeapi.com.br/json/last/{par}"
    response = requests.get(url)
    return response.json()