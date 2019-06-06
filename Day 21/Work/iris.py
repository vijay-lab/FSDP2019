# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 19:07:07 2019

@author: TAPAN

Q2. This famous classification dataset first time used in Fisher’s classic 1936 paper, The Use of Multiple Measurements in
 Taxonomic Problems. Iris dataset is having 4 features of iris flower and one target class.

The 4 features are

SepalLengthCm
SepalWidthCm
PetalLengthCm
PetalWidthCm
The target class

The flower species type is the target class and it having 3 types

Setosa
Versicolor
Virginica
The idea of implementing svm classifier in Python is to use the iris features to train an svm classifier and use the trained
svm model to predict the Iris species type. To begin with let’s try to load the Iris dataset.

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn.model_selection import train_test_split as TTS

iris=datasets.load_iris()

x=iris.data
y=iris.target

# Splitting the data into test and train groups
x_train,x_test,y_train,y_test=TTS(x,y,test_size=0.20,random_state=20)

from sklearn.svm import SVC
svc_classifier=SVC(kernel='rbf',random_state=20)
svc_classifier.fit(x_train,y_train)



y_pred=svc_classifier.predict(x_test)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)

score_train=svc_classifier.score(x_train,y_train)
score_test=svc_classifier.score(x_test,y_test)

from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))




