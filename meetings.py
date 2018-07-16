import time, datetime
from datetime import date
from dateutil.relativedelta import relativedelta
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time, re, random
from random import randint
import xlwt
from xlutils.copy import copy
import xlrd
import xlwt
import xlsxwriter
import utils

def m_Draft(driver, wb, sheet, fileName, GB, GBtitle):
    sheet = wb.get_sheet('m_Draft')

    #Get Total in My Meetngs list  before startign a new meeting adn write to test results file
    utils.MyMeetings_click(driver)
    # shoudl i clean blank meeting s here?
    #totalM = utils.MyMeetings_Total(driver)
    totalM = utils.getTotalNumber(driver)
    print totalM
    try:
        if (int(totalM) > 30):
            utils.meetingDelete(driver,totalM)
            totalM = utils.getTotalNumber(driver)
    except ValueError, e:
        print "error", e

    utils.testResults_file_x(wb, sheet,str(totalM),fileName, 30, 'p')

    #  click start new
    time.sleep(2)
    try:
        element = WebDriverWait(driver, 20).until( EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Start New')]")))
    finally:
        driver.find_element_by_xpath("//div[contains(text(), 'Start New')]").click()
    time.sleep(2)

    utils.spinner_wait(driver)

    # select Meeting in Start New
    try:
        element = WebDriverWait(driver, 20).until( EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Meeting')]")))
    finally:
        driver.find_element_by_xpath("//div[contains(text(), 'Meeting')]").click()
    time.sleep(4)

    # select Governing Body
    if (GB == 1):
        GBtitle = utils.selectGoverningBody(driver, GB, GBtitle)
    else:
        GBtitle = ""

    # click Next to get to Draft new meeting page
    try:
        #element = WebDriverWait(driver, 20).until( EC.presence_of_element_located((By.ID, "confirmServiceRequestConfirmBtn")))
        element = WebDriverWait(driver, 50).until( EC.element_to_be_clickable((By.ID, "confirmServiceRequestConfirmBtn")))
    finally:
        driver.find_element_by_id("confirmServiceRequestConfirmBtn").click()
    time.sleep(4)

    #check for a spinner here , if spinner is on, wait
    utils.spinner_wait(driver)
    # try:
    #     element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//paper-spinner[@id='spinner']")))
    # finally:
    #     sp = driver.find_element_by_xpath("//paper-spinner[@id='spinner']")
    # if sp.is_displayed():
    #     while sp.value_of_css_property("display") == "block":
    #         print "spinning..."
    #         time.sleep(1)

    #Confirm Draft page
    #     Save button  verify
    utils.SaveButton_Draft_InDev_Meeting(driver, wb, sheet, fileName)

    #     Assign button verify
    utils.AssignButton_Draft_InDev_Meeting(driver, wb, sheet, fileName)

    #   Cancel Meeting button verify  ; button removed May 22 2018, replaced by Delete button
    #utils.CancelMeetingButton_Draft_InDev_Meeting(driver, wb, sheet, fileName)

    #   Delete button verify
    utils.DeleteMeetingButton_Draft_InDev_Meeting(driver, wb, sheet, fileName)

    #   Open MEETING button verify
    utils.OpenMeetingButton_DraftMeeting(driver, wb, sheet, fileName)

    # Draft title verify
    utils.title_DraftMeeting(driver, wb, sheet, fileName)

    # Instructions title verify
    utils.InstructionsTitle_Draft_InDev_Meeting(driver, wb, sheet, fileName)

    #Instructions text verify
    #utils.InstructionsText_Draft_Meeting(driver, wb, sheet, fileName)
    utils.InstructionsText_Meeting(driver, wb, sheet, fileName)


    # get the first and last names of the initiator from the right top corner
    firstLastName = driver.find_element_by_xpath("//div[@id='topBar']/div/task-requestor/div/a[@id='userName']").text
    #print "first and last name is " + firstLastName
    time.sleep(2)
    #check for a spinner here , if spinner is on, wait
    # if driver.find_element_by_xpath("//div[@id='backdrop']"):
    #     while driver.find_element_by_xpath("//div[@id='backdrop']"):
    #         time.sleep(1)
    try:
        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//paper-spinner[@id='spinner']")))
    finally:
        sp = driver.find_element_by_xpath("//paper-spinner[@id='spinner']")
    if sp.is_displayed():
        while sp.value_of_css_property("display") == "block":
            time.sleep(1)

    #---------------------------------------------------

    #click "Meetign Information" link to scroll Meetign Title line up
    try:
        element = WebDriverWait(driver, 20).until( EC.presence_of_element_located((By.XPATH, "//paper-menu[@id='menu']/div/paper-item[2]")))
        #element = driver.find_element_by_xpath("//div[contains(text(), 'Meeting')]")
    finally:
        driver.find_element_by_xpath("//paper-menu[@id='menu']/div/paper-item[2]").click()
    time.sleep(1)

    # fil in all required fields:
    now = datetime.datetime.now()
    meetingTitle = "m_" + now.strftime("%Y-%m-%d %H:%M")
    # driver.find_elements_by_xpath("//input[@id='input']")[4].send_keys(meetingTitle)
    time.sleep(1)
    try:
        element = WebDriverWait(driver, 20).until( EC.presence_of_element_located((By.XPATH, "//div[@id='labelAndInputContainer']/input[@id='input']")))
    finally:
        driver.find_element_by_xpath("//div[@id='labelAndInputContainer']/input[@id='input']").send_keys(meetingTitle)
    time.sleep(1)
    #set a date 3 months from today
    #driver.find_elements_by_xpath("//input[@id='input']")[5].send_keys("Apr 30 2018")
    # driver.find_elements_by_xpath("//input[@id='input']")[5].send_keys(now.strftime('%b %d %Y'))
    # time.sleep(1)
    try:
        element = WebDriverWait(driver, 20).until( EC.presence_of_element_located((By.XPATH, "//div[@id='labelAndInputContainer']/input[@id='input']")))
    finally:
        driver.find_element_by_xpath("//section[@id='Meeting%20Information']/awi-datepicker/paper-input[@id='input']/paper-input-container/div/div[@id='labelAndInputContainer']/input").send_keys(now.strftime('%b %d %Y'))
    time.sleep(1)

    #driver.find_elements_by_xpath("//input[@id='input']")[6].send_keys("1:21 PM")
    #driver.find_elements_by_xpath("//input[@id='input']")[6].send_keys(now.strftime("%I:%M %p"))
    try:
        element = WebDriverWait(driver, 20).until( EC.presence_of_element_located((By.XPATH, "//div[@id='labelAndInputContainer']/input[@id='input']")))
    finally:
        driver.find_element_by_xpath("//section[@id='Meeting%20Information']/awi-time-picker/paper-input[@id='input']/paper-input-container/div[2]/div[@id='labelAndInputContainer']/input").send_keys(now.strftime("%I:%M %p"))
    time.sleep(1)

    # location
    #driver.find_elements_by_xpath("//input[@id='input']")[8].send_keys("location " + meetingTitle)
    try:
        element = WebDriverWait(driver, 20).until( EC.presence_of_element_located((By.XPATH, "//div[@id='labelAndInputContainer']/input[@id='input']")))
    finally:
        driver.find_element_by_xpath("//section[@id='Meeting%20Information']/awi-textbox[2]/div/paper-input-container/div/div[@id='labelAndInputContainer']/input").send_keys("location " + meetingTitle)
    time.sleep(1)


    driver.find_elements_by_xpath("//div[@id='toggleIcon']/iron-icon")[2].click()
    #click "No Approval required"
    try:
        element =  driver.find_element_by_xpath("//awi-combobox-overlay[@id='overlay']")
    finally:
        workflowRouteItems = driver.find_elements_by_xpath("//awi-combobox-overlay[@id='overlay']/div/iron-list/div/awi-combobox-item")
        for w in workflowRouteItems:
            if w.text == "No Approval Required":
                #wfPlan = w.text
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
    utils.spinner_wait(driver)
    time.sleep(3)
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
    n = datetime.datetime.now()
    privateNote = "Typing some text !!!.........." + n.strftime("%m%d_%H%M")
    driver.find_element_by_xpath("//paper-dialog[@id='dialog']/div[2]/textarea[@id='input']").send_keys(privateNote)
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
    #print "typedText is ..." + typedText
    if typedText == privateNote:
        utils.testResults_file_x(wb, sheet,"pass",fileName, 29, 'p')
    else:
        utils.testResults_file_x(wb, sheet,"fail" + typedText ,fileName, 29, 'f')

    time.sleep(2)

    # trying to get back to left navigation bar
    #driver.find_element_by_xpath("//div[@id='task-main-section']").click()
    try:
        #element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//avocado-frame/awi-app/main-container[@id='mainContainer']/app-router[@id='router']/app-route[15]/confirm-service-request-selection/dynamic-task-view/paper-drawer-panel/iron-selector/div[@id='drawer']/paper-header-panel/div[@id='mainPanel']/div[@id='mainContainer']/sidebar-navigation/div/div/paper-menu[@id='sidebarNavigation']/div/sidebar-menu-item[5]/paper-item/pushstate-anchor/a/div")))
        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//confirm-service-request-selection/dynamic-task-view/paper-drawer-panel/iron-selector/div[@id='drawer']/paper-header-panel/div[@id='mainPanel']/div[@id='mainContainer']/sidebar-navigation/div/div/paper-menu[@id='sidebarNavigation']/div/sidebar-menu-item[5]/paper-item/pushstate-anchor/a/div")))
    finally:
        #driver.find_element_by_xpath("//avocado-frame/awi-app/main-container[@id='mainContainer']/app-router[@id='router']/app-route[15]/confirm-service-request-selection/dynamic-task-view/paper-drawer-panel/iron-selector/div[@id='drawer']/paper-header-panel/div[@id='mainPanel']/div[@id='mainContainer']/sidebar-navigation/div/div/paper-menu[@id='sidebarNavigation']/div/sidebar-menu-item[5]/paper-item/pushstate-anchor/a/div").click()
        #driver.find_element_by_xpath("//awi-app/main-container[@id='mainContainer']/app-router[@id='router']/app-route[15]/confirm-service-request-selection/dynamic-task-view/paper-drawer-panel/iron-selector/div[@id='drawer']/paper-header-panel/div[@id='mainPanel']/div[@id='mainContainer']/sidebar-navigation/div/div/paper-menu[@id='sidebarNavigation']/div/sidebar-menu-item[5]/paper-item/pushstate-anchor/a/div").click()
        driver.find_element_by_xpath("//confirm-service-request-selection/dynamic-task-view/paper-drawer-panel/iron-selector/div[@id='drawer']/paper-header-panel/div[@id='mainPanel']/div[@id='mainContainer']/sidebar-navigation/div/div/paper-menu[@id='sidebarNavigation']/div/sidebar-menu-item[5]/paper-item/pushstate-anchor/a/div").click()
    time.sleep(2)

    # My Meetings screen, Get Total, compare; find the new meetign, verify Status
    utils.MyMeetings_click(driver)
    #totalM = utils.MyMeetings_Total(driver)
    totalM = utils.getTotalNumber(driver)
    utils.testResults_file_x(wb, sheet,str(totalM),fileName, 31, 'p')

    l = len( driver.find_elements_by_xpath("//div[@id='items']/awi-grid-row"))
    i=1
    for i in range (len(driver.find_elements_by_xpath("//div[@id='items']/awi-grid-row"))):
        if (i != 0):
            #meeting and its status:
            meeting = driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell/div/span"%str(i)).text
            # find the new meeting and verify its status
            if meeting == meetingTitle:
                utils.testResults_file_x(wb, sheet,"pass: " + meetingTitle + " is found in the list",fileName, 25, 'p')
                status = driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell[6]/div/span"%str(i)).text
                if status == "Draft":
                    utils.testResults_file_x(wb, sheet,"pass",fileName, 26, 'p')
                else:
                    utils.testResults_file_x(wb, sheet,"fail" + " the status is " + status,fileName, 26, 'f')
                m_assignedTo = driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell[7]/div/span"%str(i)).text
                if m_assignedTo == firstLastName:
                    utils.testResults_file_x(wb, sheet,"pass" + " is assigned to the initiator of the meeting, who is " + m_assignedTo ,fileName, 27, 'p')
                else:
                    utils.testResults_file_x(wb, sheet,"fail" + " not assigned to the initiator of the meeting; The initiator is " + firstLastName + " and Assigned to is " + m_assignedTo,fileName, 26, 'f')
    return (meetingTitle, GBtitle)

def m_InDev(driver, wb, sheet, fileName, meetingT):
    sheet = wb.get_sheet('m_InDev')
    time.sleep(3)
    #click on the Draft meeting
    for i in range (1, len(driver.find_elements_by_xpath("//div[@id='items']/awi-grid-row"))):
        #print "line 149 ................ i is" + str(i)
        meeting = driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell/div/span"%str(i)).text
        print " line 286 meetings.py meetign is " + meeting
        if meeting == meetingT:
            driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell/div/span"%str(i)).click()
            print "the meeting is found and clicked!"
            break
    time.sleep(3)

    utils.spinner_wait(driver)
    # click the Open Meeting button
    try:
        #element = WebDriverWait(driver, 20).until( EC.presence_of_element_located((By.ID, "actionButton1")))
        #element = driver.find_element_by_id("actionButton1")
        element = WebDriverWait(driver, 20).until( EC.presence_of_element_located((By.ID, "actionButton0")))
    finally:
        #driver.find_element_by_id("actionButton1").click()
        driver.find_element_by_id("actionButton0").click()
    time.sleep(3)

    try:
        element = driver.find_element_by_xpath("//paper-dialog[@id='dialog']/div[2]/div/paper-button[contains(text(), 'Ok')]")
    finally:
        driver.find_element_by_xpath("//paper-dialog[@id='dialog']/div[2]/div/paper-button[contains(text(), 'Ok')]").click()

    time.sleep(5)

    #refresh My Meeting spage
    utils.MyMeetings_click(driver)
    #print "line 172 after refreshing My Meetings page"
    #verify the In Dev state
    try:
        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@id='items']/awi-grid-row")))
    finally:
        leng = len(driver.find_elements_by_xpath("//div[@id='items']/awi-grid-row"))
    for i in range (len(driver.find_elements_by_xpath("//div[@id='items']/awi-grid-row"))):
        if (i != 0):
            meeting = driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell/div/span"%str(i)).text
            if meeting == meetingT:
                status = driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell[6]/div/span"%str(i)).text
                if status == "In Development":
                    utils.testResults_file_x(wb, sheet,"pass " + status,fileName, 25, 'p')
                else:
                    utils.testResults_file_x(wb, sheet,"fail" + " the status is " + status,fileName, 25, 'f')
                #click on the meeting
                driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell/div/span"%str(i)).click()
                time.sleep(3)
                break

    #verify the In Dev page:

    #     Save button  verify
    utils.SaveButton_Draft_InDev_Meeting(driver, wb, sheet, fileName)

    #     Assign button
    time.sleep(1)
    utils.AssignButton_Draft_InDev_Meeting(driver, wb, sheet, fileName)

    #   Cancel Meeting
    time.sleep(1)
    #utils.CancelMeetingButton_Draft_InDev_Meeting(driver, wb, sheet, fileName)

    #   Delete button verify
    utils.DeleteMeetingButton_Draft_InDev_Meeting(driver, wb, sheet, fileName)

    #   Close MEETING
    time.sleep(1)
    utils.CloseMeetingButton_InDev_Meeting(driver, wb, sheet, fileName)

    # In Development title
    time.sleep(1)
    utils.title_InDevMeeting(driver, wb, sheet, fileName)

    # Instructions title verify
    time.sleep(1)
    utils.InstructionsTitle_Draft_InDev_Meeting(driver, wb, sheet, fileName)

    #Instructions text
    time.sleep(1)
    utils.InstructionsText_InDev_Meeting(driver, wb, sheet, fileName)

def meeting_ai(driver, wb, sheet, fileName, meetingTitle, aiTitle, gb_formatChar, status):
    sheet = wb.get_sheet('ai_m')
    utils.spinner_wait(driver)
    # get the numbering from GB formatting to use it to verify the agenda item's numbering
    #*******************************************************
    #if there are multiple governign bodies
    # first get the governing body from teh meetign page; done in agenda_item page when creating it
    #GovBod = driver.find_element_by_xpath("//div[@id='topBar']/div/task-breadcrumbs[@id='breadcrumbs']/div/div/span").text
    # second get thsi governing body format by going to the utils.GoverningBodies
    # gb_format = utils.GoverningBodies(driver, GovBod)
    # print "line 347  in master:::::: this is teh governign body format " + gb_format
    #
    # if gb_format != "":
    #     # get the first numbering from teh format
    #     fn = gb_format[12]
    #     print "line 353 of meetings.py , gettign the char from teh format, that should be in ai numbering: " + fn
    # else: fn = ""
    #*************************************************

    time.sleep(2)
    utils.MyMeetings_click(driver)
    utils.MyMeetings_blanksDelete(driver)
    time.sleep(2)

    #select the meeting in My Meetings
    try:
        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@id='items']/awi-grid-row")))
    finally:
        element = driver.find_element_by_xpath("//div[@id='items']/awi-grid-row")

    time.sleep(2)
    print " The meetign needed is " + meetingTitle
    print('length is', len(driver.find_elements_by_xpath("//div[@id='items']/awi-grid-row")))
    testRange = range(1, len(driver.find_elements_by_xpath("//div[@id='items']/awi-grid-row")))
    print('length of ', testRange, ' is ', len(driver.find_elements_by_xpath("//div[@id='items']/awi-grid-row")))
    for i in range (len(driver.find_elements_by_xpath("//div[@id='items']/awi-grid-row"))):
        #if (i != 0):
        i=i+1
        print driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell/div/span"%str(i)).text
        if meetingTitle == driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell/div/span"%str(i)).text:
            print "meeting clicked"
            driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell/div/span"%str(i)).click()
            break

    time.sleep(3)

    #wait till meeting loads:
    #check for a spinner here , if spinner is on, wait
    utils.spinner_wait(driver)
    # try:
    #     element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//paper-spinner[@id='spinner']")))
    # finally:
    #     sp = driver.find_element_by_xpath("//paper-spinner[@id='spinner']")
    # if sp.is_displayed():
    #     while sp.value_of_css_property("display") == "block":
    #         time.sleep(1)

    #---------------------------------------------------

    #  agenda item link click to get to agenda items tree
    #print "***************AGENDA ITEM IN A MEETING ********** below"
    # click Agenda Items link on meeting page
    try:
        element = WebDriverWait(driver, 30).until( EC.presence_of_element_located((By.XPATH, "//paper-menu[@id='menu']/div/paper-item[3]/span")))
    finally:
        driver.find_element_by_xpath("//paper-menu[@id='menu']/div/paper-item[3]/span").click()
    time.sleep(2)

    # set numbers to write into the test results file depending on whether it is Draft or Posted ai
    if status == "DRAFT":
        print "Drafted ai"
        aiT = 1
        aiC = 2
        aiCol = "rgb(170, 170, 170)"
        aiN = 3
        aiS = 4
        aiSh = "rgba(177, 189, 174, 0.5)"
    else:
        print "Posted ai"
        aiT = 7
        aiC = 8
        aiCol = "rgb(9, 194, 0)"
        aiN = 9
        aiS = 10
        aiSh = "rgba(0, 0, 0, 0.87)"

    #find the agenda items tree with nodes; if theer is no node, means no agenda items
    try:
        element = WebDriverWait(driver, 30).until( EC.presence_of_element_located((By.XPATH, "//section[@id='Agenda%20Items']/awi-agenda-view/awi-agenda-tree/items-node")))
    finally:
        element = driver.find_element_by_xpath("//section[@id='Agenda%20Items']/awi-agenda-view/awi-agenda-tree/items-node")

    if element:
    # for loop is not needed, since theer is onyl one agenda item at this point
    #for i in range (1, len(driver.find_elements_by_xpath("//section[@id='Agenda%20Items']/awi-agenda-view/awi-agenda-tree/items-node"))+1):
        #if (i != 0):
        #print "line 230, aiTitle is transferred from agenda_items.py and is %s"%aiTitle
        #read the agenda item's title , displayed
        #ai = driver.find_element_by_xpath("//section/awi-agenda-view/awi-agenda-tree/items-node[%s]/div/items-pane/div/div[2]/div/span[@id='_title']/a"%str(i)).text
        ai = driver.find_element_by_xpath("//section/awi-agenda-view/awi-agenda-tree/items-node/div/items-pane/div/div[2]/div/span[@id='_title']/a").text
        #print "the ai is in the ai tree on the meetign page and its title  is " + ai
        #match teh displayed agend aitem text with the item that was started earlier
        if ai == aiTitle:
            #print "displayed agenda item's title  match"
            utils.testResults_file_x(wb, sheet, "pass", fileName, aiT, 'p')
        else:
            utils.testResults_file_x(wb, sheet, "fail", fileName, aiT, 'f')
        #get the color of the horizontal line of Drafted agenda item
        #posted agenda item should be  gray "#AAAAAA"
        ai_color = driver.find_element_by_xpath("//section/awi-agenda-view/awi-agenda-tree/items-node/div/items-pane/div/div[2]/span[@id='_gutter']")
        #if ai_color.value_of_css_property("background") == "rgb(170, 170, 170)":
        if ai_color.value_of_css_property("background").find(aiCol) == -1:
            #print "teh horizontal line color of this drafted ai is NOT rgb(170, 170, 170) - gray, it is " + ai_color.value_of_css_property("background")
            utils.testResults_file_x(wb, sheet, "fail - horizontal line is not expected color", fileName, aiC, 'f')
        else:
            utils.testResults_file_x(wb, sheet, "pass", fileName, aiC, 'p')

        #get the numbering only if GB is not empty
        ai_number = driver.find_element_by_xpath("//section/awi-agenda-view/awi-agenda-tree/items-node/div/items-pane/div/div[2]/span[2]").text
        # if Fn is not empty
        if gb_formatChar != "":
            if ai_number == gb_formatChar:
                utils.testResults_file_x(wb, sheet, "pass", fileName, aiN, 'p')
            else:
                utils.testResults_file_x(wb, sheet, "fail", fileName, aiN, 'f')
        else:
            utils.testResults_file_x(wb, sheet, "fail - dont have access to GB", fileName, aiN, 'f')
        # if no access ot GB to get its format, get the char displayed here and use it in future tests, is kept in ai_number


        #get the 3 dots menu color
        ai_shelveMenu = driver.find_element_by_xpath("//section/awi-agenda-view/awi-agenda-tree/items-node/div/items-pane/div/div[2]/div[@id='_menu']/paper-menu-button[@id='_menuButton']/div[@id='trigger']/paper-icon-button")
        #gray colors pf 3 dots: rgba(177,189,174,0.5) - for Draft agenda item
        #black color for 3 dots: rgba(0,0,0,0.87) - for Posted agenda item
        if ai_shelveMenu.value_of_css_property("color") == aiSh:
            #print "the displayed color is rgba(177,189,174,0.5), which is gray color for Draft items "
            utils.testResults_file_x(wb, sheet, "pass", fileName,aiS, 'p')
        else:
            #print "the displayed color is NOT rgba(177,189,174,0.5), gray color for Draft, instead this color is shown " + ai_shelveMenu.value_of_css_property("color")
            utils.testResults_file_x(wb, sheet, "fail - 3 dots are not grey color", fileName, aiS, 'f')

    #------------------------------------------------------------
    time.sleep(2)
    print "about to click this Draft agenda item "
    # click the agenda item
    if status == "DRAFT":
        print "about about to click this agenda item  with status == " + status
        try:
            element = WebDriverWait(driver, 30).until( EC.presence_of_element_located((By.XPATH, "//section/awi-agenda-view/awi-agenda-tree/items-node/div/items-pane/div/div[2]/div/span[@id='_title']/a")))
        finally:
            driver.find_element_by_xpath("//section/awi-agenda-view/awi-agenda-tree/items-node/div/items-pane/div/div[2]/div/span[@id='_title']/a[contains(text(),'%s')]"%aiTitle).click()
    time.sleep(3)
    return ai_number

