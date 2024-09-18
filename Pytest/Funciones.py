import time
import unittest

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait



class Funciones_Globales():

    def __init__(self, driver):
        self.driver = driver

    def Tiempo(self, tie):
        t = time.sleep(tie)
        return t

    def Navegar(self, Url, Tiempo):
        self.driver.get(Url)
        self.driver.maximize_window()
        t = time.sleep(Tiempo)
        return t

    def SEX(self, elemento):
        val = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, elemento)))
        val = self.driver.execute_script("arguments[0].scrollIntoView(true);", val)
        val = self.driver.find_element(By.XPATH, elemento)
        return val

    def SEI(self, elemento):
        val = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, elemento)))
        val = self.driver.execute_script("arguments[0].scrollIntoView(true);", val)
        val = self.driver.find_element(By.ID, elemento)
        return val

    def Texto_Mixto(self, tipo, selector, texto, tiempo=.1):
        if (tipo == "xpath"):
            try:
                val = self.SEX(selector)
                val.clear()
                val.send_keys(texto)
                print("Escribiendo en el campo {} el texto -> {}".format(selector, texto))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento" + selector)
                return t
        elif (tipo == "id"):
            try:
                val = self.SEI(selector)
                val.clear()
                val.send_keys(texto)
                print("Escribiendo en el campo {} el texto -> {}".format(selector, texto))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento" + selector)
                return t
    def Click_Mixto(self, tipo, selector, tiempo=.1):
        if (tipo == "xpath"):
            try:
                val = self.SEX(selector)
                val.click()
                print("dando click en {} -> {}".format(selector, selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento" + selector)
                return t
        elif (tipo == "id"):
            try:
                val = self.SEI(selector)
                val.click()
                print("dando click en {} -> {}".format(selector, selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento" + selector)
                return t

    def Text_Xpath(self, xpath, texto, Tiempo):
        val = self.driver.find_element(By.XPATH, xpath)
        val.clear()
        val.send_keys(texto)
        t = time.sleep(Tiempo)
        return t

    def Texto_Xpath_Validacion(self, xpath, texto, Tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView()", val)
            val = self.driver.find_element(By.XPATH, xpath)
            val.clear()
            val.send_keys(texto)
            t = time.sleep(Tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento" + xpath)

    def Texto_ID(self, ID, texto, Tiempo):
        val = self.driver.find_element(By.ID, ID)
        val.clear()
        val.send_keys(texto)
        t = time.sleep(Tiempo)
        return t

    def Click_Xpath_Validacion(self, xpath, Tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView()", val)
            val = self.driver.find_element(By.XPATH, xpath)
            val.click()
            t = time.sleep(Tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento" + xpath)
            return t

    def Select_Xpath_Type(self, xpath, tipo, dato, tiempo):
        try:
            val = self.SEX(xpath)
            val = Select(val)
            if(tipo == "text"):
                val.select_by_visible_text(dato)
            elif(tipo == "index"):
                val.select_by_index(dato)
            elif(tipo == "value"):
                val.select_by_value(dato)
            print("El campo seleccionado es {}".format(dato))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento" + xpath)
            return t

    def Select_ID_Type(self, id, tipo, dato, tiempo):
        try:
            val = self.SEI(id)
            val = Select(val)
            if(tipo == "text"):
                val.select_by_visible_text(dato)
            elif(tipo == "index"):
                val.select_by_index(dato)
            elif(tipo == "value"):
                val.select_by_value(dato)
            print("El campo seleccionado es {}".format(dato))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento" + id)
            return t

    def Upload_Xpath(self, xpath, ruta, tiempo):
        try:
            val = self.SEX(ruta)
            val.send_keys(ruta)
            print("Se carga la imagen {}".format(ruta))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento" + xpath)
            return t

    def Upload_ID(self, id, ruta, tiempo):
        try:
            val = self.SEI(ruta)
            val.send_keys(ruta)
            print("Se carga la imagen {}".format(ruta))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento" + id)
            return t

    #Funcion radio y check
    def Check_Xpath(self, xpath, tiempo):
        try:
            val = self.SEX(xpath)
            val.click()
            print("Click en el elemento {}".format(xpath))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento" + xpath)
            return t

    def Check_Xpath_Multiples(self, tiempo, *args):
        try:
            for num in args:
                val = self.SEX(num)
                val.click()
                print("Click en el elemento {}".format(num))
                t = time.sleep(tiempo)
                return t
        except TimeoutException as ex:
            for num in args:
                print(ex.msg)
                print("No se encontro el elemento" + num)
                return t

    def Mouse_Doble(self, tipo, selector, tiempo):
        if (tipo == "xpath"):
            try:
                val = self.SEX(selector)
                act = ActionChains(self.driver)
                act.double_click(val).perform()
                print("DoubleClick en {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento" + selector)
                return t
        elif (tipo == "id"):
            try:
                val = self.SEI(selector)
                act = ActionChains(self.driver)
                act.double_click(val).perform()
                print("DoubleClick en {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento" + selector)
                return t