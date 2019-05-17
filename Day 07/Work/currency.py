# -*- coding: utf-8 -*-
"""
Created on Tue May 14 17:10:27 2019

@author: TAPAN
"""
import json
import requests
amount=int(input("Enter amount to convert \n>>"))


url1 = "https://free.currconv.com/api/v7/convert"


url2 = "?q="
url3 ="usd"
url4 = "_INR&compact=ultra&apiKey=91d5d4382cf5d11bd3ea"

url = url1 + url2 + url3 + url4
print (url)


response = requests.get(url)
# requests.get(url,params={"q":"Jaipur", "appid"="e9185b28e9969fb7a300801eb026de9c"})
response.content

# Content in binary form
print (type(response.content))


#print ("Status code: " + str(response.status_code))
#print ("Headers : " + str(response.headers))
#print ("Data : " + response.text)



my_data = json.loads(response.text)
current_val_of_inr=my_data["USD_INR"]
val=float(my_data["USD_INR"])

print("current value of {} usd to inr".format(amount),val*amount)

