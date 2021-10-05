# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 18:55:25 2020

@author: Rohan
"""

import pandas as pd
from sklearn import linear_model

df=pd.read_csv('BostonHousePricing.csv')

#check for null values
df.isnull().sum()

#building model:
reg=linear_model.LinearRegression()
reg.fit(df[['AREA','BEDROOM','AGE']],df.PRICE)

#equation : y=a+a1x+a2x+a3x
#coefficients here are a1,a2,a3
reg.coef_
#intercept: a
reg.intercept_

#predict the model for 4000 area, 4 bedrooms, 30 age
prediction=reg.predict([[4000,4,30]])
print("predicted price is: ", prediction)