def m_Appr(driver, wb, sheet, fileName, meetingT):
    sheet = wb.get_sheet('ai_mAppr')
    time.sleep(2)

    utils.MyMeetings_click(driver)
    time.sleep(3)
    #click on the meeting
    for i in range (1, len(driver.find_elements_by_xpath("//div[@id='items']/awi-grid-row"))):
        #print "line 149 ................ i is" + str(i)
        #if (i != 0):
        meeting = driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell/div/span"%str(i)).text
        if meeting == meetingT:
            driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell/div/span"%str(i)).click()
            #print "the meeting is found and clicked!"
            break
    time.sleep(3)
    utils.spinner_wait(driver)

    # click the Close Meeting button
    try:
        #element = WebDriverWait(driver, 20).until( EC.presence_of_element_located((By.ID, "actionButton1")))
        #element = driver.find_element_by_id("actionButton1")
        element = WebDriverWait(driver, 30).until( EC.presence_of_element_located((By.ID, "actionButton0")))
    finally:
        #driver.find_element_by_id("actionButton1").click()
        driver.find_element_by_id("actionButton0").click()
    time.sleep(3)

    try:
        element = driver.find_element_by_xpath("//paper-dialog[@id='dialog']/div[2]/div/paper-button[contains(text(), 'Ok')]")
    finally:
        driver.find_element_by_xpath("//paper-dialog[@id='dialog']/div[2]/div/paper-button[contains(text(), 'Ok')]").click()

    time.sleep(5)

    #refresh My Meeting spage
    utils.MyMeetings_click(driver)
    #print "line 172 after refreshing My Meetings page"
    #verify the Approved state
    try:
        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@id='items']/awi-grid-row")))
    finally:
        leng = len(driver.find_elements_by_xpath("//div[@id='items']/awi-grid-row"))
    for i in range (1, len(driver.find_elements_by_xpath("//div[@id='items']/awi-grid-row"))):
        meeting = driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell/div/span"%str(i)).text
        if meeting == meetingT:
            status = driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell[6]/div/span"%str(i)).text
            if status == "Approved":
                utils.testResults_file_x(wb, sheet,"pass " + status,fileName, 30, 'p')
            else:
                utils.testResults_file_x(wb, sheet,"fail" + " the status is " + status,fileName, 30, 'f')
            #click on the meeting
            driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell/div/span"%str(i)).click()
            time.sleep(3)
            break

    #verify the Approved page:

    #     Save button  verify
    utils.SaveButton_Draft_InDev_Meeting(driver, wb, sheet, fileName)

    #     Assign button
    time.sleep(1)
    utils.AssignButton_Draft_InDev_Meeting(driver, wb, sheet, fileName)

    #   Cancel Meeting removed
    time.sleep(1)
    #utils.CancelMeetingButton_Draft_InDev_Meeting(driver, wb, sheet, fileName)

    #   Delete button verify
    utils.DeleteMeetingButton_Draft_InDev_Meeting(driver, wb, sheet, fileName)

    #   Move to In Development button
    time.sleep(1)
    utils.actionButton0_toolBar(driver, wb, sheet, fileName)

    # Publish Meeting button
    time.sleep(1)
    utils.actionButton1_toolBar(driver, wb, sheet, fileName)

    # Approved title
    time.sleep(1)
    meetingStatusTitle = utils.title_Meeting(driver, wb, sheet, fileName)

    # Instructions title verify
    time.sleep(1)
    utils.InstructionsTitle_Meeting(driver, wb, sheet, fileName)

    #Instructions text
    time.sleep(1)
    utils.InstructionsText_Meeting(driver, wb, sheet, fileName)

