# nutrition_api_documentation
# https://docs.google.com/document/d/1_q-K-ObMTZvO0qUEAxROrN3bwMujwAN25sLHwJzliK0/edit#
import os
import requests
from dotenv import load_dotenv
from datetime import datetime

# TODO: 1.  Using the Sheety Documentation, write some code to use the Sheety API to
#  generate a new row of data in your Google Sheet for each of the exercises that you
#  get back from the Nutritionix API. The date and time columns should contain the current
#  date and time from the Python datetime module.
#  url: https://dashboard.sheety.co/projects/

load_dotenv()
time_now = datetime.now()
date_today = time_now.strftime("%d/%m/%Y, %H:%M:%S").split(',')
gender = "male"
weight = 83.5
height = 174
age = 36

# header and data dict
nutrition_url = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "x-app-id": os.getenv('nutrition_app_id'),
    "x-app-key": os.getenv('nutritionix_api_key'),
    "Content-Type": "application/json"
}

user_input = input("Please enter what you did today?:\n ")
params = {
    "query": user_input,
    "gender": gender,
    "weight_kg": weight,
    "height_cm": height,
    "age": age
}

# request to the nutrition endpoint with NLP which gives data about the exercise info
response = requests.post(url=nutrition_url, json=params, headers=headers)
response.raise_for_status()
outs = response.json()

sheety_input = {
    "workout":
        {
            "date": date_today[0],
            "time": date_today[1],
            "exercise": outs['exercises'][0]["user_input"],
            "duration": outs['exercises'][0]["duration_min"],
            "calories": outs['exercises'][0]["nf_calories"],
            "id": outs['exercises'][0]["tag_id"]
        }
}
sheety_url = os.getenv('sheety_url')
bearer_headers = {"Authorization": os.getenv('sheety_bearer_token')}

# this send the auth header token for authorization
post_request = requests.post(url=sheety_url, json=sheety_input, headers=bearer_headers)
post_request.raise_for_status()

