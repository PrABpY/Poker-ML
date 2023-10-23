from sklearn.svm import SVC
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

df = pd.read_excel('poker.xlsx',sheet_name = 'dataset')

scale = StandardScaler()

X = df[['Position1','Position2']]
y = df['Rank']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.5,random_state = 0)

model = SVC(kernel = 'rbf',gamma = 1)
model.fit(X_train,y_train)

print(model.score(X_test,y_test))