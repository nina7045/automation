import time, datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time, re, random
from random import randint
import xlwt
from xlutils.copy import copy
import xlrd
import xlsxwriter
import utils

def ai_Draft(driver, wb, sheet, fileName, meetingTitle, GB, GBtitle):
    sheet = wb.get_sheet('ai_Draft')

    #Get Total in My Items list  before starting a new agenda item and write to test results file
    utils.MyItems_click(driver)
    utils.spinner_wait(driver)
    totalAI = utils.getTotalNumber(driver)
    print totalAI
    #totalAI = utils.MyMeetings_Total(driver)
    utils.testResults_file_x(wb, sheet,totalAI,fileName, 24, 'p')

    #start new agenda item
    time.sleep(2)
    try:
        element = WebDriverWait(driver, 20).until( EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Start New')]")))
    finally:
        driver.find_element_by_xpath("//div[contains(text(), 'Start New')]").click()
    time.sleep(2)

    utils.spinner_wait(driver)
    try:
        element = WebDriverWait(driver, 20).until( EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Agenda Item')]")))
    finally:
        driver.find_element_by_xpath("//div[contains(text(), 'Agenda Item')]").click()
    time.sleep(3)

    #  Select a Governing BODY
    if (GBtitle != ""):
        utils.selectGoverningBody(driver, GB, GBtitle)


    try:
        element = WebDriverWait(driver, 20).until( EC.presence_of_element_located((By.ID, "confirmServiceRequestConfirmBtn")))
    finally:
        driver.find_element_by_id("confirmServiceRequestConfirmBtn").click()
    time.sleep(4)

    #Confirm Draft page
    #     Save button  verify
    utils.SaveButton_Draft_InDev_Meeting(driver, wb, sheet, fileName)

    #     Assign button verify
    utils.AssignButton_Draft_InDev_Meeting(driver, wb, sheet, fileName)

    #   Add to Agenda button verify
    utils.AddToAgendaButton_Draft_agendaItem(driver, wb, sheet, fileName)

    #   Send to Workflow button verify
    utils.SendToWorkflowButton_Draft_agendaItem(driver, wb, sheet, fileName)

    # Draft title verify
    status = utils.title_DraftMeeting(driver, wb, sheet, fileName)

    # Instructions title verify
    utils.InstructionsTitle_Draft_InDev_Meeting(driver, wb, sheet, fileName)

    #Instructions text verify
    utils.InstructionsText_Draft_agendaItem(driver, wb, sheet, fileName)

    # get the governing body title displayed on agenda item page and return it to another method, that will use it to get the GB's format
    GovBodTitle = driver.find_element_by_xpath("//div[@id='topBar']/div/task-breadcrumbs[@id='breadcrumbs']/div/div/span").text
    if (GBtitle == GovBodTitle):
        print "Governign bodies selected matches the Governign Body displayed in the breadcrumb"
    else:
        print "Governign bodies selected: " + GBtitle + " does NOT match the Governign Body displayed in the breadcrumb: " + GovBodTitle

    #print "line 65 of agenda_item : Governing body Title is " + GovBodTitle

    # get the first and last names of the initiator from the right top corner
    firstLastName = driver.find_element_by_xpath("//div[@id='topBar']/div/task-requestor/div/a[@id='userName']").text
    #print "first and last name is " + firstLastName
    time.sleep(3)

    #wait till meeting loads:
    #check for a spinner here , if spinner is on, wait

    try:
        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//paper-spinner[@id='spinner']")))
    finally:
        sp = driver.find_element_by_xpath("//paper-spinner[@id='spinner']")
    if sp.is_displayed():
        while sp.value_of_css_property("display") == "block":
            time.sleep(1)

    #---------------------------------------------------
    #can place for loop to create more than one agenda item
    #click Agenda Information link to scroll teh titel line up
    try:
        element = WebDriverWait(driver, 20).until( EC.presence_of_element_located((By.XPATH, "//div[@id='mainContainer']/div/div/awi-dynamic-navigation-menu/paper-menu[@id='menu']/div/paper-item[2]")))
    finally:
        driver.find_element_by_xpath("//div[@id='mainContainer']/div/div/awi-dynamic-navigation-menu/paper-menu[@id='menu']/div/paper-item[2]").click()
    #for i in range(100):
    i = 1
    # fil in all required fields:
    now = datetime.datetime.now()
    aiTitle = "ai_" + now.strftime("%Y-%m-%d %H:%M")

    driver.find_element_by_xpath("//section[@id='Agenda%20Information']/awi-textbox/div/paper-input-container/div/div/input").send_keys(aiTitle)
    time.sleep(1)

    #type in Select Meetign input field:
    driver.find_element_by_xpath("//awi-combobox[@id='meetingsCombobox']/div[2]/paper-input-container[@id='inputContainer']/div[2]/div[@id='labelAndInputContainer']/iron-input/input[@id='input']").send_keys(meetingTitle)
    #time.sleep(1)
    driver.find_element_by_xpath("//awi-combobox-overlay[@id='overlay']/div[2][@id='scroller']/iron-list[@id='selector']/div[@id='items']/awi-combobox-item[contains(text(), '%s')]"%meetingTitle).click()
    time.sleep(2)

    #driver.find_elements_by_xpath("//div[@id='toggleIcon']/iron-icon")[3].click()
    #driver.find_elements_by_xpath("//paper-input-container[@id='inputContainer']/div/div[3]/iron-icon").click()
    #driver.find_elements_by_xpath("//div[@id='toggleIcon']")[3].click()
    try:
        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//section[@id='Agenda%20Information']/awi-user-route-select/awi-combobox/div[2]/paper-input-container/div/div[3]")))
    finally:
        driver.find_element_by_xpath("//section[@id='Agenda%20Information']/awi-user-route-select/awi-combobox/div[2]/paper-input-container/div/div[3]").click()
    #click "No Approval required"
    try:
        element =  driver.find_element_by_xpath("//awi-combobox-overlay[@id='overlay']")
    finally:
        workflowRouteItems = driver.find_elements_by_xpath("//awi-combobox-overlay[@id='overlay']/div/iron-list/div/awi-combobox-item")
        for w in workflowRouteItems:
            if w.text == "No Approval Required":
                w.click()
                break
    time.sleep(1)

    #select type
    for b in range(500):
        typeNum = random.randint(0,5)
        if typeNum !=2:
            break

    driver.find_elements_by_xpath("//awi-checkbox/paper-checkbox[@id='checkbox']/div[@id='checkboxContainer']")[typeNum].click()
    time.sleep(1)


    #Summary section
    Summary = driver.find_element_by_xpath("//section[@id='Quick%20Summary/Abstract']/awi-editor/div/div/div/iframe")
    driver.switch_to.frame(Summary)
    driver.find_element_by_tag_name("body").clear()
    driver.find_element_by_tag_name("body").send_keys("%d. -------------start of Quick Summary/Abstract section       \n for the agenda item .....%s.....\n and meeting %s --------------end of Quick Summary/Abstract section for the agenda item  "%(i,aiTitle,meetingTitle))
    time.sleep(1)
    driver.switch_to.default_content()
    time.sleep(1)

    #Description section
    Description = driver.find_element_by_xpath("//section[@id='Description']/awi-editor/div/div/div/iframe")
    driver.switch_to.frame(Description)
    driver.find_element_by_tag_name("body").clear()
    driver.find_element_by_tag_name("body").send_keys("%d. -------------start of Description section for \n the agenda item ... %s.... adn meeting %s ------------- \n end of Description section for the agenda item"%(i,aiTitle,meetingTitle))
    time.sleep(1)
    driver.switch_to.default_content()
    time.sleep(1)

    #Motion section
    Motion = driver.find_element_by_xpath("//section[@id='Recommended%20Motion']/awi-editor/div/div/div/iframe")
    driver.switch_to.frame(Motion)
    driver.find_element_by_tag_name("body").clear()
    driver.find_element_by_tag_name("body").send_keys("%d. -------------start of Recommended Motion section for the agenda item  ......%s....and the meeting %s-------------END of Recommended Motion section for the agenda item    "%(i, aiTitle, meetingTitle))
    time.sleep(1)
    driver.switch_to.default_content()
    time.sleep(2)

    # add an attachment   does nto work as of May 16 2018

    # try:
    #     element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//paper-button[@id='addButton']")))
    # finally:
    #     driver.find_element_by_xpath("//paper-button[@id='addButton']").click()
    # time.sleep(2)
    # try:
    #     element = WebDriverWait(driver, 20).until( EC.presence_of_element_located((By.XPATH, "//paper-dialog[@id='dialog']")))
    # finally:
    #     Attachment = driver.find_element_by_xpath("//paper-dialog[@id='dialog']")
    #     driver.switch_to.frame(Attachment)
    #     #driver.find_element_by_xpath("//iron-icon[@id='upload-document']").click()
    #     driver.find_element_by_xpath("//input[@id='fileinput']").send_keys("C:\_attachments\chicken.pdf")
    #     driver.find_element_by_xpath("//input[@id='input']").send_keys("some_attachment")
    #     driver.find_element_by_xpath("//paper-dialog[@id='dialog']/div/paper-button[contains(text(), 'Save')]")

    # end of add attachment section

    #saveActionButton
    try:
        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.ID, "saveActionButton")))
    finally:
        driver.find_element_by_id("saveActionButton").click()
    time.sleep(9)
    utils.spinner_wait(driver)

    #click Agenda Information link to scroll teh titel line up
    try:
        element = WebDriverWait(driver, 20).until( EC.presence_of_element_located((By.XPATH, "//div[@id='mainContainer']/div/div/awi-dynamic-navigation-menu/paper-menu[@id='menu']/div/paper-item[2]")))
    finally:
        driver.find_element_by_xpath("//div[@id='mainContainer']/div/div/awi-dynamic-navigation-menu/paper-menu[@id='menu']/div/paper-item[2]").click()

    # trying to get back to left navigation bar
    try:
        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//confirm-service-request-selection/dynamic-task-view/paper-drawer-panel/iron-selector/div[@id='drawer']/paper-header-panel/div[@id='mainPanel']/div[@id='mainContainer']/sidebar-navigation/div/div/paper-menu[@id='sidebarNavigation']/div/sidebar-menu-item[5]/paper-item/pushstate-anchor/a/div")))
    finally:
        driver.find_element_by_xpath("//confirm-service-request-selection/dynamic-task-view/paper-drawer-panel/iron-selector/div[@id='drawer']/paper-header-panel/div[@id='mainPanel']/div[@id='mainContainer']/sidebar-navigation/div/div/paper-menu[@id='sidebarNavigation']/div/sidebar-menu-item[5]/paper-item/pushstate-anchor/a/div").click()
    time.sleep(3)

    #Get Total in My Items list  after creating a new agenda item and write to test results file
    utils.MyItems_click(driver)
    totalAI = utils.getTotalNumber(driver)
    #totalAI = utils.MyMeetings_Total(driver)
    utils.testResults_file_x(wb, sheet,str(totalAI),fileName, 25, 'p')

    return (aiTitle,GovBodTitle, status)

