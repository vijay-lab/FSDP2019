# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 15:38:26 2019

@author: TAPAN
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans

delivery_df = pd.read_csv('deliveryfleet.csv')
features = delivery_df.iloc[:, [1, 2]].values
plt.scatter(features[:,0],features[:,1])


# for 2 cluster
kmeans = KMeans(n_clusters = 2, init = 'k-means++', random_state = 0)
pred_cluster = kmeans.fit_predict(features)
# Visualising the clusters
#plt.scatter(features[:,0][y_kmeans == 0], features[:,1][y_kmeans == 0], s = 100, c = 'red', label = 'Cluster 1')
# [pred_cluster == 0, 0] cluster 0 column 0
#[pred_cluster == 0, 1] cluster 0 column 1
plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'Cluster 1')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'Cluster 2')

plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
plt.title('Clusters of datapoints')
plt.xlabel('X Cordindates')
plt.ylabel('Y Cordinates')
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
    
    
#For 4 clusters
  
kmeans_4 = KMeans(n_clusters = 4, init = 'k-means++', random_state = 0)
pred_cluster_4 = kmeans_4.fit_predict(features)

plt.scatter(features[pred_cluster_4 == 0, 0], features[pred_cluster_4 == 0, 1], c = 'blue', label = 'Cluster 1')
plt.scatter(features[pred_cluster_4== 1, 0], features[pred_cluster_4 == 1, 1], c = 'red', label = 'Cluster 2')
plt.scatter(features[pred_cluster_4== 2, 0], features[pred_cluster_4 == 2, 1], c = 'green', label = 'Cluster 3')
plt.scatter(features[pred_cluster_4== 3, 0], features[pred_cluster_4 == 3, 1], c = 'silver', label = 'Cluster 4')
plt.scatter(kmeans_4.cluster_centers_[:, 0], kmeans_4.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
plt.title('Clusters of datapoints')
plt.xlabel('Distance travelled')
plt.ylabel('Speed')
plt.legend()
plt.show()
    
