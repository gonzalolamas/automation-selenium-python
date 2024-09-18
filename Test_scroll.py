import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()

driver.get("https://pixabay.com/es/")
driver.maximize_window()
t = 3


try:
    Buscar = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//span[@class='label--Ngqjq'][contains(.,'Descubre más')]")))
    Buscar = driver.find_element(by=By.XPATH, value="//span[@class='label--Ngqjq'][contains(.,'Descubre más')]")
    ir = driver.execute_script("arguments[0].scrollIntoView()", Buscar)
    time.sleep(t)

except TimeoutException as ex:
    print(ex.msg)

time.sleep(t)
driver.close()


