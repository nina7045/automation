import time, datetime
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
from selenium.common.exceptions import NoSuchElementException

def login(driver, wb, sheet, fileName,loginName, password, selectOrg, GB):

    driver.find_element_by_id("Username").click()
    driver.find_element_by_id("Username").clear()
    driver.find_element_by_id("Username").send_keys(loginName)
    driver.find_element_by_name("Password").click()
    driver.find_element_by_name("Password").clear()
    driver.find_element_by_name("Password").send_keys(password)
    driver.find_element_by_id("submit_button").click()
    time.sleep(4)

    # verify Select Organization, if any and select one
    try:
        element = WebDriverWait(driver, 50).until( EC.presence_of_element_located((By.XPATH, "//paper-dialog[@id='select-organization']")))
    finally:
        selectOrganization = driver.find_element_by_xpath("//paper-dialog[@id='select-organization']")

    # while (!selectOrganization):
    #     time.sleep(3)
    #     selectOrganization = driver.find_element_by_xpath("//paper-dialog[@id='select-organization']")

    if selectOrganization.is_displayed():
        testResults_file_x(wb, sheet,"pass",fileName, 0, 'p')
        try:
            #element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//paper-dialog[@id='select-organization']/div[2]/paper-listbox/paper-item/div/div/span[contains(text(), '%s')]"%selectOrganization)))
            #element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'testPremium')]")))
            #element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.NAME, "//paper-dialog[@id='select-organization']/div[2]/paper-listbox/paper-item[@name='%s']"%selectOrg)))
            #element = WebDriverWait(driver, 5).until( EC.presence_of_element_located((By.NAME, "paper-item[@name='%s']"%selectOrg)))
            element = WebDriverWait(driver, 50).until( EC.presence_of_element_located((By.XPATH, "//paper-dialog[@id='select-organization']/div[2]/paper-listbox/paper-item[@name='%s']"%selectOrg)))
        finally:
            driver.find_element_by_xpath("//paper-dialog[@id='select-organization']/div[2]/paper-listbox/paper-item/div/div/span[contains(text(), '%s')]"%selectOrg).click()
            #driver.find_element_by_xpath("//span[contains(text(), 'testPremium')]").click()
            #driver.find_element_by_xpath('//span[contains(text(), "%s")]'%selectOrganization).click()
            #driver.find_element_by_name("//paper-dialog[@id='select-organization']/div[2]/paper-listbox/paper-item[@name='%s']"%selectOrg).click()
            #driver.find_element_by_name("//paper-item[@name='%s']"%selectOrg).click()
            #element.click()
            #driver.find_element_by_xpath("//paper-dialog[@id='select-organization']/div[2]/paper-listbox/paper-item[@name='%s']"%selectOrg).click()
            time.sleep(2)
    else:
        testResults_file_x(wb, sheet,"one organization for this user",fileName, 0, 'f')



def testResults_file(text,fileName):
    #, r, c
    #n = datetime.datetime.now()
    #fileName ="meetingDraft_" + n.strftime("%m%d_%H%M")
    f = open("testResults/"+fileName,"a+")
    f.write(text)
    f.close()

def testResults_file_x(wb, sheet, text, fileName, r, pf):
    #, r, c

    #book = xlwt.Workbook()
    #sheet = book.add_sheet(sh)
    #book.save(fileName + '.xlsx')

    #rb = xlrd.open_workbook('testResults.xlsx')
    #wb = copy(rb)
    #sheet = wb.get_sheet(sh)

    #xlwt.add_palette_colour("pas", 0x21)
    #wb.set_colour_RGB(0x21, 251, 228, 228)
    #wb.set_colour_RGB(0x21, 96, 247, 72)   #pass
    #styleP = xlwt.easyxf('pattern: pattern solid, fore_colour 0x21')
    #sheet.write(5,1, 'pass', styleP)
    #wb.set_colour_RGB(0x21, 247, 72, 130)
    #styleF = xlwt.easyxf('pattern: pattern solid, fore_colour 0x21')
    #sheet.write(6,1, 'fail', styleF)


    styleP = xlwt.XFStyle()
    pattern = xlwt.Pattern()
    pattern.pattern = xlwt.Pattern.SOLID_PATTERN
    pattern.pattern_fore_colour = xlwt.Style.colour_map['green']
    styleP.pattern = pattern

    styleF = xlwt.XFStyle()
    pattern = xlwt.Pattern()
    pattern.pattern = xlwt.Pattern.SOLID_PATTERN
    pattern.pattern_fore_colour = xlwt.Style.colour_map['red']
    styleF.pattern = pattern

    styleN = xlwt.XFStyle()
    pattern = xlwt.Pattern()
    pattern.pattern = xlwt.Pattern.SOLID_PATTERN
    pattern.pattern_fore_colour = xlwt.Style.colour_map['pale_blue']
    styleN.pattern = pattern

    if pf=='p':
        sheet.write(r,1, text, styleP)
    elif pf=='f':
        sheet.write(r,1, text, styleF)
    else:
        sheet.write(r,1, text, styleN)

    #cell_format_set_font_color('red')
    #fail = wb.add_format({'bg_color': '#FF4833'})
    #if r=='p':
        #sheet.set_row(r, cell_format=pas)
    #else:
        #sheet.set_row(r, cell_format=fail)
    #sheet.write(r, c, text)
    wb.save("testResults/" + fileName + '.xls')

def meetingsTotal(driver, fileName):
    try:
        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'My Meetings')]")))
    finally:
        driver.find_element_by_xpath("//div[contains(text(), 'My Meetings')]").click()
        try:
            element = driver.find_element_by_xpath("//div[@id='topBar']/div")
        finally:
            if driver.find_element_by_xpath("//div[@id='topBar']/div").text == "My Meetings":
                time.sleep(2)
                try:
                    #element = driver.find_element_by_xpath("//div[@id='topBar']/div[1]/span[contains(text(), 'Total items:')]")
                    element = driver.find_element_by_xpath("//span[contains(text(), 'Total items:')]")
                finally:
                    #print driver.find_element_by_xpath("//div[@id='topBar']/div[1]/span[contains(text(), 'Total items:')]").text
                    #mTotal = driver.find_element_by_xpath("//div[@id='topBar']/div[1]/span[contains(text(), 'Total items:')]").text
                    mTotal = driver.find_element_by_xpath("//span[contains(text(), 'Total items:')]").text
                    return mTotal

def MyMeetings_meetingStatus(driver, meetingTitle, fileName):
    try:
        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'My Meetings')]")))
    finally:
        driver.find_element_by_xpath("//div[contains(text(), 'My Meetings')]").click()
    time.sleep(2)
    try:
        element = driver.find_element_by_xpath("//div[@id='topBar']/div")
    finally:
        if driver.find_element_by_xpath("//div[@id='topBar']/div").text == "My Meetings":
            for i in range (len(driver.find_elements_by_xpath("//div[@id='items']/awi-grid-row"))):
                if (i != 0):
                    #meting and its status:
                    meeting = driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell/div/span"%str(i)).text
                    # this is how to get status:   driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell[6]/div/span"%str(i)).text
                    # find the new meeting and verify its status and Assigned to values
                    if meeting == meetingTitle:
                        utils.testResults_file_x(wb, sheet,"pass: " + meetingTitle + " is found in the list",fileName, sh, 25, 'p')
                        status = driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell[6]/div/span"%str(i)).text
                        if status == "Draft":
                            #utils.testResults_file(meeting + "is found in My Meetings list" + "\r\n", fileName)
                            utils.testResults_file_x(wb, sheet,"pass",fileName, sh, 26, 'p')
                        else:
                            #utils.testResults_file("the new meeting is not in Draft state" + "\r\n", fileName)
                            utils.testResults_file_x(wb, sheet,"fail" + " the status is " + status,fileName, sh, 26, 'f')
                        # Assigned To value
                        assignedTo = driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell[7]/div/span"%str(i)).text
                        if assignedTo == userNameslist[1]:
                            utils.testResults_file_x(wb, sheet,"pass",fileName, sh, 27, 'p')
                        else:
                            utils.testResults_file_x(wb, sheet,"fail" + " AssignedTo is " + assignedTo,fileName, sh, 27, 'f')

