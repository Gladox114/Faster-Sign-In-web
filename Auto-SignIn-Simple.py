#!/usr/bin/python3

# config #
url = "http://172.18.4.1"
username = "yourusername"
passcode = "yourpasscode"
delay = 5 # delay till the browser closes after sign in. The server needs to process your sign in
##########

# import #
from selenium import webdriver
import time
##########

#set your web driver
driver = webdriver.PhantomJS() #needs PhantomJS
#driver = webdriver.Firefox() #needs geckodriver

#Open the page
driver.get(url)

#Find the Username box
driver.find_element_by_name("user").send_keys(username)

#Find the password box
driver.find_element_by_name("password").send_keys(passcode)

#Find the check box for terms of use
driver.find_element_by_name("visitor_accept_terms").click()

#Find the login button
test=driver.find_element_by_xpath("//input[@value='Log In']").click()


time.sleep(delay)
driver.quit()
