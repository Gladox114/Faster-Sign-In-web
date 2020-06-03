#!/usr/bin/python3

# config #
url = "http://172.18.4.1"
name = "username"
passcode = "yourcode"
##########

from selenium import webdriver
driver = webdriver.Firefox()
driver.get(url)
driver.find_element_by_name("user").send_keys("realpython")
