import unittest

from selenium import webdriver
from Pytest.Funciones import Funciones_Globales

tg = 1


class base_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        t = 2

    def test_1(self):
        driver = self.driver
        f = Funciones_Globales(driver)
        f.Navegar("https://demoqa.com/text-box", tg)
        f.Texto_Mixto("id", "userName", "Gonzalo", tg)
        f.Click_Mixto("id", "submit", tg)

    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main()