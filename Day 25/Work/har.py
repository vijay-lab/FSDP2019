# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 11:48:05 2019

@author: TAPAN
"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

# Importing the training data ans splitting it into X and y

har_df = pd.read_csv('train.csv') 

features_train=har_df.drop(['subject','Activity'],axis=1).values
label_train=har_df['Activity']

test_df=pd.read_csv('test.csv') 
features_test=test_df.drop(['subject','Activity'],axis=1).values
label_test=test_df['Activity']

from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder = LabelEncoder()
ohe=OneHotEncoder()
label_train = labelencoder.fit_transform(label_train)
label_test = labelencoder.fit_transform(label_test)

label_train = ohe.fit_transform(label_train)
label_test = ohe.fit_transform(label_test)


classifier = DecisionTreeClassifier()  
classifier.fit(features_train, label_train)

label_pred = classifier.predict(features_test) 

dtc_train_score=classifier.score(features_train,label_train)
dtc_as=accuracy_score(label_test, label_pred)

#dtc_as_train=classifier.score(features_train, label_train)
#dtc_as_test=classifier.score(features_test, label_test)


print(confusion_matrix(label_test, label_pred))  
print("---------------------------------------------------------------------")
print(accuracy_score(label_test, label_pred))
print("---------------------------------------------------------------------")
print(classification_report(label_test, label_pred))
print("---------------------------------------------------------------------")

#from sklearn import tree
#import graphviz
#dot_data = tree.export_graphviz(classifier, out_file=None) 
#graph = graphviz.Source(dot_data) 
#graph.render("decision_tree") 


# Random Forest
rf_classifier = RandomForestClassifier(n_estimators=20, random_state=0)  
rf_classifier.fit(features_train, label_train)  
rf_label_pred = rf_classifier.predict(features_test)

rf_train_score=rf_classifier.score(features_train,label_train)

rf_as=accuracy_score(label_test, rf_label_pred)


#Evaluate the algo

print(confusion_matrix(label_test,rf_label_pred))  
print("---------------------------------------------------------------------")
print(classification_report(label_test,rf_label_pred))  
print("---------------------------------------------------------------------")
print(accuracy_score(label_test, rf_label_pred))
print("---------------------------------------------------------------------")

# Logistic Regression

# Fitting Logistic Regression to the Training set
lr_classifier = LogisticRegression()
lr_classifier.fit(features_train, label_train)

lr_label_pred = lr_classifier.predict(features_test)

lr_train_score=lr_classifier.score(features_train,label_train)


lr_as=accuracy_score(label_test, lr_label_pred)


#Evaluate the algo

print(confusion_matrix(label_test,lr_label_pred))  
print("---------------------------------------------------------------------")
print(classification_report(label_test,lr_label_pred))  
print("---------------------------------------------------------------------")
print(accuracy_score(label_test, lr_label_pred))
print("---------------------------------------------------------------------")

# 4 kNN
knn_classifier = KNeighborsClassifier(n_neighbors = 5, p = 2)
knn_classifier.fit(features_train, label_train)


# Predicting the labels
knn_label_pred = knn_classifier.predict(features_test)

knn_train_score=knn_classifier.score(features_train,label_train)

knn_as=accuracy_score(label_test, knn_label_pred)

#Evaluate the algo

print(confusion_matrix(label_test,knn_label_pred))  
print("---------------------------------------------------------------------")
print(classification_report(label_test,knn_label_pred))  
print("---------------------------------------------------------------------")
print(accuracy_score(label_test, knn_label_pred))
print("---------------------------------------------------------------------")

# Now we reduce the feature by backward Elimination
#import statsmodels.api as sm
#
#features_train = sm.add_constant(features_train)
#
#features_opt = features_train[:,:]
#regressor_OLS = sm.OLS(endog = label_train, exog = features_opt).fit()
#pvalues=regressor_OLS.pvalues
#
#while True:
#    regressor_OLS = sm.OLS(endog = label_train, exog = features_opt).fit()
#    pvalues=regressor_OLS.pvalues
#    if (pvalues.max()>0.05):
#        pvalues = np.delete(features_opt,pvalues.argmax(),1)
#    else:
#        break
#        


# Code to plot bar chart
        
N = 2
dt_score = (dtc_as)
rf_score = (rf_as)
lr_score = (lr_as)
knn_score = (knn_as)
ind = np.arange(N) 
width = 0.15
     
plt.bar(ind, dtc_train_score,width, label='DT training score',color="red")
plt.bar(ind, dt_score, width, label='Decision Tree',color='gray')

plt.bar(ind+width, rf_train_score,width, label='RF training score',color="red")
plt.bar(ind + width, rf_score, width,label='Random Forest',color="orange")

plt.bar(ind + width*2, lr_train_score,width, label='LR training score',color="red")
plt.bar(ind + width*2, lr_score, width,label='Logistic Regression',color="blue")

plt.bar(ind + width*3, knn_train_score,width, label='KNN training score',color="red")
plt.bar(ind + width*3, knn_score, width,label='kNN',color="green")

plt.ylabel('Scores')
plt.title('Models')

plt.xticks(ind + width / 20, ('Before Feature Adjustment', 'After Feature Adjustment'))
plt.legend(loc='best')
plt.show()

