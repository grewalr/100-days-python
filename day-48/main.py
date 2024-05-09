from selenium import webdriver
from selenium.webdriver.common.by import By

AMAZON_URL = "https://amzn.eu/d/2BGHZxM"
PYTHON_ORG_URL = "https://python.org"

# Keep browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", False)

driver = webdriver.Chrome(options=chrome_options)
# driver.get(AMAZON_URL)
driver.get(PYTHON_ORG_URL)


# price_pound = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_pence = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# search_bar = driver.find_element(By.NAME, value="q")
# element_by_id = driver.find_element(By.ID, value="submit")
# element_by_css_selector = driver.find_element(By.CSS_SELECTOR, value=".documentation-widger a")
# element_by_xpath = driver.find_element(By.XPATH, value='/html/body/div[5]/div[1]/div/div[3]/ul/li[1]/a')

# print(price_pound.text)
# print(price_pence.text)
# print(element_by_xpath.text)


events = {}

events_from_site = [atime.text for atime in driver.find_elements(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li')]

for idx, aEvent in enumerate(events_from_site):
    date = aEvent.split("\n")[0]
    name = aEvent.split("\n")[1]
    events[idx] = {
        "time": date,
        "name": name
    }


print(events)
# driver.close() # closes active tab
driver.quit()  # shuts down browser
