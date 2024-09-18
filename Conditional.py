import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

driver.get("https://demoqa.com/")
driver.maximize_window()
t = 2

titulo = driver.find_element(by=By.XPATH, value="//img[@src='/images/Toolsqa.jpg']")
print(titulo.is_displayed())
btn1 = driver.find_element(by=By.XPATH, value="(//div[contains(@class,'card-up')])[1]")

if(titulo.is_displayed()==True):
    print("existe la imagen")
    driver.execute_script("window.scrollBy(0,200)")
    btn1.click()
    time.sleep(t)
else:
    print("non existe la imagen")

driver.close()
