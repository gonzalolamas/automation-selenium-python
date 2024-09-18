import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

driver.get("https://demo.seleniumeasy.com/basic-select-dropdown-demo.html")
driver.maximize_window()
driver.implicitly_wait(10)
t = 5

diaSelect = driver.find_element(by=By.XPATH, value="//select[contains(@id,'select-demo')]")
ds = Select(diaSelect)

ds.select_by_visible_text("Sunday")
time.sleep(t)

ds.select_by_index(3)
time.sleep(t)

ds.select_by_value("Saturday")

ciudad = Select(driver.find_element(by=By.XPATH, value="//select[contains(@id,'multi-select')]"))

ciudad.select_by_index(1)
time.sleep(t)
ciudad.select_by_index(3)

driver.execute_script("window.scrollTo(0, 300);")

time.sleep(t)
driver.close()
