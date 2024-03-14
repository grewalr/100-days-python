import smtplib
import random
import datetime as dt

MY_EMAIL = "RickyGrewal8@gmail.com"
TO_EMAIL = "rik@mcgrewal.com"
PASSWORD = "vugf pfxh tbhs rlls"
SMTP = "smtp.gmail.com"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 2:
    with open("./quotes.txt", "r") as file:
        quotes_list = file.readlines()
        random_quote = random.choice(quotes_list)

    with smtplib.SMTP(SMTP) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs=TO_EMAIL, 
            msg=f"Subject:Monday Motivation\n\n{random_quote}"
        )
