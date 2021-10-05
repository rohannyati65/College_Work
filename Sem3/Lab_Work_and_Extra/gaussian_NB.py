# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 11:30:36 2020

@author: Rohan
"""

# Assigning features and label variables
weather=['Sunny','Sunny','Overcast','Rainy','Rainy','Rainy','Overcast','Sunny','Sunny','Rainy','Sunny','Overcast','Overcast','Rainy']
temp=['Hot','Hot','Hot','Mild','Cool','Cool','Cool','Mild','Cool','Mild','Mild','Mild','Hot','Mild']
play=['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']

from sklearn import preprocessing
le=preprocessing.LabelEncoder()

weather_encoded=le.fit_transform(weather) 
print(weather_encoded)

temp_encoded=le.fit_transform(temp) 
label=le.fit_transform(play) 
print("temp:",temp_encoded) 
print("play:",label)


features=list(zip(weather_encoded,temp_encoded))
print(features)


from sklearn.naive_bayes import GaussianNB
model=GaussianNB()
model.fit(features,label)
predicted=model.predict([[0,2]])
#0:overcast,2:mild
print("presicted value:",predicted)