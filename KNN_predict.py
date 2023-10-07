import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
import ranking 
import matplotlib.pyplot as plt
import Handing_Flop as ran

df = pd.read_excel('poker.xlsx',sheet_name='dataset')
encode = LabelEncoder()

scale = StandardScaler()
x1 = df[['Position1','Position2']]
a = scale.fit_transform(df[['Position1']])
b = scale.fit_transform(df[['Position2']])
# x1 = scale.fit_transform(x1)
# x2 = scale.fit_transform(x2)
# print(x)
y = encode.fit_transform(df['Rank'])
# y = scale.fit_transform(y)
# print(y)

x_train,x_test,y_train,y_test = train_test_split(x1,y,test_size=0.5,random_state = 42)

K = 5
model = KNeighborsClassifier(n_neighbors = K)
model.fit(x_train,y_train)

table = ran.table()
print(table)
x_pre = [table]
x_pre = ranking.rank_number(ranking.encode(ranking.split_card(x_pre[0])[0]),ranking.split_card(x_pre[0])[1])
print(x_pre)
y_pre = model.predict([[x_pre,x_pre]])

plt.scatter(a,b,s = 2)

print('Rank :',encode.inverse_transform([y_pre])[0])
print('Accuracy :','{:.2f}'.format(model.score(x_test,y_test)))
plt.show()