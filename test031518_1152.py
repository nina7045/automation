import os
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
#from Funk_Lib import RS
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import datetime
#import org.openqa.selenium.WebDriver;
#import org.openqa.selenium.chrome.ChromeDriver;
#import sys
from selenium.webdriver.common.action_chains import ActionChains



class CreatingEditingDeletingVault(unittest.TestCase):
    def setUp(self):

        #System.setProperty("webdriver.chrome.driver", "C:/chromedriver.exe")
        #self.driver = webdriver.ChromeDriver()
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.binary_location = '/usr/bin/chromium-browser'
        # options.add_argument("--no-sandbox")
        # options.add_argument("--no-default-browser-check")
        # options.add_argument("--no-first-run")
        # options.add_argument("--disable-default-apps")
        # chrome = webdriver.Chrome()
        # #self.driver = webdriver.Firefox()
        #chromedriver="C://chromedriver.exe"
        # os.environ["webdriver.chrome.driver"] = chromedriver
        # self.driver = webdriver.Chrome(chromedriver)
        #self.driver = webdriver.Chrome(executable_path=r'C:/Windows/chromedriver.exe')
        #self.driver = webdriver.Chrome(executable_path="C:/Users/nbezroukova/AppData/Local/Programs/Python/Python36-32/chromedriver.exe")
        #self.driver = webdriver.Chrome(chromedriver)
        self.driver = webdriver.Chrome('C:/Python27/chromedriver.exe')
        self.base_url = "https://qa.agendaonline.com"
        self.verificationErrors = []
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def test_creating_editing_deleting_vault(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("Username").click()
        driver.find_element_by_id("Username").clear()
        driver.find_element_by_id("Username").send_keys("nbezroukova@csba.org")
        driver.find_element_by_name("Password").click()
        driver.find_element_by_name("Password").clear()
        driver.find_element_by_name("Password").send_keys("testing1")
        driver.find_element_by_id("submit_button").click()
        #self.driver.implicitly_wait(50)
        time.sleep(9)
        driver.find_element_by_xpath("//span[contains(text(), 'testPremium')]").click()
        time.sleep(4)
        #WebDriverWait(driver, 10).until(EC.presence_of_element_located(find_element_by_xpath("//div[contains(text(), 'Start New')]")))
        if driver.find_element_by_xpath("//div[contains(text(), 'Start New')]"):
            driver.find_element_by_xpath("//div[contains(text(), 'Start New')]").click()

        time.sleep(2)
        driver.find_element_by_xpath("//div[contains(text(), 'Meeting')]").click()
        time.sleep(10)
        driver.implicitly_wait(10)
        driver.find_element_by_id("confirmServiceRequestConfirmBtn").click()
        #driver.find_element_by_xpath("//paper-button[contains(text(), 'Next')]").click()
        time.sleep(7)
        now = datetime.datetime.now()
        meetingTitle = "m_"+now.strftime("%Y-%m-%d %H:%M")
        driver.find_elements_by_xpath("//input[@id='input']")[4].send_keys(meetingTitle)
        time.sleep(1)
        driver.find_elements_by_xpath("//input[@id='input']")[5].send_keys("Mar 30 2018")
        time.sleep(1)
        driver.find_elements_by_xpath("//input[@id='input']")[6].send_keys("1:21 PM")
        time.sleep(1)
        driver.find_elements_by_xpath("//input[@id='input']")[8].send_keys("location mar15 121pm")
        time.sleep(2)
        driver.find_elements_by_xpath("//div[@id='toggleIcon']/iron-icon")[2].click()
        time.sleep(1)
        if driver.find_element_by_xpath("//awi-combobox-item[contains(text(), 'No Approval Required')]"):
            driver.find_element_by_xpath("//awi-combobox-item[contains(text(), 'No Approval Required')]").click()
        else:
            driver.find_element_by_xpath("//div[contains(text(), 'Start New')]").click()
        time.sleep(2)
        driver.find_elements_by_xpath("//div[@id='toggleIcon']/iron-icon")[3].click()
        driver.find_element_by_xpath("//awi-combobox-item[contains(text(), 'att_group_march8_839')]").click()
        time.sleep(2)
        iFrame1 = driver.find_element_by_xpath("//div[@id='cke_1_contents']/iframe")
        driver.switch_to.frame(iFrame1)
        driver.find_element_by_tag_name("body").clear()
        driver.find_element_by_tag_name("body").send_keys("this is a preliminary section")
        time.sleep(1)
        driver.switch_to.default_content()
        time.sleep(2)
        iFrame2 = driver.find_element_by_xpath("//div[@id='cke_2_contents']/iframe")
        driver.switch_to.frame(iFrame2)
        driver.find_element_by_tag_name("body").clear()
        driver.find_element_by_tag_name("body").send_keys("this is a closing section")
        time.sleep(1)
        driver.switch_to.default_content()
        #driver.find_element_by_id("cke_1_contents").send_keys("this is a preliminary section")
        #driver.implicitly_wait(10)
        #driver.find_element_by_id("cke_2_contents").send_keys("this is a closing section")
        driver.implicitly_wait(5)
        driver.find_element_by_id("saveActionButton").click()
        time.sleep(2)
        driver.find_element_by_id("actionButton1").click()
        driver.implicitly_wait(10)
        #driver.find_element_by_id("dialog").click()
        #driver.find_element_by_id("actionButton1").send_keys("Mar 15 2018  text area")
        #webdriver.DesiredCapabilities.FIREFOX["unexpectedAlertBehaviour"] = "accept"
        #driver.switch_to_alert()
        #driver.find_element_by_xpath("//div[@id='main']/div/submit-action/").click(27, 21)
        #driver.find_elements_by_xpath("//textarea[@id='textarea']")[4].send_keys("typing text mar15 458pm")
        #driver.find_elements_by_xpath("//paper-dialog[@id='dialog']/div[2]/div/paper-button[2]")[2].click()
        driver.find_element_by_xpath("//paper-dialog[@id='dialog']/div[2]/div/paper-button[contains(text(), 'Ok')]").click()
        # try:
        #     alert = driver.switch_to.alert()
        #     #driver.find_element_by_xpath("//div/paper-button[contains(text(), 'Ok')]").click()
        #     alert.accept()
        #     #driver.find_elements_by_xpath("//paper-dialog[@id='dialog']/div[2]/div/paper-button[2]")[2].click()
        #     print ("alert accepted")
        # except:
        #     print ("no alert")

        time.sleep(5)

        #AGENDA ITEM
        now = datetime.datetime.now()
        aiTitle = "ai_"+ now.strftime("%y-%m-%d %H:%M")
        driver.find_element_by_xpath("//div[contains(text(), 'Agenda Item')]").click()
        time.sleep(7)
        driver.implicitly_wait(10)
        driver.find_element_by_id("confirmServiceRequestConfirmBtn").click()
        time.sleep(5)
        #driver.find_element_by_xpath("//div[@id='content']/div/ul/li[2]").click()
        driver.implicitly_wait(10)
        #time.sleep(7)

        #driver.find_elements_by_xpath("//section[@id='Item%20Settings']/h1").click()

        driver.find_elements_by_xpath("//paper-menu[@id='menu']/div/paper-item[5]/span").click()
        time.sleep(3)
        driver.find_elements_by_xpath("//paper-menu[@id='menu']/div/paper-item[2]/span").click()
        time.sleep(2)
        driver.find_elements_by_xpath("//input[@id='input']")[6].send_keys(aiTitle)

        #driver.find_elements_by_xpath("//input[@id='input']")[6].send_keys('%s')%aiTitle
        driver.find_elements_by_xpath("//div[@id='toggleIcon']/iron-icon")[3].click()
        #"03/30/2018 - " + meetingTitle
        driver.find_element_by_xpath("//awi-combobox-item[contains(text(), '03/30/2018 - ' + '%s')]"%meetingTitle).click()
        time.sleep(2)
        driver.find_elements_by_xpath("//div[@id='toggleIcon']/iron-icon")[5].click()
        driver.find_element_by_xpath("//awi-combobox-item[contains(text(), 'No Approval Required')]").click()
        time.sleep(2)
        driver.find_elements_by_xpath("//div[@id='checkboxContainer']")[4].click()
        time.sleep(1)
        Summary = driver.find_element_by_xpath("//div[@id='cke_2023_contents']/iframe")
        driver.switch_to.frame(Summary)
        driver.find_element_by_tag_name("body").clear()
        driver.find_element_by_tag_name("body").send_keys("this is a Summary section")
        time.sleep(1)
        driver.switch_to.default_content()
        time.sleep(2)
        Description = driver.find_element_by_xpath("//div[@id='cke_2024_contents']/iframe")
        driver.switch_to.frame(Description)
        driver.find_element_by_tag_name("body").clear()
        driver.find_element_by_tag_name("body").send_keys("this is a Description section")
        time.sleep(1)
        driver.switch_to.default_content()
        time.sleep(2)
        Motion = driver.find_element_by_xpath("//div[@id='cke_2025_contents']/iframe")
        driver.switch_to.frame(Motion)
        driver.find_element_by_tag_name("body").clear()
        driver.find_element_by_tag_name("body").send_keys("this is a Motion section")
        time.sleep(1)
        driver.switch_to.default_content()
        time.sleep(2)
        driver.find_element_by_id("addButton").click()
        driver.implicitly_wait(5)
        driver.find_elements_by_xpath("//iron-icon[@id='upload-document']")[3].click()

        #driver.find_element_by_xpath("//span[contains(@class, 'organization-name flex style-scope select-organization')]").[0]
        #driver.find_element_by_class_name("organization-name flex style-scope select-organization").click()

        #System.out.println(driver.find_element_by_css_selector("span.organization-name flex style-scope select-organization").get_text())
        #print(WebDriverWait(driver, 10).until(EC.presence_of_element_located))
        # driver.get(self.base_url + "/Content/Vaults/")
        # driver.find_element_by_link_text("Content").click()
        # driver.find_element_by_link_text("Vaults").click()
        # driver.find_element_by_css_selector("button.btn.dropdown-toggle").click()
        # driver.find_element_by_link_text("New vault").click()
        # driver.find_element_by_name("Name").clear()
        # driver.find_element_by_name("Name").send_keys("Test Vault")
        # driver.find_element_by_xpath("//button[@onclick=\"vault_action('createvault', null, $('#CreateVault [name=\\'Name\\']').val())\"]").click()
        # driver.find_element_by_css_selector("button.btn.dropdown-toggle").click()
        # driver.find_element_by_link_text("Rename vault").click()
        # driver.find_element_by_name("Id").click()
        # Select(driver.find_element_by_name("Id")).select_by_visible_text("Test Vault")
        # driver.find_element_by_css_selector("option[value=\"2\"]").click()
        # driver.find_element_by_name("Name").clear()
        # driver.find_element_by_name("Name").send_keys("Test Change")
        # driver.find_element_by_xpath("//button[@onclick=\"vault_action('renamevault', $('#RenameVault [name=\\'Id\\']').val(), $('#RenameVault [name=\\'Name\\']').val())\"]").click()
        # driver.find_element_by_css_selector("button.btn.dropdown-toggle").click()
        # driver.find_element_by_link_text("Delete vault").click()
        # driver.find_element_by_name("Id").click()
        # Select(driver.find_element_by_name("Id")).select_by_visible_text("Test Change")
        # driver.find_element_by_css_selector("option[value=\"2\"]").click()
        # driver.find_element_by_xpath("//button[@onclick=\"vault_action('deletevault', $('#DeleteVault [name=\\'Id\\']').val(), '')\"]").click()

    # def is_element_present(self, how, what):
    #     try: self.driver.find_element(by=how, value=what)
    #     except NoSuchElementException, e: return False
    #     return True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
