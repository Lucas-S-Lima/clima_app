import requests


"""Função que busca temperatura de uma API externa 
   de acordo com latitude e longitude.
   
   Entrada: latitude, longitude -> Saída: temperatura
"""

def get_temperature_from_coordinates(lat, lon):

        url = 'https://api.open-meteo.com/v1/forecast'
        params = {
            "latitude": lat,
            "longitude": lon,
            "current_weather": True
        }

        r = requests.get(url, params=params)

        data = r.json()
        temperature = data["current_weather"]["temperature"]

        return temperature
