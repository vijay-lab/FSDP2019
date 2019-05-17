
# Solution for the Code Challenge of ICC Ranking 
from bs4 import BeautifulSoup
import pandas as pd
import requests

lnk = "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
pg = requests.get(lnk).text
sp = BeautifulSoup(pg,"lxml")

my_tab = sp.find('table',class_="table")


A=[]
B=[]
C=[]
D=[]
E=[]


for bdy in my_tab.find_all("tbody"):
    for row in bdy.find_all("tr"):
        cel = row.find_all('td')
        A.append(cel[0].text.strip())
        B.append(cel[1].text.strip())
        C.append(cel[2].text.strip())
        D.append(cel[3].text.strip())
        E.append(cel[4].text.strip())

df = pd.DataFrame()
df["Position"]=A
df["Team"]=B
df["Matches"]=C
df["Points"]=D
df["Rating"]=E
  
df.to_csv("data/ODI_Ranking_2017.csv", index=False)


