#from selenium import selenium

from selenium import webdriver
import unittest, time, re
from selenium.webdriver.common.keys import Keys
import time


class NewTest(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []

        self.selenium = selenium("localhost", 4444, "*chrome", 'https://qa.agendaonline.com')
        self.selenium.start()

    def test_new(self):
        sel = self.selenium
# class NewTest(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.driver=webdriver.Firefox()
#         time.sleep(100)
#
#     def test_title(self):
#         self.driver.get("https://qa.agendaonline.com")
#         self.assertEqual(self.driver.title, 'CSBA Single Sign-On')
#
#
#     @classmethod
#     def tearDownClass(cls):
#         cls.driver.quit()

    # time.sleep(100)
    # inputLogin = driver.find_element_by_id("Username")
    # inputPass = driver.find_element_by_id("Password")
    # inputLogin.send_keys('nbezroukova@csba.org')
    # inputPass.send_keys('testing1')
    # inputLogin.send_keys(Keys.ENTER)

    #import webbrowser
    #new = 4

    #url = "https://qa.agendaonline.com"
    #chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'

    #webbrowser.get(using='google-chrome').open(url, new=new)