def MyMeetings_click(driver):
    spinner_wait(driver)
    try:
        #element = driver.find_element_by_xpath("//paper-menu[@id='sidebarNavigation']/div/sidebar-menu-item[5]/paper-item/pushstate-anchor/a/div")
        #element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//avocado-frame/awi-app/main-container[@id='mainContainer']/app-router[@id='router']/app-route[15]/confirm-service-request-selection/dynamic-task-view/paper-drawer-panel/iron-selector/div[@id='drawer']/paper-header-panel/div[@id='mainPanel']/div[@id='mainContainer']/sidebar-navigation/div/div/paper-menu[@id='sidebarNavigation']/div/sidebar-menu-item[5]/paper-item/pushstate-anchor")))
        #element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//paper-menu[@id='sidebarNavigation']/div/sidebar-menu-item[5]/paper-item/pushstate-anchor")))
        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//paper-drawer-panel/iron-selector/div[@id='drawer']/paper-header-panel/div[@id='mainPanel']/div[@id='mainContainer']/sidebar-navigation/div/div/paper-menu[@id='sidebarNavigation']/div/sidebar-menu-item[5]/paper-item/pushstate-anchor")))
        #element = driver.find_element_by_xpath("//avocado-frame/awi-app/main-container[@id='mainContainer']/app-router[@id='router']/app-route[15]/confirm-service-request-selection/dynamic-task-view/paper-drawer-panel/iron-selector/div[@id='drawer']/paper-header-panel/div[@id='mainPanel']/div[@id='mainContainer']/sidebar-navigation/div/div/paper-menu[@id='sidebarNavigation']/div/sidebar-menu-item[5]/paper-item/pushstate-anchor/a/div")
    finally:
        #print "got into here???????????????/ MyMeetings_click() here"
        #driver.find_element_by_xpath("//avocado-frame/awi-app/main-container[@id='mainContainer']/app-router[@id='router']/app-route[15]/confirm-service-request-selection/dynamic-task-view/paper-drawer-panel/iron-selector/div[@id='drawer']/paper-header-panel/div[@id='mainPanel']/div[@id='mainContainer']/sidebar-navigation/div/div/paper-menu[@id='sidebarNavigation']/div/sidebar-menu-item[5]/paper-item/pushstate-anchor/a/div").click()
        #driver.find_element_by_xpath("//body/avocado-frame/awi-app/main-container[@id='mainContainer']/app-router[@id='router']/app-route[15]/confirm-service-request-selection/dynamic-task-view/paper-drawer-panel/iron-selector/div[@id='drawer']/paper-header-panel/div[@id='mainPanel']/div[@id='mainContainer']/sidebar-navigation/div/div/paper-menu[@id='sidebarNavigation']/div/sidebar-menu-item[5]").click()
        # t0 = time.time()
        # for t in range(0,10000):
        # t1 = time.time()
        driver.find_element_by_xpath("//paper-drawer-panel/iron-selector/div[@id='drawer']/paper-header-panel/div[@id='mainPanel']/div[@id='mainContainer']/sidebar-navigation/div/div/paper-menu[@id='sidebarNavigation']/div/sidebar-menu-item[5]/paper-item/pushstate-anchor/a").click()
        #driver.find_element_by_xpath("//paper-drawer-panel/iron-selector/div[@id='drawer']/paper-header-panel/div[@id='mainPanel']/div[@id='mainContainer']/sidebar-navigation/div/div/paper-menu[@id='sidebarNavigation']/div/sidebar-menu-item[5]").click()
        #driver.find_element_by_xpath("//avocado-frame/awi-app/main-container[@id='mainContainer']/app-router[@id='router']/app-route[15]/confirm-service-request-selection/dynamic-task-view/paper-drawer-panel/iron-selector/div[@id='drawer']/paper-header-panel/div[@id='mainPanel']/div[@id='mainContainer']/sidebar-navigation/div/div/paper-menu[@id='sidebarNavigation']/div/sidebar-menu-item[5]/paper-item/pushstate-anchor/a/div").click()
        #time.sleep(2)
        #driver.find_element_by_xpath("//paper-menu[@id='sidebarNavigation']/div/sidebar-menu-item[5]/paper-item/pushstate-anchor/a").click()
        #driver.find_element_by_xpath("//paper-menu[@id='sidebarNavigation']/div/sidebar-menu-item[5]/paper-item/pushstate-anchor/a/div").click()
    time.sleep(3)

def meetingDelete(driver, totalM):
    temp = 0
    r=0
    meetingDeleted = 'none'
    while (totalM > 30):
        while (temp == r):
            r = randint(1, 10)
        time.sleep(2)
        #print r
        # nned to click Status column ot mix the list up
        driver.find_element_by_xpath("//div[@id='topBar']/awi-grid-header-cell[6]").click()

        #check a check box
        try:
            element = driver.find_element_by_xpath("//paper-checkbox[@id='checkbox']/div[@id='checkboxContainer']")
            #element = WebDriverWait(driver, 155).until(EC.presence_of_element_located((By.XPATH, "//awi-grid-row[%d]/div/paper-checkbox[@id='checkbox']/div[@id='checkboxContainer']"%r)))
            #element = WebDriverWait(driver, 155).until(EC.element_to_be_clickable((By.XPATH, "//awi-grid-row[%d]/div/paper-checkbox[@id='checkbox']/div[@id='checkboxContainer']"%r)))
            #element = driver.find_element_by_xpath("//awi-grid-row[%d]/div/paper-checkbox[@id='checkbox']/div[@id='checkboxContainer']"%r)
        finally:
            driver.find_element_by_xpath("//awi-grid-row[%d]/div/paper-checkbox[@id='checkbox']/div[@id='checkboxContainer']"%r).click()
        time.sleep(1)

        meetingDeleted = driver.find_element_by_xpath("//awi-grid-row[%d]/awi-grid-cell/div/span"%r).text


        #click Actions button
        try:
            element = driver.find_element_by_xpath("//div[@id='topBar']/div/paper-menu-button[@id='actionsButton']/div[@id='trigger']/paper-button")
        finally:
            driver.find_element_by_xpath("//div[@id='topBar']/div/paper-menu-button[@id='actionsButton']/div[@id='trigger']/paper-button").click()
        time.sleep(2)

        # select Delete Meeting
        try:
            #element = driver.find_element_by_xpath("//div[@id='actionsButtonContainer']/paper-menu-button/iron-dropdown[@id='dropdown']/div[@id='contentWrapper']/div/paper-listbox/paper-item[contains(text(), 'Delete Meeting')]")
            element = driver.find_element_by_xpath("//paper-menu-button[@id='actionsButton']/iron-dropdown[@id='dropdown']/div[@id='contentWrapper']/div/paper-listbox/paper-item[4]")
        finally:
            #driver.find_element_by_xpath("//div[@id='actionsButtonContainer']/paper-menu-button/iron-dropdown[@id='dropdown']/div[@id='contentWrapper']/div/paper-listbox/paper-item[contains(text(), 'Delete Meeting')]").click()
            driver.find_element_by_xpath("//paper-menu-button[@id='actionsButton']/iron-dropdown[@id='dropdown']/div[@id='contentWrapper']/div/paper-listbox/paper-item[4]").click()
        time.sleep(1)

        # click Delete button on pop up
        try:
            element = driver.find_element_by_xpath("//paper-dialog[@id='deleteMeetingModal']/div/paper-button[contains(text(), 'Delete')]")
        finally:
            driver.find_element_by_xpath("//paper-dialog[@id='deleteMeetingModal']/div/paper-button[contains(text(), 'Delete')]").click()
        time.sleep(2)

        # if a meeting cannot be deleted, click Cancel to remove the pop up
        while driver.find_element_by_xpath("//paper-dialog[@id='deleteMeetingModal']/paper-toolbar/div[@id='topBar']/div/h2").text != "":
            #print driver.find_element_by_xpath("//paper-dialog[@id='deleteMeetingModal']/paper-toolbar/div[@id='topBar']/div/h2").text
            #print "waiting for the meetign to be deleted"
            if driver.find_element_by_xpath("//avocado-frame/awi-app/awi-notify[@id='notify']/paper-toast[@id='toastError']/span[@id='label']"):
                #print driver.find_element_by_xpath("//avocado-frame/awi-app/awi-notify[@id='notify']/paper-toast[@id='toastError']/span[@id='label']").text
                if driver.find_element_by_xpath("//avocado-frame/awi-app/awi-notify[@id='notify']/paper-toast[@id='toastError']/span[@id='label']").text == "This Meeting cannot be deleted since it contains Agenda Items that are not yet Posted.":
                    # click Cancel to remove the Delete Meeting pop up
                    try:
                        element = driver.find_element_by_xpath("//paper-dialog[@id='deleteMeetingModal']/div/paper-button[contains(text(), 'Cancel')]")
                    finally:
                        driver.find_element_by_xpath("//paper-dialog[@id='deleteMeetingModal']/div/paper-button[contains(text(), 'Cancel')]").click()
                    time.sleep(2)

        # wait for the message to pop up:
        time.sleep(2)
        try:
            element = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "//avocado-frame/awi-app/awi-notify[@id='notify']/paper-toast")))
        finally:
            print "meetign deleted message poped up"
            time.sleep(1)
            if element.text == "Meeting has been successfully deleted.":
                #time.sleep(1)
                print "meetign is deleted , line 211 at utils"
            else:
                print "there is somethign else here line 217 at utils"
            #element = WebDriverWait(driver, 55).until(EC.presence_of_element_located((By.XPATH, "//avocado-frame/awi-app/awi-notify[@id='notify']/paper-toast[@id='toastInfo']/span[@id='label']")))

        #if error message pops up:
        # try:
        #     element = driver.find_element_by_xpath("//avocado-frame/awi-app/awi-notify[@id='notify']/paper-toast[@id='toastError']/span[@id='label']")
        # finally:
        #     #if driver.find_element_by_xpath("//avocado-frame/awi-app/awi-notify[@id='notify']/paper-toast").get_attribute('id').find('Error') > 0:
        #     if (driver.find_element_by_xpath("//avocado-frame/awi-app/awi-notify[@id='notify']/paper-toast[@id='toastError']/span[@id='label']") and driver.find_element_by_xpath("//avocado-frame/awi-app/awi-notify[@id='notify']/paper-toast[@id='toastError']/span[@id='label']").text == "This Meeting cannot be deleted since it contains Agenda Items that are not yet Posted."):
        #         time.sleep(3)
        #         print "found the error - cannot delete this meeting"
        #         # click Cancel to remove the Delete Meeting pop up
        #         try:
        #             element = driver.find_element_by_xpath("//paper-dialog[@id='deleteMeetingModal']/div/paper-button[contains(text(), 'Cancel')]")
        #         finally:
        #             driver.find_element_by_xpath("//paper-dialog[@id='deleteMeetingModal']/div/paper-button[contains(text(), 'Cancel')]").click()
        #         time.sleep(3)

        temp = r
        time.sleep(2)
        mTotal = driver.find_element_by_xpath("//span[contains(text(), 'Total items:')]").text
        totalM= int(mTotal[(mTotal.find(': ')+1):].strip())
    return meetingDeleted

