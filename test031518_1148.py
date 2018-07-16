import unittest
from selenium import webdriver

class AweberTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()

    def test_title(self):
        self.driver.get('https://qa.agendaonline.com')
        self.assertEqual(
            self.driver.title,
            'CSBA Single Sign-On')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