def ai_Post(driver, wb, sheet, fileName, meetingTitle, aiTitle):

    utils.spinner_wait(driver)
    # Meetign name is delayed to load; need to verify that its there before clickign the button
    time.sleep(2)
    try:
        element = WebDriverWait(driver, 20).until( EC.presence_of_element_located((By.ID, "actionButton1")))
    finally:
        driver.find_element_by_id("actionButton1").click()
        #print "Clickign Add to agenda"
    time.sleep(5)

    try:
        element = WebDriverWait(driver, 20).until( EC.presence_of_element_located((By.XPATH, "//paper-dialog[@id='dialog']/div[2]/div/paper-button[contains(text(), 'Ok')]")))
        #element = WebDriverWait(driver, 50).until( EC.element_to_be_clickable((By.XPATH, "//paper-dialog[@id='dialog']/div[2]/div/paper-button[contains(text(), 'Ok')]")))
        #?? not sure abotu the _visible element = WebDriverWait(driver, 50).until( EC.element_to_be_visible((By.XPATH, "//paper-dialog[@id='dialog']/div[2]/div/paper-button[contains(text(), 'Ok')]")))
    finally:
        driver.find_element_by_xpath("//paper-dialog[@id='dialog']/div[2]/div/paper-button[contains(text(), 'Ok')]").click()
        #element = WebDriverWait(driver, 50).until( EC.element_to_be_clickable((By.XPATH, "//paper-dialog[@id='dialog']/div[2]/div/paper-button[contains(text(), 'Ok')]"))).click()

    time.sleep(5)
    #print "agenda item is now posted"

