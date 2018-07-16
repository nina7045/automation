import os
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re, random
from random import randint
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import datetime, ast
import sys
import os
from selenium.webdriver.common.action_chains import ActionChains
import utils, meetings, agenda_items, xlwt, admin
from xlutils.copy import copy
import xlrd
import xlwt
import xlsxwriter


class MasterTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('C:/Python27/chromedriver.exe')
        self.base_url = "https://qa.agendaonline.com"
        #self.base_url = "https://app.agendaonline.com"
        self.verificationErrors = []
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get(self.base_url)


    def test_master(self):

        driver = self.driver
        n = datetime.datetime.now()
        #book = xlwt.Workbook()
        #sheet = book.add_sheet('draftMeeting')
        #book.save('testResults_' + n.strftime("%m%d_%H%M"))
        #fileName ="meetingDraft_" + n.strftime("%m%d_%H%M")
        version = "v_1.38_"
        if self.base_url == "https://qa.agendaonline.com":
            env = "qa_"
        else:
            env = "prod_"
        #fileName ="testResults_" + env + version + n.strftime("%m%d_%H%M")
        wfPlan = ''
        userNameslist = []
        GovBod = ''
        aiToAdd = 2  # number of items to add
        # create a new meeting?
        newM = "y"
        GBtitle = ""   # one GB
        #type = "Prem"     # type of tested organization: Prem has multiple GBs and Start Broadcasting button; Pro and Lite dont have those

        # Logins
        # 2  qa
        # loginName = "nina7045_mm@yahoo.com"
        # password = "testing1"
        # selectOrg = "may22_927"
        # 3  qa
        # loginName = "nina7045@yahoo.com"
        # password = "testing1"
        # selectOrg = "may25_Prem"
        # 4  qa
        # loginName = "ao2meetingmanager@gmail.com"
        # password = "testing1"
        # selectOrg = "may22_927"
        # 5   prod
        # loginName = "nbezroukova@csba.org"
        # password = "testing1"
        # selectOrg = "Demo 2 USD"
        # 6  qa
        # loginName = "nbezroukova@csba.org"
        # password = "testing2"
        # selectOrg = "Banning Test 060118"
        # 6  qa
        # loginName = "ao2meetingmanager@gmail.com"
        # password = "testing1"
        # selectOrg = "071118_Lite_3users"
        #7
        loginName = "ao2meetingmanager@gmail.com"   # MM in all 4 GBs ; Prem
        password = "testing1"
        selectOrg = "may23_prem"

        #  if it is a premium organization, it must select a GB:
        if (selectOrg.find("prem") > 0):
            type = "Prem_"
            GB = 1
        else:
            type = "Pro_"
            GB = 0

        fileName ="testResults_" + env + version + type + n.strftime("%m%d_%H%M")

        rb = xlrd.open_workbook('testResults.xlsx')
        wb = copy(rb)
        #sh = 'Meeting'
        sheet = wb.get_sheet('Login')
        wb.save("testResults/" + fileName + '.xls')

        # login
        utils.login(driver, wb, sheet, fileName, loginName, password, selectOrg, GB)   # GB is a Governogn Body , if it is 1, a GB must be selected in new Agenda Item; if 0, no GB selection
        time.sleep(1)

        #  verify the Dashboard page
        admin.Dashboard(driver, wb, sheet, fileName);

        #  get Governing Body and its format
        # run this if there is onyl one governign body, like in PRO and LITE
        #governingBody = utils.GoverningBodies(driver, GovBod)

        if newM == "y":
            # meeting Draft
            (meetingTitle, GBtitle) = meetings.m_Draft(driver, wb, sheet, fileName, GB, GBtitle)
        else:
            # select an existing meeting Draft
            print "Need to write a module to select a Draft meeting"

        # need to verify that Draft meeting is not in "My Tasks", "All Tasks: and "My Items" lists

        # meeting In Development
        meetings.m_InDev(driver, wb, sheet, fileName, meetingTitle)

        #add an agenda item to the meeting
        (aiTitle,GovBod, status) = agenda_items.ai_Draft(driver, wb, sheet, fileName, meetingTitle, GB, GBtitle)

        # get the GB's format's first char
        gb_formatChar = utils.GoverningBodies(driver, GovBod)

        #verify ai in meeting adn get the char displaye if theer was no GB format char
        formatChar = meetings.meeting_ai(driver, wb, sheet, fileName, meetingTitle, aiTitle,gb_formatChar, status)

        #post ai
        agenda_items.ai_Post(driver, wb, sheet, fileName, meetingTitle, aiTitle)
        # nullify status to work wirh Posted ai in meeting
        status = ""

        #verify Posted ai in meeting
        meetings.meeting_ai(driver, wb, sheet, fileName, meetingTitle, aiTitle,formatChar, status)

        #  add more agenda Items
        agenda_items.ai_add(driver, meetingTitle, aiToAdd, GB, GBtitle)

        # close teh meetings --> Approved, verify toolbar buttons and agenda item in place and correct
        meetings.m_Appr(driver, wb, sheet, fileName, meetingTitle)

        # Publish meeting, get time
        meetings.m_Publish(driver, wb, sheet, fileName, meetingTitle)

        # Start MEETING
        meetings.m_InProgress(driver, wb, sheet, fileName, meetingTitle)

        # Stop Meeting

    # def is_element_present(self, how, what):
    #     try: self.driver.find_element(by=how, value=what)
    #     except NoSuchElementException, e: return False
    #     return True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
