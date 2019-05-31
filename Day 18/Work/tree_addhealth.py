# -*- coding: utf-8 -*-
"""
Created on Thu May 30 08:41:05 2019

@author: TAPAN

For this Code Challenge, The National Longitudinal Study of Adolescent to Adult Health (Add Health) data set,
 an ongoing (longitudinal) survey study that began in the mid-1990s is used. The project website URL is:

http://www.cpc.unc.edu/projects/addhealth/.

This large data set is available online from the University of North Carolina's
Carolina Population Center, 
#http://www.cpc.unc.edu/projects/addhealth/data.

Import tree_addhealth.csv

The attributes are:

BIO_SEX: 1 = male 0 = female    

HISPANIC: 1=Yes,0=No    

WHITE : 1=Yes,0=No

BLACK : 1=Yes,0=No          

NAMERICAN: 1=Yes,0=No                      

ASIAN: 1=Yes,0=No                      

ALCEVR1: ever drank alcohol(1=Yes,0=No)   

marever1: ever smoked marijuana(1=Yes,0=No)    

cocever1: ever used cocaine(1=Yes,0=No)                

inhever1: ever used inhalants(1=Yes,0=No)             

cigavail: cigarettes available in home(1=Yes,0=No)

PASSIST: parents or public assistance(1=Yes,0=No)

EXPEL1: ever expelled from school(1=Yes,0=No)

TREG1: Ever smoked regularly(1=Yes,0=No)

Explanatory Variables:

Age

ALCPROBS1:alcohol problems 0-6

DEP1: depression scale

ESTEEM1: self esteem scale       

VIOL1:violent behaviour scale

DEVIANT1: deviant behaviour scale     

SCHCONN1: school connectedness scale       

GPA1: gpa scale  4 points)

FAMCONCT: family connectedness scale       

PARACTV:parent activities scale

PARPRES:parental presence scale

Build a classification tree model evaluating if an adolescent would smoke 
regularly or not based on: gender, age, (race/ethnicity) Hispanic, White, 
Black, Native American and Asian, alcohol use, alcohol problems, marijuana use,
cocaine use, inhalant use, availability of cigarettes in the home, depression,
and self-esteem.

Build a classification tree model evaluation if an adolescent gets expelled or
not from school based on their Gender and violent behavior.
 
Use random forest in relation to regular smokers as a target and explanatory 
variable specifically with Hispanic, White, Black, Native American and Asian.

(Please make confusion matrix and also check accuracy score for each and every
section)

file_name - "tree_addhealth.py"

"""



import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,accuracy_score,r2_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import Imputer
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression





health_data=pd.read_csv("tree_addhealth.csv")
health_data.isnull().any(axis=0)

#Using Imputer class for filling nan values with mean stretergy
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 1)
imputer = imputer.fit(health_data.iloc[:, :])
health_data.iloc[:, :] = imputer.transform(health_data.iloc[:, :])

label=health_data['TREG1'].values
feature_set1=['BIO_SEX','age','WHITE','BLACK','HISPANIC','NAMERICAN','ASIAN','ALCEVR1','ALCPROBS1','marever1','cocever1','inhever1','cigavail','DEP1','ESTEEM1']
features=health_data.loc[:,feature_set1].values

features_train,features_test,label_train,label_test = train_test_split(features,label,test_size=.25,random_state=0)

##KNN
classifier = KNeighborsClassifier(n_neighbors = 5, p = 2) #When p = 1, this is equivalent to using manhattan_distance (l1), and euclidean_distance (l2) for p = 2
classifier.fit(features_train, label_train)

#Calculate Class Probabilities
probability = classifier.predict_proba(features_test)

# Predicting the class labels
label_pred = classifier.predict(features_test)

# Making the Confusion Matrix
cm = confusion_matrix(label_test, label_pred)
score=classifier.score(features_test,label_test)

score1=classifier.score(features_train,label_train)
##Ask about score

##LR
classifier_lr = LogisticRegression()
classifier_lr.fit(features_train, label_train)

#Calculate Class Probabilities
probability = classifier_lr.predict_proba(features_test)

# Predicting the class labels
label_pred = classifier_lr.predict(features_test)

# Making the Confusion Matrix
cm = confusion_matrix(label_test, label_pred)
score_lr=classifier_lr.score()

#####Descision Tree Model Implemantation
dtc = DecisionTreeClassifier(criterion="entropy",random_state=0)
dtc.fit(features_train,label_train)
pred = dtc.predict(features_test)

cm = confusion_matrix(pred,label_test)
plt.plot(label,pred)
model_accuracy_dt = accuracy_score(label_test,pred)

#withot train test
dtc = DecisionTreeClassifier(criterion="entropy",random_state=0)
dtc.fit(features,label)
pred = dtc.predict(features)

cm = confusion_matrix(pred,features)
plt.plot(label,pred)
model_accuracy_dt = accuracy_score(label,pred)

###2.
features2 = health_data[["BIO_SEX","VIOL1"]].values
label2 = health_data["EXPEL1"].values

#Spliting into train,test
features2_train,features2_test,label2_train,label2_test = train_test_split(features2,label2,test_size=.25,random_state=0)

##LR
classifier2_lr = LogisticRegression()
classifier2_lr.fit(features2_train, label2_train)

#Calculate Class Probabilities
probability2 = classifier2_lr.predict_proba(features2_test)

# Predicting the class labels
label2_pred = classifier2_lr.predict(features2_test)

accuracy_score(label2_test, label2_pred)


#/knn
# Fitting Logistic Regression to the Training set
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, p = 2) #When p = 1, this is equivalent to using manhattan_distance (l1), and euclidean_distance (l2) for p = 2
classifier.fit(features2_train, label2_train)

#Calculate Class Probabilities
probability = classifier.predict_proba(features2_test)

# Predicting the class labels
labels_pred = classifier.predict(features2_test)

# Making the Confusion Matrix
cm = confusion_matrix(label2_test.round(), label2_pred)
knn_model2=accuracy_score(label2_test.round(), label2_pred)


