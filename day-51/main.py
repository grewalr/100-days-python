from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from settings import *
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "/Users/grewalr/dev/chromedriver"
SPEEDTEST_URL = "https://www.speedtest.net/"

class InternetSpeedTwitterBot:
    
    def __init__(self):
        self.driver = self.__create_driver() 
        self.up = 0
        self.down = 0
        
    def __create_driver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        return webdriver.Chrome(options=chrome_options)
    
    def get_internet_speed(self):
        self.driver.get(SPEEDTEST_URL)
        go_button = self.driver.find_element(By.XPATH, value='/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go_button.click()
        
        time.sleep(60)
        
        self.down = self.driver.find_element(By.XPATH, value='/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = self.driver.find_element(By.XPATH, value='/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
    
    def tweet_at_provider(self):
        "FUNCTION DISABLED AS DO NOT WANT TO USE THIS FEATURE TO SEND TWEETS"
        pass
    
    
bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
# bot.tweet_at_provider()
