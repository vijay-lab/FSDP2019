# -*- coding: utf-8 -*-
"""
Created on Tue May 14 22:04:22 2019

@author: TAPAN
"""

import json
import requests

Host = "https://en5n49v825de8.x.pipedream.net/"


data = {"firstname":"dev","language":"English"}

headers = {"Content-Type":"application/json","Content-Length":len(data),"data":json.dumps(data)}

def post_method():
    response = requests.post(Host,data,headers)
    return response

print ( post_method().text )


def get_method():
    response = requests.get("https://en5n49v825de8.x.pipedream.net/")
    return response

print (get_method().text)