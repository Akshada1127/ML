
##
#8. Write a python program to Implement Decision Tree whether or not to play tennis
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
df=pd.read_csv("play_tennis.csv")

x=df.iloc[:,:-1].values
y=df['playtennis'].values
dec_tree=DecisionTreeRegressor()
dec_tree.fit(x, y)

print("Prediction of playTennis are",dec_tree.predict([[1,11,333,2222,11111]]))
print("Accuracy of Decision Tree are",dec_tree.score(x,y))

