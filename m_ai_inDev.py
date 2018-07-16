import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re, random
from random import randint
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import TimeoutException
import datetime, ast
import sys
import os
from selenium.webdriver.common.action_chains import ActionChains
import utils, xlwt
from xlutils.copy import copy
import xlrd
import xlwt
import xlsxwriter


class MeetingInDev(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('C:/Python27/chromedriver.exe')
        self.base_url = "https://qa.agendaonline.com"
        self.verificationErrors = []
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get(self.base_url)


    def test_meeting_InDev(self):

        driver = self.driver
        n = datetime.datetime.now()
        fileName ="testResults_" + n.strftime("%m%d_%H%M")
        #wfPlan = ''
        meetingsList = []

        # login
        #utils.login(driver, wb, sheet, fileName)
        driver.get(self.base_url)
        driver.find_element_by_id("Username").click()
        driver.find_element_by_id("Username").clear()
        #driver.find_element_by_id("Username").send_keys("nbezroukova@csba.org")
        #driver.find_element_by_id("Username").send_keys("staff1@csba.org")
        driver.find_element_by_id("Username").send_keys("nina7045_mm@yahoo.com")
        driver.find_element_by_name("Password").click()
        driver.find_element_by_name("Password").clear()
        #driver.find_element_by_name("Password").send_keys("testing2")
        #driver.find_element_by_name("Password").send_keys("ao2user")
        driver.find_element_by_name("Password").send_keys("testing1")
        driver.find_element_by_id("submit_button").click()
        #self.driver.implicitly_wait(50)

        try:
            #element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'testPremium')]")))
            element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'may22_927')]")))
        finally:
            #driver.find_element_by_xpath("//span[contains(text(), 'testPremium')]").click()
            driver.find_element_by_xpath("//span[contains(text(), 'may22_927')]").click()

        time.sleep(2)

        utils.MyMeetings_click(driver)

        #select a meeting IN Dev status:
        for i in range (len(driver.find_elements_by_xpath("//div[@id='items']/awi-grid-row"))):
            if (i != 0):
                status = driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell[6]/div/span"%str(i)).text
                if status == "In Development":
                    meetingName = driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell/div/span"%str(i)).text
                    break


        #add an agend aitem to the meetign IN Dev:
        try:
            element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//a/div[contains(text(), 'Start New')]")))
        finally:
            driver.find_element_by_xpath("//div[contains(text(), 'Start New')]").click()


        #  new AGENDA ITEM
        time.sleep(2)
        now = datetime.datetime.now()
        aiTitle = "ai_"+ now.strftime("%y-%m-%d %H:%M")
        try:
            element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Agenda Item')]")))
        finally:
            driver.find_element_by_xpath("//div[contains(text(), 'Agenda Item')]").click()
        time.sleep(5)

        try:
            element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.ID, "confirmServiceRequestConfirmBtn")))
        finally:
            driver.find_element_by_id("confirmServiceRequestConfirmBtn").send_keys('\n')
        time.sleep(15)

        #  title
        try:
            element = WebDriverWait(driver, 30).until( EC.presence_of_element_located((By.XPATH, "//paper-menu[@id='menu']/div/paper-item[2]/span")))
        finally:
            driver.find_element_by_xpath("//paper-menu[@id='menu']/div/paper-item[2]/span").click()
        time.sleep(1)


        driver.find_element_by_xpath("//section[@id='Agenda%20Information']/awi-textbox/div/paper-input-container/div/div").click()

        driver.find_element_by_xpath("//section[@id='Agenda%20Information']/awi-textbox/div/paper-input-container/div/div/input").send_keys(aiTitle)
        time.sleep(1)

        #select meeting
        driver.find_element_by_xpath("//section[@id='Agenda%20Information']/awi-meeting-select/awi-combobox/div/paper-input-container/div/div[3]").click()
        time.sleep(2)


        #type in Select Meetign input field:
        driver.find_element_by_xpath("//awi-combobox[@id='meetingsCombobox']/div[2]/paper-input-container[@id='inputContainer']/div/div[@id='labelAndInputContainer']/iron-input/input[@id='input']").send_keys(meetingName)

        try:
            element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//awi-combobox-overlay/div/iron-list/div/awi-combobox-item[@id='it' and contains(text(), '%s')]"%meetingName)))
        finally:
            driver.find_element_by_xpath("//awi-combobox-overlay/div/iron-list/div/awi-combobox-item[@id='it' and contains(text(), '%s')]"%meetingName).click()

        time.sleep(2)
        #select workflow route

        try:
            element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//section[@id='Agenda%20Information']/awi-user-route-select/awi-combobox/div[2]/paper-input-container/div/div[3]")))
        finally:
            driver.find_element_by_xpath("//section[@id='Agenda%20Information']/awi-user-route-select/awi-combobox/div[2]/paper-input-container/div/div[3]").click()
        try:
            element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//awi-combobox-item[contains(text(), 'No Approval Required')]")))
        finally:
            driver.find_element_by_xpath("//awi-combobox-item[contains(text(), 'No Approval Required')]").click()
        time.sleep(2)

        #select type
        for b in range(500):
            typeNum = random.randint(0,5)
            if typeNum !=2:
                break
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

        #saveActionButton
        try:
            element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.ID, "saveActionButton")))
        finally:
            driver.find_element_by_id("saveActionButton").click()
        time.sleep(7)

        # trying to get back to left navigation bar
        driver.find_element_by_xpath("//div[@id='task-main-section']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='mainContainer']/div/paper-toolbar[2]").click()
        driver.find_element_by_xpath("//div[@id='mainPanel']/div[@id='mainContainer']/div/paper-toolbar[2]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//paper-header-panel[@id='panel']/div[@id='mainPanel']/div[@id='mainContainer']/div/paper-toolbar[2]").click()
        time.sleep(1)

        # My Meetings click
        driver.find_element_by_xpath("//avocado-frame/awi-app/main-container[@id='mainContainer']/app-router[@id='router']/app-route[15]/confirm-service-request-selection/dynamic-task-view/paper-drawer-panel/iron-selector/div[@id='drawer']/paper-header-panel/div[@id='mainPanel']/div[@id='mainContainer']/sidebar-navigation/div/div/paper-menu[@id='sidebarNavigation']/div/sidebar-menu-item[5]/paper-item/pushstate-anchor/a/div").click()
        time.sleep(3)

        #driver.find_element_by_xpath("//paper-drawer-panel/iron-selector/div[@id='drawer']/paper-header-panel/div[@id='mainPanel']/div[@id='mainContainer']/sidebar-navigation/div/div/paper-menu[@id='sidebarNavigation']/div/sidebar-menu-item[5]/paper-item/pushstate-anchor/a/div[contains(text(), 'My Meetings')]").click()
        #time.sleep(1)

        #   DRAFT AGENDA ITEM VERIFICATION

        # verify draft agend aitem in meeting:
        #----------------------------------------------------------__
        #click the meeting and verify the agenda item is in there
        time.sleep(5)
        utils.MyMeetings_click(driver)
        try:
            element = WebDriverWait(driver, 30).until( EC.presence_of_element_located((By.XPATH, "//div[@id='items']/awi-grid-row")))
        finally:
            elements = driver.find_elements_by_xpath("//div[@id='items']/awi-grid-row")
        time.sleep(1)
        for i in range (len(driver.find_elements_by_xpath("//div[@id='items']/awi-grid-row"))):
            if (i != 0):
                if driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell/div/span"%str(i)).text == meetingName:
                    #print "line 203, found the meeting , clicking on it; i is %s"%str(i)
                    #print 'meetign name is ' + meetingName
                    driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell/div/span"%str(i)).click()
                    time.sleep(5)
                    break


        #click Agenda Items link to get to agenda items tree section
        try:
            element = WebDriverWait(driver, 30).until( EC.presence_of_element_located((By.XPATH, "//paper-menu[@id='menu']/div/paper-item[3]/span")))
        finally:
            driver.find_element_by_xpath("//paper-menu[@id='menu']/div/paper-item[3]/span").click()
        time.sleep(2)

        #find teh agenda item
        try:
            element = WebDriverWait(driver, 30).until( EC.presence_of_element_located((By.XPATH, "//section[@id='Agenda%20Items']/awi-agenda-view/awi-agenda-tree/items-node")))
        finally:
            element = driver.find_element_by_xpath("//section[@id='Agenda%20Items']/awi-agenda-view/awi-agenda-tree/items-node")

        for i in range (len(driver.find_elements_by_xpath("//section[@id='Agenda%20Items']/awi-agenda-view/awi-agenda-tree/items-node"))+1):
            if (i != 0):
                print "line 230, aiTitle is %s"%aiTitle
                print "line 231, found text  is %s"%driver.find_element_by_xpath("//section/awi-agenda-view/awi-agenda-tree/items-node[%s]/div/items-pane/div/div[2]/div/span[@id='_title']/a"%str(i)).text
                if driver.find_element_by_xpath("//section/awi-agenda-view/awi-agenda-tree/items-node[%s]/div/items-pane/div/div[2]/div/span[@id='_title']/a"%str(i)).text == aiTitle:
                    print "agenda item is found, line 233"
                    #get the color of the agenda item
                    #posted agenda item should be  gray "#AAAAAA"
                    ai_color = driver.find_element_by_xpath("//section/awi-agenda-view/awi-agenda-tree/items-node[%s]/div/items-pane/div/div[2]/span[@id='_gutter']"%str(i))
                    if ai_color.value_of_css_property("background") == "#AAAAAA":
                        print "it is a gray color! as expected"
                    else:
                        "it is NOT the expected gray color!"
                    #get the 3 dots menu
                    ai_shelveMenu = driver.find_element_by_xpath("//section/awi-agenda-view/awi-agenda-tree/items-node[%s]/div/items-pane/div/div[2]/div[@id='_menu']/paper-menu-button[@id='_menuButton']/div[@id='trigger']/paper-icon-button"%str(i))
                    #gray colors pf 3 dots: rgba(177,189,174,0.5) - for Draft agenda item
                    #black color for 3 dots: rgba(0,0,0,0.87) - for Posted agenda item
                    if ai_shelveMenu.value_of_css_property("color") == "rgba(177,189,174,0.5)":
                        print "teh 3 dots color is black, as expected for Posted agenda item; line 201"
                    else:
                        print "the 3 dots color is NOT black, expected black for Posted agenda item"
                    #driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell/div/span"%str(i)).click
                    break
                else: print "did not find the agenda item.... how come?..i is %s"%str(i)

        #------------------------------------------------------------


        #go to agenda and click Add to Agenda button
        #``````````````````````````````````````````````````````````````````
        utils.MyItems_click(driver)
        for i in range (len(driver.find_elements_by_xpath("//div[@id='items']/awi-grid-row"))):
            if (i != 0):
                if driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell/div/span"%str(i)).text == aiTitle:
                    driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell/div/span"%str(i)).click
                    break
        time.sleep(10)

        #Add to Agenda
        try:
            element = WebDriverWait(driver, 20).until( EC.presence_of_element_located((By.ID, "actionButton0")))
        finally:
            driver.find_element_by_id("actionButton0").click()

        time.sleep(2)
        #Confirm Action
        try:
            element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//submit-action[@id='submit']/paper-dialog/div[2]/div/paper-button[2]")))
        finally:
            driver.find_element_by_xpath("//submit-action[@id='submit']/paper-dialog/div[2]/div/paper-button[2]").click()
        time.sleep(7)
        #````````````````````````````````````````````````````````````````````


        #     POSTED AGENDA ITEM VERIFICATION
        #click the meeting and verify the Posted agenda item is in there
        time.sleep(5)
        utils.MyMeetings_click(driver)
        for i in range (len(driver.find_elements_by_xpath("//div[@id='items']/awi-grid-row"))):
            if (i != 0):
                if driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell/div/span"%str(i)).text == meetingName:
                    driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell/div/span"%str(i)).click
                    break
        time.sleep(5)

        #click Agenda Items link to get to agenda items tree section
        try:
            element = WebDriverWait(driver, 30).until( EC.presence_of_element_located((By.XPATH, "//paper-menu[@id='menu']/div/paper-item[2]/span")))
        finally:
            driver.find_element_by_xpath("//paper-menu[@id='menu']/div/paper-item[2]/span").click()
        time.sleep(1)

        #find teh agenda item
        try:
            element = WebDriverWait(driver, 30).until( EC.presence_of_element_located((By.XPATH, "//section[@id='Agenda%20Items']/awi-agenda-view/awi-agenda-tree/items-node")))
        finally:
            element = driver.find_element_by_xpath("//section[@id='Agenda%20Items']/awi-agenda-view/awi-agenda-tree/items-node")

        for i in range (len(driver.find_elements_by_xpath("//section[@id='Agenda%20Items']/awi-agenda-view/awi-agenda-tree/items-node"))):
            if (i != 0):
                if driver.find_element_by_xpath("//section[@id='Agenda%20Items']/awi-agenda-view/awi-agenda-tree/items-node[%s]/div/items-pane/div/div[2]/div/span[@id='_title']/a"%str(i)).text == aiTitle:
                    print "agenda item is found, line 200"
                    #get the color of the agenda item
                    #posted agenda item should be green; draft should be gray "#AAAAAA"
                    ai_color = driver.find_element_by_xpath("//section[@id='Agenda%20Items']/awi-agenda-view/awi-agenda-tree/items-node[%s]/div/items-pane/div/div[2]/span[@id='_gutter']")
                    if color.value_of_css_property("background") == "#09C200":
                        print "it is a green color!"
                    else:
                        "it is NOT the exected green color!"
                    #get the 3 dots menu
                    ai_shelveMenu = driver.find_element_by_xpath("//section[@id='Agenda%20Items']/awi-agenda-view/awi-agenda-tree/items-node[%s]/div/items-pane/div/div[2]/div[@id='_menu']/paper-menu-button[@id='_menuButton']/div[@id='trigger']/paper-icon-button")
                    #gray colors pf 3 dots: rgba(177,189,174,0.5) - for Draft agenda item
                    #black color for 3 dots: rgba(0,0,0,0.87) - for Posted agenda item
                    if ai_shelveMenu.value_of_css_property("color") == "rgba(0,0,0,0.87)":
                        print "teh 3 dots color is black, as expected for Posted agenda item"
                    else:
                        print "the 3 dots color is NOT black, expected black for Posted agenda item"
                    #driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell/div/span"%str(i)).click
                    break

        #"//section[@id='Agenda%20Items']/awi-agenda-view/awi-agenda-tree/items-node/div/items-pane/div/div[2]/div/span[@id='_title']/a"

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