def workFlowRoute(driver,wfPlan):
    wfPlan = "Sub, Bu"
    userNameslist = []

    # click Admin
    element = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH,"//paper-menu[@id='sidebarNavigation']/div/sidebar-menu-item[8]/paper-item/pushstate-anchor/a/div[contains(text(), 'Admin')]"))
    )
    time.sleep(1)
    try:
        #element = driver.find_element_by_xpath("//avocado-frame/awi-app/main-container[@id='mainContainer']/app-router[@id='router']/app-route[15]/confirm-service-request-selection/dynamic-task-view/paper-drawer-panel/iron-selector/div[@id='drawer']/paper-header-panel/div[@id='mainPanel']/div[@id='mainContainer']/sidebar-navigation/div/div/paper-menu[@id='sidebarNavigation']/div/sidebar-menu-item[8]/paper-item/pushstate-anchor/a/div")
        element = driver.find_element_by_xpath("//paper-menu[@id='sidebarNavigation']/div/sidebar-menu-item[8]/paper-item/pushstate-anchor/a/div[contains(text(), 'Admin')]")
    finally:
        #driver.find_element_by_xpath("//avocado-frame/awi-app/main-container[@id='mainContainer']/app-router[@id='router']/app-route[15]/confirm-service-request-selection/dynamic-task-view/paper-drawer-panel/iron-selector/div[@id='drawer']/paper-header-panel/div[@id='mainPanel']/div[@id='mainContainer']/sidebar-navigation/div/div/paper-menu[@id='sidebarNavigation']/div/sidebar-menu-item[8]/paper-item/pushstate-anchor/a/div").click()
        driver.find_element_by_xpath("//paper-menu[@id='sidebarNavigation']/div/sidebar-menu-item[8]/paper-item/pushstate-anchor/a/div[contains(text(), 'Admin')]").click()
    time.sleep(2)

    # Workflow routes Click
    driver.find_element_by_xpath("//div[@id='mainContainer']/div/div[4]/div/paper-toolbar/div[@id='topBar']/a/span").click()
    time.sleep(2)

    # number of lines in Workflow Routes list
    routesLength = driver.find_elements_by_xpath("//div[@id='items']/awi-grid-row")
    for rl in range (len(driver.find_elements_by_xpath("//div[@id='items']/awi-grid-row"))):
        if (rl != 0):
            # print driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell[2]/div/span"%str(rl)).text
            # find a workflow route from the list and click on it
            if driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell[2]/div/span"%str(rl)).text == wfPlan:
                driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell/div/span"%str(rl)).click()
                time.sleep(1)
                # get names of all users in the selected workflow route
                users = driver.find_elements_by_xpath("//paper-dialog[@id='editRouteDialog']/div/div[2]/div[2]/awi-grid[@id='usersGrid']/div/div/div/iron-list[@id='list']/div[@id='items']/awi-grid-row/awi-grid-cell[2]/div/span")
                for u in users:
                    userNameslist.append(u.text)
                #nextUserName = driver.find_element_by_xpath("//paper-dialog[@id='editRouteDialog']/div/div[2]/div[2]/awi-grid[@id='usersGrid']/div/div/div/iron-list[@id='list']/div[@id='items']/awi-grid-row/awi-grid-cell[2]/div/span").text
                #print "line 137 here , and nextUserName is " + nextUserName
                #userNameslist.append(nextUserName)
    # Cancel
    driver.find_element_by_xpath("//paper-dialog[@id='editRouteDialog']/div[2]/paper-button").click()
    #print "lists length is " + str(len(userNameslist))
    return userNameslist

def GoverningBodies(driver, GovBod):

    # there might be one GB or multiple
    # if one - get it
    # if multiple - get a random and work with it only

    # click Admin
    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,"//paper-menu[@id='sidebarNavigation']/div/sidebar-menu-item[8]/paper-item/pushstate-anchor/a/div[contains(text(), 'Admin')]")))
    time.sleep(1)
    try:
        element = WebDriverWait(driver, 30).until( EC.presence_of_element_located((By.XPATH, "//paper-drawer-panel/iron-selector/div[@id='drawer']/paper-header-panel/div[@id='mainPanel']/div[@id='mainContainer']/sidebar-navigation/div/div/paper-menu[@id='sidebarNavigation']/div/sidebar-menu-item[8]/paper-item/pushstate-anchor")))
    finally:
        #driver.find_element_by_xpath("//avocado-frame/awi-app/main-container[@id='mainContainer']/app-router[@id='router']/app-route[15]/confirm-service-request-selection/dynamic-task-view/paper-drawer-panel/iron-selector/div[@id='drawer']/paper-header-panel/div[@id='mainPanel']/div[@id='mainContainer']/sidebar-navigation/div/div/paper-menu[@id='sidebarNavigation']/div/sidebar-menu-item[8]/paper-item/pushstate-anchor/a/div").click()
        driver.find_element_by_xpath("//paper-menu[@id='sidebarNavigation']/div/sidebar-menu-item[8]/paper-item/pushstate-anchor/a/div[contains(text(), 'Admin')]").click()
    time.sleep(2)

    # Governing Bodies Click; if it is just a regular manager, they may not have access to GB; check if GB is there
    paneTitle = driver.find_element_by_xpath("//div[@id='mainContainer']/div/div[2]/div/paper-toolbar/div[@id='topBar']/a/span").text

    if paneTitle == "Governing Bodies":
        #print "Governing Body is available"
        driver.find_element_by_xpath("//div[@id='mainContainer']/div/div[2]/div/paper-toolbar/div[@id='topBar']/a/span").click()
        time.sleep(2)

        # number of lines in Governing Bodies list
        gbLength = len(driver.find_elements_by_xpath("//div[@id='items']/awi-grid-row"))

        # go thru each line and find required governing body
        for i in range (1, gbLength+1):
            gb = driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell/div/span"%str(i)).text
            if gb == GovBod:
                driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell/div/span"%str(i)).click()
                time.sleep(2)

            # get format of the governing body
            try:
                element = WebDriverWait(driver, 20).until( EC.presence_of_element_located((By.XPATH, "//paper-dialog[@id='editGoverningBodiesModal']/div/awi-combobox[@id='numberingScheme']")))
            finally:
                driver.find_element_by_xpath("//paper-dialog[@id='editGoverningBodiesModal']/div/awi-combobox[@id='numberingScheme']/div[2]/paper-input-container[@id='inputContainer']/div[2]/div[@id='labelAndInputContainer']/iron-input/input[@id='input']").click()
            fList = driver.find_elements_by_xpath("//paper-dialog[@id='editGoverningBodiesModal']/div/awi-combobox[@id='numberingScheme']/awi-combobox-overlay[@id='overlay']/div[@id='scroller']/iron-list[@id='selector']/div[@id='items']/awi-combobox-item[@id='it']")
            #print "its text is " + driver.find_element_by_xpath("//paper-dialog[@id='editGoverningBodiesModal']/div/awi-combobox[@id='numberingScheme']/awi-combobox-overlay[@id='overlay']/div[@id='scroller']/iron-list[@id='selector']/div[@id='items']/awi-combobox-item[3]").text
            for fl in fList:
                #print fl.text
                #print fl.value_of_css_property("color")
                if fl.value_of_css_property("color") == "rgba(51, 136, 193, 1)":
                    format = fl.text
                    #print "!!!!!!!!!!!!!!!!! here is the format " + format
                    break

            # click anywhere , here is on the text field, to get rid of the drop-down
            try:
                element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//paper-dialog[@id='editGoverningBodiesModal']/div/awi-textarea[2]")))
            finally:
                driver.find_element_by_xpath("//paper-dialog[@id='editGoverningBodiesModal']/div/awi-textarea[2]/div[@id='content']/div/paper-input-container/div/div[@id='labelAndInputContainer']/iron-autogrow-textarea[@id='input']/div/textarea[@id='textarea']").click()

            # click CANCEL
            try:
                element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//paper-dialog[@id='editGoverningBodiesModal']/div[2]/paper-button[2]")))
            finally:
                driver.find_element_by_xpath("//paper-dialog[@id='editGoverningBodiesModal']/div[2]/paper-button[2]").click()


            # extract the first char from the format and return it
            fn = format[12]
            return fn
    else:
        return " "

def MyMeetings_Total(driver):
    #get the column's name;
    try:
        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@id='topBar']/awi-grid-header-cell")))
    finally:
        columnName = driver.find_element_by_xpath("//div[@id='topBar']/awi-grid-header-cell/span[@id='column-name']").text
    #print "column name is " + columnName + "...........line 422"
    #  delete blank meetings:
    if (columnName == 'Meeting Name' or columnName == 'Meeting Title'):    ## changed from Meetign Title July3, 2018 , v 1.37
        MyMeetings_blanksDelete(driver)
        try:
            #element = driver.find_element_by_xpath("//span[contains(text(), 'Total items:')]")
            element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Total items:')]")))
        finally:
            mTotal = driver.find_element_by_xpath("//span[contains(text(), 'Total items:')]").text
            mTotal1= mTotal[(mTotal.find(': ')+1):].strip()
            time.sleep(1)

            return int(mTotal1)
    else:
        MyItems_blanksDelete(driver)
        #print "MyMeetings_Total line 436"
        try:
            element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//awi-grid[@id='tasksListMy']/div/paper-header-panel")))
        finally:
            el = driver.find_element_by_xpath("//awi-grid[@id='tasksListMy']/div/paper-header-panel")

def getTotalNumber(driver):
    try:
        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@id='topBar']/div")))
    finally:
        title = driver.find_element_by_class_name('title').text

    if (title == "My Items" or title == "My Meetings"):
        try:
            element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@id='topBar']/div[3]/span[contains(text(), 'Total items:')]")))
        finally:
            totalText = driver.find_element_by_xpath("//div[@id='topBar']/div[3]/span").text
        #print totalText
        if (totalText):
            totalN = totalText[(totalText.find(': ')+1):].strip()
            time.sleep(1)
            #print totalN
            return totalN
        else:
            return 0


def SaveButton_Draft_InDev_Meeting(driver, wb, sheet, fileName):
    #check for a spinner here , if spinner is on, wait
    try:
        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//paper-spinner[@id='spinner']")))
    finally:
        sp = driver.find_element_by_xpath("//paper-spinner[@id='spinner']")
    if sp.is_displayed():
        while sp.value_of_css_property("display") == "block":
            print "spinning..."
            time.sleep(1)
    try:
        element = WebDriverWait(driver, 20).until( EC.presence_of_element_located((By.XPATH, "//div[@id='topBar']/paper-button[@id='saveActionButton']")))
    finally:
        saveButton = driver.find_element_by_xpath("//div[@id='topBar']/paper-button[@id='saveActionButton']")
    if saveButton.is_displayed():
        testResults_file_x(wb, sheet,"pass",fileName, 1, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 1, 'f')
    if saveButton.value_of_css_property("background-color") == "rgba(255, 255, 255, 1)":
        testResults_file_x(wb, sheet,"pass",fileName, 2, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 2, 'f')
    if saveButton.value_of_css_property("color") == "rgba(51, 136, 193, 1)":
        testResults_file_x(wb, sheet,"pass",fileName, 3, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 3, 'f')
    if saveButton.text == "SAVE":
        testResults_file_x(wb, sheet,"pass",fileName, 0, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 0, 'f')