def ai_add(driver, meetingName, ais, GB, GBtitle):
    try:
        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//a/div[contains(text(), 'Start New')]")))
    finally:
        driver.find_element_by_xpath("//div[contains(text(), 'Start New')]").click()


    for i in range(1, ais):
        #AGENDA ITEM
        time.sleep(2)
        # textRand = random.randint(0,10)
        # if textRand == 5:
        #     textToType = ""

        now = datetime.datetime.now()
        aiTitle = "ai_"+ now.strftime("%y-%m-%d %H:%M")
        try:
            element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Agenda Item')]")))
        finally:
            driver.find_element_by_xpath("//div[contains(text(), 'Agenda Item')]").click()
        time.sleep(5)

        # # SELECT GOVERNING BODY:
        if (GBtitle != ""):
            utils.selectGoverningBody(driver, GB, GBtitle)

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

        #type in Select Meetign input field:
        driver.find_element_by_xpath("//awi-combobox[@id='meetingsCombobox']/div[2]/paper-input-container[@id='inputContainer']/div/div[@id='labelAndInputContainer']/iron-input/input[@id='input']").send_keys(meetingName)
        #select meetign from drop-down list
        try:
            element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//awi-combobox-overlay/div/iron-list/div/awi-combobox-item[@id='it' and contains(text(), '%s')]"%meetingName)))
        finally:
            driver.find_element_by_xpath("//awi-combobox-overlay/div/iron-list/div/awi-combobox-item[@id='it' and contains(text(), '%s')]"%meetingName).click()

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

        # for b in range(500):
        #     typeNum = random.randint(0,5)
        #     if typeNum !=2:
        #         break
        # closed session is included in selection
        typeNum = random.randint(0,5)
        #driver.find_elements_by_xpath("//div[@id='checkboxContainer']")[random.randint(3,5)].click()
        driver.find_elements_by_xpath("//div[@id='checkboxContainer']")[typeNum].click()
        time.sleep(1)
        if typeNum == 2:
            closedSessionReason = random.randint(1,9)
            #driver.find_element_by_xpath("//div[@id='labelAndInputContainer']/iron-input/input[@id='input']").click()
            driver.find_element_by_xpath("//section[@id='Agenda%20Information']/awi-combobox/div[2]/paper-input-container[@id='inputContainer']/div[2]/div[@id='toggleIcon']/iron-icon").click()
            time.sleep(1)
            driver.find_element_by_xpath("//awi-combobox-overlay[@id='overlay']/div[@id='scroller']/iron-list[@id='selector']/div[@id='items']/awi-combobox-item[%d]"%closedSessionReason).click()

        #Summary section
        Summary = driver.find_element_by_xpath("//section[@id='Quick%20Summary/Abstract']/awi-editor/div/div/div/iframe")
        driver.switch_to.frame(Summary)
        driver.find_element_by_tag_name("body").clear()
        #driver.find_element_by_tag_name("body").send_keys("%d. -------------start of Quick Summary/Abstract section for the agenda item .....%s.....and meeting %s : %s --------------end of Quick Summary/Abstract section  "%(i,aiTitle,meetingName,textToType))
        driver.find_element_by_tag_name("body").send_keys("%d. -------------start of Quick Summary/Abstract section \n for the agenda item .....%s.....\n and meeting %s :  \n--------------end of Quick Summary/Abstract section  "%(i,aiTitle,meetingName))
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
        time.sleep(8)

        #Add to Agenda
        try:
            #element = WebDriverWait(driver, 20).until( EC.presence_of_element_located((By.ID, "actionButton1")))
            element = WebDriverWait(driver, 50).until( EC.element_to_be_clickable((By.ID, "actionButton1")))
        finally:
            driver.find_element_by_id("actionButton1").click() # does NOT work

        time.sleep(2)
        #driver.implicitly_wait(5)

        #Confirm Action
        #driver.find_element_by_xpath("//paper-dialog[@id='dialog']/div[2]/div/paper-button[2]").click() #does NOT work
        try:
            element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//submit-action[@id='submit']/paper-dialog/div[2]/div/paper-button[2]")))
        finally:
            driver.find_element_by_xpath("//submit-action[@id='submit']/paper-dialog/div[2]/div/paper-button[2]").click()
        time.sleep(7)
