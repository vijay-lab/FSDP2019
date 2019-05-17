# -*- coding: utf-8 -*-
"""
Created on Thu May 16 14:29:08 2019

@author: TAPAN
"""

from  selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as BS

#url = "http://keralaresults.nic.in/sslc2018rgr8364/swr_sslc.htm"
url = "https://padhai.onefourthlabs.in/users/sign_in"



browser = webdriver.Chrome("D:\Forsk\Day 08\Work\chromedriver.exe")
browser.get(url)


 
uname = browser.find_element_by_xpath('//*[@id="user[email]"]')
un="tapanvijayvargiya@gmail.com"


passw = browser.find_element_by_xpath('//*[@id="user[password]"]')

rem_me = browser.find_element_by_xpath('//*[@id="user[remember_me]"]') 

sgn_in =  browser.find_element_by_xpath('//*[@id="sign-in"]')

pw="Vijay@padhai"
uname.send_keys(un)

passw.send_keys(pw)

rem_me.click()

sgn_in.click()

sleep(2)


get_school_result = browser.find_element_by_xpath('//*[@id="ctrltr"]/td[3]/input[1]')
get_school_result.click()


sleep(5)
 
html_page = browser.page_source

soup = BS(html_page)


sleep(3)


browser.quit()