def SaveButton_Meeting(driver, wb, sheet, fileName):
    #check for a spinner here , if spinner is on, wait
    spinner_wait(driver)

    try:
        element = WebDriverWait(driver, 20).until( EC.presence_of_element_located((By.XPATH, "//div[@id='topBar']/paper-button[@id='saveActionButton']")))
    finally:
        saveButton = driver.find_element_by_xpath("//div[@id='topBar']/paper-button[@id='saveActionButton']")
    if saveButton.is_displayed():
        testResults_file_x(wb, sheet,"pass",fileName, 1, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 1, 'f')
    if saveButton.value_of_css_property("background-color") == "rgba(255, 255, 255, 1)":
        testResults_file_x(wb, sheet,"pass",fileName, 2, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 2, 'f')
    if saveButton.value_of_css_property("color") == "rgba(51, 136, 193, 1)":
        testResults_file_x(wb, sheet,"pass",fileName, 3, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 3, 'f')
    if saveButton.text == "SAVE":
        testResults_file_x(wb, sheet,"pass",fileName, 0, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 0, 'f')

def AssignButton_Draft_InDev_Meeting(driver, wb, sheet, fileName):
    time.sleep(1)
    try:
        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@id='topBar']/paper-button[@id='assignActionButton']")))
    finally:
        assignButton = driver.find_element_by_xpath("//div[@id='topBar']/paper-button[@id='assignActionButton']")
    if assignButton.is_displayed():
        testResults_file_x(wb, sheet,"pass",fileName, 5, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 5, 'f')
    if assignButton.value_of_css_property("background-color") == "rgba(255, 255, 255, 1)":
        testResults_file_x(wb, sheet,"pass",fileName, 6, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 6, 'f')
    if assignButton.value_of_css_property("color") == "rgba(51, 136, 193, 1)":
        testResults_file_x(wb, sheet,"pass",fileName, 7, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 7, 'f')
    if assignButton.text == "ASSIGN":
        testResults_file_x(wb, sheet,"pass",fileName, 4, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 4, 'f')

def AssignButton_Meeting(driver, wb, sheet, fileName):
    time.sleep(1)
    try:
        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@id='topBar']/paper-button[@id='assignActionButton']")))
    finally:
        assignButton = driver.find_element_by_xpath("//div[@id='topBar']/paper-button[@id='assignActionButton']")
    if assignButton.is_displayed():
        testResults_file_x(wb, sheet,"pass",fileName, 5, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 5, 'f')
    if assignButton.value_of_css_property("background-color") == "rgba(255, 255, 255, 1)":
        testResults_file_x(wb, sheet,"pass",fileName, 6, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 6, 'f')
    if assignButton.value_of_css_property("color") == "rgba(51, 136, 193, 1)":
        testResults_file_x(wb, sheet,"pass",fileName, 7, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 7, 'f')
    if assignButton.text == "ASSIGN":
        testResults_file_x(wb, sheet,"pass",fileName, 4, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 4, 'f')

def CancelMeetingButton_Draft_InDev_Meeting(driver, wb, sheet, fileName):
    time.sleep(1)
    try:
        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@id='topBar']/div/paper-button[@id='actionButton0']")))
    finally:
        cancelButton = driver.find_element_by_xpath("//div[@id='topBar']/div/paper-button[@id='actionButton0']/span")
    if cancelButton.is_displayed():
        testResults_file_x(wb, sheet,"pass",fileName, 9, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 9, 'f')
    if cancelButton.value_of_css_property("background-color") == "rgba(0, 0, 0, 0)":
        testResults_file_x(wb, sheet,"pass",fileName, 10, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 10, 'f')
    if cancelButton.value_of_css_property("color") == "rgba(51, 136, 193, 1)":
        testResults_file_x(wb, sheet,"pass",fileName, 11, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 11, 'f')
    if cancelButton.text == "CANCEL MEETING":
        testResults_file_x(wb, sheet,"pass",fileName, 8, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 8, 'f')


def CancelMeetingButton(driver, wb, sheet, fileName):
    time.sleep(1)

    m_status = driver.find_element_by_xpath("//div[@id='mainContainer']/div/div[2]/div/div/div[2]").text
    if (m_status == "Published" or m_status == "PUBLISHED"):
        cm = 12
        d = 13
        bc = 14
        tc = 15
        buttonID = "actionButton1"
    else:
        cm = 8
        d = 9
        bc = 10
        tc = 11
        buttonID = "actionButton0"
    try:
        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@id='topBar']/div/paper-button[@id='%s']"%buttonID)))
    finally:
        cancelButton = driver.find_element_by_xpath("//div[@id='topBar']/div/paper-button[@id='%s']/span"%buttonID)
    if cancelButton.is_displayed():
        testResults_file_x(wb, sheet,"pass",fileName, d, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, d, 'f')
    if cancelButton.value_of_css_property("background-color") == "rgba(0, 0, 0, 0)":
        testResults_file_x(wb, sheet,"pass",fileName, bc, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, bc, 'f')
    if cancelButton.value_of_css_property("color") == "rgba(51, 136, 193, 1)":
        testResults_file_x(wb, sheet,"pass",fileName, tc, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, tc, 'f')
    if cancelButton.text == "CANCEL MEETING":
        testResults_file_x(wb, sheet,"pass",fileName, cm, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, cm, 'f')

def StartMeetingButton(driver, wb, sheet, fileName):
    time.sleep(1)

    m_status = driver.find_element_by_xpath("//div[@id='mainContainer']/div/div[2]/div/div/div[2]").text
    if (m_status == "Published" or m_status == "PUBLISHED"):
        cm = 16
        d = 17
        bc = 18
        tc = 19
        buttonID = "actionButton2"
    # else:
    #     cm = 8
    #     d = 9
    #     bc = 10
    #     tc = 11
    #     buttonID = "actionButton0"
    try:
        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@id='topBar']/div/paper-button[@id='actionButton2']")))
    finally:
        startMeetingButton = driver.find_element_by_xpath("//div[@id='topBar']/div/paper-button[@id='actionButton2']")
    if startMeetingButton.is_displayed():
        testResults_file_x(wb, sheet,"pass",fileName, d, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, d, 'f')
    if startMeetingButton.value_of_css_property("background-color") == "rgba(227, 119, 68, 1)":
        print startMeetingButton.value_of_css_property("background-color")
        testResults_file_x(wb, sheet,"pass",fileName, bc, 'p')
    else:
        print startMeetingButton.value_of_css_property("background-color")
        testResults_file_x(wb, sheet,"fail",fileName, bc, 'f')
    if startMeetingButton.value_of_css_property("color") == "rgba(255, 255, 255, 1)":
        print startMeetingButton.value_of_css_property("color")
        testResults_file_x(wb, sheet,"pass",fileName, tc, 'p')
    else:
        print startMeetingButton.value_of_css_property("color")
        testResults_file_x(wb, sheet,"fail",fileName, tc, 'f')
    if startMeetingButton.text == "START MEETING":
        testResults_file_x(wb, sheet,"pass",fileName, cm, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, cm, 'f')

def StopMeeting_button(driver, wb, sheet, fileName):
    try:
        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@id='contentContainer']/app-header-layout/div[@id='wrapper']/div[@id='contentContainer']/app-toolbar/paper-button")))
    finally:
        stopMeetingButton = driver.find_element_by_xpath("//div[@id='contentContainer']/app-header-layout/div[@id='wrapper']/div[@id='contentContainer']/app-toolbar/paper-button")
    if stopMeetingButton.is_displayed():
        testResults_file_x(wb, sheet,"pass",fileName, 4, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 4, 'f')
    if stopMeetingButton.value_of_css_property("background-color") == "rgba(227, 119, 68, 1)":   # orange
        #print stopMeetingButton.value_of_css_property("background-color")
        testResults_file_x(wb, sheet,"pass",fileName, 5, 'p')
    else:
        #print stopMeetingButton.value_of_css_property("background-color")
        testResults_file_x(wb, sheet,"fail",fileName, 5, 'f')
    if stopMeetingButton.value_of_css_property("color") == "rgba(255, 255, 255, 1)":    # white
        #print stopMeetingButton.value_of_css_property("color")
        testResults_file_x(wb, sheet,"pass",fileName, 6, 'p')
    else:
        #print stopMeetingButton.value_of_css_property("color")
        testResults_file_x(wb, sheet,"fail",fileName, 6, 'f')
    if stopMeetingButton.text == "STOP MEETING":
        testResults_file_x(wb, sheet,"pass",fileName, 3, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 3, 'f')

def MInProgress_buttons(driver, wb, sheet, fileName, buttonTitle):
    if (buttonTitle == "broadcast"):
        i = "2"
        d = 8
        bc = 9
        c = 10
        title = "START BROADCASTING"
        t = 7
    elif (buttonTitle == "attendance"):
        i = "3"
        d = 12
        bc = 13
        c = 14
        title = "TAKE ATTENDANCE"
        t = 11
    else:
        i = "4"
        d = 16
        bc = 17
        c = 18
        title = "MAKE LEADER"
        t = 15
    #for i in range(2,6):
    try:
        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@id='contentContainer']/app-header-layout/div[@id='wrapper']/div[@id='contentContainer']/app-toolbar/paper-button[%s]"%i)))
    finally:
        buttons = driver.find_element_by_xpath("//div[@id='contentContainer']/app-header-layout/div[@id='wrapper']/div[@id='contentContainer']/app-toolbar/paper-button[%s]"%i)
    if buttons.is_displayed():
        testResults_file_x(wb, sheet,"pass",fileName, d, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, d, 'f')
    if buttons.value_of_css_property("background-color") == "rgba(255, 255, 255, 1)":   # white
        #print stopMeetingButton.value_of_css_property("background-color")
        testResults_file_x(wb, sheet,"pass",fileName, bc, 'p')
    else:
        #print stopMeetingButton.value_of_css_property("background-color")
        testResults_file_x(wb, sheet,"fail",fileName, bc, 'f')
    if buttons.value_of_css_property("color") == "rgba(51, 136, 193, 1)":   # blue
        testResults_file_x(wb, sheet,"pass",fileName, c, 'p')
    else:
        #print startBroadcastButton.value_of_css_property("color")
        testResults_file_x(wb, sheet,"fail",fileName, c, 'f')
    if buttons.text == title:
        testResults_file_x(wb, sheet,"pass",fileName, t, 'p')
    else:
        print buttons.text
        testResults_file_x(wb, sheet,"fail; it is " + buttons.text,fileName, t, 'f')

