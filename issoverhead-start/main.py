import requests
import smtplib
from datetime import datetime
from time import sleep


MY_LAT = 51.638821
MY_LONG = -0.469190
MY_EMAIL = "RickyGrewal8@gmail.com"
PASSWORD = "vugf pfxh tbhs rlls"
SMTP = "smtp.gmail.com"
TO_EMAIL = "rik@mcgrewal.com"

def is_within_five_degrees():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    MY_LAT -5 <= iss_latitude <= MY_LAT +5 and MY_LONG -5 <= iss_longitude <= MY_LONG +5
        

def send_email(email_address, body="", subject="TEST"):
    with smtplib.SMTP(SMTP) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs=email_address, 
            msg=f"Subject:{subject}\n\n{body}"
        )  

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

while True:
    print("Now running...")
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    hour = time_now.hour

    if (hour >= sunset or hour <= sunrise) and is_within_five_degrees():
        send_email(TO_EMAIL, subject="Look Up!", bosy="The ISS is above you in the sky!")    
    else:
        print("Cannot see satellite")
        

    sleep(60)
    #If the ISS is close to my current position
    # and it is currently dark
    # Then send me an email to tell me to look up.
    # BONUS: run the code every 60 seconds.
