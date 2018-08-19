__author__ = "Hipolito Concepcion"
from selenium.webdriver.common.by import By
from src.common.WaitAction import WaitAction


class WikiMainPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.inputSearch_ID = "searchInput"
        self.linkPyArticles_TEXT = "Python (programming language)"

    def getinputsearch(self):
        return self.driver.find_element(By.ID, self.inputSearch_ID)

    def getdlinkpyarticle(self):
        WaitAction().waitforelementbytext(self.driver, self.linkPyArticles_TEXT, 3)
        return self.driver.find_element(By.LINK_TEXT, self.linkPyArticles_TEXT)
