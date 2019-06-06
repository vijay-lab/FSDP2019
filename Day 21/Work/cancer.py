# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 13:20:23 2019

@author: TAPAN

Q1. (Create a program that fulfills the following specification.)

Program Specification:

Import breast_cancer.csv file.

This breast cancer database was obtained from the University of Wisconsin

Hospitals, Madison from Dr. William H. Wolberg.

Attribute Information: (class attribute has been moved to last column)

Sample Code Number(id number)                     ----> represented by column A.

Clump Thickness (1 – 10)                                     ----> represented by column B.
Uniformity of Cell Size(1 - 10)                             ----> represented by column C.
Uniformity of Cell Shape (1 - 10)                        ----> represented by column D.
Marginal Adhesion (1 - 10)                                  ----> represented by column E.
Single Epithelial Cell Size (1 - 10)                        ----> represented by column F.
Bare Nuclei (1 - 10)                                               ----> represented by column G.
Bland Chromatin (1 - 10)                                     ----> represented by column H.
Normal Nucleoli (1 - 10)                                      ----> represented by column I.
Mitoses (1 - 10)                                                     ----> represented by column J.
Class: (2 for Benign and 4 for Malignant)         ----> represented by column K. 
A Benign tumor is not a cancerous tumor and Malignant tumor is a cancerous tumor.

                   1. Impute the missing values with the most frequent values.(use mode)
                   2. Perform Classification on the given data-set to predict if the tumor is cancerous or not.
                   3. Check the accuracy of the model.
                   4. Predict whether a women has Benign tumor or Malignant tumor, if her Clump thickness is around 6, 
                   uniformity of cell size is 2, Uniformity of Cell Shape is 5, Marginal Adhesion is 3, Bland Chromatin is 9,
                   Mitoses is 4, Bare Nuclei is 7, Normal Nuclei is 2 and Single Epithelial Cell Size is 2

(you can neglect the id number column as it doesn't seem  a predictor column)

"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split as tts
from sklearn.svm import SVC

#from sklearn.datasets import load_breast_cancer
#cancer = load_breast_cancer()
#print(cancer.keys())
#cancer.DESCR
#cancer.target
#cancer_df=pd.DataFrame(cancer.data,columns=cancer.feature_names)
#cancer_df['Type of Cancer']=cancer.target
cancer_df=pd.read_csv("breast_cancer.csv")

cancer_df['G']=cancer_df['G'].fillna(cancer_df['G'].mode()[0])

cancer_df.isnull().any(axis=0)

x=cancer_df.iloc[:,1:-1].values
y=cancer_df.iloc[:,-1].values

#imp=Imputer(missing_values='NaN', strategy='median',axis=1)
#imp=imp.fit(x.iloc[:,:])
#cancer_df.iloc[:,:]=imp.transform(cancer_df.iloc[:,:])


#Create train and test data with 70o/o and 30°/o split
x_train, x_test, y_train,y_test	=tts(x, y, test_size=0.3, random_state=0)

# using SV Classifier
svc_class=SVC(kernel='rbf',random_state=0)
svc_class.fit(x_train, y_train)
y_pred=svc_class.predict(x_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

# Model Score
score_test = svc_class.score(x_test,y_test)
score_train = svc_class.score(x_train,y_train)

dat_pred=np.array([6,2,5,3,2,7,9,2,4]).reshape(1,-1)

dat_pred_val=svc_class.predict(dat_pred)
if (dat_pred_val==4):
        print("The test subject has malignant cancer")
else:
    print("The test subject has benign cancer")

