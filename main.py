import requests
from datetime import datetime
import os

APP_ID = os.environ.get("APP_ID")
APP_KEY = os.environ.get("APP_KEY")

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
question = input("what exercise did you do today? ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}
params = {
        "query": question
        }

response = requests.post(url=nutritionix_endpoint, json=params, headers=headers)
result = response.json()
print(result)

now = datetime.now()
today = now.date().strftime("%d/%m/%Y")
time = now.time().strftime("%X")

print(result["exercises"][0]["duration_min"])

sheety_endpoint = "https://api.sheety.co/d9e521453d80d23aeb05291b1dc787af/myWorkouts/workouts"
y_headers = {
    "Authorization": os.environ.get("AUTHORIZATION")
}

for i in result["exercises"]:
    sheety_params = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": i["user_input"],
            "duration": i["duration_min"],
            "calories": i["nf_calories"],
        }
    }
    response = requests.post(url=sheety_endpoint, json=sheety_params, headers=y_headers)
    print(response.text)
