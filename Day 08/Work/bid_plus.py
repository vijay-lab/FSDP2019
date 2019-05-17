# -*- coding: utf-8 -*-
"""
Created on Wed May 15 17:05:34 2019

@author: TAPAN
"""

import pandas as pd
from selenium import webdriver
from collections import OrderedDict




source = "https://bidplus.gem.gov.in/bidlists"


#driver = webdriver.Firefox(executable_path=r'C:/Users/hp/Downloads/geckodriver')
driver = webdriver.Chrome(r"D:\Forsk\Day 08\Work\chromedriver.exe")

driver.get(source)    # Opening the submission url




right_table=driver.find_element_by_xpath('//*[@id="pagi_content"]/div[1]')


#//*[@id="pagi_content"]/div[1]/div[1]/p[1]/a
#//*[@id="pagi_content"]/div[2]/div[1]/p[1]/a

#//*[@id="pagi_content"]/div[1]/div[2]/p[1]/span
#//*[@id="pagi_content"]/div[2]/div[2]/p[1]/span


#//*[@id="pagi_content"]/div[1]/div[2]/p[2]/span
#
#//*[@id="pagi_content"]/div[1]/div[3]/p[2]
#
#
#//*[@id="pagi_content"]/div[1]/div[4]/p[1]/span
#
#//*[@id="pagi_content"]/div[1]/div[4]/p[2]/span


bid_id=[]
item=[]
quantity=[]
dept_name_address=[]
start_date=[]
end_date=[]
start_time=[]




for val in range(1,11):
    bid_id.append(driver.find_element_by_xpath('//*[@id="pagi_content"]/div[{}]/div[1]/p[1]/a'.format(val)).text)
    item.append(driver.find_element_by_xpath('//*[@id="pagi_content"]/div[{}]/div[2]/p[1]/span'.format(val)).text)
    quantity.append(driver.find_element_by_xpath('//*[@id="pagi_content"]/div[{}]/div[2]/p[2]/span'.format(val)).text)
    dept_name_address.append(driver.find_element_by_xpath('//*[@id="pagi_content"]/div[{}]/div[3]/p[2]'.format(val)).text)
    start_date.append(driver.find_element_by_xpath('//*[@id="pagi_content"]/div[{}]/div[4]/p[1]/span'.format(val)).text)
    end_date.append(driver.find_element_by_xpath('//*[@id="pagi_content"]/div[{}]/div[4]/p[2]/span'.format(val)).text)
    

start_date_list=[i[:i.find(' ')] for i in start_date]
start_time_list=[i[i.find(' ') + 1:] for i in start_date]


    
col_name = ["Bid No.","Item","Quantity","Dept name & address","Start Date","End Date"]
col_data = OrderedDict(zip(col_name,[bid_id,item,quantity,dept_name_address,start_date,end_date,]))
df = pd.DataFrame(col_data) 
df.to_csv("AgriCsv.csv")



print(bid_id)
print(item)
print(quantity)




