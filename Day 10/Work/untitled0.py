# -*- coding: utf-8 -*-
"""
Created on Sun May 19 17:37:51 2019

@author: TAPAN

Code Challenge 5

Fortune Teller (Horoscope)

A program that checks your horoscope on various astrology sites and puts them 
together for you each day. The code should share the Horoscope on Tweeter account
 of the user.


"""

import pandas as pd
from selenium import webdriver
from collections import OrderedDict

source = "https://www.astrology.com/horoscope/daily/libra.html"

driver = webdriver.Chrome(r"D:\Forsk\Day 08\Work\chromedriver.exe")
driver.get(source)


libra_horoscope=[]


libra_horoscope.append(driver.find_element_by_xpath('/html/body/section/section[1]/div[2]/main/p[1]'))




#driver = webdriver.Firefox(executable_path=r'C:/Users/hp/Downloads/geckodriver')