def m_Publish(driver, wb, sheet, fileName, meetingT):
    sheet = wb.get_sheet('m_Publish')
    time.sleep(2)

    # click Publish Meeting button
    try:
        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@id='topBar']/div[2]/paper-button")))
    finally:
        driver.find_element_by_xpath("//div[@id='topBar']/div[2]/paper-button").click()
    time.sleep(3)

    try:
        element = driver.find_element_by_xpath("//paper-dialog[@id='dialog']/div[2]/div/paper-button[contains(text(), 'Ok')]")
    finally:
        driver.find_element_by_xpath("//paper-dialog[@id='dialog']/div[2]/div/paper-button[contains(text(), 'Ok')]").click()
    t0 = time.time()
    time.sleep(5)

    utils.MyMeetings_click(driver)
    time.sleep(2)
    utils.spinner_wait(driver)

    # find teh meetign in the list and get its status, wait when Publishing Meetign changes to Published, get time when Published
    try:
        element = WebDriverWait(driver, 20).until( EC.presence_of_element_located((By.XPATH, "//div[@id='items']/awi-grid-row")))
    finally:
        el = driver.find_element_by_xpath("//div[@id='items']/awi-grid-row")

    for i in range (1, len(driver.find_elements_by_xpath("//div[@id='items']/awi-grid-row"))):
        meeting = driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell/div/span"%str(i)).text
        if meeting == meetingT:
            publishing = driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell[6]/div/span"%str(i)).text
            #print "the meeting's status is " + publishing
            while (publishing == "Publishing Meeting"):
                utils.MyMeetings_click(driver)
                time.sleep(2)
                utils.spinner_wait(driver)
                publishing = driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell[6]/div/span"%str(i)).text
            t1 = time.time()
            #driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell/div/span"%str(i)).click()   # if its published click on it; but sometimes
            #the i changes after the meetign gets Published; thats why it must get out of thsi loop and start another one
            break;
            time.sleep(3)

    publishTime = t1 - t0
    print publishTime
    utils.testResults_file_x(wb, sheet,publishTime,fileName, 31, 'p')

    # click on the Published meeting - find it in the list first
    utils.MyMeetings_click(driver)
    time.sleep(2)
    utils.spinner_wait(driver)

    for i in range (1, len(driver.find_elements_by_xpath("//div[@id='items']/awi-grid-row"))):
        meeting = driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell/div/span"%str(i)).text
        print meeting
        print meetingT
        if meeting == meetingT:
            print "foudn th emeeting??????"
            status = driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell[6]/div/span"%str(i)).text
            if (status == "Published"):
                print "is th estatus published???"
                driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell/div/span"%str(i)).click()
                break;
        # else:
        #     # click Status column and go thru the meetings again
        #     driver.find_element_by_xpath("//div[@id='topBar']/awi-grid-header-cell[6]").click()
        #     time.sleep(1)
        #     for i in range (1, len(driver.find_elements_by_xpath("//div[@id='items']/awi-grid-row"))):
        #         meeting = driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell/div/span"%str(i)).text
        #         print meeting
        #         print meetingT
        #         if meeting == meetingT:
        #             print "clicked Status column and lookign again .... found the meeting  yet??????"
        #             status = driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell[6]/div/span"%str(i)).text
        #             if (status == "Published"):
        #                 print "is th estatus published???"
        #                 driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell/div/span"%str(i)).click()
        #                 break;
    time.sleep(3)

    # verify Published page
    #     Save button  verify
    utils.SaveButton_Meeting(driver, wb, sheet, fileName)

    #     Assign button verify
    utils.AssignButton_Meeting(driver, wb, sheet, fileName)

    #    Regenerate Meeting Report button
    utils.RegenReportButton(driver, wb, sheet, fileName)

    #   Cancel Meeting button
    utils.CancelMeetingButton(driver, wb, sheet, fileName)

    #   Start Meeting button
    utils.StartMeetingButton(driver, wb, sheet, fileName)

    # Published title verify
    utils.title_Meeting(driver, wb, sheet, fileName)

    # Instructions title verify
    utils.InstructionsTitle_Meeting(driver, wb, sheet, fileName)

    #Instructions text verify
    utils.InstructionsText_Meeting(driver, wb, sheet, fileName)

    # count agenda items in the meeting
    i = 0
    agendaItems = driver.find_elements_by_xpath("//section[@id='Agenda%20Items']/awi-agenda-view/awi-agenda-tree/items-node")
    utils.testResults_file_x(wb, sheet,str(len(agendaItems)),fileName, 32, 'p')

    #  Agenda Outline Report  and Board Packet Report links
    utils.reportsLinks(driver, wb, sheet, fileName)

    #  count Attachments
    utils.attachments(driver, wb, sheet, fileName)

