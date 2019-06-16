# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 17:09:12 2019

@author: TAPAN

Q3.Code Challenge -
Data: "data.csv"

This data is provided by The Metropolitan Museum of Art Open Access
1. Visualize the various countries from where the artworks are coming.
2. Visualize the top 2 classification for the artworks
3. Visualize the artist interested in the artworks
4. Visualize the top 2 culture for the artworks
"""




import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
art_data = pd.read_csv('data.csv')

# 1
Freq_by_country=art_data['Country'].value_counts()
plt.pie(Freq_by_country,labels=Freq_by_country.index,autopct='%1.2f%%')

art_data['Country'].value_counts()


fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

recipe = Freq_by_country.index

data = Freq_by_country

wedges, texts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=-40)

bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
kw = dict(arrowprops=dict(arrowstyle="-"),
          bbox=bbox_props, zorder=0, va="center")

for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1)/2. + p.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    connectionstyle = "angle,angleA=0,angleB={}".format(ang)
    kw["arrowprops"].update({"connectionstyle": connectionstyle})
    ax.annotate(recipe[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                horizontalalignment=horizontalalignment, **kw)

ax.set_title("Matplotlib bakery: A donut")

plt.show()

# 2 Visualize the top 2 classification for the artworks

classification=art_data['Classification'].value_counts()

plt.pie(classification[:2],labels=classification[:2].index,autopct='%1.2f%%',startangle=90)

# 3. Visualize the artist interested in the artworks
list=[]
for i in range(44):
    data=art_data.iloc[:,i].value_counts()
    list.append(data)

# 4. Visualize the top 2 culture for the artworks








#
#x = Freq_by_country.index
#y = Freq_by_country
#porcent = 100.*y/y.sum()
#
#patches, texts = plt.pie(y, startangle=90, radius=1.2)
#labels = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(x, porcent)]
#
#sort_legend = True
#if sort_legend:
#    patches, labels, dummy =  zip(*sorted(zip(patches, labels, y),
#                                          key=lambda x: x[2],
#                                          reverse=True))
#
#plt.legend(patches, labels, loc='left center', bbox_to_anchor=(-0.1, 1.),
#           fontsize=8)
#
#plt.savefig('piechart.png', bbox_inches='tight')
#
#
#
