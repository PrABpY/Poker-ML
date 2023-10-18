from sklearn.naive_bayes import GaussianNB
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_excel('poker.xlsx',sheet_name = 'dataset')

X = df[['Position1','Position2']]
y = df['Rank']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.5,random_state = 0)

model = GaussianNB()
model.fit(X_train,y_train)

print(model.score(X_test,y_test))