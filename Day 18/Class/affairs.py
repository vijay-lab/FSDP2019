"""
Import the affairs.csv file.

It was derived from a survey of women in 1974 by Redbook magazine, in which married women were asked about their participation in extramarital affairs.


Description of Variables

The dataset contains 6366 observations of 10 variables:(modified and cleaned)

rate_marriage: woman's rating of her marriage (1 = very poor, 5 = very good)

age: women's age

yrs_married: number of years married

children: number of children

religious: women's rating of how religious she is (1 = not religious, 
4 = strongly religious)

educ: level of education (9 = grade school, 12 = high school, 14 = some college
, 16 = college graduate, 17 = some graduate school, 20 = advanced degree)

occupation: women's occupation (1 = student, 2 = farming/semi-skilled/unskilled
, 3 = "white collar", 4 = teacher/nurse/writer/technician/skilled,
5 = managerial/business, 6 = professional with advanced degree)

occupation_husb: husband's occupation (same coding as above)

affair: outcome 0/1, where 1 means a woman had at least 1 affair.

Now, perform Classification using logistic regression and check your model 
accuracy using confusion matrix and also through .score() function.

NOTE: Perform OneHotEncoding for occupation and occupation_husb, since they 
should be treated as categorical variables. Careful from dummy variable trap 
for both!!

What percentage of total women actually had an affair?

(note that Increases in marriage rating and religiousness correspond to a 
decrease in the likelihood of having an affair.)

Predict the probability of an affair for a random woman not present in the 
dataset. She's a 25-year-old teacher who graduated college, has been married 
for 3 years, has 1 child, rates herself as strongly religious, rates her 
marriage as fair, and her husband is a farmer.

Optional :-

    Build an optimum model, observe all the coefficients.

file name - "affairs.py"

"""

import numpy as np
import pandas as pd

# Reading data from csv
dataset = pd.read_csv("affairs.csv")

# Separating data into Independent and Dependent Variables
fe = dataset.iloc[:,:-1].values
la = dataset.iloc[:,-1].values

def Model(features, labels):
    # Applying OneHotEncoding
    from sklearn.preprocessing import OneHotEncoder
    
    col_to_ohe = [6,7]  # Columns to be OneHotEncoded
    ohe=OneHotEncoder(categorical_features=[col_to_ohe])
    features = ohe.fit_transform(features).toarray()
    
    # Getting indexes for the columns to be dropped, to avoid dummy variable trap
    total_col, indexes = 0, []
    for col in col_to_ohe:
        unique_val_count = len(dataset.iloc[:,col].value_counts())
        total_col += unique_val_count
        indexes.append(total_col - unique_val_count)
    
    # Dropping the dummy variable trap columns
    features = np.delete(features, indexes, axis=1)
    
    # Splitting the dataset into train and test
    from sklearn.model_selection import train_test_split as TTS
    
    f_train,f_test,l_train,l_test = TTS(features, labels, test_size = 0.25,
                                        random_state = 0)
    
    # Logistic Regression Model
    from sklearn.linear_model import LogisticRegression
    reg = LogisticRegression(random_state=0)
    reg = reg.fit(f_train, l_train)
    
    pred = reg.predict(f_test)   # Prediction on test data
    
    # np.array([1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 3, 25, 3, 1, 4, 16]).reshape(1,-1)
    # Preprocessing the new individual's data
    val = np.array([3, 25, 3, 1, 4, 16, 4, 2]).reshape(1,-1)
    val = ohe.transform(val).toarray()
    val = np.delete(val, indexes, axis=1)
    
    val_pred = reg.predict_proba(val)  # Predicting Individual's value
    
    # Confusion Matrix
    from sklearn.metrics import confusion_matrix
    cm = confusion_matrix(l_test, pred)
    
    # check the accuracy on the Model
    mod_score = reg.score(f_test, l_test)
    
    return pred,val_pred,cm,mod_score

Pred, val_Pred, CM, Score = Model(fe,la)

print ("model accuracy using confusion matrix : "+str(CM))
print ("model accuracy using .score() function : "+str(round(Score*100,2)))
print ("percentage of total women actually had an affair : "+str(round(dataset["affair"].mean()*100,2))+"%")
print ("probability of an affair for a random woman is : "+str(val_Pred))

# Optional (OLS MOdel)
"""
import statsmodels.formula.api as sm

fe = np.append(arr = np.ones((fe.shape[0], 1)).astype(int), 
                     values = fe, axis = 1)
feat_opt = fe[:,:]
reg_OLS = sm.OLS(endog=la, exog=feat_opt).fit()
reg_OLS.summary()

feat_opt = fe[:,[0,1,2,3,5,6,7,8]]
reg_OLS = sm.OLS(endog=la, exog=feat_opt).fit()
reg_OLS.summary()

feat_opt = fe[:,[0,1,2,3,5,6,7]]
reg_OLS = sm.OLS(endog=la, exog=feat_opt).fit()
reg_OLS.summary()

feat_opt = fe[:,[0,1,2,3,5,7]]
reg_OLS = sm.OLS(endog=la, exog=feat_opt).fit()
print reg_OLS.summary()
"""