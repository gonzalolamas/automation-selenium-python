import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")
driver.maximize_window()
t = 2

#btn = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[@href='#'][contains(.,'No, thanks!')]")))
#btn.click()

driver.find_element(by=By.XPATH, value="//input[@id='user-message']").send_keys("Bienvenida a Selenium" + Keys.TAB + Keys.ENTER)
time.sleep(t)

driver.find_element(by=By.XPATH, value="//input[@id='value1']").send_keys("5" + Keys.TAB + "5" + Keys.TAB + Keys.ENTER)
time.sleep(t)

driver.execute_script("window.scrollTo(0, 300);")

driver.close()
