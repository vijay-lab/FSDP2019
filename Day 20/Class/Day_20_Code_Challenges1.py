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

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split as TTS
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


cancer_df=pd.read_csv("http://www.stat.cmu.edu/~ryantibs/statcomp/data/pros.dat",delimiter=" ")
label=cancer_df['lpsa'].values
feature=cancer_df.iloc[:,:-1].values

x_train,x_test,y_train,y_test=TTS(feature,label,test_size=0.20,random_state=0)

lr_a1=LinearRegression()
lr_a1.fit(x_train,y_train)

y_pred=lr_a1.predict(x_test)
Compare_pred = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})  
MSE=mean_squared_error(y_test,y_pred)

score_train=lr_a1.score(x_train,y_train)
score_test=lr_a1.score(x_test,y_test)

## Regularized model
from sklearn.linear_model import Lasso,Ridge,ElasticNet
lr_la=Lasso()
lr_ri=Ridge()
lr_en=ElasticNet()

#fitting & predicting the data
lr_la.fit(x_train,y_train)
y_pred_la=lr_la.predict(x_test)
Compare_pred_la = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred_la})  
MSE_la=mean_squared_error(y_test,y_pred_la)


lr_ri.fit(x_train,y_train)
y_pred_ri=lr_ri.predict(x_test)
MSE_ri=mean_squared_error(y_test,y_pred_ri)

lr_en.fit(x_train,y_train)
y_pred_en=lr_en.predict(x_test)
MSE_en=mean_squared_error(y_test,y_pred_en)


print ("RSquare Value for Lasso Regresssion TEST data is-")
print (np.round (lr_la.score(x_test,y_test)*100,2))

print ("RSquare Value for Ridge Regresssion TEST data is-")
print (np.round (lr_ri.score(x_test,y_test)*100,2))

from sklearn import metrics
from sklearn.metrics import confusion_matrix as cm

print ("Lasso Regression Mean Square Error (MSE) for TEST data is") 
print (np.round (metrics .mean_squared_error(y_test, y_pred_la),2))

print ("Ridge Regression Mean Square Error (MSE) for TEST data is") 
print (np.round (metrics .mean_squared_error(label_test, predict_test_ridge),2))
