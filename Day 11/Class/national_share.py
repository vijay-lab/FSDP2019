"""
Code Challenge

https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area


Scrap the data from State/Territory and National Share (%) columns for top 6 
states basis on National Share (%). 
Create a Pie Chart using MatPlotLib and explode the state with largest national share %.

"""


# scraping and pie chart

import requests as re
from bs4 import BeautifulSoup
import pandas as pd
from collections import OrderedDict


url = "https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area"


data = re.get(url)

all_table= soup.find_all('table')

right_table= soup.find('table', class_= 'wikitable')


A = []
B = []

for row in right_table.findAll('tr'):
    cells = row.findAll('th')

    if len(cells) == 5:
        A.append(cells[1].text.strip())
        B.append(cells[4].text.strip())
        


final_table= ["states", "National share"]

table_data = OrderedDict(zip(final_table,[A,B]))

data = pd.DataFrame(table_data) 


labels = 'States', 'national share'

colors = ['blue', 'orange']


plt.pie(,explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', startangle=0)