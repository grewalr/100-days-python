import requests
from datetime import datetime

APP_ID = "e8546140"
API_KEY = ""
URL = "https://trackapi.nutritionix.com"
END_POINT = "/v2/natural/exercise"
HEADERS = {
    'Content-Type': 'application/json',
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

SHEETY_URL = "https://api.sheety.co/b9efb4077c4782f60a6946f066852b9b/workoutTracking/workouts"
SHEETY_HEADER = {
    "Authorization": "Bearer allowaccess"
}

exercise_input =input("Tell me which exercises you did: ")

payload = {
    "query": exercise_input,
    "gender": "male",
    "weight_kg": "80",
    "height_cm": "173",
    "age": 47
}

payload = {
    "query": exercise_input
}

response = requests.post(url=f"{URL}{END_POINT}", json=payload, headers=HEADERS)
response.raise_for_status()
results = response.json()

todays_date = datetime.now().strftime("%d/%m/%Y")
now_time = now_time = datetime.now().strftime("%X")

for x in results["exercises"]:
    workout = {
       "workout": {
            "date": todays_date,
            "time": now_time,
            "exercise": str(x["name"]).title(),
            "duration": x["duration_min"],
            "calories": x["nf_calories"]
       } 
    }
    
    response = requests.post(url=SHEETY_URL, json=workout, headers=SHEETY_HEADER)
    results = response.json()
    print(results)
    