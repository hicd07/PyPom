__author__ = "Hipolito Concepcion"
from selenium.webdriver.common.by import By
from src.common.WaitAction import WaitAction


class WikiArticlePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.lblArticleTitle_TEXT = "Python (programming language)"

    def getlblarticletitle(self):
        WaitAction().waitforelementbytext(self.driver, self.lblArticleTitle_TEXT, 3)
        return self.driver.find_element(By.LINK_TEXT, self.lblArticleTitle_TEXT)
