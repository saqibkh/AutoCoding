#!/usr/bin/python

from pyvirtualdisplay import Display
from selenium import webdriver

display = Display(visible=0, size=(800, 600))
display.start()
driver = webdriver.Firefox()
driver.get('https://www.youtube.com/watch?v=iO62OyWfUY0')
print driver.title
