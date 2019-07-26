# -*- coding: utf-8 -*-
"""
Created on Thu May 30 17:58:06 2019

@author: TAPAN


Q2. (Create a program that fulfills the following specification.)
PastHires.csv


Here, we are building a decision tree to check if a person is hired or not based on certain predictors.

Import PastHires.csv File.

scikit-learn needs everything to be numerical for decision trees to work.

So, use any technique to map Y,N to 1,0 and levels of education to some scale of 0-2.

Build and perform Decision tree based on the predictors and see how accurate your prediction is for a being hired.

Now use a random forest of 10 decision trees to predict employment of specific candidate profiles:

Predict employment of a currently employed 10-year veteran, previous employers 4, went to top-tire school, having Bachelor's Degree without Internship.
Predict employment of an unemployed 10-year veteran, ,previous employers 4, didn't went to any top-tire school, having Master's Degree with Internship.


"""
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split as tts
from sklearn.preprocessing import Imputer,LabelEncoder,OneHotEncoder

le = LabelEncoder()
hire_data2=pd.read_csv("PastHires.csv")
# checking for null values
hire_data.isnull().values.any()

#Preparing the dataset in dataframe
hire_data=pd.read_csv("PastHires.csv")
hire_data.iloc[:,1]=le.fit_transform(hire_data.iloc[:,1])
hire_data.iloc[:,3]=le.fit_transform(hire_data.iloc[:,3])
hire_data.iloc[:,4]=le.fit_transform(hire_data.iloc[:,4])
hire_data.iloc[:,5]=le.fit_transform(hire_data.iloc[:,5])
hire_data.iloc[:,6]=le.fit_transform(hire_data.iloc[:,6])

label=hire_data.iloc[:,-1].values
features=hire_data.iloc[:,0:-1].values

features_train, features_test, labels_train, labels_test = tts(features, label, test_size=0.20, random_state=0) 

## Fitting in Decision Tree
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier()  
classifier.fit(features_train, labels_train)  

label_pred = classifier.predict(features_test)
pred_df=pd.DataFrame({'Actual':labels_test, 'Predicted':label_pred})  
score_test=classifier.score(features_train,labels_train)
score_train=classifier.score(features_test,labels_test)


## Fitting in Random Forest
from sklearn.ensemble import RandomForestClassifier

classifier_rf = RandomForestClassifier(n_estimators=10, random_state=0)  
classifier_rf.fit(features_train, labels_train)  
labels_pred_rf = classifier_rf.predict(features_test)
#score for model
score_test_rf=classifier_rf.score(features_train,labels_train)
score_train_rf=classifier_rf.score(features_test,labels_test)

#Predict employment of a currently employed 10-year veteran, previous employers 4, went to top-tire school, having Bachelor's Degree without Internship.
WI=[10,1,4,0,1,0]
WI=np.reshape(WI,(1,-1))
WI_pred_dtc = classifier.predict(WI)
WI_pred_rf = classifier_rf.predict(WI)
print("The prediction of both model is that he will get hired")


#Predict employment of an unemployed 10-year veteran, ,previous employers 4, didn't went to any top-tire school, having Master's Degree with Internship.

WoI=[10,0,4,1,0,1]
#WoI=np.array(WoI)
#WoI=WoI.reshape(1,-1) or do this below
WoI=np.reshape(WoI,(1,-1))
WoI_pred_dtc = classifier.predict(WoI)
WoI_pred_rf = classifier_rf.predict(WoI)
print("The prediction of both model is that he will get hired")

