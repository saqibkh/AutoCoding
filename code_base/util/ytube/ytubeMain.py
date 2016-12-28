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
from pyvirtualdisplay import Display
from random import randint
from ytubeConstants import ytubeConstants
from google import google


class ytubeMain():

    ##
	# This file contain the MAIN class for running all youtube automation
	#

    def __init__(self):
        self.youtube_baseurl = "https://youtube.com"
        self.driver = None

    def openBrowser(self):
        display = Display(visible=0, size=(800, 600))
        display.start()
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(100)
        self.accept_next_alert = True
        self.google = google(self.driver)



    def runTest(self):
        URLs = ytubeConstants.URLS;
        for url in URLs:
            self.openBrowser()

            # 1% of views would come from google accounts
            if((randint(1,100)) == 1):
                self.googleSignIn()

            # Start the video using the link
            self.driver.get(url[0])
            self.driver.implicitly_wait(100)

            # 5% of views would pause here for 5-30 sends
            if ((randint(1, 100)) <= 5):
                time.sleep((randint(30,60)))
                self.pauseORresume()
                time.sleep((randint(5,30)))
                self.pauseORresume()

            time.sleep((url[1]*60) - (randint(0,60)))

            #10% of videos will be paused here
            if ((randint(1, 100)) <= 10):
                self.pauseORresume()
		time.sleep((randint(15,120)))

            # 10% of videos will move to next video here
            if ((randint(1, 100)) <= 10):
                self.nextVideo()
		time.sleep((randint(15,120)))


            self.tearDown()
        return Constants.SUCCESS


    def tearDown(self):
        self.driver.quit()

    def pauseORresume(self):
        self.driver.find_element_by_css_selector("button.ytp-play-button.ytp-button").click()

    def nextVideo(self):
        self.driver.find_element_by_css_selector("a.ytp-next-button.ytp-button").click()

    def googleSignIn(self):
        l_googleIDs = ytubeConstants.ACCOUNTS;
        l_id = l_googleIDs[(randint(0, len(l_googleIDs) - 1))]
        self.google.googleLOGIN(l_id[0], l_id[1])












