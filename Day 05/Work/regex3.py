# -*- coding: utf-8 -*-
"""
Created on Sat May 11 18:31:12 2019

@author: TAPAN
"""
import re

card_detail=input("Enter card number>>\n")


card_value=re.match(r'^[456]{1}[0-9]{3}-?[0-9]{4}-?[0-9]{4}-?[0-9]{4}-?$',card_detail)

card_search_repeat=re.()
