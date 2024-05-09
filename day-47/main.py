import requests
from bs4 import BeautifulSoup
from pprint import pprint
from notification_manager import NotificationManager

AMAZON_URL = "https://amzn.eu/d/2BGHZxM"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept-Language": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
}

TARGET_PRICE = 26

response = requests.get(url=AMAZON_URL, headers=HEADERS)
response.raise_for_status()

amazon_web_page = response.text
soup = BeautifulSoup(amazon_web_page, "html.parser")

price_str = soup.find("span", class_="a-offscreen")
price = float(price_str.get_text().strip("£"))

print(price)

nm = NotificationManager()

if price < TARGET_PRICE:
    nm.send_email(subject="*** AMAZON PRICE DROP ALERT ***", 
                  body=f"Price is now {price} which is less than your target price of {TARGET_PRICE}")

