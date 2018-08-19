__author__ = "Hipolito Concepcion"
from selenium.webdriver.remote import webelement
from selenium.common.exceptions import NoSuchElementException


class UserAction(object):

    def doclick(self, element: webelement):
            try:
                element.click()
                print("Element Clicked")
            except NoSuchElementException:
                print("Not able to click element")

    def dotypeintext(self, element: webelement, text):
        try:
            print("Typing: " + text)
            element.send_keys(text)
        except NoSuchElementException:
            print("Not able to input on this element")
