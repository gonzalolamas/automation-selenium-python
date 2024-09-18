import time
import unittest
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from Funciones import Funciones_Globales

t = 0.5

@pytest.fixture(scope='module')
def setup_login_uno():
    global driver, f
    driver = webdriver.Chrome()
    driver.get("https://demo.testim.io/")
    driver.maximize_window()
    driver.implicitly_wait(20)
    f = Funciones_Globales(driver)
    f.Click_Mixto("xpath", "//button[@class='NavButton__nav-button___34wHC'][contains(.,'Log in')]", t)
    f.Texto_Mixto("xpath", "//input[@tabindex='1']", "John", t)
    f.Texto_Mixto("xpath", "//input[contains(@type,'password')]", "Conor12", t)
    f.Click_Mixto("xpath", "//button[@form='login'][contains(.,'Log in')]", t)
    print("Entrando al sistema")
    yield
    print("salida del login")
    driver.close()

@pytest.fixture(scope='module')
def setup_login_dos():
    global driver, f
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    driver.implicitly_wait(20)
    f = Funciones_Globales(driver)
    f.Texto_Mixto("xpath", "//input[contains(@name,'username')]", "Admin", t)
    f.Texto_Mixto("xpath", "//input[contains(@type,'password')]", "admin123", t)
    f.Click_Mixto("xpath", "//button[@type='submit']", 3)
    print("Entrando al sistema")
    yield
    print("salida del login")
    driver.close()

@pytest.mark.usefixtures("setup_login_uno")
def test_uno():
    print("Entrando al sistema uno")
    f.Click_Mixto("xpath", "//input[contains(@value,'Planet color')]", 2)
    f.Click_Mixto("xpath", "//li[contains(.,'Blue')]", 2)

@pytest.mark.usefixtures("setup_login_dos")
def test_dos():
    print("Entrando al sistema dos")
    f.Click_Mixto("xpath", "//a[@href='/web/index.php/pim/viewPimModule']", t)
    f.Click_Mixto("xpath", "//button[@type='button'][contains(.,'Add')]", t)
    nombre = driver.find_element(by=By.XPATH, value="//input[contains(@name,'firstName')]")
    nombre.send_keys("Gonzalo"+Keys.TAB+"Gon"+Keys.TAB+"Leme")
    time.sleep(t)
    f.Click_Mixto("xpath", "//button[@type='submit'][contains(.,'Save')]", t)
    f.Click_Mixto("xpath", "//a[@href='/web/index.php/pim/viewPimModule']", t)
    f.Texto_Mixto("xpath", "(//input[contains(@placeholder,'Type for hints...')])[1]","Gonzalo", t)
    #f.Texto_Mixto("xpath", "(//input[contains(@class,'oxd-input oxd-input--active')])[2]", "col2", t)
    f.Click_Mixto("xpath", "//button[@type='submit'][contains(.,'Search')]", t)

    element = driver.find_element(by=By.XPATH, value="(//div[contains(.,'Gonzalo Gon')])[21]")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(3)
