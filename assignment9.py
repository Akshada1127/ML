##
#9. Write a python program to implement linear SVM. 
##


import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
df=pd.read_csv("area.csv")
x=df['area'].values
y=df["price"].values
x=x.reshape(-1,1)
y=y.reshape(-1,1)
sv=SVR();
sv.fit(x,y)
print("Prediction of support vector machine is",sv.predict(([[2100]])))
print("Accuracy is",sv.score(x,y))