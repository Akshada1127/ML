# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 17:20:02 2022

@author: Akshida
"""

import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df=pd.read_csv("house.csv")

x=df.iloc[:,:-1].values
y=df['price'].values
reg=LinearRegression()
reg.fit(x,y)

print("Prediction is:",reg.predict([[10000,4,23]]))