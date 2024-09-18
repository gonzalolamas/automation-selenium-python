import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/upload")
driver.maximize_window()
t = 3

try:
    Buscar = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@id,'file-upload')]")))
    Buscar = driver.find_element(by=By.XPATH, value="//input[contains(@id,'file-upload')]")
    Buscar.send_keys("C://Users//Arbusta//PycharmProjects//pythonProject//Imagenes//update-5238354_640.jpg")
    time.sleep(t)
    driver.find_element(by=By.XPATH, value="//input[contains(@id,'file-submit')]").click()
    time.sleep(t)


except TimeoutException as ex:
    print(ex.msg)

time.sleep(t)
driver.close()


