# Original Script:
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestCase(unittest.TestCase):

    def test_search_wikipedia(self):
        driver = webdriver.Chrome()
        driver.get("https://www.wikipedia.org/")
        driver.find_element(By.ID, "js-link-box-en").click()
        driver.find_element(By.ID, "searchInput").send_keys("Python" + Keys.RETURN)
        driver.find_element(By.LINK_TEXT,"Python (programming language)").click()
        driver.find_element(By.XPATH, "//h1[text()='Python (programming language)']").click()