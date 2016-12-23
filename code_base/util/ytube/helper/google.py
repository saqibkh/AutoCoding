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


class google():

    ##
	# This file contain the MAIN class for running all youtube automation
	#

    def __init__(self, i_driver):
        self.youtube_baseurl = "https://google.com"
        self.driver = i_driver


    def googleLOGIN(self, i_id, i_passwd):
        self.driver.get("https://www.google.com/")
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_id("gb_70").click()
        time.sleep(1)
        self.driver.find_element_by_id("Email").clear()
        self.driver.find_element_by_id("Email").send_keys(i_id)
        self.driver.find_element_by_id("next").click()
        time.sleep(1)
        self.driver.find_element_by_id("Passwd").clear()
        self.driver.find_element_by_id("Passwd").send_keys(i_passwd)
        self.driver.find_element_by_id("signIn").click()
        time.sleep(1)









