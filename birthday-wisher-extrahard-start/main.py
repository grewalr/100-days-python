##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv - month and day

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address at 8 am

import pandas
import random
import smtplib
from datetime import datetime as dt

MY_EMAIL = "RickyGrewal8@gmail.com"
PASSWORD = "vugf pfxh tbhs rlls"
SMTP = "smtp.gmail.com"
HOUR_TO_SEND = 8

def send_email(letter, email_address):
    with smtplib.SMTP(SMTP) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs=email_address, 
            msg=f"Subject:Happy Birthday\n\n{letter}"
        )


now = dt.now()
current_hour = now.hour

if current_hour == HOUR_TO_SEND:
    weekday = now.weekday()
    month = now.month
    date = now.day

    birthdays_df = pandas.read_csv("birthdays.csv")
    birthday_df = birthdays_df[(birthdays_df["month"] == month) & (birthdays_df["day"] == date)]
    
    if not birthday_df.empty:
        letter_template = f"./letter_templates/letter_{random.randint(1,3)}.txt"

        name = birthday_df.name.item()
        email = birthday_df.email.item()

        with open(letter_template, "r") as bday_file:
            a = bday_file.read()
            new_letter = a.replace("[NAME]", name)

        send_email(new_letter, email)
    else:
        print("NO BIRTHDAY WISHES TO SEND!!!")
