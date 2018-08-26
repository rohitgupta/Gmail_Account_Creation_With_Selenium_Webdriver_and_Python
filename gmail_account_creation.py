#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 17:44:47 2018

@author: rohit
"""

from selenium import webdriver
import time
url = 'http://www.gmail.com/'
firstname = input('Please enter First Name:\n')
lastname = input('Please enter Last Name:\n')
username = input('Please enter username Name:\n')
password = input('Please enter Password:\n')
ConfirmPassword = input('Please enter ConfirmPassword:\n')
driver = webdriver.Chrome()
driver.get(url)
print ('Gmail Page is open successfully.')
driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[2]/div/div/content/span').click()
print('Create Account is clicked')
driver.find_element_by_id('firstName').send_keys(firstname)
print ('Enter First Name')
driver.find_element_by_id('lastName').send_keys(lastname)
print ('Enter Last Name')
driver.find_element_by_id('username').send_keys(username)
print ('enter username')
driver.find_element_by_name('Passwd').send_keys(password)
print ('Password Enter Successfully')
print ("Start : %s" % time.ctime())
time.sleep(5)
print ("End : %s" % time.ctime())
driver.find_element_by_xpath('//*[@aria-label="Confirm password"]').send_keys(ConfirmPassword)
print ('Confirm Password Successfully')
#driver.find_element_by_xpath('//*[@id="view_container"]/form/div[2]/div/div[1]/div[3]/div[2]/div/content/span/span[1]/svg/path[2]').click()
driver.find_element_by_xpath('//*[@id="accountDetailsNext"]/content/span').click()
print ('Next Button click')
#driver.quit()
