# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 17:31:33 2020

@author: Rohan
"""
import pandas as pd
from sklearn.model_selection import  train_test_split

dataset = pd.DataFrame()

dataset["X"] = [2,4,5,6]
dataset["Y"] = [3,4,5,7]
print(dataset)

X = dataset["X"]

y = dataset["Y"]

rows = (len(dataset.index))
print("rows = ",rows)
#y = ax +b

sum_x = 0    #for summation of x 
sum_y = 0    #for summation of y
sum_xy = 0   #for summation of x*y
sum_x2 = 0   #for summation of x^2

for i in range(rows):
    sum_x += dataset.iloc[i,0]
    sum_y += dataset.iloc[i,1]
    sum_xy += dataset.iloc[i,0]*dataset.iloc[i,1]
    sum_x2 += dataset.iloc[i,0]*dataset.iloc[i,0]
    
    #calculating coefficients a & b

a = ((rows * sum_xy) - (sum_x * sum_y))/((rows * sum_x2) - (sum_x * sum_x))

b = ((sum_y * sum_x2) - (sum_x * sum_xy))/((rows * sum_x2)- (sum_x * sum_x))

print("a = ",a)
print("b = ",b)

 # equation is y = ax + b

txt = "y = {}x + {}"
print(txt.format(a,b))

 #prediction and accuracy

x = int(input("enter value of x: "))

y = a*(x) + b
print("The value of Y predicted = ",y)



