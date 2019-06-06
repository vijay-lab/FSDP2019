"""
Code Challenge 01: (Prostate Dataset)

This is the Prostate Cancer dataset. Perform the train test split before you apply the model.
(a) Train the unregularized model (linear regressor) and calculate the mean squared error.
(b) Apply a regularized model now - Ridge regression and lasso as well and check the mean squared error.

(2) Can we predict whether lpsa is high or low, from other variables?

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


from sklearn.linear_model import LinearRegression,Lasso,Ridge,LogisticRegression

lr = LinearRegression ()
lr_lasso = Lasso() 
lr_ridge =  Ridge() 

lr.fit(features_train, label_train)
lr_lasso.fit(features_train, label_train)
lr_ridge.fit(features_train, label_train)

predict_test_lm =	lr.predict(features_test ) 
predict_test_lasso = lr_lasso.predict (features_test) 
predict_test_ridge = lr_ridge.predict (features_test)

from sklearn import metrics
from sklearn.metrics import confusion_matrix as cm

print ("Lasso Regression Mean Square Error (MSE) for TEST data is") 
print (np.round (metrics .mean_squared_error(label_test, predict_test_lasso),2))

print ("Ridge Regression Mean Square Error (MSE) for TEST data is") 
print (np.round (metrics .mean_squared_error(label_test, predict_test_ridge),2))

"""
(2) Can we predict whether lpsa is high or low, from other variables?
"""
features_b=features
label_b=cancer_df['lpsa'].apply(lambda x:1 if cancer_df['lpsa'].mean()<x else 0)
featuresb_train, featuresb_test, labelb_train, labelb_test = train_test_split(features_b, label_b, test_size=0.20, random_state=0)  

lr=LogisticRegression()
lr.fit(featuresb_train,labelb_train)
labb_predict=lr.predict(featuresb_test)

cm=cm(labelb_test,labb_predict)

"""

Code Challenges 02: (House Data)
This is kings house society data.
In particular, we will: 
• Use Linear Regression and see the results
• Use Lasso (L1) and see the resuls
• Use Ridge and see the score

"""
