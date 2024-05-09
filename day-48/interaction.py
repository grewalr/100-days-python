from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

WIKIPEDIA_URL = "https://en.wikipedia.org/wiki/Main_Page"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(options=chrome_options)
# driver.get(WIKIPEDIA_URL)

# article_count = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')
# article_count.click()

# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

# search = driver.find_element(By.NAME, value="search")
# search.send_keys("Python", Keys.ENTER)


##############################################

SIGN_UP_URL = "https://secure-retreat-92358.herokuapp.com/"

driver = webdriver.Chrome(options=chrome_options)
driver.get(SIGN_UP_URL)

fname = driver.find_element(By.NAME, value="fName")
fname.send_keys("Rik")

lname = driver.find_element(By.NAME, value="lName")
lname.send_keys("Grewal")

email = driver.find_element(By.NAME, value="email")
email.send_keys("rik@gmail.com")

button = driver.find_element(By.CLASS_NAME, value="btn")
button.click()