# def TakeAttendance_button(driver, wb, sheet, fileName):
#     try:
#         element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@id='contentContainer']/app-header-layout/div[@id='wrapper']/div[@id='contentContainer']/app-toolbar/paper-button[3]")))
#     finally:
#         takeAttButton = driver.find_element_by_xpath("//div[@id='contentContainer']/app-header-layout/div[@id='wrapper']/div[@id='contentContainer']/app-toolbar/paper-button[3]")
#     if startBroadcastButton.is_displayed():
#         testResults_file_x(wb, sheet,"pass",fileName, 8, 'p')
#     else:
#         testResults_file_x(wb, sheet,"fail",fileName, 8, 'f')
#     if startBroadcastButton.value_of_css_property("background-color") == "rgba(255, 255, 255, 1)":   # white
#         #print stopMeetingButton.value_of_css_property("background-color")
#         testResults_file_x(wb, sheet,"pass",fileName, 9, 'p')
#     else:
#         #print stopMeetingButton.value_of_css_property("background-color")
#         testResults_file_x(wb, sheet,"fail",fileName, 9, 'f')
#     if startBroadcastButton.value_of_css_property("color") == "rgba(51, 136, 193, 1)":   # blue
#         testResults_file_x(wb, sheet,"pass",fileName, 10, 'p')
#     else:
#         #print startBroadcastButton.value_of_css_property("color")
#         testResults_file_x(wb, sheet,"fail",fileName, 10, 'f')
#     if startBroadcastButton.text == "START BROADCASTING":
#         testResults_file_x(wb, sheet,"pass",fileName, 7, 'p')
#     else:
#         testResults_file_x(wb, sheet,"fail",fileName, 7, 'f')

def DeleteMeetingButton_Draft_InDev_Meeting(driver, wb, sheet, fileName):
    time.sleep(1)
    try:
        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@id='topBar']/paper-button[@id='deleteActionButton']")))
    finally:
        deleteButton = driver.find_element_by_xpath("//div[@id='topBar']/paper-button[@id='deleteActionButton']/span")
    if deleteButton.is_displayed():
        testResults_file_x(wb, sheet,"pass",fileName, 9, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 9, 'f')
    if deleteButton.value_of_css_property("background-color") == "rgba(0, 0, 0, 0)":
        testResults_file_x(wb, sheet,"pass",fileName, 10, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 10, 'f')
    if deleteButton.value_of_css_property("color") == "rgba(51, 136, 193, 1)":
        testResults_file_x(wb, sheet,"pass",fileName, 11, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 11, 'f')
    if deleteButton.text == "DELETE":
        testResults_file_x(wb, sheet,"pass",fileName, 8, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 8, 'f')

def OpenMeetingButton_DraftMeeting(driver, wb, sheet, fileName):
    time.sleep(1)
    try:
        #element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@id='topBar']/div/paper-button[@id='actionButton1']")))
        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@id='topBar']/div/paper-button[@id='actionButton0']")))
    finally:
        #openButton = driver.find_element_by_xpath("//div[@id='topBar']/div/paper-button[@id='actionButton1']")  # does nto work may 24 2018
        openButton = driver.find_element_by_xpath("//div[@id='topBar']/div/paper-button[@id='actionButton0']")
    if openButton.is_displayed():
        testResults_file_x(wb, sheet,"pass",fileName, 13, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 13, 'f')
    if openButton.value_of_css_property("background-color") == "rgba(227, 119, 68, 1)":
        testResults_file_x(wb, sheet,"pass",fileName, 14, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 14, 'f')
    if openButton.value_of_css_property("color") == "rgba(255, 255, 255, 1)":
        testResults_file_x(wb, sheet,"pass",fileName, 15, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 15, 'f')
    if openButton.text == "OPEN MEETING":
        testResults_file_x(wb, sheet,"pass",fileName, 12, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 12, 'f')

def CloseMeetingButton_InDev_Meeting(driver, wb, sheet, fileName):
    time.sleep(1)
    try:
        #element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@id='topBar']/div/paper-button[@id='actionButton1']")))
        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@id='topBar']/div/paper-button[@id='actionButton0']")))
    finally:
        #openButton = driver.find_element_by_xpath("//div[@id='topBar']/div/paper-button[@id='actionButton1']")
        openButton = driver.find_element_by_xpath("//div[@id='topBar']/div/paper-button[@id='actionButton0']")
    if openButton.is_displayed():
        testResults_file_x(wb, sheet,"pass",fileName, 13, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 13, 'f')
    if openButton.value_of_css_property("background-color") == "rgba(227, 119, 68, 1)":
        testResults_file_x(wb, sheet,"pass",fileName, 14, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 14, 'f')
    if openButton.value_of_css_property("color") == "rgba(255, 255, 255, 1)":
        testResults_file_x(wb, sheet,"pass",fileName, 15, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 15, 'f')
    if openButton.text == "CLOSE MEETING":
        testResults_file_x(wb, sheet,"pass",fileName, 12, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 12, 'f')

def RegenReportButton(driver, wb, sheet, fileName):
    time.sleep(1)
    try:
        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@id='topBar']/div/paper-button[@id='actionButton0']")))
    finally:
        aButton = driver.find_element_by_xpath("//div[@id='topBar']/div/paper-button[@id='actionButton0']")
    if aButton.is_displayed():
        testResults_file_x(wb, sheet,"pass",fileName, 9, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 9, 'f')
    if aButton.value_of_css_property("background-color") == "rgba(255, 255, 255, 1)":
        testResults_file_x(wb, sheet,"pass",fileName, 10, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 10, 'f')
    if aButton.value_of_css_property("color") == "rgba(51, 136, 193, 1)":
        testResults_file_x(wb, sheet,"pass",fileName, 11, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 11, 'f')
    if aButton.text == "REGENERATE MEETING REPORT":
        testResults_file_x(wb, sheet,"pass",fileName, 8, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 8, 'f')

def actionButton0_toolBar(driver, wb, sheet, fileName):
    if driver.find_element_by_xpath("//div[@id='mainContainer']/div/div[2]/div/div/div[2]").text == "Approved":
        #print "1..................driver.find_element_by_xpath).text is " + driver.find_element_by_xpath("//div[@id='mainContainer']/div/div[2]/div/div/div[2]").text
        buttonTitle = "MOVE TO IN DEVELOPMENT"
    else:
        #print "2..................driver.find_element_by_xpath).text is " + driver.find_element_by_xpath("//div[@id='mainContainer']/div/div[2]/div/div/div[2]").text
        buttonTitle = "MOVE TO IN DEVELOPMENT"
    time.sleep(1)
    try:
        #element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@id='topBar']/div/paper-button[@id='actionButton1']")))
        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@id='topBar']/div/paper-button[@id='actionButton0']")))
    finally:
        #openButton = driver.find_element_by_xpath("//div[@id='topBar']/div/paper-button[@id='actionButton1']")
        actionButton = driver.find_element_by_xpath("//div[@id='topBar']/div/paper-button[@id='actionButton0']")
    if actionButton.is_displayed():
        testResults_file_x(wb, sheet,"pass",fileName, 13, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 13, 'f')
    #if actionButton.value_of_css_property("background-color") == "rgba(227, 119, 68, 1)":
    if actionButton.value_of_css_property("background-color") == "rgba(255, 255, 255, 1)":  # background white
        testResults_file_x(wb, sheet,"pass",fileName, 14, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 14, 'f')
    #if actionButton.value_of_css_property("color") == "rgba(255, 255, 255, 1)":
    if actionButton.value_of_css_property("color") == "rgba(51, 136, 193, 1)":     # text color - light blue
        testResults_file_x(wb, sheet,"pass",fileName, 15, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 15, 'f')
    #if openButton.text == "CLOSE MEETING":
    if actionButton.text == buttonTitle:
        testResults_file_x(wb, sheet,"pass",fileName, 12, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 12, 'f')

def actionButton1_toolBar(driver, wb, sheet, fileName):
    if driver.find_element_by_xpath("//div[@id='mainContainer']/div/div[2]/div/div/div[2]").text == "Approved":
        #print "Publish meetign text is this ......." + driver.find_element_by_xpath("//div[@id='mainContainer']/div/div[2]/div/div/div[2]").text
        buttonTitle = "PUBLISH MEETING"
    else:
        buttonTitle = "PUBLISH MEETING"
    time.sleep(1)
    try:
        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@id='topBar']/div/paper-button[@id='actionButton1']")))
    finally:
        openButton = driver.find_element_by_xpath("//div[@id='topBar']/div/paper-button[@id='actionButton1']")
    if openButton.is_displayed():
        testResults_file_x(wb, sheet,"pass",fileName, 17, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 17, 'f')
    if openButton.value_of_css_property("background-color") == "rgba(227, 119, 68, 1)":      #background - orange
        testResults_file_x(wb, sheet,"pass",fileName, 18, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 18, 'f')
    if openButton.value_of_css_property("color") == "rgba(255, 255, 255, 1)":     # text color -white
        testResults_file_x(wb, sheet,"pass",fileName, 19, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 19, 'f')
    #if openButton.text == "CLOSE MEETING":
    if openButton.text == buttonTitle:
        testResults_file_x(wb, sheet,"pass",fileName, 16, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 16, 'f')

