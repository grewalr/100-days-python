import requests
from datetime import datetime
from twilio.rest import Client
import os

TWILIO_RECOVERY_CODE = "**********************"
API_KEY = os.environ.get("API_KEY")
LATITUDE = 51.638821
LONGITUDE = -0.469190
END_POINT = "https://api.openweathermap.org/data/2.5/forecast"
PARAMETERS = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": API_KEY,
    "cnt": 4
}

account_sid = "***********************************"
auth_token = os.environ.get("AUTH_TOKEN")

response = requests.get(END_POINT, params=PARAMETERS)
response.raise_for_status()
data = response.json()
condition_codes = []

will_rain = False
for item in data["list"]:
    condition_code = item["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
    
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☂️",
        from_="+447480619998",
        to="+447810888018"
    )
    
    print(message.status)
