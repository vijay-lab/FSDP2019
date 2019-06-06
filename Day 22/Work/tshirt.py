# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 16:23:54 2019

@author: TAPAN


2. (Create a program that fulfills the following specification.)
tshirts.csv


T-Shirt Factory:

You own a clothing factory. You know how to make a T-shirt given the height and weight of a customer.

You want to standardize the production on three sizes: small, medium, and large. How would you figure out the actual size
of these 3 types of shirt to better fit your customers?

Import the tshirts.csv file and perform Clustering on it to make sense out of the data as stated above.


 
 """
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans


tshirt_df = pd.read_csv('tshirts.csv')
features = tshirt_df.iloc[:, [1, 2]].values
plt.scatter(features[:,0],features[:,1])
plt.title('Clusters of datapoints')
plt.xlabel('Height')
plt.ylabel('Weight')
plt.legend()
plt.show()


## no of clusters can be found with this
#for n_clusters in range(2,6):
#    clusterer = KMeans (n_clusters=n_clusters)
#    preds = clusterer.fit_predict(features)
#    centers = clusterer.cluster_centers_
#
#    score = silhouette_score (features, preds, metric='euclidean')
#    print("For n_clusters =", n_clusters,
#          "The average silhouette_score is :", score)

#For 3 clusters
  
kmeans_3 = KMeans(n_clusters = 3, init = 'k-means++', random_state = 0)
pred_cluster_3 = kmeans_3.fit_predict(features)

plt.scatter(features[pred_cluster_3 == 0,0], features[pred_cluster_3==0,1],c='red',label='Cluster 1')
plt.scatter(features[pred_cluster_3 == 1,0], features[pred_cluster_3==1,1],c='green',label='Cluster 2')
plt.scatter(features[pred_cluster_3 == 2,0], features[pred_cluster_3==2,1],c='black',label='Cluster 3')
plt.title('Clusters of datapoints')
plt.xlabel('Height')
plt.ylabel('Weight')
plt.legend()
plt.show()