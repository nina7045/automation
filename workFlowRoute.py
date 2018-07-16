import time, datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time, re, random
from random import randint
import utils

def_workFlowRoute():
    try:
        #element = driver.find_element_by_xpath("//avocado-frame/awi-app/main-container[@id='mainContainer']/app-router[@id='router']/app-route[15]/confirm-service-request-selection/dynamic-task-view/paper-drawer-panel/iron-selector/div[@id='drawer']/paper-header-panel/div[@id='mainPanel']/div[@id='mainContainer']/sidebar-navigation/div/div/paper-menu[@id='sidebarNavigation']/div/sidebar-menu-item[8]/paper-item/pushstate-anchor/a/div")
        element = driver.find_element_by_xpath("//paper-menu[@id='sidebarNavigation']/div/sidebar-menu-item[8]/paper-item/pushstate-anchor/a/div")
    finally:
        #driver.find_element_by_xpath("//avocado-frame/awi-app/main-container[@id='mainContainer']/app-router[@id='router']/app-route[15]/confirm-service-request-selection/dynamic-task-view/paper-drawer-panel/iron-selector/div[@id='drawer']/paper-header-panel/div[@id='mainPanel']/div[@id='mainContainer']/sidebar-navigation/div/div/paper-menu[@id='sidebarNavigation']/div/sidebar-menu-item[8]/paper-item/pushstate-anchor/a/div").click()
        driver.find_element_by_xpath("//paper-menu[@id='sidebarNavigation']/div/sidebar-menu-item[8]/paper-item/pushstate-anchor/a/div").click()
    time.sleep(4)
    # Workflow routes Click
    driver.find_element_by_xpath("//div[@id='mainContainer']/div/div[4]/div/paper-toolbar/div[@id='topBar']/a/span").click()
    time.sleep(2)
    routesLength = driver.find_elements_by_xpath("//div[@id='items']/awi-grid-row")
    for rl in range (len(driver.find_elements_by_xpath("//div[@id='items']/awi-grid-row"))):
        if (rl != 0):
            print driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell/div/span"%str(rl)).text
            if driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell/div/span"%str(rl)).text == wfPlan:
                driver.find_element_by_xpath("//div[@id='items']/awi-grid-row[%s]/awi-grid-cell/div/span"%str(rl)).click()
                time.sleep(1)
                nextUserName = driver.find_element_by_xpath("//paper-dialog[@id='editRouteDialog']/div/div[2]/div[2]/awi-grid[@id='usersGrid']/div/div/div/iron-list[@id='list']/div[@id='items']/awi-grid-row/awi-grid-cell[2]/div/span").text
                print nextUserName
