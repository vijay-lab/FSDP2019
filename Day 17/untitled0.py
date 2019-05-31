# -*- coding: utf-8 -*-
"""
Created on Tue May 28 22:22:45 2019

@author: TAPAN
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.preprocessing import Imputer


cancer_data = pd.read_csv('cancer_reg.csv')
cancer_data.describe()
cancer_data.head()
cancer_data.shape

features = cancer_data.iloc[:, :-1]
labels = cancer_data.iloc[:, -1].values


#check null values in numpy array
np.isnan(features).any(axis=1)


imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(features)
features = imputer.transform(features)

#This is done because statsmodels library requires it to be done for constants.
#features = np.append(arr = np.ones((30, 1)), values = features, axis = 1)

#adds a constant column to input data set.
features = sm.add_constant(features)



features_opt = features[:, :]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()

features_opt=np.delete(features_opt,[7],1)

features_opt = features_opt[:, :]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()

features_opt=np.delete(features_opt,[26],1)
features_opt = features_opt[:, :]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()

features_opt=np.delete(features_opt,[7],1)

features_opt = features_opt[:, :]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()

features_opt=np.delete(features_opt,[12],1)

features_opt = features_opt[:, :]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()

features_opt=np.delete(features_opt,[8],1)

features_opt = features_opt[:, :]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()

features_opt=np.delete(features_opt,[17],1)

features_opt = features_opt[:, :]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()

features_opt=np.delete(features_opt,[11],1)

features_opt = features_opt[:, :]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()

features_opt=np.delete(features_opt,[14],1)

features_opt = features_opt[:, :]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()

features_opt=np.delete(features_opt,[19],1)

features_opt = features_opt[:, :]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()

features_opt=np.delete(features_opt,[16],1)

features_opt = features_opt[:, :]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()
features_opt=np.delete(features_opt,[16],1)

features_opt = features_opt[:, :]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()

features_opt=np.delete(features_opt,[4],1)

features_opt = features_opt[:, :]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()

features_opt=np.delete(features_opt,[5],1)

features_opt = features_opt[:, :]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()





from sklearn.linear_model import LinearRegression
lin_reg_1 = LinearRegression()
lin_reg_1.fit(features_opt, labels)

from sklearn.metrics import r2_score
r2_score(labels,lin_reg_1.predict(features_opt))


# Visualising the Linear Regression results
plt.scatter(features, labels, color = 'red')
plt.plot(features_opt, lin_reg_1.predict(features_opt), color = 'blue')

plt.show()




from sklearn.preprocessing import PolynomialFeatures
poly_object = PolynomialFeatures(degree = 5)
features_poly = poly_object.fit_transform(features_opt)


lin_reg_2 = LinearRegression()
lin_reg_2.fit(features_poly, labels)


print "Predicting result with Polynomial Regression",
print lin_reg_2.predict(poly_object.transform(1981))

# Visualising the Polynomial Regression results
plt.scatter(features_opt, labels, color = 'red')
plt.plot(features_opt, lin_reg_2.predict(poly_object.fit_transform(features_opt)), color = 'blue')
plt.title('Polynomial Regression')
plt.xlabel('Year')
plt.ylabel('Claims Paid')
plt.show()




pred=lin_reg_2.predict(poly_object.fit_transform(features_opt))

from sklearn.metrics import r2_score
r2_score(labels,pred)



























