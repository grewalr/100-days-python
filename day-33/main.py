import requests
from datetime import datetime as dt

URL = "https://api.sunrise-sunset.org/json"
MY_LAT = 51.638821
MY_LONG = -0.469190

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get(url=URL, params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

print(sunrise)
print(sunset)

time_now = dt.now()
hour = time_now.hour

print(hour)
# print(time_now)


