from selenium import webdriver
from selenium.webdriver.common.by import By
from settings import *
import time

LINKEDIN_URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(LINKEDIN_URL)

sign_in_button = driver.find_element(By.XPATH, "/html/body/div[3]/header/nav/div/a[2]")
sign_in_button.click()

time.sleep(2)

username = driver.find_element(By.ID, value="username")
username.send_keys(MY_EMAIL)

password = driver.find_element(By.ID, value="password")
password.send_keys(PASSWORD)

time.sleep(2)
sign_in_after_creds = driver.find_element(By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')
sign_in_after_creds.click()

time.sleep(2)
save_job_button = driver.find_element(By.XPATH, value='//*[@id="main"]/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[6]/div/button')
save_job_button.click()