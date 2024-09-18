import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
driver.implicitly_wait(10)

t = 1
time.sleep(t)

driver.execute_script("window.scrollTo(0, 200);")
time.sleep(t)

nom = driver.find_element(by=By.XPATH, value="//*[@type='text' and @id='userName']")
nom.send_keys("Gonzalo")
time.sleep(t)
driver.find_element(by=By.XPATH, value="//*[@id='userEmail']").send_keys("gonzalo@gmail.com")
time.sleep(t)
driver.find_element(by=By.XPATH, value="//*[@id='currentAddress']").send_keys("Calle Mitre 11")
time.sleep(t)
driver.find_element(by=By.XPATH, value="//*[@id='permanentAddress']").send_keys("Diagonal Norte 22")
time.sleep(t)

driver.execute_script("window.scroll(0, 600);")
time.sleep(t)

driver.find_element(by=By.XPATH, value="//*[@id='submit']").click()
time.sleep(t)

driver.close()
