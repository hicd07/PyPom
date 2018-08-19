__author__ = "Hipolito Concepcion"
import unittest
from selenium import webdriver
from src.pages.PortalHomePage import PortalHomePage
from src.pages.WikiMainPage import WikiMainPage
from src.pages.WikiArticlePage import WikiArticlePage
from src.common.UserAction import UserAction


class TestCase(unittest.TestCase):

    def test_testcase1(self):

        # Initializing objects
        useraction = UserAction()
        driver = webdriver.Chrome()
        portalhome = PortalHomePage(driver)
        wikimain = WikiMainPage(driver)
        wikiarticle = WikiArticlePage(driver)

        # Performing user actions
        url = portalhome.geturl()
        driver.get(url)
        useraction.doclick(portalhome.getlinkenglang())
        useraction.doclick(wikimain.getinputsearch())
        useraction.dotypeintext(wikimain.getinputsearch(), "Python")
        useraction.doclick(wikimain.getdlinkpyarticle())
        useraction.doclick(wikiarticle.getlblarticletitle())
