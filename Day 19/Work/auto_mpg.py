# -*- coding: utf-8 -*-
"""
Created on Thu May 30 17:56:54 2019

@author: TAPAN



Q1. (Create a program that fulfills the following specification.)
Auto_mpg.txt

Here is the dataset about cars. The data concerns city-cycle fuel consumption in miles per gallon (MPG).

Import the dataset Auto_mpg.txt
1.Give the column names as "mpg", "cylinders", "displacement","horsepower","weight","acceleration", "model year", "origin", "car name" respectively
2.Display the Car Name with highest miles per gallon value.
3.Build the Decision Tree and Random Forest models and find out which of the two is more accurate in predicting the MPG value
4.Find out the MPG value of a 80's model car of origin 3, weighing 2630 kgs with 6 cylinders, having acceleration around 22.2 m/s due to it's 100 horsepower 
engine giving it a displacement of about 215. (Give the prediction from both the models)

"""
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split as tts
from sklearn.preprocessing import Imputer,LabelEncoder,OneHotEncoder
from sklearn.ensemble import RandomForestRegressor


#Preparing the dataset in dataframe
col_nam=["mpg", "cylinders", "displacement","horsepower","weight","acceleration", "model year", "origin", "car name" ]
car_data=pd.read_csv("Auto_mpg.txt",sep="\s+",names=col_nam)

car_data['horsepower']=car_data['horsepower'].replace("?",np.nan).astype(np.float64)
car_data['horsepower']=car_data['horsepower'].fillna(car_data['horsepower'].mean())

label=car_data.iloc[:,0].values
features=car_data.iloc[:,1:8].values
# DIY Imputer class
#imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
#imputer = imputer.fit(features.iloc[:, 3])
#features.iloc[:, 3] = features.transform(car_data.iloc[:, 3])


# 2.Display the Car Name with highest miles per gallon value.
# DIY car_data['mpg'].max()

zz=car_data['mpg'].idxmax() # or use .argmax()
car_name=car_data.iloc[zz][8]# [8] specifies column value or can be done as car_name=car_data.iloc[zz] and then print(car_name[8])
#name=car_data['car name']  [ car_data['mpg'] == car_data['mpg'].max() ] another method to access data
print("the car with the maximum milage is",car_name)

# 3.Build the Decision Tree and Random Forest models and find out which of the two is more accurate in predicting the MPG value
# Removed cause car name is not needed to predict

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()  
features = sc.fit_transform(features)  

feature_train,feature_test,label_train,label_test=tts(features,label,test_size=0.20,random_state=20)


from sklearn.tree import DecisionTreeRegressor
dtr=DecisionTreeRegressor()
dtr.fit(feature_train, label_train)  

label_pred = dtr.predict(feature_test)
dtr_pred_df=pd.DataFrame({'Actual':label_test, 'Predicted':label_pred})  
dt_score_train=dtr.score(feature_train,label_train)
dt_score_test=dtr.score(feature_test,label_test)

## RF Model
rfr = RandomForestRegressor(n_estimators=10)  
rfr.fit(feature_train, label_train)  
label_pred = rfr.predict(feature_test)  

label_pred = rfr.predict(feature_test)
rf_pred_df=pd.DataFrame({'Actual':label_test, 'Predicted':label_pred})  
rf_score_train=rfr.score(feature_train,label_train)
rf_score_test=rfr.score(feature_test,label_test)

"""
4.Find out the MPG value of a 80's model car of origin 3, weighing 2630 kgs with 6 cylinders, having acceleration around 22.2 m/s 
due to it's 100 horsepower engine giving it a displacement of about 215. (Give the prediction from both the models)
"""
val_predict=[8,307,130,3504,12,70,1]
#[6,215,100,2630,22.2,80,3]
val_predict=np.array(val_predict)## for some reason dtr is predicting better ???????????????????????
val_predict=val_predict.reshape(1,-1)

pred_dtr=dtr.predict(sc.transform(val_predict))
pred_rf=rfr.predict(sc.transform(val_predict))
