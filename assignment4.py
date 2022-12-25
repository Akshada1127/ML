##
#   4. Write a python program to implement simple Linear Regression for predicting house 
#   price

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#Read data from the dataset

df=pd.read_csv("salary.csv")

#set independent and dependent variable
x=df['year'].values
y=df['salary'].values

#spliting dataset
xtr,xte,ytr,yte=train_test_split(x,y,test_size=0.2,random_state=1)

#feature scalling
xtr=xtr.reshape(-1,1)
ytr=ytr.reshape(-1,1)

#apply simple linear regression
reg=LinearRegression()
reg.fit(xtr,ytr)

#prediction
print("Prediction is",reg.predict([[2001]]))

#visualization
plt.scatter(xtr,ytr,color="red")
plt.title("simple linear regression")
plt.xlabel("year of experience")
plt.ylabel("salary")
plt.plot(xtr,reg.predict(xtr),color="blue")
plt.show()