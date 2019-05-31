



import matplotlib.pyplot as plt   

from selenium import webdriver

url = "https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area"

driver = webdriver.Chrome("D:\Forsk\Day 08\Work\chromedriver.exe")

driver.get(url)    # Opening the submission url

state_list=[]
national_share_list=[]

for i in range(3,9):
    states=driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/table[2]/tbody/tr[{}]/td[2]/a'.format(i))
    state_list.append(states.text)
#    //*[@id="mw-content-text"]/div/table[2]/tbody/tr[1]/td[2]/a
    national_share=driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/table[2]/tbody/tr[{}]/td[5]'.format(i))
    national_share_list.append(national_share.text)
    

labels = state_list
sizes = national_share_list
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','blue','red']
explode = (0.1, 0, 0, 0,0,0)
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=0)

