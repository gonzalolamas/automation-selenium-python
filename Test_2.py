import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(1)

driver.execute_script("window.scrollTo(0, 200);")
time.sleep(1)

nom = driver.find_element(by=By.ID, value="userName")
nom.send_keys("gonzalo")
driver.find_element(by=By.ID, value="userEmail").send_keys("gonzalo@gmial.com")
driver.find_element(by=By.ID, value="currentAddress").send_keys("calle vergeara 121")
driver.find_element(by=By.ID, value="permanentAddress").send_keys("Calle 2 dirrecion")

driver.execute_script("window.scrollTo(0, 400);")
time.sleep(1)

driver.find_element(by=By.ID, value="submit").click()
time.sleep(2)

driver.close()
