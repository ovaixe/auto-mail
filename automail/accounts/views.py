from django.shortcuts import render
import requests


API_KEY = '480964840049453263fc0c97440ffdd7'

COLD = '\U0001F976'
MODERATE = '\U0001F601'
HOT = '\U0001F975'
TOO_HOT = '\U0001F92F'

def get_temperature(city_name):
    try:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}'
        response = requests.get(url, allow_redirects=True)
    except:
        return None
    else:
        response = response.json()
        temperature = response['main']['temp']
        return temperature

def set_emoji(temperature):
    if temperature < 288.15:
        return COLD
    elif temperature >= 288.15 and temperature < 298.15:
        return MODERATE
    elif temperature >= 298.15 and temperature < 308.15:
        return HOT
    else:
        return TOO_HOT