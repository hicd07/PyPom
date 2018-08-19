__author__ = "Hipolito Concepcion"
from selenium import webdriver
from selenium.webdriver.common.by import By


class PortalHomePage(object):

    def __init__(self, driver: webdriver):
        self.driver = driver
        self.linkEnglishLang_ID = "js-link-box-en"
        self.url = "https://www.wikipedia.org/"

    def getlinkenglang(self):
        return self.driver.find_element(By.ID, self.linkEnglishLang_ID)

    def geturl(self):
        print("Url: " + self.url)
        return self.url
