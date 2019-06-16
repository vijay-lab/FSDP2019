# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 15:24:40 2019

@author: TAPAN
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

crime = pd.read_csv('crime_data.csv') 
features = crime.iloc[:, [1,2,4]].values

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

features = sc.fit_transform(features)

# Applying PCA
from sklearn.decomposition import PCA
pca = PCA(n_components = 2)
features = pca.fit_transform(features)
explained_variance = pca.explained_variance_ratio_

from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = 0)
pred_cluster1 = kmeans.fit_predict(features)

#DO scaling of x and y
# Visualising the clusters
#plt.scatter(features[:,0][y_kmeans == 0], features[:,1][y_kmeans == 0], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(features[pred_cluster1 == 0, 0], features[pred_cluster1 == 0, 1], c = 'blue', label = 'Cluster 1')
plt.scatter(features[pred_cluster1 == 1, 0], features[pred_cluster1 == 1, 1], c = 'red', label = 'Cluster 2')
plt.scatter(features[pred_cluster1 == 2, 0], features[pred_cluster1 == 2, 1], c = 'green', label = 'Cluster 3')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
plt.title('Clusters of datapoints')
plt.xlabel('X Cordindates')
plt.ylabel('Y Cordinates')
plt.legend()
plt.show()