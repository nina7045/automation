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
        # Have two meetings: meeting1, created from a template and
        # meeting2, whose agenda items added from Start New.
        #Test with both metings.

        driver = self.driver
        n = datetime.datetime.now()
        fileName ="testResults_" + n.strftime("%m%d_%H%M")
        wfPlan = ''
        meetingsList = []

        rb = xlrd.open_workbook('testResults.xlsx')
        wb = copy(rb)
        sh = 'm_InDev'
        sheet = wb.get_sheet(sh)
        wb.save("testResults/" + fileName + '.xls')


        # login
        utils.login(driver)
        time.sleep(2)

        utils.MyMeetings_click(driver)

        #select a meetign IN Dev status






        mDeleted = utils.meetingDelete(driver, 15)
        try:
            element = WebDriverWait(driver, 20).until( EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Start New')]")))
        finally:
            driver.find_element_by_xpath("//div[contains(text(), 'Start New')]").click()
        time.sleep(2)

        # create 2 new meetings In Dev state: meeting 1 with new agenda item; meeting 2 is with template
        # to create 2 meetings
        for i in range(2):
            now = datetime.datetime.now()
            meetingTitle = "m" + str(i) + "_" + now.strftime("%Y-%m-%d %H:%M")
            if i == 0:
                m1 = meetingTitle
            else:
                m2 = meetingTitle
            # click Meeting
            try:
                element = EC.presence_of_element_located((By.XPATH, "//ul/li[1]/a/div[contains(text(), 'Meeting')]"))
                WebDriverWait(driver, 20).until(element)
            except TimeoutException:
                print "timed out waiting for Meeting link"
            finally:
                driver.find_element_by_xpath("//div[contains(text(), 'Meeting')]").click()
            time.sleep(3)

            #second meeting should be from template
            if i == 1:
                try:
                    element = driver.find_element_by_xpath("//awi-combobox[@id='_selectTemplate']")
                finally:
                    driver.find_element_by_xpath("//awi-combobox[@id='_selectTemplate']/div[2]/paper-input-container[@id='inputContainer']/div/div[@id='toggleIcon']/iron-icon").click()
                    time.sleep(1)
                    driver.find_element_by_xpath("//awi-combobox-overlay[@id='overlay']/div[@id='scroller']/iron-list[@id='selector']/div[@id='items']/awi-combobox-item[@id='it']").click()
                    time.sleep(2)

                driver.find_element_by_id("confirmServiceRequestConfirmBtn").click()
                time.sleep(5)

                # if from tmplate generating Agenda is running, wait when its done:
                #if driver.find_element_by_xpath("//paper-dialog[@id='showProgress']"):
                    #for t in range (10000):
                        #print "t is " + str(t)
                while driver.find_element_by_xpath("//paper-dialog[@id='showProgress']"):
                    try:
                        driver.find_element_by_xpath("//paper-dialog[@id='showProgress']/div[2]/paper-button[contains(text(), 'Go to Meeting')]").click()
                        break
                    except NoSuchElementException:
                        print "waiting for Go To Meeting button"

                # fil in required fields:
                driver.find_elements_by_xpath("//input[@id='input']")[4].clear()
                driver.find_elements_by_xpath("//input[@id='input']")[4].send_keys(meetingTitle)
                # add the meetign to the list; that will contain two meetings
                meetingsList.append(meetingTitle)
                time.sleep(1)
                driver.find_elements_by_xpath("//input[@id='input']")[5].send_keys(now.strftime('%b %d %Y'))
                time.sleep(1)
                driver.find_elements_by_xpath("//input[@id='input']")[6].clear()
                driver.find_elements_by_xpath("//input[@id='input']")[6].send_keys(now.strftime("%I:%M %p"))

            else:
                time.sleep(3)
                try:
                    element = EC.presence_of_element_located((By.ID, "confirmServiceRequestConfirmBtn"))
                    WebDriverWait(driver, 20).until(element)
                except TimeoutException:
                    print "timed out waiting for Next link"
                finally:
                    driver.find_element_by_id("confirmServiceRequestConfirmBtn").click()

                #driver.find_element_by_id("confirmServiceRequestConfirmBtn").click()
                time.sleep(4)

                # fil in all required fields:
                driver.find_elements_by_xpath("//input[@id='input']")[4].send_keys(meetingTitle)
                # add the meetign to the list; that will contain two meetings
                meetingsList.append(meetingTitle)
                time.sleep(1)
                driver.find_elements_by_xpath("//input[@id='input']")[5].send_keys(now.strftime('%b %d %Y'))
                time.sleep(1)
                driver.find_elements_by_xpath("//input[@id='input']")[6].send_keys(now.strftime("%I:%M %p"))
                time.sleep(1)
                driver.find_elements_by_xpath("//input[@id='input']")[8].send_keys("location " + meetingTitle)
                time.sleep(1)
                driver.find_elements_by_xpath("//div[@id='toggleIcon']/iron-icon")[2].click()
                time.sleep(1)
                try:
                    element =  driver.find_element_by_xpath("//awi-combobox-overlay[@id='overlay']")
                    #element =  driver.find_element_by_xpath("//awi-combobox-item[contains(text(), 'No Approval Required')]")
                finally:
                    driver.find_element_by_xpath("//awi-combobox-overlay[@id='overlay']/div/iron-list/div/awi-combobox-item[contains(text(), 'No Approval Required')]").click()

                time.sleep(1)
                driver.find_elements_by_xpath("//div[@id='toggleIcon']/iron-icon")[3].click()
                # if it cannot be found, continue the script
                try: driver.find_element_by_xpath("//awi-combobox-item[@id='it']").click()
                except NoSuchElementException:
                    print "no need to select group, its selected itself"
                # to get out of the input attendance group field
                driver.find_element_by_xpath("//div[@id='task-main-section']/div").click()
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

            # Save button
            try:
                element = driver.find_element_by_id("saveActionButton")
            finally:
                driver.find_element_by_id("saveActionButton").click()
            time.sleep(3)

            # click the Open Meeting button --> the meeting is in Dev state
            try:
                element = driver.find_element_by_id("actionButton1")
            finally:
                driver.find_element_by_id("actionButton1").click()
            time.sleep(3)

            try:
                element = driver.find_element_by_xpath("//paper-dialog[@id='dialog']/div[2]/div/paper-button[contains(text(), 'Ok')]")
            finally:
                driver.find_element_by_xpath("//paper-dialog[@id='dialog']/div[2]/div/paper-button[contains(text(), 'Ok')]").click()
                #driver.find_element_by_xpath("//div[@id='topBar']/a/span").text
            time.sleep(5)

            # wait till Start New is on
            try:
                element = WebDriverWait(driver, 55).until(EC.presence_of_element_located((By.XPATH, "//ul/li[1]/a/div[contains(text(), 'Meeting')]")))
            finally:
                print "found!"

        print "first meeting is " + m1
        print "second meeting is " + m2
        # My Meetings click
        utils.MyMeetings_click(driver)

        # find the first meeting , created above
        for i in range (len(driver.find_elements_by_xpath("//div[@id='items']/awi-grid-row"))):
            if (i != 0):
                # meeting and its status:
                meeting = driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell/div/span"%str(i)).text
                # this is how to get status:   driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell[6]/div/span"%str(i)).text
                # find the new meeting and verify its status and Assigned to values
                if meeting == m1:
                    utils.testResults_file_x(wb, sheet,"pass: " + m1 + " is found in the list",fileName, 0, 'p')
                    status = driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell[6]/div/span"%str(i)).text
                    if status == "In Development":
                        #utils.testResults_file(meeting + "is found in My Meetings list" + "\r\n", fileName)
                        utils.testResults_file_x(wb, sheet,"pass " + status,fileName, 1, 'p')
                    else:
                        #utils.testResults_file("the new meeting is not in Draft state" + "\r\n", fileName)
                        utils.testResults_file_x(wb, sheet,"fail" + " the status is " + status,fileName, 1, 'f')

                    #click on the new meeting
                    driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell/div/span"%str(i)).click()
                    print "clicked on the new meeting"
                    time.sleep(2)
                    break

        #     Save button  verify
        utils.SaveButton_Draft_InDev_Meeting(driver, wb, sheet, fileName)
        # try:
        #     element = WebDriverWait(driver, 50).until( EC.presence_of_element_located((By.XPATH, "//div[@id='topBar']/paper-button[@id='saveActionButton']")))
        # finally:
        #     saveButton = driver.find_element_by_xpath("//div[@id='topBar']/paper-button[@id='saveActionButton']")
        # if saveButton.is_displayed():
        #     utils.testResults_file_x(wb, sheet,"pass",fileName, 1, 'p')
        # else:
        #     utils.testResults_file_x(wb, sheet,"fail",fileName, 1, 'f')
        # if saveButton.value_of_css_property("background-color") == "rgba(255, 255, 255, 1)":
        #     utils.testResults_file_x(wb, sheet,"pass",fileName, 2, 'p')
        # else:
        #     utils.testResults_file_x(wb, sheet,"fail",fileName, 2, 'f')
        # if saveButton.value_of_css_property("color") == "rgba(51, 136, 193, 1)":
        #     utils.testResults_file_x(wb, sheet,"pass",fileName, 3, 'p')
        # else:
        #     utils.testResults_file_x(wb, sheet,"fail",fileName, 3, 'f')
        # if saveButton.text == "SAVE":
        #     utils.testResults_file_x(wb, sheet,"pass",fileName, 0, 'p')
        # else:
        #     utils.testResults_file_x(wb, sheet,"fail",fileName, sh, 0, 'f')

        #     Assign button
        time.sleep(1)
        utils.AssignButton_Draft_InDev_Meeting(driver, wb, sheet, fileName)
        # try:
        #     element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@id='topBar']/paper-button[@id='assignActionButton']")))
        # finally:
        #     assignButton = driver.find_element_by_xpath("//div[@id='topBar']/paper-button[@id='assignActionButton']")
        # if assignButton.is_displayed():
        #     utils.testResults_file_x(wb, sheet,"pass",fileName, 5, 'p')
        # else:
        #     utils.testResults_file_x(wb, sheet,"fail",fileName, 5, 'f')
        # if assignButton.value_of_css_property("background-color") == "rgba(255, 255, 255, 1)":
        #     utils.testResults_file_x(wb, sheet,"pass",fileName, 6, 'p')
        # else:
        #     utils.testResults_file_x(wb, sheet,"fail",fileName, 6, 'f')
        # if assignButton.value_of_css_property("color") == "rgba(51, 136, 193, 1)":
        #     utils.testResults_file_x(wb, sheet,"pass",fileName, 7, 'p')
        # else:
        #     utils.testResults_file_x(wb, sheet,"fail",fileName, 7, 'f')
        # if assignButton.text == "ASSIGN":
        #     utils.testResults_file_x(wb, sheet,"pass",fileName, 4, 'p')
        # else:
        #     utils.testResults_file_x(wb, sheet,"fail",fileName, 4, 'f')

        #   Cancel Meeting
        time.sleep(1)
        utils.CancelMeetingButton_Draft_InDev_Meeting(driver, wb, sheet, fileName)
        # try:
        #     element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@id='topBar']/div/paper-button[@id='actionButton0']")))
        # finally:
        #     cancelButton = driver.find_element_by_xpath("//div[@id='topBar']/div/paper-button[@id='actionButton0']/span")
        # if cancelButton.is_displayed():
        #     utils.testResults_file_x(wb, sheet,"pass",fileName, 9, 'p')
        # else:
        #     utils.testResults_file_x(wb, sheet,"fail",fileName, 9, 'f')
        # if cancelButton.value_of_css_property("background-color") == "rgba(0, 0, 0, 0)":
        #     utils.testResults_file_x(wb, sheet,"pass",fileName, 10, 'p')
        # else:
        #     utils.testResults_file_x(wb, sheet,"fail",fileName, 10, 'f')
        # if cancelButton.value_of_css_property("color") == "rgba(51, 136, 193, 1)":
        #     utils.testResults_file_x(wb, sheet,"pass",fileName, 11, 'p')
        # else:
        #     utils.testResults_file_x(wb, sheet,"fail",fileName, 11, 'f')
        # if cancelButton.text == "CANCEL MEETING":
        #     utils.testResults_file_x(wb, sheet,"pass",fileName, 8, 'p')
        # else:
        #     utils.testResults_file_x(wb, sheet,"fail",fileName, 8, 'f')

        #   Close MEETING
        time.sleep(1)
        utils.CloseMeetingButton_InDev_Meeting(driver, wb, sheet, fileName)
        # try:
        #     element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@id='topBar']/div/paper-button[@id='actionButton1']/span")))
        # finally:
        #     openButton = driver.find_element_by_xpath("//div[@id='topBar']/div/paper-button[@id='actionButton1']/span")
        # if openButton.is_displayed():
        #     utils.testResults_file_x(wb, sheet,"pass",fileName, 13, 'p')
        # else:
        #     utils.testResults_file_x(wb, sheet,"fail",fileName, 13, 'f')
        # if openButton.value_of_css_property("background-color") == "rgba(227, 119, 68, 1)":
        #     utils.testResults_file_x(wb, sheet,"pass",fileName, 14, 'p')
        # else:
        #     utils.testResults_file_x(wb, sheet,"fail",fileName, 14, 'f')
        # if openButton.value_of_css_property("color") == "rgba(255, 255, 255, 1)":
        #     utils.testResults_file_x(wb, sheet,"pass",fileName, 15, 'p')
        # else:
        #     utils.testResults_file_x(wb, sheet,"fail",fileName, 15, 'f')
        # if openButton.text == "Close Meeting":
        #     utils.testResults_file_x(wb, sheet,"pass",fileName, 12, 'p')
        # else:
        #     utils.testResults_file_x(wb, sheet,"fail",fileName, 12, 'f')

        # In Development title
        time.sleep(1)
        utils.title_InDevMeeting(driver, wb, sheet, fileName)
        # try:
        #     element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@id='mainContainer']/div/div[2]/div/div/div[2]")))
        # finally:
        #     draftTitle = driver.find_element_by_xpath("//div[@id='mainContainer']/div/div[2]/div/div/div[2]")
        # if draftTitle.is_displayed():
        #     utils.testResults_file_x(wb, sheet,"pass",fileName, 17, 'p')
        # else:
        #     utils.testResults_file_x(wb, sheet,"fail",fileName, 17, 'f')
        # if draftTitle.value_of_css_property("color") == "rgba(51, 136, 193, 1)":
        #     utils.testResults_file_x(wb, sheet,"pass",fileName, 18, 'p')
        # else:
        #     utils.testResults_file_x(wb, sheet,"fail",fileName, 18, 'f')
        # if draftTitle.text == "In Development":
        #     utils.testResults_file_x(wb, sheet,"pass",fileName, 16, 'p')
        # else:
        #     utils.testResults_file_x(wb, sheet,"fail",fileName, 16, 'f')


        # Instructions title
        time.sleep(1)
        utils.InstructionsTitle_InDev_Meeting(driver, wb, sheet, fileName)
        # try:
        #     element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//section[@id='Instructions']/h1")))
        # finally:
        #     instructionsTitle = driver.find_element_by_xpath("//section[@id='Instructions']/h1")
        #
        # if instructionsTitle.is_displayed():
        #     utils.testResults_file_x(wb, sheet,"pass",fileName, 20, 'p')
        # else:
        #     utils.testResults_file_x(wb, sheet,"fail",fileName, 20, 'f')
        # if instructionsTitle.value_of_css_property("color") == "rgba(0, 0, 0, 0.54)":
        #     utils.testResults_file_x(wb, sheet,"pass",fileName, 21, 'p')
        # else:
        #     utils.testResults_file_x(wb, sheet,"fail",fileName, 21, 'f')
        # if instructionsTitle.text == "Instructions":
        #     utils.testResults_file_x(wb, sheet,"pass",fileName, 19, 'p')
        # else:
        #     utils.testResults_file_x(wb, sheet,"fail",fileName, 19, 'f')

        #Instructions text
        utils.InstructionsText_InDev_Meeting(driver, wb, sheet, fileName)
        try:
            element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//section[@id='Instructions']/h1")))
        finally:
            instructionsText = driver.find_element_by_xpath("//div[@id='content']/div/ul")
            i=22
        items = instructionsText.find_elements_by_tag_name("li")
        for item in items:
            if item.text == "Fill in the necessary fields for this meeting.":
                #utils.testResults_file("item 1 matches and is: "+ item.text + "\r\n", fileName)
                utils.testResults_file_x(wb, sheet,"pass",fileName, 22, 'p')
                i+=1
            elif item.text == "To place the meeting on the public calendar without releasing the agenda, check the box to Calendar the Meeting.":
                utils.testResults_file_x(wb, sheet,"pass",fileName, 23, 'p')
                i+=1
            elif item.text == "In order to open meeting to submitters the required fields are Title, Date, Location, and Open Session time.":
                utils.testResults_file_x(wb, sheet,"pass",fileName, 24, 'p')
            else:
                utils.testResults_file_x(wb, sheet,"fail" + " it reads: " + item.text,fileName, i, 'f')
                i+=1




        #  Add couple agenda items to thsi meeting
        #********* agenda item starts here ********************
#         for i in range(1):
#             #AGENDA ITEM
#             time.sleep(2)
#             now = datetime.datetime.now()
#             aiTitle = "ai_"+ now.strftime("%y-%m-%d %H:%M")
#             try:
#                 element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Agenda Item')]")))
#             finally:
#                 driver.find_element_by_xpath("//div[contains(text(), 'Agenda Item')]").click()
#             time.sleep(6)
#
#             try:
#                 element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.ID, "confirmServiceRequestConfirmBtn")))
#             finally:
#                 driver.find_element_by_id("confirmServiceRequestConfirmBtn").send_keys('\n')
#             time.sleep(9)
#
#             #  title
#             try:
#                 element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//paper-menu[@id='menu']/div/paper-item[2]/span")))
#             finally:
#                 driver.find_element_by_xpath("//paper-menu[@id='menu']/div/paper-item[2]/span").click()
#             time.sleep(2)
#
#             #Agenda%20Information
#             driver.find_element_by_xpath("//section[@id='Agenda%20Information']/awi-textbox/div/paper-input-container/div/div").click()
#             driver.find_element_by_xpath("//section[@id='Agenda%20Information']/awi-textbox/div/paper-input-container/div/div/input").send_keys(aiTitle)
#             time.sleep(1)
#
#             #select meeting
#             driver.find_element_by_xpath("//section[@id='Agenda%20Information']/awi-meeting-select/awi-combobox/div/paper-input-container/div/div[3]").click()
#             time.sleep(3)
#
#             try:
#                 element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//awi-combobox-overlay/div/iron-list/div/awi-combobox-item[@id='it' and contains(text(), '%s')]"%meetingTitle)))
#             finally:
#                 driver.find_element_by_xpath("//awi-combobox-overlay/div/iron-list/div/awi-combobox-item[@id='it' and contains(text(), '%s')]"%meetingTitle).click()
#             time.sleep(2)
#
#             #select workflow route
#             try:
#                 element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//section[@id='Agenda%20Information']/awi-user-route-select/awi-combobox/div[2]/paper-input-container/div/div[3]")))
#             finally:
#                 driver.find_element_by_xpath("//section[@id='Agenda%20Information']/awi-user-route-select/awi-combobox/div[2]/paper-input-container/div/div[3]").click()
#             try:
#                 element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//awi-combobox-item[contains(text(), 'No Approval Required')]")))
#             finally:
#                 driver.find_element_by_xpath("//awi-combobox-item[contains(text(), 'No Approval Required')]").click()
#             time.sleep(2)
#
#             #select type
#             for b in range(500):
#                 typeNum = random.randint(0,5)
#                 if typeNum !=2:
#                     break
#             driver.find_elements_by_xpath("//div[@id='checkboxContainer']")[typeNum].click()
#             time.sleep(1)
#
#             #Summary section
#             Summary = driver.find_element_by_xpath("//section[@id='Quick%20Summary/Abstract']/awi-editor/div/div/div/iframe")
#             driver.switch_to.frame(Summary)
#             driver.find_element_by_tag_name("body").clear()
#             driver.find_element_by_tag_name("body").send_keys("%d. -------------start of Quick Summary/Abstract section for the agenda item .....%s.....and meeting %s --------------end of Quick Summary/Abstract section for the agenda item  "%(i,aiTitle,meetingTitle))
#             time.sleep(1)
#             driver.switch_to.default_content()
#             time.sleep(1)
#
#             #Description section
#             Description = driver.find_element_by_xpath("//section[@id='Description']/awi-editor/div/div/div/iframe")
#             driver.switch_to.frame(Description)
#             driver.find_element_by_tag_name("body").clear()
#             driver.find_element_by_tag_name("body").send_keys("%d. -------------start of Description section for the agenda item ... %s.... adn meeting %s -------------end of Description section for the agenda item"%(i,aiTitle,meetingTitle))
#             time.sleep(1)
#             driver.switch_to.default_content()
#             time.sleep(1)
#
#             #Motion section
#             Motion = driver.find_element_by_xpath("//section[@id='Recommended%20Motion']/awi-editor/div/div/div/iframe")
#             driver.switch_to.frame(Motion)
#             driver.find_element_by_tag_name("body").clear()
#             driver.find_element_by_tag_name("body").send_keys("%d. -------------start of Recommended Motion section for the agenda item  ......%s....and the meeting %s-------------END of Recommended Motion section for the agenda item    "%(i, aiTitle, meetingTitle))
#             time.sleep(1)
#             driver.switch_to.default_content()
#             time.sleep(2)
#
#
#             #saveActionButton
#             try:
#                 element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.ID, "saveActionButton")))
#             finally:
#                 driver.find_element_by_id("saveActionButton").click()
#             time.sleep(9)
#
#             #Add to Agenda
#             try:
#                 element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.ID, "actionButton0")))
#             finally:
#                 driver.find_element_by_id("actionButton0").click() # does NOT work
#             time.sleep(2)
#
#             #Confirm Action
#             try:
#                 element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//submit-action[@id='submit']/paper-dialog/div[2]/div/paper-button[2]")))
#             finally:
#                 driver.find_element_by_xpath("//submit-action[@id='submit']/paper-dialog/div[2]/div/paper-button[2]").click()
#             time.sleep(8)
#
# # ********************* agenda item ends here
#
#         #  My Meetings screen, verify the 3 buttons on top
#         try:
#             element = driver.find_element_by_xpath("//div[contains(text(), 'My Meetings')]")
#         finally:
#             driver.find_element_by_xpath("//div[contains(text(), 'My Meetings')]").click()
#
#         # Active Meetings button
#         time.sleep(1)
#         try:
#             element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@id='topBar']/div/iron-selector[@id='tabs']/paper-button[@id='activeButton']")))
#         finally:
#             activeMeetings = driver.find_element_by_xpath("//div[@id='topBar']/div/iron-selector[@id='tabs']/paper-button[@id='activeButton']")
#         if activeMeetings.is_displayed():
#             utils.testResults_file_x(wb, sheet,"pass",fileName, sh, 1, 'p')
#         else:
#             utils.testResults_file_x(wb, sheet,"fail",fileName, sh, 1, 'f')
#         if activeMeetings.value_of_css_property("background-color") == "rgba(227, 119, 68, 1)":
#             utils.testResults_file_x(wb, sheet,"pass",fileName, sh, 2, 'p')
#         else:
#             utils.testResults_file_x(wb, sheet,"fail",fileName, sh, 2, 'f')
#         #if activeMeetings.value_of_css_property("color") == "rgba(255, 255, 255, 1)":
#         if activeMeetings.value_of_css_property("color") == "white":
#             utils.testResults_file_x(wb, sheet,"pass",fileName, sh, 3, 'p')
#         else:
#             utils.testResults_file_x(wb, sheet,"fail",fileName, sh, 3, 'f')
#         if activeMeetings.text == "Active Meetings":
#             utils.testResults_file_x(wb, sheet,"pass",fileName, sh, 0, 'p')
#         else:
#             utils.testResults_file_x(wb, sheet,"fail",fileName, sh, 0, 'f')
#
#         # Archived Meetings button
#         time.sleep(1)
#         try:
#             element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@id='topBar']/div/iron-selector[@id='tabs']/paper-button[@id='completedButton']")))
#         finally:
#             archiveMeetings = driver.find_element_by_xpath("//div[@id='topBar']/div/iron-selector[@id='tabs']/paper-button[@id='completedButton']")
#         if archiveMeetings.is_displayed():
#             utils.testResults_file_x(wb, sheet,"pass",fileName, sh, 5, 'p')
#         else:
#             utils.testResults_file_x(wb, sheet,"fail",fileName, sh, 5, 'f')
#         if archiveMeetings.value_of_css_property("background-color") == "rgba(255, 255, 255, 1)":
#             utils.testResults_file_x(wb, sheet,"pass",fileName, sh, 6, 'p')
#         else:
#             utils.testResults_file_x(wb, sheet,"fail",fileName, sh, 6, 'f')
#         #if activeMeetings.value_of_css_property("color") == "rgba(255, 255, 255, 1)":
#         if archiveMeetings.value_of_css_property("color") == "rgba(51, 136, 193, 1)":
#             utils.testResults_file_x(wb, sheet,"pass",fileName, sh, 7, 'p')
#         else:
#             utils.testResults_file_x(wb, sheet,"fail",fileName, sh, 7, 'f')
#         if archiveMeetings.text == "Archived Meetings":
#             utils.testResults_file_x(wb, sheet,"pass",fileName, sh, 4, 'p')
#         else:
#             utils.testResults_file_x(wb, sheet,"fail",fileName, sh, 4, 'f')
#
#         # Actions button
#         try:
#             element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@id='topBar']/div[@id='actionsButtonContainer']/paper-menu-button[@id='actionsButton']/div[@id='trigger']/paper-button")))
#         finally:
#             actions = driver.find_element_by_xpath("//div[@id='topBar']/div[@id='actionsButtonContainer']/paper-menu-button[@id='actionsButton']/div[@id='trigger']/paper-button")
#         if actions.get_attribute("disabled") == 'true':
#             utils.testResults_file_x(wb, sheet,"pass",fileName, sh, 8, 'p')
#         else:
#             utils.testResults_file_x(wb, sheet,"fail",fileName, sh, 8, 'f')
#         if actions.is_displayed():
#             utils.testResults_file_x(wb, sheet,"pass",fileName, sh, 12, 'p')
#         else:
#             utils.testResults_file_x(wb, sheet,"fail",fileName, sh, 12, 'f')
#         if actions.value_of_css_property("background-color") == "rgba(0, 0, 0, 0.07)":
#             utils.testResults_file_x(wb, sheet,"pass",fileName, sh, 10, 'p')
#         else:
#             utils.testResults_file_x(wb, sheet,"fail",fileName, sh, 10, 'f')
#         #if activeMeetings.value_of_css_property("color") == "rgba(255, 255, 255, 1)":
#         if actions.value_of_css_property("color") == "rgba(0, 0, 0, 0.40)":
#             utils.testResults_file_x(wb, sheet,"pass",fileName, sh, 11, 'p')
#         else:
#             utils.testResults_file_x(wb, sheet,"fail",fileName, sh, 11, 'f')
#         if actions.text == "Actions":
#             utils.testResults_file_x(wb, sheet,"pass",fileName, sh, 9, 'p')
#         else:
#             utils.testResults_file_x(wb, sheet,"fail",fileName, sh, 9, 'f')

#    find the meetign in the list and check its check checkbox



    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
