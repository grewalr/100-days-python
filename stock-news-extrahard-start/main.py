## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

import requests
from datetime import *
from twilio.rest import Client
import os
from dotenv import dotenv_values
import math

config = dotenv_values("./.project_config")

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_PRICE_URL = "https://www.alphavantage.co/query"
STOCK_NEWS_URL = "https://newsapi.org/v2/everything"
TWILIO_URL = "https://www.twilio.com"
NUMBER_OF_NEWS_ARTICLES = 3

stock_price_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": config.get("STOCK_MARKET_API_KEY"),
}

def send_text(body_text):
    client = Client(config.get("ACCOUNT_SID"), config.get("AUTH_TOKEN"))
    message = client.messages.create(
        body=body_text,
        from_="+447480619998",
        to="+447810888018"
    )

yesterdays_datetime = datetime.today() - timedelta(days=1)

if yesterdays_datetime.isoweekday() > 5:
    time_delta = yesterdays_datetime.isoweekday() - 5
    yesterdays_datetime = yesterdays_datetime - timedelta(days=time_delta)

yesterdays_date = datetime.strftime(yesterdays_datetime, "%Y-%m-%d")

day_before_yesterday_datetime = yesterdays_datetime - timedelta(days=1)
day_before_yesterday_date = datetime.strftime(yesterdays_datetime - timedelta(days=1), "%Y-%m-%d")

stock_price_resp = requests.get(
    STOCK_PRICE_URL, 
    params=stock_price_params
)

stock_price_resp.raise_for_status()
stock_price_data = stock_price_resp.json()

yesterdays_close = float(stock_price_data['Time Series (Daily)'][yesterdays_date]['4. close'])
day_before_yesterday_close = float(stock_price_data['Time Series (Daily)'][day_before_yesterday_date]['4. close'])

percentage_change = int((yesterdays_close - day_before_yesterday_close) / day_before_yesterday_close * 100)

if percentage_change < 5:
    news_params = {
        "q": "tesla",
        "from": yesterdays_date,
        "to": day_before_yesterday_date,
        "sortBy": "publishedAt",
        "language": "en",
        "apikey": config.get("NEWS_API_KEY"),
    }
    
    "https://newsapi.org/v2/everything?q=apple&from=2024-03-21&to=2024-03-21&sortBy=popularity&apiKey=633a2f637ce940538750fa999a6d5fa6"
    
    news_response = requests.get(
        STOCK_NEWS_URL, 
        params=news_params
    )
    
    news_response.raise_for_status()
    news_response_data = news_response.json()
    
    news_articles = news_response_data["articles"][:NUMBER_OF_NEWS_ARTICLES]
    headlines = []
    briefs = []
    
    for item in news_articles:
        headlines.append(item["title"])
        briefs.append(item["description"])
    
    delta = "🔺"
    if percentage_change < 0:
        delta = "🔻"
    
    output = ""
    for i in range(len(headlines)):
        send_text(
            f"""
            {STOCK}: {delta}{abs(percentage_change)}%
            Headline: {headlines[i]}
            Description: {briefs[i]}
            """
        )
 
