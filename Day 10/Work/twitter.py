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

from selenium import webdriver
import tweepy 
  
# personal details 
consumer_key ="yourkey"
consumer_secret ="yourkey"
access_token ="yourkey"
access_token_secret ="yourkey"
# authentication of consumer key and secret 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
# authentication of access token and secret 
auth.set_access_token(access_token, access_token_secret) 
api = tweepy.API(auth) 

source = "https://www.astroyogi.com"

driver = webdriver.Chrome(r"D:\Forsk Wkspace\FSDP2019\Day 08\Work\chromedriver.exe")
driver.get(source)
driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div[7]').click()

libra_horoscope=[]



libra_horoscope.append(driver.find_element_by_xpath('//*[@id="today1"]/p/span').text)
index_to_remove=libra_horoscope[0].find('\n')


horoscope=libra_horoscope[0][0:index_to_remove]
print(horoscope)

split_loc=275
begin_loc=0
i=1
while len(horoscope)>=275:
    horoscopex='horoscope' + str(i)
    horoscopex=horoscope[begin_loc:split_loc]
    begin_loc=begin_loc+split_loc
    split_loc=split_loc+(len(horoscope)-split_loc)
    i+=1
    api.update_status(status =horoscopex) 
    



  

  


