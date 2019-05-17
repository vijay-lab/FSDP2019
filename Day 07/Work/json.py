# -*- coding: utf-8 -*-
"""
Created on Tue May 14 16:47:16 2019

@author: TAPAN
"""
from datetime import datetime as dt
import json


City=input("Enter city name\n>>")

import requests

url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q="
url3 = City
url4 = "&appid=e9185b28e9969fb7a300801eb026de9c"

url = url1 + url2 + url3 + url4
print (url)


response = requests.get(url)
# requests.get(url,params={"q":"Jaipur", "appid"="e9185b28e9969fb7a300801eb026de9c"})
response.content

# Content in binary form
print (type(response.text))

my_data = json.loads(response.text)

print(" longitude and Latitute of {} is".format(City),my_data['coord']['lon'],"and",my_data['coord']['lat'])

print(" Weather Condition of {} is".format(City),my_data['weather'][0]['main'])

print(" Wind Speed in in {} is ".format(City),my_data['wind']['speed'],"km/h")

print(" Sun Rise and Set timing in {} is".format(City), dt.fromtimestamp(my_data['sys']['sunrise']),"and",dt.fromtimestamp(my_data['sys']['sunrise']))