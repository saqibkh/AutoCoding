#!/usr/bin/python

##
#    @brief This file contains Main class for youtube automation
#
#    @author Saqib Khan
##
import unittest, time, re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from FWConstants import FWConstants





class youtubeMain():

    ##
	# This file contain the MAIN class for running all youtube automation
	#

    def __init__(self):
        self.youtube_baseurl = "https://youtube.com"
        self.driver = None

    def openBrowser(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.accept_next_alert = True


    def runTest(self):
        self.openBrowser()
        self.driver.get("https://www.youtube.com/watch?v=6KBgmakci9Q")
        self.driver.implicitly_wait(100)
        time.sleep(3)
        self.tearDown()
        return FWConstants.SUCCESS


    def tearDown(self):
        self.driver.quit()