__author__ = "Hipolito Concepcion"
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class WaitAction(object):

    def waitforelementbyxpath(self, driver: webdriver, xpath, seconds):
        print("Waiting for element")
        for i in range(seconds):
            try:
                driver.find_element(By.XPATH, xpath)
                break
            except NoSuchElementException:
                driver.implicitly_wait(1)

    def waitforelementbytext(self, driver: webdriver, text, seconds):
        print("Waiting for element")
        for i in range(seconds):
            try:
                driver.find_element(By.LINK_TEXT, text)
                break
            except NoSuchElementException:
                driver.implicitly_wait(1)
