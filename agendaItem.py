#import com.easy.upload
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import datetime
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import random
#from Selenium2Library import Selenium2Library
import Tkinter as tk
import subprocess
import pywinauto
from pywinauto import Desktop, Application
#import win32com.client
#import tkinter as tk   #for python3
#import java.awt.Robot
import utils




class CreatingAgendaItem(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('C:/Python27/chromedriver.exe')
        #self.base_url = "https://qa.agendaonline.com"
        self.base_url = "https://app.agendaonline.com"
        self.verificationErrors = []
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)


    def test_creating_agenda_item(self):
        ais = 21
        # 1
        # userName = "nbezroukova@csba.org"
        # passw = "testing2"
        # subscr = "Banning Test 060118"
        # meetingName = "jun4_1012"
        # 2
        # userName = "nina7045_mm@yahoo.com"
        # passw = "testing1"
        # subscr = "may22_927"
        # meetingName = "m_2018-06-18 09:07"
        # ais = 21
        # 3
        # userName = "nina7045@yahoo.com"
        # passw = "testing1"
        # subscr = "may25_Prem"
        # meetingName = "m_2018-06-14 15:25"
        # 4
        # userName = "ao2meetingmanager@gmail.com"
        # passw = "testing1"
        # subscr = "may22_927"
        # meetingName = "m_2018-06-20 09:22"
        #5
        userName = "nbezroukova@csba.org"
        passw = "testing1"
        subscr = "Demo USD"
        meetingName = "m_2018-06-20 13:25"

        driver = self.driver
        driver.get(self.base_url)
        try:
            element = WebDriverWait(driver, 20).until( EC.presence_of_element_located((By.ID, "Username")))
        finally:
            driver.find_element_by_id("Username").click()
        #driver.find_element_by_id("Username").click()
        driver.find_element_by_id("Username").clear()
        #driver.find_element_by_id("Username").send_keys("nbezroukova@csba.org")
        #driver.find_element_by_id("Username").send_keys("staff1@csba.org")
        #driver.find_element_by_id("Username").send_keys("nina7045@yahoo.com")
        #driver.find_element_by_id("Username").send_keys("mm1meetingmanager@gmail.com")
        #driver.find_element_by_id("Username").send_keys("nina7045_mm@yahoo.com")
        driver.find_element_by_id("Username").send_keys(userName)
        driver.find_element_by_name("Password").click()
        driver.find_element_by_name("Password").clear()
        #driver.find_element_by_name("Password").send_keys("testing2")
        #driver.find_element_by_name("Password").send_keys("ao2user")
        #driver.find_element_by_name("Password").send_keys("testing1")
        driver.find_element_by_name("Password").send_keys(passw)
        driver.find_element_by_id("submit_button").click()
        #self.driver.implicitly_wait(50)
        time.sleep(3)

        # verify Select Organization, if any and select one
        try:
            element = WebDriverWait(driver, 20).until( EC.presence_of_element_located((By.XPATH, "//paper-dialog[@id='select-organization']")))
        finally:
            selectOrganization = driver.find_element_by_xpath("//paper-dialog[@id='select-organization']")
        if selectOrganization.is_displayed():
            try:
                #element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'testPremium')]")))
                #element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Beta Testing District')]")))
                #element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'may25_Prem')]")))
                #element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'may23_prem')]")))
                #element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'may22_927')]")))
                element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//span[contains(text(), '%s')]"%subscr)))
            finally:
                #driver.find_element_by_xpath("//span[contains(text(), 'may25_Prem')]").click()
                #driver.find_element_by_xpath("//span[contains(text(), 'Beta Testing District')]").click()
                #driver.find_element_by_xpath("//span[contains(text(), 'may23_prem')]").click()
                driver.find_element_by_xpath("//span[contains(text(), '%s')]"%subscr).click()
                #driver.quit()


        time.sleep(3)

        #delete blank Items
        #utils.MyItems_blanksDelete(driver)

        try:
            element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//a/div[contains(text(), 'Start New')]")))
        finally:
            driver.find_element_by_xpath("//div[contains(text(), 'Start New')]").click()

            #driver.quit()
        #time.sleep(2)
        #driver.find_element_by_xpath("//div[contains(text(), 'Start New')]").click()
        #time.sleep(2)

        for i in range(1, ais):
            #AGENDA ITEM
            time.sleep(2)
            now = datetime.datetime.now()
            aiTitle = "ai_"+ now.strftime("%y-%m-%d %H:%M")
            try:
                element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Agenda Item')]")))
            finally:
                driver.find_element_by_xpath("//div[contains(text(), 'Agenda Item')]").click()
            time.sleep(5)

            # # SELECT GOVERNING BODY:
            # try:
            #     element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@id='toggleIcon']/iron-icon")))
            # finally:
            #     driver.find_element_by_xpath("//div[@id='toggleIcon']/iron-icon").click()
            # time.sleep(1)
            # #driver.find_element_by_xpath("//awi-combobox-item[contains(text(), 'Beta Testing GB')]").click()
            # #driver.find_element_by_xpath("//awi-combobox-item[contains(text(), 'GB_format1_(1.1.1)')]").click()
            # #driver.find_element_by_xpath("//awi-combobox-item[contains(text(), 'GB_format2_(1.a.1)')]").click()
            # #driver.find_element_by_xpath("//awi-combobox-item[contains(text(), 'GB_format4_(A.1.a)')]").click()
            # driver.find_element_by_xpath("//awi-combobox-item[contains(text(), 'GB_format5_(A.a.1)')]").click()
            # time.sleep(2)

            #  SELECT TEMPLATE

            # try:
            #     element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//awi-combobox[@id='_selectTemplate']/div[2]/paper-input-container[@id='inputContainer']/div[2]/div[3]")))
            # finally:
            #     driver.find_element_by_xpath("//awi-combobox[@id='_selectTemplate']/div[2]/paper-input-container[@id='inputContainer']/div[2]/div[@id='toggleIcon']/iron-icon").click()
            # #driver.find_elements_by_xpath("//div[@id='toggleIcon']/iron-icon")[5].click()
            # try:
            #     element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//awi-combobox-overlay[@id='overlay']/div[@id='scroller']/iron-list[@id='selector']/div[@id='items']/awi-combobox-item[contains(text(), 'aiT_tables')]")))
            # finally:
            #     driver.find_element_by_xpath("//awi-combobox-item[contains(text(), 'aiT_tables')]").click()
            # time.sleep(4)

            # #click Next
            try:
                element = WebDriverWait(driver, 20).until( EC.presence_of_element_located((By.ID, "confirmServiceRequestConfirmBtn")))
            finally:
                #driver.find_element_by_id("confirmServiceRequestConfirmBtn").click()
                driver.find_element_by_id("confirmServiceRequestConfirmBtn").send_keys('\n')
            time.sleep(7)

            #check for a spinner here , if spinner is on, wait
            try:
                element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//paper-spinner[@id='spinner']")))
            finally:
                sp = driver.find_element_by_xpath("//paper-spinner[@id='spinner']")
            if sp.is_displayed():
                while sp.value_of_css_property("display") == "block":
                    print "spinning..."
                    time.sleep(1)

            #---------------------------------------------------
            #  title
            try:
                element = WebDriverWait(driver, 30).until( EC.presence_of_element_located((By.XPATH, "//paper-menu[@id='menu']/div/paper-item[2]/span")))
            finally:
                #driver.find_element_by_xpath("//paper-menu[@id='menu']/div/paper-item[2]/span").click()
                driver.find_element_by_xpath("//paper-menu[@id='menu']/div/paper-item[2]").click()
            time.sleep(1)

            #Agenda%20Information
            #driver.find_element_by_xpath("//section[@id='Agenda%20Information']/awi-textbox/div/paper-input-container/div/div").click()
            #time.sleep(1)
            #driver.find_element_by_xpath("//section[@id='Item%20Settings']/awi-textbox/div/paper-input-container/div/div").click()
            driver.find_element_by_xpath("//section[@id='Agenda%20Information']/awi-textbox/div/paper-input-container/div/div").click()
            #driver.find_element_by_xpath("//section[@id='Item%20Settings']/awi-textbox/div/paper-input-container/div/div/input").send_keys(aiTitle)
            driver.find_element_by_xpath("//section[@id='Agenda%20Information']/awi-textbox/div/paper-input-container/div/div/input").send_keys(aiTitle)
            time.sleep(1)

            #select meeting
            #driver.find_element_by_xpath("//section[@id='Item%20Settings']/awi-meeting-select/awi-combobox/div/paper-input-container/div/div[3]").click()
            driver.find_element_by_xpath("//section[@id='Agenda%20Information']/awi-meeting-select/awi-combobox/div/paper-input-container/div/div[3]").click()
            time.sleep(2)
            #driver.find_elements_by_xpath("//awi-combobox-overlay/div/iron-list/div/awi-combobox-item[@id='it']")[7].click() #works
            #driver.find_element_by_xpath("//awi-combobox-overlay/div/iron-list/div/awi-combobox-item[contains(text(), 'm_2018-03-16 11:23')]").click()   #works
            #driver.find_element_by_xpath("//awi-combobox-overlay/div/iron-list/div/awi-combobox-item[contains(text(), 'm_mar23_1131')]").click()  #works
            #time.sleep(1)
            #driver.implicitly_wait(10)
            # meetings = driver.find_elements_by_xpath("//awi-combobox-overlay/div/iron-list/div/awi-combobox-item")
            # for m in meetings:
            #     print m.text
            # print '**************************'
            # for x in range(0, 30):
            #     tempM = driver.find_elements_by_xpath("//awi-combobox-overlay/div/iron-list/div/awi-combobox-item[@id='it']")[x].text
            #     print 'found ' + x
            #     if tempM.find(meetingName)>1:
            #         tempM.click()
            #         print tempM
            #         break
            # print driver.find_elements_by_xpath("//awi-combobox-overlay/div/iron-list/div/awi-combobox-item[@id='it']")[10].text
            # driver.find_elements_by_xpath("//awi-combobox-overlay/div/iron-list/div/awi-combobox-item[@id='it']")[10].click()
            #driver.find_element_by_xpath("//awi-combobox-overlay/div/iron-list/div/awi-combobox-item[contains(text(), 'm_mar23_1131')]").click()

            #type in Select Meetign input field:
            driver.find_element_by_xpath("//awi-combobox[@id='meetingsCombobox']/div[2]/paper-input-container[@id='inputContainer']/div/div[@id='labelAndInputContainer']/iron-input/input[@id='input']").send_keys(meetingName)
            #select meetign from drop-down list
            try:
                element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//awi-combobox-overlay/div/iron-list/div/awi-combobox-item[@id='it' and contains(text(), '%s')]"%meetingName)))
            finally:
                driver.find_element_by_xpath("//awi-combobox-overlay/div/iron-list/div/awi-combobox-item[@id='it' and contains(text(), '%s')]"%meetingName).click()
            #driver.find_element_by_xpath("//awi-combobox-overlay/div/iron-list/div/awi-combobox-item[text()='03/31/2018 - m_mar23_1131' and count(awi-combobox-item)>5]").click()  #does NOT work
            #driver.find_element_by_xpath("//section[@id='Agenda%20Information']/awi-meeting-select/awi-combobox/awi-combobox-overlay/div/iron-list/div/awi-combobox-item[contains(text(), '%s')]"%meetingName).click()  #does NOT work
            #driver.find_element_by_xpath("//awi-combobox-item[@id='it' and contains(text(), '%s')]"%meetingName).click()
            time.sleep(2)
            #select workflow route
            #driver.find_element_by_xpath("//section[@id='Item%20Settings']/awi-user-route-select/awi-combobox/div[2]/paper-input-container/div/div[3]").click()
            try:
                element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//section[@id='Agenda%20Information']/awi-user-route-select/awi-combobox/div[2]/paper-input-container/div/div[3]")))
            finally:
                driver.find_element_by_xpath("//section[@id='Agenda%20Information']/awi-user-route-select/awi-combobox/div[2]/paper-input-container/div/div[3]").click()
            #driver.find_elements_by_xpath("//div[@id='toggleIcon']/iron-icon")[5].click()
            try:
                element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//awi-combobox-item[contains(text(), 'No Approval Required')]")))
            finally:
                driver.find_element_by_xpath("//awi-combobox-item[contains(text(), 'No Approval Required')]").click()
            time.sleep(2)

            #select type
            #driver.find_elements_by_xpath("//div[@id='checkboxContainer']")[random.sample(range(4,5),1)].click() #does NOT work
            for b in range(500):
                typeNum = random.randint(0,5)
                if typeNum !=2:
                    break
            #driver.find_elements_by_xpath("//div[@id='checkboxContainer']")[random.randint(3,5)].click()
            driver.find_elements_by_xpath("//div[@id='checkboxContainer']")[typeNum].click()
            time.sleep(1)

            #Summary section
            Summary = driver.find_element_by_xpath("//section[@id='Quick%20Summary/Abstract']/awi-editor/div/div/div/iframe")
            driver.switch_to.frame(Summary)
            driver.find_element_by_tag_name("body").clear()
            driver.find_element_by_tag_name("body").send_keys("%d. -------------start of Quick Summary/Abstract section for the agenda item .....%s.....and meeting %s --------------end of Quick Summary/Abstract section for the agenda item  "%(i,aiTitle,meetingName))
            time.sleep(1)
            driver.switch_to.default_content()
            time.sleep(1)

            #Description section
            Description = driver.find_element_by_xpath("//section[@id='Description']/awi-editor/div/div/div/iframe")
            driver.switch_to.frame(Description)
            driver.find_element_by_tag_name("body").clear()
            driver.find_element_by_tag_name("body").send_keys("%d. -------------start of Description section for the agenda item ... %s.... adn meeting %s -------------end of Description section for the agenda item"%(i,aiTitle,meetingName))
            time.sleep(1)
            driver.switch_to.default_content()
            time.sleep(1)

            #Motion section
            Motion = driver.find_element_by_xpath("//section[@id='Recommended%20Motion']/awi-editor/div/div/div/iframe")
            driver.switch_to.frame(Motion)
            driver.find_element_by_tag_name("body").clear()
            driver.find_element_by_tag_name("body").send_keys("%d. -------------start of Recommended Motion section for the agenda item  ......%s....and the meeting %s-------------END of Recommended Motion section for the agenda item    "%(i, aiTitle, meetingName))
            time.sleep(1)
            driver.switch_to.default_content()
            time.sleep(2)

            # add an attachment
            #  this sections works >>>>>>>>>>>>>>>
            # try:
            #     element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//paper-button[@id='addButton']")))
            # finally:
            #     driver.find_element_by_xpath("//paper-button[@id='addButton']").click()
            # time.sleep(3)
            # try:
            #     element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//paper-dialog[@id='dialog']")))
            # finally:
            #     Attachment = driver.find_element_by_xpath("//paper-dialog[@id='dialog']")
            #     #driver.switch_to.frame(Attachment)
            #     #driver.find_element_by_xpath("//iron-icon[@id='upload-document']").click()
            # try:
            #     element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//awi-form/form/awi-document/div/div[3]/iron-icon[@id='upload-document']")))
            # finally:
            #     driver.find_element_by_xpath("//awi-form/form/awi-document/div/div[3]/iron-icon[@id='upload-document']").click()
            #     #driver.find_element_by_xpath("//iron-icon[2]").click()
            # time.sleep(3)

            # end of section that works >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.

            #subprocess.Popen('explorer "C:\_attachments\chicken.pdf"')

            #-----------------------------------------------------
            # shell = win32com.client.Dispatch("WScript.Shell")
            # shell.send_keys("C:\_attachments\chicken.pdf")
            # shell.send_keys("~")
            #------------------------------------------------------

            #************************ switch to the new open window
            # driver.switch_to.window(driver.windowHandles.last())
            #driver.find_element_by_id("Open").send_keys("C:\_attachments\chicken.pdf")

            #Runtime.getRuntime().exec("cmd C:\\automation\\selectAttachment.exe")

            # Robot rb1 = new Robot()
            # rb1.delay(3000)
            # rb1.keyPress(KeyEvent.VK_CONTROL)
            # rb1.keyPress(KeyEvent.VK_V)

            # app=Application(backend="uia").connect(path="explorer.exe", title="Open")
            #
            # driver.find_element_by_xpath("//input[@id='fileinput']").send_keys("C:\_attachments\chicken.pdf")
            # driver.find_element_by_xpath("//input[@id='input']").send_keys("some_attachment")
            # driver.find_element_by_xpath("//paper-dialog[@id='dialog']/div/paper-button[contains(text(), 'Save')]")
            # driver.find_element_by_xpath("//paper-dialog[@id='dialog']/div/paper-button[2]").click()

            #   end add attachment section ****************************************



            #saveActionButton
            try:
                element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.ID, "saveActionButton")))
            finally:
                driver.find_element_by_id("saveActionButton").click()
            time.sleep(8)
            #driver.implicitly_wait(5)

            #Add to Agenda
            try:
                element = WebDriverWait(driver, 20).until( EC.presence_of_element_located((By.ID, "actionButton1")))
            finally:
                driver.find_element_by_id("actionButton1").click() # does NOT work
            #driver.find_element_by_xpath("//paper-toolbar/div/paper-button/span[contains(text(), 'Add to Agenda')]").click()  #does NOT work
            #driver.find_element_by_xpath("//div[@id='topBar']/div/paper-button").click()  # does NOT work
            #driver.find_element_by_xpath("//div[@id='topBar']/div/paper-button/span").click() #does NOT work
            time.sleep(2)
            #driver.implicitly_wait(5)

            #Confirm Action
            #driver.find_element_by_xpath("//paper-dialog[@id='dialog']/div[2]/div/paper-button[2]").click() #does NOT work
            try:
                element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//submit-action[@id='submit']/paper-dialog/div[2]/div/paper-button[2]")))
            finally:
                driver.find_element_by_xpath("//submit-action[@id='submit']/paper-dialog/div[2]/div/paper-button[2]").click()
            time.sleep(7)

    # def is_element_present(self, how, what):
    #     try: self.driver.find_element(by=how, value=what)
    #     except NoSuchElementException, e: return False
    #     return True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
