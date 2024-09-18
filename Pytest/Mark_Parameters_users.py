import time
import unittest
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from Funciones import Funciones_Globales

t = 0.2

def get_Data():
    return [
        ("Rodrigo", "1234"),
        ("Lautaro", "12341"),
        ("Emanuel", "123554"),
        ("Fizz", "12347"),
        ("Test", "12348"),
        ("Leme", "12349"),
    ]

@pytest.mark.login
@pytest.mark.parametrize("user, clave", get_Data())
def test_login(user, clave):
    global driver, f
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    driver.implicitly_wait(20)
    f = Funciones_Globales(driver)
    f.Texto_Mixto("xpath", "//input[contains(@name,'username')]", user, t)
    f.Texto_Mixto("xpath", "//input[contains(@type,'password')]", clave, t)
    f.Click_Mixto("xpath", "//button[@type='submit']", 2)
    print("Entrando al sistema")

def teardown_function():
    print("Salida del test")
    driver.close()