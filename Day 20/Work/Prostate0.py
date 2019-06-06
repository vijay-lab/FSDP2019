"""
Code Challenge 01: (Prostate Dataset)
Load the dataset from given link: 
pd.read_csv("http://www.stat.cmu.edu/~ryantibs/statcomp/data/pros.dat")

This is the Prostate Cancer dataset. Perform the train test split before you apply the model.

(a) Can we predict lpsa from the other variables?
(1) Train the unregularized model (linear regressor) and calculate the mean squared error.
(2) Apply a regularized model now - Ridge regression and lasso as well and check the mean squared error.

(b) Can we predict whether lpsa is high or low, from other variables?



Code Challenges 02: (House Data)
This is kings house society data.
In particular, we will: 
• Use Linear Regression and see the results
• Use Lasso (L1) and see the resuls
• Use Ridge and see the score

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

cancer_df=pd.read_csv("http://www.stat.cmu.edu/~ryantibs/statcomp/data/pros.dat",sep=" ")

features=cancer_df.iloc[:,0:-1].values
label=cancer_df.iloc[:,-1].values

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()  
features = sc.fit_transform(features)  

from sklearn.model_selection import train_test_split  
features_train, features_test, label_train, label_test = train_test_split(features, label, test_size=0.20, random_state=0)  

from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(features_train,label_train)

label_pred = lr.predict(features_test) 

from sklearn import metrics

MSE=metrics.mean_squared_error(label_test, label_pred)
MAE=metrics.mean_absolute_error(label_test, label_pred)
RMSE=np.sqrt(metrics.mean_squared_error(label_test, label_pred))
print('Mean Absolute Error:', MAE)  
print('Mean Squared Error:', MSE)  
print('Root Mean Squared Error:',RMSE ) 
np.mean(label)*(10/100)
"""
RMSE should be less then np.mean(label)*(10/100)
"""

""""
a(2).
""""

from sklearn.linear_model import Lasso,Ridge,ElasticNet


lr= LinearRegression ()
lr_lasso = Lasso() 
lr_ridge =  Ridge() 
lr_elastic = ElasticNet() 

lr.fit(features_train, label_train)
lr_lasso.fit(features_train, label_train)
lr_ridge.fit(features_train, label_train)
lr_elastic.fit(features_train, label_train)

print ("mean Square Value for Simple Regresssion TEST data is-",MSE) 
MSE=metrics.mean_squared_error(label_test, label_pred)


print ("mean Square Value for Lasso Regresssion TEST data is-")
print (np.round (lr_lasso.score(features_test,label_test)*100,2))

print ("mean Square Value for Ridge Regresssion TEST data is-")
print (np.round (lr_ridge.score(features_test,label_test)*100,2))

print ("RSquare Value for Elastic Net Regresssion TEST data is-")
print (np.round (lr_elastic.score(features_test,label_test)*100,2))

predict_test_lr =	lr.predict(features_test ) 
predict_test_lasso = lr_lasso.predict (features_test) 
predict_test_ridge = lr_ridge.predict (features_test)
predict_test_elastic = lr_elastic.predict(features_test)