def title_Meeting(driver, wb, sheet, fileName):
    time.sleep(1)

    m_status = driver.find_element_by_xpath("//div[@id='mainContainer']/div/div[2]/div/div/div[2]").text

    if (m_status == "Approved" or m_status == "APPROVED"):
        #print "text is " + driver.find_element_by_xpath("//div[@id='mainContainer']/div/div[2]/div/div/div[2]").text + ", btu expecting Approved"
        titleText = "APPROVED"
        tl = 20
        d = 21
        c = 22
    else:
        if (m_status == "Published" or m_status == "PUBLISHED"):
            titleText = "PUBLISHED"
            tl = 20
            d = 21
            c = 22
    try:
        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@id='mainContainer']/div/div[2]/div/div/div[2]")))
    finally:
        statusTitle = driver.find_element_by_xpath("//div[@id='mainContainer']/div/div[2]/div/div/div[2]")
    if statusTitle.is_displayed():
        testResults_file_x(wb, sheet,"pass",fileName, d, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, d, 'f')
    if statusTitle.value_of_css_property("color") == "rgba(51, 136, 193, 1)":
        testResults_file_x(wb, sheet,"pass",fileName, c, 'p')
    else:
        #print "&&&&&&  color is " + statusTitle.value_of_css_property("color")
        testResults_file_x(wb, sheet,"fail",fileName, c, 'f')
    if statusTitle.text == titleText:
        testResults_file_x(wb, sheet,"pass",fileName, tl, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, tl, 'f')
    return statusTitle.text

def title_DraftMeeting(driver, wb, sheet, fileName):
    try:
        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@id='mainContainer']/div/div[2]/div/div/div[2]")))
    finally:
        draftTitle = driver.find_element_by_xpath("//div[@id='mainContainer']/div/div[2]/div/div/div[2]")
    if draftTitle.is_displayed():
        testResults_file_x(wb, sheet,"pass",fileName, 17, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 17, 'f')
    if draftTitle.value_of_css_property("color") == "rgba(51, 136, 193, 1)":
        testResults_file_x(wb, sheet,"pass",fileName, 18, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 18, 'f')
    if draftTitle.text == "DRAFT":
        testResults_file_x(wb, sheet,"pass",fileName, 16, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 16, 'f')
    return draftTitle.text

def title_InDevMeeting(driver, wb, sheet, fileName):
    try:
        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@id='mainContainer']/div/div[2]/div/div/div[2]")))
    finally:
        draftTitle = driver.find_element_by_xpath("//div[@id='mainContainer']/div/div[2]/div/div/div[2]")
    if draftTitle.is_displayed():
        testResults_file_x(wb, sheet,"pass",fileName, 17, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 17, 'f')
    if draftTitle.value_of_css_property("color") == "rgba(51, 136, 193, 1)":
        testResults_file_x(wb, sheet,"pass",fileName, 18, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 18, 'f')
    if draftTitle.text == "IN DEVELOPMENT":
        testResults_file_x(wb, sheet,"pass",fileName, 16, 'p')
    else:
        testResults_file_x(wb, sheet,"fail:" + draftTitle.text ,fileName, 16, 'f')

def InstructionsTitle_Draft_InDev_Meeting(driver, wb, sheet, fileName):
    if driver.find_element_by_xpath("//div[@id='mainContainer']/div/div[2]/div/div/div[2]").text == "Approved":
        instrTitleText = 23
        instrTitleDisplayed = 24
        instrTitleColor = 25
    else:
        instrTitleText = 19
        instrTitleDisplayed = 20
        instrTitleColor = 21
    try:
        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//section[@id='Instructions']/h1")))
    finally:
        instructionsTitle = driver.find_element_by_xpath("//section[@id='Instructions']/h1")
    if instructionsTitle.is_displayed():
        testResults_file_x(wb, sheet,"pass",fileName, instrTitleDisplayed, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, instrTitleDisplayed, 'f')
    if instructionsTitle.value_of_css_property("color") == "rgba(0, 0, 0, 0.54)":
        testResults_file_x(wb, sheet,"pass",fileName, instrTitleColor, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, instrTitleColor, 'f')
    if instructionsTitle.text == "Instructions":
        testResults_file_x(wb, sheet,"pass",fileName, instrTitleText, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, instrTitleText, 'f')

def InstructionsTitle_Meeting(driver, wb, sheet, fileName):
    #print "approved meetign title is Approved or APPROVED ??" + driver.find_element_by_xpath("//div[@id='mainContainer']/div/div[2]/div/div/div[2]").text

    m_title = driver.find_element_by_xpath("//div[@id='mainContainer']/div/div[2]/div/div/div[2]").text
    if (m_title == "Approved" or m_title =="APPROVED"):
        instrTitleText = 23
        instrTitleDisplayed = 24
        instrTitleColor = 25
    elif (m_title == "Published" or m_title =="PUBLISHED"):
        instrTitleText = 23
        instrTitleDisplayed = 24
        instrTitleColor = 25
    else:
        instrTitleText = 19
        instrTitleDisplayed = 20
        instrTitleColor = 21
    try:
        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//section[@id='Instructions']/h1")))
    finally:
        instructionsTitle = driver.find_element_by_xpath("//section[@id='Instructions']/h1")
    if instructionsTitle.is_displayed():
        testResults_file_x(wb, sheet,"pass",fileName, instrTitleDisplayed, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, instrTitleDisplayed, 'f')
    if instructionsTitle.value_of_css_property("color") == "rgba(0, 0, 0, 0.54)":
        testResults_file_x(wb, sheet,"pass",fileName, instrTitleColor, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, instrTitleColor, 'f')
    if instructionsTitle.text == "Instructions":
        testResults_file_x(wb, sheet,"pass",fileName, instrTitleText, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, instrTitleText, 'f')

def InstructionsText_Draft_Meeting(driver, wb, sheet, fileName):
    if driver.find_element_by_xpath("//div[@id='mainContainer']/div/div[2]/div/div/div[2]").text == "Approved":
        t1 = "The meeting has been approved by the appropriate workflow (if applicable) and is ready to publish."
        t2 = "Once published all contents of the meeting will be available to the public unless noted as closed session item."
        t3 = "An email will also be sent to all meeting participants including the text entered in the Message to Particpants field."
        t1Line = 26
        t2Line = 27
        t3Line = 28
    else:
        t1 = "Fill in the necessary fields for this meeting."
        t2 = "To place the meeting on the public calendar without releasing the agenda, check the box to Calendar the Meeting."
        t3 = "In order to open meeting to submitters the required fields are Title, Date, Location, and Open Session time."
        t1Line = 22
        t2Line = 23
        t3Line = 24
    try:
        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//section[@id='Instructions']/h1")))
    finally:
        instructionsText = driver.find_element_by_xpath("//div[@id='content']/div/ul")
        i=t1Line
    items = instructionsText.find_elements_by_tag_name("li")
    for item in items:
        #print "@@@@@@@@@@@@******************************item is " + item.text
        if item.text == t1:
            testResults_file_x(wb, sheet,"pass",fileName, t1Line, 'p')
            i+=1
        elif item.text == t2:
            testResults_file_x(wb, sheet,"pass",fileName, t2Line, 'p')
            i+=1
        elif item.text == t3:
            testResults_file_x(wb, sheet,"pass",fileName, t3Line, 'p')
        else:
            testResults_file_x(wb, sheet,"fail" + " it reads: " + item.text,fileName, i, 'f')
            i+=1

def InstructionsText_InDev_Meeting(driver, wb, sheet, fileName):

    try:
        #element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//section[@id='Instructions']/h1")))
        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@id='content']/div/ul")))
    finally:
        instructionsText = driver.find_element_by_xpath("//div[@id='content']/div/ul")
        i=22  #used in line 584 below, this line is 571
    #print "*******************instructionsText is " + instructionsText  # instructionsText is an object , cannot be printed
    items = instructionsText.find_elements_by_tag_name("li")
    text_contents = [el.text for el in driver.find_elements_by_xpath("//div[@id='content']/div/ul/li")]
    for tc in text_contents:
        if tc != "":
            #print "^^^^^^^^^^^^^^^^^^^^^  " + tc
            if tc == "This meeting is open to submitters (if applicable) and agenda items will be placed on this agenda.":
                testResults_file_x(wb, sheet,"pass",fileName, 22, 'p')
                i+=1
            elif tc == "Drag and drop them into position, click an individual item to open or go to My Tasks to see the items on this agenda waiting for your action.":
                testResults_file_x(wb, sheet,"pass",fileName, 23, 'p')
                i+=1
            else:
                testResults_file_x(wb, sheet,"fail - " + " it reads: " + tc, fileName, i, 'f')
                i+=1
        else:
            print "tc is blank here ^^^^^^^^^^^^^^^^^^^^^  "
    # for item in items:
    #     print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@item is " + item.text
    #     if item.text == "This meeting is open to submitters (if applicable) and agenda items will be placed on this agenda.":
    #         testResults_file_x(wb, sheet,"pass",fileName, 22, 'p')
    #         i+=1
    #     elif item.text == "Drag and drop them into position, click an individual item to open or go to My Tasks to see the items on this agenda waiting for your action.":
    #         testResults_file_x(wb, sheet,"pass",fileName, 23, 'p')
    #         i+=1
    #     else:
    #         testResults_file_x(wb, sheet,"fail" + " it reads: " + item.text,fileName, i, 'f')
    #         i+=1

def InstructionsText_Meeting(driver, wb, sheet, fileName):
    mStatus = driver.find_element_by_xpath("//div[@id='mainContainer']/div/div[2]/div/div/div[2]").text
    if (mStatus == "Approved" or mStatus == 'APPROVED'):
        t1 = "The meeting has been approved by the appropriate workflow (if applicable) and is ready to publish."
        t2 = "Once published all contents of the meeting will be available to the public unless noted as closed session item."
        t3 = "An email will also be sent to all meeting participants including the text entered in the Message to Particpants field."
        t1Line = 26
        t2Line = 27
        t3Line = 28
    elif (mStatus == "Published" or mStatus == 'PUBLISHED'):
        t1 = "The meeting has been published and is available to the public."
        t2 = "If changes have been made to any agenda items after publishing, click Regenerate Meeting Report to replace and update reports available at the bottom of this page."
        t3 = "To start the meeting, click Start Meeting and navigate to the Meetings in Progress page to participate in, manage or lead the meeting."
        t1Line = 26
        t2Line = 27
        t3Line = 28
    else:
        if (mStatus == "Draft" or mStatus == 'DRAFT'):
            t1 = "Fill in the necessary fields for this meeting."
            t2 = "To place the meeting on the public calendar without releasing the agenda, check the box to Calendar the Meeting."
            t3 = "In order to open meeting to submitters the required fields are Title, Date, Location, and Open Session time."
            t1Line = 22
            t2Line = 23
            t3Line = 24
    try:
        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//section[@id='Instructions']/h1")))
    finally:
        instructionsText = driver.find_element_by_xpath("//div[@id='content']/div/ul")
        i=t1Line
    items = instructionsText.find_elements_by_tag_name("li")
    text_contents = [el.text for el in driver.find_elements_by_xpath("//div[@id='content']/div/ul/li")]
    #for item in items:
    for item in text_contents:
        if (item != ""):
            if item == t1:
                testResults_file_x(wb, sheet,"pass",fileName, t1Line, 'p')
                i+=1
            elif item == t2:
                testResults_file_x(wb, sheet,"pass",fileName, t2Line, 'p')
                i+=1
            elif item == t3:
                testResults_file_x(wb, sheet,"pass",fileName, t3Line, 'p')
            else:
                testResults_file_x(wb, sheet,"fail" + " it reads: " + item,fileName, i, 'f')
                print i
                i+=1
        else:
            print "just another blank li"

