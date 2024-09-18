import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

driver.get("https://demo.seleniumeasy.com/input-form-demo.html")
driver.maximize_window()
t = 2

btn = driver.find_element(by=By.XPATH, value="//button[@type='submit'][contains(.,'Send')]")
btn.click()
time.sleep(t)

name_val=driver.find_element(by=By.XPATH, value="//small[@class='help-block'][contains(.,'Please supply your first name')]")
name=name_val.text
print("El valor del error es: " + name)
if(name=="Please supply your first name"):
    print("falta el nombre")
    cn=driver.find_element(by=By.XPATH, value="//input[contains(@name,'first_name')]")
    cn.send_keys("Gonzalo")
else:
    print("nombre incorrecto")

print(btn.is_enabled())
if(btn.is_enabled()==False):
    print("faltan campos por llenar")
else:
    print("todo ok")

time.sleep(t)
driver.close()
