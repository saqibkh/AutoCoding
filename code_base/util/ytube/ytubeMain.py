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


    def runTest(self):
        URLs = ytubeConstants.URLS;
        for url in URLs:
            self.openBrowser()
            self.driver.get(url[0])
            self.driver.implicitly_wait(100)
            time.sleep((url[1]*60) - (randint(0,60)))
            self.tearDown()
        return Constants.SUCCESS


    def tearDown(self):
        self.driver.quit()

    def pauseORresume(self):
        self.driver.find_element_by_css_selector("button.ytp-play-button.ytp-button").click()

    def nextVideo(self):
        self.driver.find_element_by_css_selector("a.ytp-next-button.ytp-button").click()

    def googleLOGIN(self):
        self.driver.get("https://www.google.com/")
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_id("gb_70").click()
        self.driver.find_element_by_id("Email").clear()
        self.driver.find_element_by_id("Email").send_keys("skhansa00001@gmail.com")
        self.driver.find_element_by_id("next").click()
        self.driver.find_element_by_id("Passwd").clear()
        self.driver.find_element_by_id("Passwd").send_keys("saqibkhan1992")
        self.driver.find_element_by_id("signIn").click()









