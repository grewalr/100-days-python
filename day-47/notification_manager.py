import smtplib
from settings import *


class NotificationManager:

    def send_email(self, subject, body):
        message = f"""
        Subject: {subject}
        
        {body}
        """
        
        
        with smtplib.SMTP(SMTP, port=PORT) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL, 
                to_addrs=MY_EMAIL,
                msg=message
            )