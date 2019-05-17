# -*- coding: utf-8 -*-
"""
Created on Thu May 16 17:45:00 2019

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
end_time=[]


for val in range(1,11):
    bid_id.append(driver.find_element_by_xpath('//*[@id="pagi_content"]/div[{}]/div[1]/p[1]/a'.format(val)).text)
    item.append(driver.find_element_by_xpath('//*[@id="pagi_content"]/div[{}]/div[2]/p[1]/span'.format(val)).text)
    quantity.append(driver.find_element_by_xpath('//*[@id="pagi_content"]/div[{}]/div[2]/p[2]/span'.format(val)).text)
    dept_name_address.append(driver.find_element_by_xpath('//*[@id="pagi_content"]/div[{}]/div[3]/p[2]'.format(val)).text)
    start_date.append(driver.find_element_by_xpath('//*[@id="pagi_content"]/div[{}]/div[4]/p[1]/span'.format(val)).text)
    end_date.append(driver.find_element_by_xpath('//*[@id="pagi_content"]/div[{}]/div[4]/p[2]/span'.format(val)).text)
    

start_date_list=[i[:i.find(' ')] for i in start_date]
start_time=[i[i.find(' ') + 1:] for i in start_date]

end_date_list=[i[:i.find(' ')] for i in end_date]
end_time=[i[i.find(' ') + 1:] for i in end_date]


    
col_name = ["Bid No.","Item","Quantity","Dept name & address","Start Date","End Date","Start Time","End Time"]
col_data = OrderedDict(zip(col_name,[bid_id,item,quantity,dept_name_address,start_date_list,end_date_list,start_time,end_time]))



print(bid_id)
print(item)
print(quantity)
print(start_time)
print (end_time)




import mysql.connector 
# connect to  MySQL server along with Database name

conn = mysql.connector.connect(user='CUQQMCS80b', password='TRLKYhvlac',
                              host='remotemysql.com', database = 'CUQQMCS80b')
#, database = 'forsk_test'

# creating cursor
c = conn.cursor()

# STEP 0
#c.execute("DROP DATABASE employee;")

# STEP 1
#c.execute("CREATE DATABASE GeM;")

# STEP 2
#c.execute("DROP Table dat;")


# STEP 3
c.execute ("""CREATE TABLE dat(
          Bid_id TEXT,
          item  TEXT,
          Quantity INTEGER,
          Dept_name_address TEXT,
          Start_Date TEXT,
          End_Date TEXT,
          Start_Time TEXT,
          End_Time TEXT
          )""")


for i in range(10):
    c.execute("INSERT INTO dat VALUES ('{}','{}',{},'{}','{}','{}','{}','{}')".format (bid_id[i],item[i],quantity[i],dept_name_address[i],start_date[i],end_date[i],start_time[i],end_time[i]))






# c.execute("INSERT INTO employee VALUES ({},'{}', '{}', {})".format(idd, first,last,pay))


c.execute("SELECT * FROM dat")

conn.commit()
conn.close()

# STEP 5
# returns one or otherwise None as a tuple
#print ( c.fetchone()) 
#
## returns one or otherwise None as a tuple
#print ( c.fetchmany(2)) 
#
## returns a list of tuples
#print ( c.fetchall() )
#
#
## Since now the cursor has read all the rows and we are at End
## So again fetching the records from the database
#c.execute("SELECT * FROM employees")
#
#
## STEP 6
#df = DataFrame(c.fetchall())  # putting the result into Dataframe
#df.columns = ["id","first","last","pay"]



































