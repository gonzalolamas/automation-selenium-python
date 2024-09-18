import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

driver.get("https://demo.seleniumeasy.com/bootstrap-modal-demo.html")
driver.maximize_window()
t = 2

driver.find_element(by=By.XPATH, value="//a[@href='#myModal0']").click()
time.sleep(t)

try:
    Buscar = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "(//a[@href='#'][contains(.,'Save changes')])[1]")))
    Buscar = driver.find_element(by=By.XPATH, value="(//a[@href='#'][contains(.,'Save changes')])[1]")
    time.sleep(t)

except TimeoutException as ex:
    print(ex.msg)

driver.close()