def MyItems_click(driver):
    time.sleep(2)
    spinner_wait(driver)
    try:
        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//paper-menu[@id='sidebarNavigation']/div/sidebar-menu-item[6]/paper-item/pushstate-anchor/a")))
        element = WebDriverWait(driver, 10).until( EC.element_to_be_clickable((By.XPATH, "//paper-menu[@id='sidebarNavigation']/div/sidebar-menu-item[6]/paper-item/pushstate-anchor/a")))
        #element = driver.find_element_by_xpath("//avocado-frame/awi-app/main-container[@id='mainContainer']/app-router[@id='router']/app-route[15]/confirm-service-request-selection/dynamic-task-view/paper-drawer-panel/iron-selector/div[@id='drawer']/paper-header-panel/div[@id='mainPanel']/div[@id='mainContainer']/sidebar-navigation/div/div/paper-menu[@id='sidebarNavigation']/div/sidebar-menu-item[6]/paper-item/pushstate-anchor/a/div")
    finally:
        #driver.find_element_by_xpath("//avocado-frame/awi-app/main-container[@id='mainContainer']/app-router[@id='router']/app-route[15]/confirm-service-request-selection/dynamic-task-view/paper-drawer-panel/iron-selector/div[@id='drawer']/paper-header-panel/div[@id='mainPanel']/div[@id='mainContainer']/sidebar-navigation/div/div/paper-menu[@id='sidebarNavigation']/div/sidebar-menu-item[6]/paper-item/pushstate-anchor/a/div").click()
        driver.find_element_by_xpath("//paper-menu[@id='sidebarNavigation']/div/sidebar-menu-item[6]/paper-item/pushstate-anchor/a/div").click()
    time.sleep(3)

def MyItems_Total(driver):
    try:
        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Total items:')]")))
    finally:
        aiTotal = driver.find_element_by_xpath("//span[contains(text(), 'Total items:')]").text
        aiTotal1= mTotal[(mTotal.find(': ')+1):].strip()
        time.sleep(1)
    return int(mTotal1)

def InstructionsText_Draft_agendaItem(driver, wb, sheet, fileName):
    try:
        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//section[@id='Instructions']/h1")))
    finally:
        instructionsText = driver.find_element_by_xpath("//div[@id='content']/div/ul")
        i=22
    items = instructionsText.find_elements_by_tag_name("li")
    for item in items:
        if item.text == "Fill in the necessary fields for this agenda item.":
            testResults_file_x(wb, sheet,"pass",fileName, 22, 'p')
            i+=1
        elif item.text == "The required fields to submit or add to an agenda are: Title, Meeting and Workflow Route":
            testResults_file_x(wb, sheet,"pass",fileName, 23, 'p')
            i+=1
        else:
            testResults_file_x(wb, sheet,"fail" + " it reads: " + item.text,fileName, i, 'f')
            i+=1

def AddToAgendaButton_Draft_agendaItem(driver, wb, sheet, fileName):
    time.sleep(1)
    try:
        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@id='topBar']/div/paper-button[@id='actionButton0']")))
    finally:
        cancelButton = driver.find_element_by_xpath("//div[@id='topBar']/div/paper-button[@id='actionButton0']/span")
    if cancelButton.is_displayed():
        testResults_file_x(wb, sheet,"pass",fileName, 9, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 9, 'f')
    if cancelButton.value_of_css_property("background-color") == "rgba(0, 0, 0, 0)":
        testResults_file_x(wb, sheet,"pass",fileName, 10, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 10, 'f')
    if cancelButton.value_of_css_property("color") == "rgba(51, 136, 193, 1)":
        testResults_file_x(wb, sheet,"pass",fileName, 11, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 11, 'f')
    #if cancelButton.text == "ADD TO AGENDA":
    if cancelButton.text == "SEND TO WORKFLOW":
        testResults_file_x(wb, sheet,"pass",fileName, 8, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 8, 'f')

def SendToWorkflowButton_Draft_agendaItem(driver, wb, sheet, fileName):
    time.sleep(1)
    try:
        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@id='topBar']/div/paper-button[@id='actionButton1']")))
    finally:
        sendToWorkflowButton = driver.find_element_by_xpath("//div[@id='topBar']/div/paper-button[@id='actionButton1']")
    if sendToWorkflowButton.is_displayed():
        testResults_file_x(wb, sheet,"pass",fileName, 13, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 13, 'f')
    if sendToWorkflowButton.value_of_css_property("background-color") == "rgba(255, 255, 255, 1)":
        testResults_file_x(wb, sheet,"pass",fileName, 14, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 14, 'f')
    if sendToWorkflowButton.value_of_css_property("color") == "rgba(51, 136, 193, 1)":
        testResults_file_x(wb, sheet,"pass",fileName, 15, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 15, 'f')
    #if sendToWorkflowButton.text == "SEND TO WORKFLOW":
    if sendToWorkflowButton.text == "ADD TO AGENDA":
        testResults_file_x(wb, sheet,"pass",fileName, 12, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 12, 'f')

def MyMeetings_blanksDelete(driver):
    spinner_wait(driver)
    try:
        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@id='items']/awi-grid-row")))
    finally:
        deletedM = driver.find_element_by_xpath("//div[@id='items']/awi-grid-row")

    # sort by meeting name to haev blank meetings on top:
    try:
        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@id='topBar']")))
    finally:
        driver.find_element_by_xpath("//div[@id='topBar']/awi-grid-header-cell").click()
        time.sleep(1)

    spinner_wait(driver)
    for i in range (len(driver.find_elements_by_xpath("//div[@id='items']/awi-grid-row"))):
        if (i != 0):
            # get meetign name:
            meeting = driver.find_element_by_xpath("//div[@id='items']/awi-grid-row/awi-grid-cell/div/span").text
            #meeting = driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell/div/span"%str(i)).text
            #print ""

            if meeting == '':
                # check check box
                try:
                    #element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@id='mainPanel']/div[@id='mainContainer']/div/awi-grid[@id='myMeetingsGrid']/div/div/div/iron-list[@id='list']/div[@id='items']/awi-grid-row/div/paper-checkbox[@id='checkbox']/div[@id='checkboxContainer']")))
                    element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@id='items']/awi-grid-row/div/paper-checkbox[@id='checkbox']/div[@id='checkboxContainer']")))
                finally:
                    deletedM = driver.find_element_by_xpath("//div[@id='items']/awi-grid-row/div/paper-checkbox[@id='checkbox']/div[@id='checkboxContainer']").click()

                #click Actions button
                try:
                    #element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@id='actionsButtonContainer']/paper-menu-button/div[@id='trigger']/paper-button")))  # does nto work may 24 2018
                    #element = driver.find_element_by_xpath("//div[@id='actionsButtonContainer']/paper-menu-button/div[@id='trigger']/paper-button")
                    element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div/paper-menu-button/div[@id='trigger']/paper-button")))
                finally:
                    #driver.find_element_by_xpath("//div[@id='actionsButtonContainer']/paper-menu-button/div[@id='trigger']/paper-button").click() #does nto work may 24 2018
                    driver.find_element_by_xpath("//div/paper-menu-button/div[@id='trigger']/paper-button").click()
                time.sleep(2)

                # verify if teh dropdown is showing
                try:
                    #element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@id='actionsButtonContainer']/paper-menu-button/iron-dropdown[@id='dropdown']")))   #does NOT work may 24 2018
                    #element = driver.find_element_by_xpath("//div[@id='actionsButtonContainer']/paper-menu-button/div[@id='trigger']/paper-button")
                    element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div/paper-menu-button/iron-dropdown[@id='dropdown']")))
                finally:
                    #meetingDropDown = driver.find_element_by_xpath("//div[@id='actionsButtonContainer']/paper-menu-button/iron-dropdown[@id='dropdown']")  #does NOT work may 24 2018
                    meetingDropDown = driver.find_element_by_xpath("//div/paper-menu-button/iron-dropdown[@id='dropdown']")

                if meetingDropDown.value_of_css_property("display") == "none":
                    #driver.find_element_by_xpath("//div[@id='actionsButtonContainer']/paper-menu-button/div[@id='trigger']/paper-button").click()
                    driver.find_element_by_xpath("//div/paper-menu-button/div[@id='trigger']/paper-button").click()
                    time.sleep(1)

                # select Delete Meeting
                try:
                    #element = driver.find_element_by_xpath("//div[@id='actionsButtonContainer']/paper-menu-button/iron-dropdown[@id='dropdown']/div[@id='contentWrapper']/div/paper-listbox/paper-item[contains(text(), 'Delete Meeting')]")
                    #element = driver.find_element_by_xpath("//div[@id='actionsButtonContainer']/paper-menu-button/iron-dropdown[@id='dropdown']/div[@id='contentWrapper']/div/paper-listbox/paper-item[4]")
                    element = driver.find_element_by_xpath("//div/paper-menu-button/iron-dropdown[@id='dropdown']/div[@id='contentWrapper']/div/paper-listbox/paper-item[4]")
                finally:
                    #driver.find_element_by_xpath("//div[@id='actionsButtonContainer']/paper-menu-button/iron-dropdown[@id='dropdown']/div[@id='contentWrapper']/div/paper-listbox/paper-item[contains(text(), 'Delete Meeting')]").click()
                    #driver.find_element_by_xpath("//div[@id='actionsButtonContainer']/paper-menu-button/iron-dropdown[@id='dropdown']/div[@id='contentWrapper']/div/paper-listbox/paper-item[4]").click()
                    driver.find_element_by_xpath("//div/paper-menu-button/iron-dropdown[@id='dropdown']/div[@id='contentWrapper']/div/paper-listbox/paper-item[4]").click()
                time.sleep(1)

                # click Delete button on pop up
                try:
                    element = driver.find_element_by_xpath("//paper-dialog[@id='deleteMeetingModal']/div/paper-button[contains(text(), 'Delete')]")
                finally:
                    driver.find_element_by_xpath("//paper-dialog[@id='deleteMeetingModal']/div/paper-button[contains(text(), 'Delete')]").click()
                time.sleep(2)

