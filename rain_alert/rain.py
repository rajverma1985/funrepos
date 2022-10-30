import os
import requests
from dotenv import load_dotenv

# api documentation here: https://openweathermap.org/current
# load all env variables
load_dotenv()
url = "https://api.openweathermap.org/data/2.5/onecall"
params = {
            "lat": os.getenv('lat'),
            "lon": os.getenv('long'),
            "exclude": "current,minutely,daily",
            "appid": os.getenv('weather_api_key')
            }

response = requests.get(url, params=params)
response.raise_for_status()
data = response.json()
print(data['weather'])
