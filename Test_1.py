import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(1)

driver.execute_script("window.scrollTo(0, 200);")
time.sleep(1)

nom = driver.find_element(by=By.XPATH, value="//*[@type='text' and @id='userName']")
nom.send_keys("Gonzalo")
driver.find_element(by=By.XPATH, value="//*[@id='userEmail']").send_keys("gonzalo@gmial.com")
driver.find_element(by=By.XPATH, value="//*[@id='currentAddress']").send_keys("calle vergeara 121")
driver.find_element(by=By.XPATH, value="//*[@id='permanentAddress']").send_keys("Calle 2 dirrecion")

driver.execute_script("window.scrollTo(0, 400);")
time.sleep(1)

driver.find_element(by=By.XPATH, value="//*[@id='submit']").click()
time.sleep(2)

driver.close()
