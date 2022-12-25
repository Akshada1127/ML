##
##5. Write a python program to implement multiple Linear Regression for a given dataset

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression

#Read data from the dataset

df=pd.read_csv("salary1.csv")

#set independent and dependent variable
x=df.iloc[:,:-1].values
y=df['salary'].values


#apply multiple linear regression
reg=LinearRegression()
reg.fit(x,y)

#prediction
print("Prediction is",reg.predict([[2001,4]]))

#visualization
plt.plot(x,y,color="red")
plt.title("multiple linear regression")
plt.xlabel("year of experience")
plt.ylabel("salary")

plt.show()
