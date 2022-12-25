##
#6. Write a python program to implement Polynomial Regression for given dataset. 

##

#import the Library
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

#Read data from dataset

df=pd.read_csv("salary1.csv")

#Set Variables

x=df.iloc[:,:-1].values
y=df['salary'].values

# Apply Polynomial Regression
poly=PolynomialFeatures(degree=3)
x_poly=poly.fit_transform(x)
reg=LinearRegression()
reg.fit(x,y)

print("Prediction is",reg.predict([[2005,5]]))
print("Accuracy is",reg.score(x,y))

