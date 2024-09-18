import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(1)

driver.execute_script("window.scrollTo(0, 200);")
time.sleep(1)

nom = driver.find_element(by=By.ID, value="userName")
nom.send_keys("gonzalo")
nom.send_keys(Keys.TAB + "gonz@gmail.com" + Keys.TAB + "dirrecion one" + Keys.TAB + "dirrecion two" + Keys.TAB + Keys.ENTER)

driver.execute_script("window.scrollTo(0, 500);")
time.sleep(1)

driver.find_element(by=By.XPATH, value="//span[@class='text'][contains(.,'Check Box')]").click()
time.sleep(2)

driver.close()
