import requests

"""Função que busca latitude e longitude de uma 
   API externa de acordo com a cidade.

   Entrada: cidade -> Saída: latitude, longitude
"""


def get_coordinates_from_city(name_city):

    url = 'https://nominatim.openstreetmap.org/search'
    params = {
        "q": name_city,
        "format": "json",
    }

    headers = {"User-Agent": "climaapp/1.0"} 

    r = requests.get(url, params=params, headers=headers)

    data = r.json()

    if not data: 
        raise ValueError("Cidade não encontrada")

    lat = str(data[0]["lat"][:-4])
    lon = str(data[0]["lon"][:-4])

    return (lat, lon)

    
        
