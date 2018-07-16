import xlwt
import utils
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def Dashboard(driver, wb, sheet, fileName):
    sheet = wb.get_sheet('Dashboard')

    # verify title "Dashboard"
    utils.spinner_wait(driver)
    try:
        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@id='main']/div/awi-master-page/paper-header-panel[@id='panel']/paper-toolbar/div[@id='topBar']/div[contains(text(), 'Dashboard')]")))
    finally:
        #dashboardTitle = driver.find_element_by_xpath("//div[@id='topBar']/div")
        dashboardTitle = driver.find_element_by_class_name('title').text
    if (dashboardTitle == "Dashboard"):
        utils.testResults_file_x(wb, sheet,"pass",fileName, 0, 'p')
    else:
        utils.testResults_file_x(wb, sheet,"fail - the title displayed is " + dashboardTitle,fileName, 0, 'f')


    # this Dashboard is for a MM admin:

    # My Tasks
    try:
        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@id='topBar']/a/span")))
    finally:
        MyTasks = driver.find_element_by_xpath("//div[@id='topBar']/a/span").text
    if (MyTasks == "My Tasks"):
        utils.testResults_file_x(wb, sheet,"pass",fileName, 1, 'p')
    else:
        utils.testResults_file_x(wb, sheet,"fail - the title displayed is " + MyTasks,fileName, 1, 'f')

    # My Tasks text
    try:
        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@id='mainContainer']/div/div/div/div/div/span")))
    finally:
        MyTasksText = driver.find_element_by_xpath("//div[@id='mainContainer']/div/div/div/div/div/span").text
    if (MyTasksText == "View upcoming tasks"):
        utils.testResults_file_x(wb, sheet,"pass",fileName, 2, 'p')
    else:
        utils.testResults_file_x(wb, sheet,"fail - the text displayed is " + MyTasksText,fileName, 2, 'f')

    #   title
    for i in range(2, 6):
        if (i == 2):
            title = "Start New"
            a = 3
            text = "Click to see all Start New options"
            b = 4
        elif (i == 3):
            title = "Notifications"
            a = 5
            text = "You have no unread notifications."
            b = 6
        elif (i == 4):
            title = "Administration"
            a = 7
            text = "Perform administrative setup Tasks"
            b = 8
        else:
            title = "Meetings"
            a = 9
            text = "Click to View all Calendared and Completed Meetings"
            b = 10
        try:
            element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@id='mainContainer']/div/div[%s]/div/paper-toolbar/div[@id='topBar']/a/span"%str(i))))
        finally:
            getT = driver.find_element_by_xpath("//div[@id='mainContainer']/div/div[%s]/div/paper-toolbar/div[@id='topBar']/a/span"%str(i)).text

        if (getT == title):
            utils.testResults_file_x(wb, sheet,"pass",fileName, a, 'p')
        else:
            utils.testResults_file_x(wb, sheet,"fail - the title displayed is " + getT,fileName, a, 'f')
        time.sleep(1)
        #   text
        if (i == 3):
            try:
                element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@id='mainContainer']/div/div[%s]/div/div/notifications-widget/div/span"%str(i))))
            finally:
                getTe = driver.find_element_by_xpath("//div[@id='mainContainer']/div/div[%s]/div/div/notifications-widget/div/span"%str(i)).text

            if (getTe == text):
                utils.testResults_file_x(wb, sheet,"pass",fileName, b, 'p')
            else:
                utils.testResults_file_x(wb, sheet,"fail - the text displayed is " + getTe,fileName, b, 'f')
        else:
            try:
                element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@id='mainContainer']/div/div[%s]/div/div/div/span"%str(i))))
            finally:
                getTe = driver.find_element_by_xpath("//div[@id='mainContainer']/div/div[%s]/div/div/div/span"%str(i)).text

            if (getTe == text):
                utils.testResults_file_x(wb, sheet,"pass",fileName, b, 'p')
            else:
                utils.testResults_file_x(wb, sheet,"fail - the text displayed is " + getTe,fileName, b, 'f')
