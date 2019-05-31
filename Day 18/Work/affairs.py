# -*- coding: utf-8 -*-
"""
Created on Wed May 29 15:56:14 2019

@author: TAPAN


Q1. (Create a program that fulfills the following specification.)
affairs.csv

Import the affairs.csv file.

It was derived from a survey of women in 1974 by Redbook magazine, in which married women were asked about their participation in extramarital affairs.

Description of Variables

The dataset contains 6366 observations of 10 variables:(modified and cleaned)

rate_marriage: woman's rating of her marriage (1 = very poor, 5 = very good)

age: women's age

yrs_married: number of years married

children: number of children

religious: women's rating of how religious she is (1 = not religious, 4 = strongly religious)

educ: level of education (9 = grade school, 12 = high school, 14 = some college, 16 = college graduate, 17 = some graduate school, 20 = advanced degree)

occupation: women's occupation (1 = student, 2 = farming/semi-skilled/unskilled, 3 = "white collar", 4 = teacher/nurse/writer/technician/skilled, 5 = managerial/business, 6 = professional with advanced degree)

occupation_husb: husband's occupation (same coding as above)

affair: outcome 0/1, where 1 means a woman had at least 1 affair.

    Now, perform Classification using logistic regression and check your model accuracy using confusion matrix and also through .score() function.

NOTE: Perform OneHotEncoding for occupation and occupation_husb, since they should be treated as categorical variables. Careful from dummy variable trap for both!!

    What percentage of total women actually had an affair?

(note that Increases in marriage rating and religiousness correspond to a decrease in the likelihood of having an affair.)

    Predict the probability of an affair for a random woman not present in the dataset. She's a 25-year-old teacher who graduated college, has been married for 3 years, has 1 child, rates herself as strongly religious, rates her marriage as fair, and her husband is a farmer.

Optional

    Build an optimum model, observe all the coefficients.
    
"""

import pandas as pd
import numpy as np

affair_data = pd.read_csv('affairs.csv',  header=0)  
affair_data.head()

features=affair_data.iloc[:,:-1].values
label=affair_data.iloc[:,-1].values
from sklearn.preprocessing import OneHotEncoder

### Don't one hot encode multiple values together one hot encode single feature and then drop it then do it for another feature

onehotencoder = OneHotEncoder(categorical_features = [6,7])
features = onehotencoder.fit_transform(features).toarray()

##removing dummy variable colum

features = features[:,[1,2,3,4,5,7,8,9,10,11,12,13,14,15,16,17]]
# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, label, test_size = 0.25, random_state = 0)

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(features_train, labels_train)



#Calculate Class Probabilities
probability = classifier.predict_proba(features_test)

# Predicting the class labels
labels_pred = classifier.predict(features_test)


# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)

#score
score_train=classifier.score(features_train,labels_train)


score_test=classifier.score(features_test,labels_test)

# % of women that had an affair
affair_data['affair'].value_counts(normalize=1)[1]

#She's a 25-year-old teacher who graduated college, has been married for 3 years, has 1 child, rates herself as strongly religious, rates her marriage as fair, and her husband is a farmer.

que=np.array([3,25,3,1,4,16,4,2])
que=que.reshape(1,-1)
quen=onehotencoder.transform(que).toarray()

quen = quen[:,[1,2,3,4,5,7,8,9,10,11,12,13,14,15,16,17]]
# prediction
print(classifier.predict(quen))