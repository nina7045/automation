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
import utils, xlwt
from xlutils.copy import copy
import xlrd
import xlwt
import xlsxwriter


class MeetingDraft(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('C:/Python27/chromedriver.exe')
        self.base_url = "https://qa.agendaonline.com"
        self.verificationErrors = []
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get(self.base_url)


    def test_meeting_draft(self):

        driver = self.driver
        n = datetime.datetime.now()
        #book = xlwt.Workbook()
        #sheet = book.add_sheet('draftMeeting')
        #book.save('testResults_' + n.strftime("%m%d_%H%M"))
        #fileName ="meetingDraft_" + n.strftime("%m%d_%H%M")
        fileName ="testResults_" + n.strftime("%m%d_%H%M")
        wfPlan = ''
        userNameslist = []

        rb = xlrd.open_workbook('testResults.xlsx')
        wb = copy(rb)
        sh = 'draftM_delete'
        sheet = wb.get_sheet(sh)
        wb.save("testResults/" + fileName + '.xls')


        # login
        utils.login(driver)
        time.sleep(2)

        try:
            #element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//a/div[contains(text(), 'My Meetings')]")))
            element = driver.find_element_by_xpath("//div[contains(text(), 'My Meetings')]")
        finally:
            driver.find_element_by_xpath("//div[contains(text(), 'My Meetings')]").click()
            #driver.find_element_by_xpath("//avocado-frame/awi-app/main-container[@id='mainContainer']/app-router[@id='router']/app-route[15]/confirm-service-request-selection/dynamic-task-view/paper-drawer-panel/iron-selector/div[@id='drawer']/paper-header-panel/div[@id='mainPanel']/div[@id='mainContainer']/sidebar-navigation/div/div/paper-menu[@id='sidebarNavigation']/div/sidebar-menu-item[5]/paper-item/pushstate-anchor/a/div").click()
        time.sleep(2)

        totalM = utils.MyMeetings_Total(driver)

        if (totalM > 10):
            # delete meetings
            meetingDeleted = utils.meetingDelete(driver, totalM)
            utils.testResults_file_x(wb, sheet,"pass" + meetingDeleted,fileName, 30, 'p')

        time.sleep(2)
        try:
            element = WebDriverWait(driver, 20).until( EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Start New')]")))
        finally:
            driver.find_element_by_xpath("//div[contains(text(), 'Start New')]").click()

        time.sleep(2)
        try:
            element = WebDriverWait(driver, 20).until( EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Meeting')]")))
            #element = driver.find_element_by_xpath("//div[contains(text(), 'Meeting')]")
        finally:
            driver.find_element_by_xpath("//div[contains(text(), 'Meeting')]").click()
        time.sleep(3)
        try:
            element = WebDriverWait(driver, 20).until( EC.presence_of_element_located((By.ID, "confirmServiceRequestConfirmBtn")))
        finally:
            driver.find_element_by_id("confirmServiceRequestConfirmBtn").click()
        time.sleep(4)

        #     Save button  verify
        utils.SaveButton_Draft_InDev_Meeting(driver, wb, sheet, fileName)

        #     Assign button verify
        utils.AssignButton_Draft_InDev_Meeting(driver, wb, sheet, fileName)

        #   Cancel Meeting button verify
        utils.CancelMeetingButton_Draft_InDev_Meeting(driver, wb, sheet, fileName)

        #   Open MEETING button verify
        utils.OpenMeetingButton_DraftMeeting(driver, wb, sheet, fileName)
        # time.sleep(1)
        # try:
        #     element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@id='topBar']/div/paper-button[@id='actionButton1']")))
        # finally:
        #     openButton = driver.find_element_by_xpath("//div[@id='topBar']/div/paper-button[@id='actionButton1']")
        # if openButton.is_displayed():
        #     utils.testResults_file_x(wb, sheet,"pass",fileName, sh, 13, 'p')
        # else:
        #     utils.testResults_file_x(wb, sheet,"fail",fileName, sh, 13, 'f')
        # if openButton.value_of_css_property("background-color") == "rgba(227, 119, 68, 1)":
        #     utils.testResults_file_x(wb, sheet,"pass",fileName, sh, 14, 'p')
        # else:
        #     utils.testResults_file_x(wb, sheet,"fail",fileName, sh, 14, 'f')
        # if openButton.value_of_css_property("color") == "rgba(255, 255, 255, 1)":
        #     utils.testResults_file_x(wb, sheet,"pass",fileName, sh, 15, 'p')
        # else:
        #     utils.testResults_file_x(wb, sheet,"fail",fileName, sh, 15, 'f')
        # if openButton.text == "OPEN MEETING":
        #     utils.testResults_file_x(wb, sheet,"pass",fileName, sh, 12, 'p')
        # else:
        #     utils.testResults_file_x(wb, sheet,"fail",fileName, sh, 12, 'f')

        # Draft title verify
        utils.title_DraftMeeting(driver, wb, sheet, fileName)

        # Instructions title verify
        utils.InstructionsTitle_Draft_InDev_Meeting(driver, wb, sheet, fileName)

        #Instructions text verify
        utils.InstructionsText_DraftMeeting(driver, wb, sheet, fileName)

        # get the first and last names of the initiator from the right top corner
        firstLastName = driver.find_element_by_xpath("//div[@id='topBar']/div/task-requestor/div/a[@id='userName']").text
        #print "first and last name is " + firstLastName

        # fil in all required fields:
        now = datetime.datetime.now()
        meetingTitle = "m_" + now.strftime("%Y-%m-%d %H:%M")
        driver.find_elements_by_xpath("//input[@id='input']")[4].send_keys(meetingTitle)
        time.sleep(1)
        #driver.find_elements_by_xpath("//input[@id='input']")[5].send_keys("Apr 30 2018")
        driver.find_elements_by_xpath("//input[@id='input']")[5].send_keys(now.strftime('%b %d %Y'))
        time.sleep(1)
        #driver.find_elements_by_xpath("//input[@id='input']")[6].send_keys("1:21 PM")
        driver.find_elements_by_xpath("//input[@id='input']")[6].send_keys(now.strftime("%I:%M %p"))
        time.sleep(1)
        driver.find_elements_by_xpath("//input[@id='input']")[8].send_keys("location " + meetingTitle)
        time.sleep(1)
        driver.find_elements_by_xpath("//div[@id='toggleIcon']/iron-icon")[2].click()
        #time.sleep(1)
        #get all items in the Agenda Workflow Route
        try:
            element =  driver.find_element_by_xpath("//awi-combobox-overlay[@id='overlay']")
            #element =  driver.find_element_by_xpath("//awi-combobox-item[contains(text(), 'No Approval Required')]")
        finally:
            workflowRouteItems = driver.find_elements_by_xpath("//awi-combobox-overlay[@id='overlay']/div/iron-list/div/awi-combobox-item")
            for w in workflowRouteItems:
                if w.text != "No Approval Required":
                    wfPlan = w.text
                    w.click()
                    break
        time.sleep(1)
        driver.find_elements_by_xpath("//div[@id='toggleIcon']/iron-icon")[3].click()
        driver.find_element_by_xpath("//awi-combobox-item[@id='it']").click()
        time.sleep(1)
        iFrame1 = driver.find_element_by_xpath("//div[@id='cke_1_contents']/iframe")
        driver.switch_to.frame(iFrame1)
        driver.find_element_by_tag_name("body").clear()
        driver.find_element_by_tag_name("body").send_keys("this is a preliminary section")
        time.sleep(1)
        driver.switch_to.default_content()
        time.sleep(1)
        iFrame2 = driver.find_element_by_xpath("//div[@id='cke_2_contents']/iframe")
        driver.switch_to.frame(iFrame2)
        driver.find_element_by_tag_name("body").clear()
        driver.find_element_by_tag_name("body").send_keys("this is a closing section")
        time.sleep(1)
        driver.switch_to.default_content()
        time.sleep(2)

        try:
            element = driver.find_element_by_id("saveActionButton")
        finally:
            driver.find_element_by_id("saveActionButton").click()
        time.sleep(3)

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

        # Open Meeting button
        # try:
        #     element = driver.find_element_by_id("actionButton1")
        # finally:
        #     driver.find_element_by_id("actionButton1").click()
        # driver.implicitly_wait(5)
        #
        # try:
        #     element = driver.find_element_by_xpath("//paper-dialog[@id='dialog']/div[2]/div/paper-button[contains(text(), 'Ok')]")
        # finally:
        #     driver.find_element_by_xpath("//paper-dialog[@id='dialog']/div[2]/div/paper-button[contains(text(), 'Ok')]").click()
        #     #driver.find_element_by_xpath("//div[@id='topBar']/a/span").text
        # time.sleep(2)


        # Start New screen
        # try:
        #     element = driver.find_element_by_xpath("//div[@id='topBar']/a/span")
        # finally:
        #     driver.find_element_by_xpath("//div[@id='topBar']/a/span").text
        #     if driver.find_element_by_xpath("//div[@id='topBar']/a/span").text == "Agenda Management":
        #         utils.testResults_file("Back to Start New page" + "\r\n", fileName)
        #     else:
        #         utils.testResults_file("NOT Back to Start New page... where are you???" + "\r\n", fileName)
        #time.sleep(4)

        # Workflow Routes  to get the selected above workflow route and get the next user's name in the route
        #userNameslist = utils.workFlowRoute(driver, wfPlan)
        #for u in userNameslist:
            #print "user name is " + u

        # # Admin click
        # try:
        #     #element = driver.find_element_by_xpath("//avocado-frame/awi-app/main-container[@id='mainContainer']/app-router[@id='router']/app-route[15]/confirm-service-request-selection/dynamic-task-view/paper-drawer-panel/iron-selector/div[@id='drawer']/paper-header-panel/div[@id='mainPanel']/div[@id='mainContainer']/sidebar-navigation/div/div/paper-menu[@id='sidebarNavigation']/div/sidebar-menu-item[8]/paper-item/pushstate-anchor/a/div")
        #     element = driver.find_element_by_xpath("//paper-menu[@id='sidebarNavigation']/div/sidebar-menu-item[8]/paper-item/pushstate-anchor/a/div")
        # finally:
        #     #driver.find_element_by_xpath("//avocado-frame/awi-app/main-container[@id='mainContainer']/app-router[@id='router']/app-route[15]/confirm-service-request-selection/dynamic-task-view/paper-drawer-panel/iron-selector/div[@id='drawer']/paper-header-panel/div[@id='mainPanel']/div[@id='mainContainer']/sidebar-navigation/div/div/paper-menu[@id='sidebarNavigation']/div/sidebar-menu-item[8]/paper-item/pushstate-anchor/a/div").click()
        #     driver.find_element_by_xpath("//paper-menu[@id='sidebarNavigation']/div/sidebar-menu-item[8]/paper-item/pushstate-anchor/a/div").click()
        # time.sleep(4)
        # # Workflow routes Click
        # driver.find_element_by_xpath("//div[@id='mainContainer']/div/div[4]/div/paper-toolbar/div[@id='topBar']/a/span").click()
        # time.sleep(2)
        # routesLength = driver.find_elements_by_xpath("//div[@id='items']/awi-grid-row")
        # for rl in range (len(driver.find_elements_by_xpath("//div[@id='items']/awi-grid-row"))):
        #     if (rl != 0):
        #         print driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell/div/span"%str(rl)).text
        #         if driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell/div/span"%str(rl)).text == wfPlan:
        #             driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell/div/span"%str(rl)).click()
        #             time.sleep(1)
        #             nextUserName = driver.find_element_by_xpath("//paper-dialog[@id='editRouteDialog']/div/div[2]/div[2]/awi-grid[@id='usersGrid']/div/div/div/iron-list[@id='list']/div[@id='items']/awi-grid-row/awi-grid-cell[2]/div/span").text
        #             print nextUserName

        # click My Meetings left nav bar link again:
        #time.sleep(2)
        #driver.find_element_by_xpath("//avocado-frame/awi-app/main-container[@id='mainContainer']/app-router[@id='router']/app-route[15]/confirm-service-request-selection/dynamic-task-view/paper-drawer-panel/iron-selector/div[@id='drawer']/paper-header-panel/div[@id='mainPanel']/div[@id='mainContainer']/sidebar-navigation/div/div/paper-menu[@id='sidebarNavigation']/div/sidebar-menu-item[5]/paper-item/pushstate-anchor/a/div").click()
        #driver.find_element_by_xpath("//paper-menu[@id='sidebarNavigation']/div/sidebar-menu-item[5]/paper-item/pushstate-anchor/a/div").click()
        #time.sleep(2)

        # My Meetings screen to find the new meeting and verify its Status and Assigned to
        try:
            element = driver.find_element_by_xpath("//span[contains(text(), 'Total items:')]")
        finally:
            mTotal3 = driver.find_element_by_xpath("//span[contains(text(), 'Total items:')]").text
            mTotal3= mTotal3[(mTotal3.find(': ')+1):].strip()
            #print "mtotal 3 is " + mTotal3
            #utils.testResults_file("Total meetings : " + mTotal3 + "\r\n", fileName)
        time.sleep(2)

        # find the new meeting in the list and verify its status and Assigned to values

        # meetings = driver.find_elements_by_xpath("//div[@id='items']/awi-grid-row")
        # for m in meetings:
        #     print 'm.text is ' + m.text
        #     if m.text.find(meetingTitle) > 0:
        #         utils.testResults_file_x(wb, sheet,"pass" + " the new meeting: " + meetingTitle + " is found in the list",fileName, sh, 25, 'p')
        #         # meetings's status:
        #         if driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell[6]/div/span"%str(i)).text == "Draft":
        #
        #     else:
        #         utils.testResults_file_x(wb, sheet,"fail" + " the new meeting: " + meetingTitle + " is NOT found in the list",fileName, sh, 25, 'f')
        #

        l = len( driver.find_elements_by_xpath("//div[@id='items']/awi-grid-row"))
        i=1
        for i in range (len(driver.find_elements_by_xpath("//div[@id='items']/awi-grid-row"))):
            if (i != 0):
                #meting and its status:
                meeting = driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell/div/span"%str(i)).text
                # this is how to get status:   driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell[6]/div/span"%str(i)).text
                # find the new meeting and verify its status and Assigned to values
                #if meeting.strip() == meetingTitle.strip():
                if meeting == meetingTitle:
                    utils.testResults_file_x(wb, sheet,"pass: " + meetingTitle + " is found in the list",fileName, 25, 'p')
                    status = driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell[6]/div/span"%str(i)).text
                    if status == "Draft":
                        #utils.testResults_file(meeting + "is found in My Meetings list" + "\r\n", fileName)
                        utils.testResults_file_x(wb, sheet,"pass",fileName, 26, 'p')
                    else:
                        #utils.testResults_file("the new meeting is not in Draft state" + "\r\n", fileName)
                        utils.testResults_file_x(wb, sheet,"fail" + " the status is " + status,fileName, 26, 'f')

                    # Assigned To value
                    assignedTo = driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell[7]/div/span"%str(i)).text
                    print "assigned to is " + assignedTo
                    if assignedTo == firstLastName:
                        utils.testResults_file_x(wb, sheet,"pass",fileName, 27, 'p')
                    else:
                        utils.testResults_file_x(wb, sheet,"fail" + " AssignedTo is " + assignedTo,fileName, 27, 'f')

                    #click on the new meeting
                    driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell/div/span"%str(i)).click()
                    print "clicked on the new meeting"
                    break
                #else:
                    #utils.testResults_file("the new meetign is not found in My Meetings list" + "\r\n", fileName)
                    #utils.testResults_file_x(wb, sheet,"fail" + " the new meeting: " + meetingTitle + " is NOT found in the list",fileName, sh, 25, 'f')


        time.sleep(5)
        # click on Private note icon
        try:
            element = driver.find_element_by_id("privateNote")
        finally:
            driver.find_element_by_id("privateNote").click()
        # try:
        #     element = driver.find_elements_by_xpath("//private-note[@id='privateNote']/div/paper-icon-button[@id='note-button']/iron-icon[@id='icon']")
        # finally:
        #     #driver.find_elements_by_xpath("//private-note[@id='privateNote']/div/paper-icon-button[@id='note-button']/iron-icon[@id='icon']").click()
        #     #driver.find_elements_by_xpath("//private-note[@id='privateNote']/div/paper-icon-button[@id='note-button']").click()
        #     driver.find_elements_by_xpath("//private-note[@id='privateNote']").click()
        #     #driver.find_elements_by_xpath("//private-note[@id='privateNote']/div/paper-icon-button[@id='note-button']/iron-icon[@id='icon']").select()
        time.sleep(2)
        placeholderText = driver.find_element_by_xpath("//paper-dialog[@id='dialog']/div[2]/textarea[@id='input']").get_attribute("placeholder")
        #print "Private note shows this text: " + driver.find_element_by_xpath("//paper-dialog[@id='dialog']/div[2]/textarea[@id='input']").get_attribute("placeholder")
        if placeholderText == "Type Private Notes here...":
            utils.testResults_file_x(wb, sheet,"pass",fileName, 28, 'p')
        else:
            utils.testResults_file_x(wb, sheet,"fail" + placeholderText,fileName, 28, 'f')
        time.sleep(1)
        driver.find_element_by_xpath("//paper-dialog[@id='dialog']/div[2]/textarea[@id='input']").send_keys("Typing some text !!!")
        time.sleep(1)
        #close the private note win
        driver.find_element_by_xpath("//paper-dialog[@id='dialog']/div/paper-icon-button[@id='close-button']").click()
        time.sleep(1)
        try:
            element = driver.find_element_by_id("privateNote")
        finally:
            driver.find_element_by_id("privateNote").click()
        time.sleep(1)
        typedText = driver.find_element_by_xpath("//paper-dialog[@id='dialog']/div[2]/textarea[@id='input']").get_attribute('value')
        print "typedText is ..." + typedText
        if typedText == "Typing some text !!!":
            utils.testResults_file_x(wb, sheet,"pass",fileName, 29, 'p')
        else:
            utils.testResults_file_x(wb, sheet,"fail" + typedText ,fileName, 29, 'f')
    # def is_element_present(self, how, what):
    #     try: self.driver.find_element(by=how, value=what)
    #     except NoSuchElementException, e: return False
    #     return True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
