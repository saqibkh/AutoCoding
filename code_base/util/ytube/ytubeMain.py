#!/usr/bin/python

##
#    @brief This file contains Main class for ytube automation
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
from Constants import Constants





class ytubeMain():

    ##
	# This file contain the MAIN class for running all youtube automation
	#

    def __init__(self):
        self.youtube_baseurl = "https://youtube.com"
        self.driver = None

    def openBrowser(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(100)
        self.accept_next_alert = True


    def runTest(self):
        self.openBrowser()
        self.driver.get("https://www.youtube.com/watch?v=6KBgmakci9Q")
        self.driver.implicitly_wait(100)
        time.sleep(360)
        self.tearDown()
        return Constants.SUCCESS


    def tearDown(self):
        self.driver.quit()