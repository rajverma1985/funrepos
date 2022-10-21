import os
import requests
from dotenv import load_dotenv

# load all env variables
load_dotenv()

# example call: https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&exclude={part}&appid={API key}
url = "https://api.openweathermap.org/data/2.5/weather"
params = {
            "lat": os.getenv('lat'),
            "lon": os.getenv('long'),
            "exclude": "current,minutely,daily",
            "appid": os.getenv('weather_api_key')
            }

response = requests.get(url, params=params)
response.raise_for_status()
data = response.json()
print(data)