def MyItems_blanksDelete(driver):
    MyItems_click(driver)

    if driver.find_element_by_xpath("//awi-grid[@id='tasksListMy']/div/paper-header-panel").value_of_css_property("display")=="flex":
        print "list is empty"
    else:
        print "list is NOT empty ..........."

        try:
            element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@id='items']/awi-grid-row")))
        except NoSuchElementException:
            print "the list is blank"

        agendaItem = driver.find_element_by_xpath("//div[@id='items']/awi-grid-row")

        #click Item Name to sort by name
        driver.find_element_by_xpath("//div[@id='topBar']/awi-grid-header-cell").click()

        for i in range (len(driver.find_elements_by_xpath("//div[@id='items']/awi-grid-row"))):
             if (i != 0):

                 #itemName = driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell/div/span"%str(i)).text
                 #print "i is "+ str(i)

                itemName = driver.find_element_by_xpath("//div[@id='items']/awi-grid-row/awi-grid-cell/div/span").text
                # if it is a blank agenda item
                if itemName == '':
                    #check its check box
                    #driver.find_element_by_xpath("//awi-grid-row[%s]/div/paper-checkbox[@id='checkbox']/div[@id='checkboxContainer']"%str(i)).click()
                    driver.find_element_by_xpath("//awi-grid-row/div/paper-checkbox[@id='checkbox']/div[@id='checkboxContainer']").click()

                    #click Actions button
                    try:
                        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@id='topBar']/div/paper-menu-button[@id='actionsButton']/div[@id='trigger']/paper-button")))
                        #element = driver.find_element_by_xpath("//div[@id='actionsButtonContainer']/paper-menu-button/div[@id='trigger']/paper-button")
                    finally:
                        driver.find_element_by_xpath("//div[@id='topBar']/div/paper-menu-button[@id='actionsButton']/div[@id='trigger']/paper-button/iron-icon").click()
                    time.sleep(2)

                    # if the drop down is not displayed, click Action button again:
                    try:
                        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@id='topBar']/div/paper-menu-button[@id='actionsButton']/iron-dropdown[@id='dropdown']")))
                        #element = driver.find_element_by_xpath("//div[@id='actionsButtonContainer']/paper-menu-button/div[@id='trigger']/paper-button")
                    finally:
                        itemDropdown = driver.find_element_by_xpath("//div[@id='topBar']/div/paper-menu-button[@id='actionsButton']/iron-dropdown[@id='dropdown']")

                    if itemDropdown.value_of_css_property("display") == "none":
                        driver.find_element_by_xpath("//div[@id='topBar']/div/paper-menu-button[@id='actionsButton']/div[@id='trigger']/paper-button/iron-icon").click()

                    # select Delete item
                    try:
                        #element = driver.find_element_by_xpath("//div[@id='actionsButtonContainer']/paper-menu-button/iron-dropdown[@id='dropdown']/div[@id='contentWrapper']/div/paper-listbox/paper-item[contains(text(), 'Delete Meeting')]")
                        element = driver.find_element_by_xpath("//iron-dropdown[@id='dropdown']/div[@id='contentWrapper']/div/paper-listbox/paper-item[3]")
                    finally:
                        #driver.find_element_by_xpath("//div[@id='actionsButtonContainer']/paper-menu-button/iron-dropdown[@id='dropdown']/div[@id='contentWrapper']/div/paper-listbox/paper-item[contains(text(), 'Delete Meeting')]").click()
                        driver.find_element_by_xpath("//iron-dropdown[@id='dropdown']/div[@id='contentWrapper']/div/paper-listbox/paper-item[3]").click()
                    time.sleep(1)

                    # click Delete button on pop up
                    try:
                        element = driver.find_element_by_xpath("//paper-dialog[@id='deleteItemModal']/div/paper-button[contains(text(), 'Delete')]")
                    finally:
                        driver.find_element_by_xpath("//paper-dialog[@id='deleteItemModal']/div/paper-button[contains(text(), 'Delete')]").click()
                    time.sleep(2)

def spinner_wait(driver):
    try:
        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//paper-spinner[@id='spinner']")))
    finally:
        sp = driver.find_element_by_xpath("//paper-spinner[@id='spinner']")
    if sp.is_displayed():
        while sp.value_of_css_property("display") == "block":
            time.sleep(2)

def reportsLinks(driver, wb, sheet, fileName):
    oReport = driver.find_element_by_xpath("//form/awi-section[@id='Reports']/section[@id='Reports']/awi-document/div/div[2]/div/a").text
    if (oReport == "Agenda Outline Report"):
        #print "outline report link is found"
        testResults_file_x(wb, sheet,"pass",fileName, 29, 'p')
    else:
        print "outline report link is not found"
        testResults_file_x(wb, sheet,"fail",fileName, 29, 'f')

    pReport = driver.find_element_by_xpath("//form/awi-section[@id='Reports']/section[@id='Reports']/awi-document[2]/div/div[2]/div/a").text
    if (pReport == "Board Packet Report"):
        testResults_file_x(wb, sheet,"pass",fileName, 30, 'p')
    else:
        testResults_file_x(wb, sheet,"fail",fileName, 30, 'f')

def reportsLinks_InProgress(driver, wb, sheet, fileName, reports):
    if (reports == "outline"):
        i = "2"
        l = 19
        Rtitle ="Agenda Outline Report"
    else:
        i = "3"
        l = 20
        Rtitle ="Board Packet Report"
    try:
        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@id='contentContainer']/div/div/div/div/div/div[%s]/a"%i)))
    finally:
        ReportN = driver.find_element_by_xpath("//div[@id='contentContainer']/div/div/div/div/div/div[%s]/a"%i).text

    if (ReportN == Rtitle):
        testResults_file_x(wb, sheet,"pass",fileName, l, 'p')
    else:
        testResults_file_x(wb, sheet,"fail" + ReportN,fileName, l, 'f')


def attachments(driver, wb, sheet, fileName):
    attCount = 0
    # if there are attachments, count them
    if (driver.find_elements_by_xpath("//form/awi-section[@id='Attachments']/section[@id='Attachments']/awi-agenda-attachments-view/attachments-node")):
        attNodes = driver.find_elements_by_xpath("//form/awi-section[@id='Attachments']/section[@id='Attachments']/awi-agenda-attachments-view/attachments-node")
        for i in range(1, len(attNodes)):
            attPane = driver.find_elements_by_xpath("//form/awi-section[@id='Attachments']/section[@id='Attachments']/awi-agenda-attachments-view/attachments-node[%s]/div/div[2]/attachments-pane"%str(i))
            attCount = attCount + len(attPane)
            print attPane
    else:
        att = driver.find_element_by_xpath("//form/awi-section[@id='Attachments']/section[@id='Attachments']/awi-agenda-attachments-view/div").text
        if att == ("This Meeting does not have any Attachments."):
            print "no attachments"
            #testResults_file_x(wb, sheet,str(attCount),fileName, 33, 'p')
    testResults_file_x(wb, sheet,str(attCount),fileName, 33, 'p')

def sections_InProgress(driver, wb, sheet, fileName, section):
    if (section == "preliminary"):
        iden = "meetingHeader"
        w = 21
        t = "Preliminary Information"
    else:
        iden = "meetingFooter"
        w = 22
        t = "Closing Information"
    try:
        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@id='contentContainer']/div/div/div/div/div/div[@id='%s']"%iden)))
    finally:
        mProgressS = driver.find_element_by_xpath("//div[@id='contentContainer']/div/div/div/div/div/div[@id='%s']"%iden).text

    if (mProgressS == t):
        testResults_file_x(wb, sheet,"pass",fileName, w, 'p')
    else:
        testResults_file_x(wb, sheet,"fail" + mProgressS,fileName, w, 'f')

def selectGoverningBody(driver, GB, GBtitle):
    try:
        element = WebDriverWait(driver, 20).until( EC.presence_of_element_located((By.XPATH, "//div[@id='mainContainer']/div/div/select-client/div/awi-combobox[@id='clients']/div[2]/paper-input-container/div[2]")))
    finally:
        driver.find_element_by_xpath("//div[@id='mainContainer']/div/div/select-client/div/awi-combobox[@id='clients']/div[2]/paper-input-container/div[2]").click()

    # get a GB from the drop-down list
    try:
        element = WebDriverWait(driver, 20).until( EC.presence_of_element_located((By.XPATH, "//awi-combobox-overlay[@id='overlay']/div[@id='scroller']/iron-list[@id='selector']/div[@id='items']")))
    finally:
        GBs = driver.find_elements_by_xpath("//awi-combobox-overlay[@id='overlay']/div[@id='scroller']/iron-list[@id='selector']/div[@id='items']/awi-combobox-item")

    print len(GBs)

    if (GBtitle != ""):
        # find the GBtitle in the list and click on it
        for gb in GBs:
            if (gb.text == GBtitle):
                gb.click()
                break
    else:
        r = randint(1, len(GBs))
        GBtitle = driver.find_element_by_xpath("//awi-combobox-overlay[@id='overlay']/div[@id='scroller']/iron-list[@id='selector']/div[@id='items']/awi-combobox-item[%s]"%str(r)).text
        driver.find_element_by_xpath("//awi-combobox-overlay[@id='overlay']/div[@id='scroller']/iron-list[@id='selector']/div[@id='items']/awi-combobox-item[%s]"%str(r)).click()
    time.sleep(2)

    return GBtitle
