from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
import time

timeout = time.time() + 5

COOKIE_URL = "https://orteil.dashnet.org/experiments/cookie/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", False)

driver = webdriver.Chrome(options=chrome_options)
driver.get(COOKIE_URL)

cookie = driver.find_element(By.ID, value="cookie")

buy_cursor = driver.find_element(By.ID, value="buyCursor")
buy_cursor_price = int(buy_cursor.text.split("\n")[0].split("-")[1].strip())
 
buy_grandma = driver.find_element(By.ID, value="buyGrandma")
buy_grandma_price = int(buy_grandma.text.split("\n")[0].split("-")[1].strip())

buy_factory = driver.find_element(By.ID, value="buyFactory")
buy_factory_price = int(buy_factory.text.split("\n")[0].split("-")[1].strip())

buy_mine = driver.find_element(By.ID, value="buyMine")
buy_mine_price = int(buy_mine.text.split("\n")[0].split("-")[1].strip().replace(",", ""))

buy_shipment = driver.find_element(By.ID, value="buyShipment")
buy_shipment_price = int(buy_shipment.text.split("\n")[0].split("-")[1].strip().replace(",", ""))

buy_alchemy_lab = driver.find_element(By.ID, value="buyAlchemy lab")
buy_alchemy_lab_price = int(buy_alchemy_lab.text.split("\n")[0].split("-")[1].strip().replace(",", ""))

buy_portal = driver.find_element(By.ID, value="buyPortal")
buy_portal_price = int(buy_portal.text.split("\n")[0].split("-")[1].strip().replace(",", ""))

buy_time_machine = driver.find_element(By.ID, value="buyTime machine")
buy_time_machine_price = int(buy_time_machine.text.split("\n")[0].split("-")[1].strip().replace(",", ""))

def reset_timer():
    timeout = time.time() + 5 

def is_greyed(object: WebElement) -> bool:
    return object.get_attribute("class") == "greyed"

def purchase(object: WebElement):
    if not is_greyed(object):
        object.click()
    
def buy_item(money):
    if money > buy_time_machine_price:
        purchase(buy_time_machine)
    elif money > buy_portal_price:
        purchase(buy_portal)
    elif money > buy_alchemy_lab_price:
        purchase(buy_alchemy_lab)
    elif money > buy_shipment_price:
        purchase(buy_shipment)
    elif money > buy_mine_price:
        purchase(buy_mine)
    elif money > buy_factory_price:
        purchase(buy_factory)
    elif money > buy_grandma_price:
        purchase(buy_grandma)
    elif money > buy_cursor_price:
        purchase(buy_cursor)
    else:
        return

def click_cookie():
    while time.time() < timeout: 
        cookie.click()
    
    money = int(driver.find_element(By.ID, value="money").text)
    
    buy_item(money)
    reset_timer()
    click_cookie()
    
click_cookie()