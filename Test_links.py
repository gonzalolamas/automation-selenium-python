import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()

driver.get("https://demo.seleniumeasy.com/input-form-demo.html")
driver.maximize_window()
t = 3

#obtener todos los links de la pagina
links = driver.find_elements(by=By.TAG_NAME, value="a")

print("el numero de links son: ", len(links))

for num in links:
    print(num.text)

driver.find_element(by=By.LINK_TEXT, value="Date pickers").click()
time.sleep(t)
driver.find_element(by=By.LINK_TEXT, value="JQuery Date Picker").click()
time.sleep(t)

time.sleep(t)
driver.close()


