import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
t = 2

btn = driver.find_element(by=By.XPATH, value="//button[contains(@id,'submit')]")
print(btn.is_enabled())

if(btn.is_enabled()==True):
    print("puedes dar click")
else:
    print("no puedes dar click")

driver.close()
