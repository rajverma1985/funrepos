# nutrition_api_documentation
# https://docs.google.com/document/d/1_q-K-ObMTZvO0qUEAxROrN3bwMujwAN25sLHwJzliK0/edit#
import os
from dotenv import load_dotenv
from datetime import datetime

time_now = datetime.now()
# TODO: 1.  Using the Sheety Documentation, write some code to use the Sheety API to
#  generate a new row of data in your Google Sheet for each of the exercises that you
#  get back from the Nutritionix API. The date and time columns should contain the current
#  date and time from the Python datetime module.
#  url: https://dashboard.sheety.co/projects/

# header and data dict
load_dotenv()
nutrition_url = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "x-app-id": os.getenv('nutrition_app_id'),
    "x-app-key": os.getenv('nutritionix_api_key'),
    "Content-Type": "application/json"
}
user_input = input("Please enter what you did today?:\n ")
params = {
    "query": user_input,
    "gender": "male",
    "weight_kg": 83.5,
    "height_cm": 174,
    "age": 36
}

# response = requests.post(url=nutrition_url, json=params, headers=headers)
# response.raise_for_status()
# print(response.text)
# print(response.json())

print(time_now.strftime("%d/%m/%Y, %H:%M:%S").split(','))
