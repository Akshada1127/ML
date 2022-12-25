##
#2. Write a python program to find all null values in a given data set and remove them

import pandas as pd
df=pd.read_csv("data.csv");
print(df)
print("........................................................................")
print("........................................................................")
df.dropna(axis=0,how='any',inplace=True);
print(df)