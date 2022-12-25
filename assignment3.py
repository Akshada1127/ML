##
#3. Write a python program the Categorical values in numeric format for a given dataset.


import pandas as pd1
from sklearn.preprocessing import LabelEncoder
df1=pd1.read_csv("data1.csv");
print("the content of file is....")
print(df1)
y=df1["salary"].values
le=LabelEncoder()
y=le.fit_transform(y)
print("the y values:")
print(y)
