# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 23:27:28 2019

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
label_train=har_df['Activity'].values

test_df=pd.read_csv('test.csv') 
features_test=test_df.drop(['subject','Activity'],axis=1).values
label_test=test_df['Activity'].values



"""
Label encoding to convert catagorical data into numerical equivalent data

"""

from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
label_train = labelencoder.fit_transform(label_train).reshape(-1,1)
label_test= labelencoder.transform(label_test).reshape(-1,1)



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
import statsmodels.api as sm

features_train_fr = sm.add_constant(features_train)
features_test_fr = sm.add_constant(features_test)

#
#while True:
#    regressor_OLS = sm.OLS(endog = label_train, exog = features_train).fit()
#    pvalues=regressor_OLS.pvalues
#    if (pvalues.max()>0.05):
#        np.delete(features_train,pvalues.argmax(),1)
#    else:
#        break
#        
    
def backwardElimination(x1,x2,sl):
    numVars = len(x1[0])
    for i in range(0, numVars):
        regressor_OLS = sm.OLS(endog = label_train_fr, exog = features_train_fr).fit()
        maxVar = max(regressor_OLS.pvalues).astype(float)
        if maxVar > sl:
            for j in range(0, numVars - i):
                if (regressor_OLS.pvalues[j].astype(float) == maxVar):
                    x1 = np.delete(x1, j, 1)
                    x2 = np.delete(x2, j, 1)
                    x=[x1,x2]
    regressor_OLS.summary()
    return x
 
SL = 0.05
features_array = backwardElimination(features_train, features_test, SL)

features_array_1=np.array(features_array)

features_train_fr=features_array_1[0]
features_test_fr=features_array_1[1]


## 2. Testing accuracy with features removed.


### Model creation with new data
label_train_fr=label_train[:]
label_test_fr=label_test[:]

classifier = DecisionTreeClassifier()  
classifier.fit(features_train_fr, label_train_fr)
label_pred_fr = classifier.predict(features_test_fr) 
dtc_train_score_fr=classifier.score(features_train_fr,label_train_fr)
dtc_as_fr=accuracy_score(label_test_fr, label_pred_fr)

#from sklearn import tree
#import graphviz
#dot_data = tree.export_graphviz(classifier, out_file=None) 
#graph = graphviz.Source(dot_data) 
#graph.render("decision_tree") 


# Random Forest
rf_classifier = RandomForestClassifier(n_estimators=20, random_state=0)  
rf_classifier.fit(features_train_fr, label_train_fr)  
rf_label_pred_fr = rf_classifier.predict(features_test_fr)

rf_train_score_fr=rf_classifier.score(features_train_fr,label_train_fr)

rf_as_fr=accuracy_score(label_test_fr, rf_label_pred_fr)



# Logistic Regression
lr_classifier = LogisticRegression()
# Fitting Logistic Regression to the Training set
lr_classifier.fit(features_train_fr, label_train_fr)

lr_label_pred_fr = lr_classifier.predict(features_test_fr)

lr_train_score_fr=lr_classifier.score(features_train_fr,label_train_fr)

lr_as_fr=accuracy_score(label_test_fr, lr_label_pred_fr)


# 4 kNN
knn_classifier = KNeighborsClassifier(n_neighbors = 5, p = 2)
knn_classifier.fit(features_train_fr, label_train_fr)

# Predicting the labels
knn_label_pred_fr = knn_classifier.predict(features_test_fr)

knn_train_score_fr=knn_classifier.score(features_train_fr,label_train_fr)

knn_as_fr=accuracy_score(label_test_fr, knn_label_pred_fr)

# Code to plot bar chart
        
N = 2
dt_score_plt = (dtc_as,dtc_as_fr)
rf_score_plt = (rf_as,rf_as_fr)
lr_score_plt = (lr_as,lr_as_fr)
knn_score_plt = (knn_as,knn_as_fr)
dtc_train_score_plt=(dtc_train_score,dtc_train_score_fr)
rf_train_score_plt=(rf_train_score,rf_train_score_fr)
lr_train_score_plt=(lr_train_score,lr_train_score_fr)
knn_train_score_plt=(knn_train_score,knn_train_score_fr)
ind = np.arange(N) 
width = 0.15
     
plt.bar(ind, dtc_train_score_plt,width, label='Training score',color="red")
plt.bar(ind, dt_score_plt, width, label='Decision Tree',color='gray')

plt.bar(ind+width, rf_train_score_plt,width,color="red")
plt.bar(ind + width, rf_score_plt, width,label='Random Forest',color="orange")

plt.bar(ind + width*2, lr_train_score_plt,width,color="red")
plt.bar(ind + width*2, lr_score_plt, width,label='Logistic Regression',color="blue")

plt.bar(ind + width*3, knn_train_score_plt,width,color="red")
plt.bar(ind + width*3, knn_score_plt, width,label='kNN',color="green")

plt.ylabel('Scores')
plt.title('Comaprison between Different Models before and after Feature Optimization')

plt.xticks(ind + width / 20, ('Before Feature Adjustment', 'After Feature Adjustment'))
#plt.legend(loc='upper center')
# Put a legend below current axis
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.09),fancybox=True, shadow=True, ncol=5)
plt.show()

