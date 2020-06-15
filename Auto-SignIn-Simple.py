#!/usr/bin/python3

# config #
username = "username"
passcode = "passcode"

browser = "firefox" # phantomjs,firefox,chrome
#url = "http://google.com"
url = "http://172.18.4.1"
#delay = 5 # delay till the browser closes after sign in. The server needs to process your sign in
##########

# import #
from selenium import webdriver
import time
##########

#set your web driver
if browser == "phantomjs":
    driver = webdriver.PhantomJS() #needs PhantomJS
elif browser == "firefox":
    driver = webdriver.Firefox() #needs geckodriver
elif browser == "chrome":
    driver = webdriver.Chrome() #needs N/A not sure if this works

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
"""
# Cheaply closing the browser
time.sleep(delay)
driver.quit()
"""
while True:
	if driver.current_url.find("google"):
		print("pass cuz of",driver.current_url)
		driver.quit()
		break
	time.sleep(0.1)
