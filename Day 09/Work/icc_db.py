# -*- coding: utf-8 -*-
"""
Created on Thu May 16 23:58:14 2019

@author: TAPAN
"""

import sqlite3


from bs4 import BeautifulSoup
import requests



host_url = "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
host = requests.get(host_url).text
#or
#source = urllib.request.urlopen(wiki)

soup = BeautifulSoup(host,"lxml")

print (soup.prettify())

all_tables=soup.find_all('table')

print (all_tables)

right_table=soup.find('table', class_='table')

print (right_table)


#Generate lists
A=[]
B=[]
C=[]
D=[]
E=[]


for row in right_table.findAll('tr'):
    column = row.findAll('td')
    if len(column) == 5:
        A.append(column[0].text.strip())
        B.append(column[1].text.strip())
        C.append(column[2].text.strip())
        D.append(column[3].text.strip())
        E.append(column[3].text.strip())
        
        
        






# File based database ( connects if exits or creates a new one if it does not exists ) 
conn = sqlite3.connect ( 'iccrankings.db' )


# creating cursor
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS Rankings")


#c.execute("Drop Table Rankings")
# STEP 1
# www.sqlite.org/datatype3.html
c.execute ("""CREATE TABLE Rankings(
          Positions INTEGER,
          country  TEXT,
          weighted matches INTEGER,
          Points INTEGER,
          Rankings INTEGER
          )""")


for i in range(16):
    c.execute("INSERT INTO Rankings VALUES ('{}','{}', '{}', '{}','{}')".format (A[i],B[i],C[i],D[i],E[i]))


# STEP 3
c.execute("SELECT * FROM Rankings")
# "SELECT * FROM employees WHERE last = 'Fernandes' "



# STEP 4
# returns one or otherwise None as a tuple
print ( c.fetchone()) 

# returns one or otherwise None as a tuple
print ( c.fetchmany(2)) 

# returns a list of tuples
print ( c.fetchall() )


# Since now the cursor has read all the rows and we are at End
# So again fetching the records from the database
c.execute("SELECT * FROM Rankings")

c.arraysize
# STEP 5


# STEP 6
# commits the current transaction 
conn.commit()

# STEP 7
# closing the connection 
#conn.close()