def m_InProgress(driver, wb, sheet, fileName, meetingT):
    sheet = wb.get_sheet('m_InProgress')
    time.sleep(2)

    # click Start Meeting button
    try:
        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@id='topBar']/div[3]/paper-button")))
    finally:
        driver.find_element_by_xpath("//div[@id='topBar']/div[3]/paper-button").click()
    time.sleep(3)

    try:
        element = WebDriverWait(driver, 20).until( EC.presence_of_element_located((By.XPATH, "//paper-dialog[@id='dialog']/div[2]/div/paper-button[contains(text(), 'Ok')]")))
    finally:
        driver.find_element_by_xpath("//paper-dialog[@id='dialog']/div[2]/div/paper-button[contains(text(), 'Ok')]").click()
    time.sleep(5)

    # click My Meetings and verify the meetings status is "Meeting in Progress"
    utils.MyMeetings_click(driver)

    # find teh meetign in the list and get its status
    for i in range (1, len(driver.find_elements_by_xpath("//div[@id='items']/awi-grid-row"))):
        meeting = driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell/div/span"%str(i)).text
        if meeting == meetingT:
            status = driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell[6]/div/span"%str(i)).text
            if (status == "Meeting In Progress"):
                utils.testResults_file_x(wb, sheet,"pass",fileName, 0, 'p')
            else:
                utils.testResults_file_x(wb, sheet,"fail - status is" + status,fileName, 0, 'f')
            break;
            time.sleep(3)

    # click Meetings In Progress and verify the meetings status is "Meeting in Progress", click on it
    try:
        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//paper-drawer-panel/iron-selector/div[@id='drawer']/paper-header-panel/div[@id='mainPanel']/div[@id='mainContainer']/sidebar-navigation/div/div/paper-menu[@id='sidebarNavigation']/div/sidebar-menu-item[7]/paper-item/pushstate-anchor")))
    finally:
        driver.find_element_by_xpath("//paper-drawer-panel/iron-selector/div[@id='drawer']/paper-header-panel/div[@id='mainPanel']/div[@id='mainContainer']/sidebar-navigation/div/div/paper-menu[@id='sidebarNavigation']/div/sidebar-menu-item[7]/paper-item/pushstate-anchor/a").click()
    time.sleep(2)

    # find teh meetign in the list and get its status
    for i in range (1, len(driver.find_elements_by_xpath("//div[@id='items']/awi-grid-row"))):
        print str(i)
        meeting = driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell/div/span"%str(i)).text
        print meeting + "  " + meetingT
        if (meeting == meetingT):
            status = driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell[6]/div/span"%str(i)).text
            print status
            if (status == "Meeting In Progress"):
                print status
                utils.testResults_file_x(wb, sheet,"pass",fileName, 1, 'p')
                driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell/div/span"%str(i)).click()
                break;
            else:
                utils.testResults_file_x(wb, sheet,"fail - status is" + status,fileName, 1, 'f')
                break;
    time.sleep(3)

    # Meeting In Progress page, verify .....

    #  Meetign In Progress title
    try:
        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@id='contentContainer']/app-toolbar/div")))
    finally:
        mProgressT = driver.find_element_by_xpath("//div[@id='contentContainer']/app-toolbar/div").text
    time.sleep(1)

    if (mProgressT == "Meeting in Progress - " + meetingT):
        utils.testResults_file_x(wb, sheet,"pass",fileName, 2, 'p')
    else:
        utils.testResults_file_x(wb, sheet,"fail: " + mProgressT,fileName, 2, 'f')

    #  Stop Meeting buttons
    utils.StopMeeting_button(driver, wb, sheet, fileName)

    # verify Start Broadcasting, Take Attendance and Make Leader buttons
    buttons = ["broadcast", "attendance", "leader"]
    for b in buttons:
        utils.MInProgress_buttons(driver, wb, sheet, fileName, b)

    #  verify Closing Information section

    #  Agenda Outline Report and Board Packet Report links
    rLinks = ["outline", "packet"]
    for r in rLinks:
        utils.reportsLinks_InProgress(driver, wb, sheet, fileName, r)

    #  verify Preliminary and Closing Information section
    sections = ["preliminary", "closing"]
    for s in sections:
        utils.sections_InProgress(driver, wb, sheet, fileName, s)

    # count items in the list
    items = driver.find_elements_by_tag_name("items-node")
    print len(items)
    utils.testResults_file_x(wb, sheet,str(len(items)),fileName, 23, 'n')

    #  if there is an attachment , the paper clip icon should be blue; if not - gray
