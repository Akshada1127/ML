#Importing the libraries  
  
import pandas as pd  
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB 
# Importing the dataset  
df=pd.read_csv('user_data1.csv')  
x=df.iloc[:,:-1].values  
y=df['Purchased'].values
xtr,xte,ytr,yte=train_test_split(x,y,test_size=0.2,random_state=1)
naive= GaussianNB()  
naive.fit(xtr,ytr)  
# Predicting the Test set results  
print("Prediction the purchased of age 20 and salary 400000",naive.predict([[4,20,15000]]))  
print("Accuracy is",naive.score(x,y))
