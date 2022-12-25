#
#1. Write a python program to Prepare Scatter Plot (Use Forge Dataset / Iris Dataset)

import matplotlib.pyplot as plt
import pandas as pd
iris=pd.read_csv("iris.csv");
df=pd.DataFrame(iris)
x=df['sepal.length'].values;
y=df['variety'].values;
plt.scatter(x,y)
print(df.shape)
plt.show()


