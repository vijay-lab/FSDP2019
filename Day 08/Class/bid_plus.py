
"""
Code Challenge:
  Name: 
    Bid Plus
  Filename: 
    bid_plus.py
  Problem Statement:
      USE SELENIUM
      Write a Python code to Scrap data and download data from given url.
      url = "https://bidplus.gem.gov.in/bidlists"
      Make list and append given data:
          1. BID NO
          2. items
          3. Quantity Required
          4. Department Name And Address
          5. Start Date/Time(Enter date and time in different columns)
          6. End Date/Time(Enter date and time in different columns)
     Make a csv file add all data in it.
      csv Name: bid_plus.csv
"""
    
from selenium import webdriver
from time import sleep
import csv

bids=[]
itemss=[]
quantitys=[]
addresss=[]
start_date_time=[]
end_date_time=[]
start_dates=[]
start_time=[]
end_time=[]
end_dates=[]

options = webdriver.ChromeOptions()
browser = webdriver.Chrome(chrome_options=options)
url="https://bidplus.gem.gov.in/servicelists"

browser.get(url)

for i in range(1,11):
    path_bid='''//*[@id="pagi_content"]/div['''+str(i)+''']/div[1]/p[1]/a'''
    try:
        bid_no=browser.find_element_by_xpath(path_bid)
    except Exception as e:
        print("[ERROR]: "+str(e))
        break
    bids.append(bid_no.text)
    
    path_items='''//*[@id="pagi_content"]/div['''+str(i)+''']/div[2]/p[1]/span'''
    items=browser.find_element_by_xpath(path_items)
    itemss.append(items.text)
    
    path_quantity='''//*[@id="pagi_content"]/div['''+str(i)+''']/div[2]/p[2]/span'''
    quantity=browser.find_element_by_xpath(path_quantity)
    quantitys.append(quantity.text)
    
    path_address='''//*[@id="pagi_content"]/div['''+str(i)+''']/div[3]/p[2]'''
    address=browser.find_element_by_xpath(path_address)
    addresss.append(address.text)
    
    path_start_date='''//*[@id="pagi_content"]/div['''+str(i)+''']/div[4]/p[1]/span'''
    start_date=browser.find_element_by_xpath(path_start_date)
    start_date_time.append(start_date.text)
    
    path_end_date='''//*[@id="pagi_content"]/div['''+str(i)+''']/div[4]/p[2]/span'''
    end_date=browser.find_element_by_xpath(path_end_date)
    end_date_time.append(end_date.text)
    
    bid_no.click()
sleep(10)
browser.quit() 

for z in range(0,len(start_date_time)):
    start_dates.append(start_date_time[z][:10])
    start_time.append(start_date_time[z][10:])
    end_dates.append(end_date_time[z][:10])
    end_time.append(end_date_time[z][10:])
  



with open("bid_plus.csv","r+") as file:
    write=csv.writer(file,delimiter=",")
    write.writerow(["BID NO","Items","Quantity","Address","Start Date","Start Time","End Time","End Time"])
    for i in range(len(bids)):
        tmp_lst = [bids[i],itemss[i],quantitys[i],addresss[i],start_dates[i],start_time[i],end_dates[i],end_time[i]]
        for i in range(len(tmp_lst)):
            tmp_lst[i] = tmp_lst[i].replace("\n"," ")
        write.writerow(tmp_lst)
  
      