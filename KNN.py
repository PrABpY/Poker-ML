import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.model_selection import train_test_split
import ranking 
import matplotlib.pyplot as plt
import Handing_Flop as ran

df = pd.read_excel('poker.xlsx',sheet_name='dataset')
# df['Rank'] = encode.fit_transform(df['Rank'])

scale = StandardScaler()
x1 = df[['Position1']]
x2 = df[['Position2']]
# x1 = scale.fit_transform(x1)
# x2 = scale.fit_transform(x2)
# print(x)
y = df[['Rank']]
# y = scale.fit_transform(y)
# print(y)

x_train,x_test,y_train,y_test = train_test_split(x1,y,test_size=0.3,random_state = 42)

K = 3
model = KNeighborsClassifier(n_neighbors = K)
model.fit(x_train,y_train)

table = ran.table()
print(table)
x_pre = [table]
x_pre = ranking.rank_number(ranking.encode(ranking.split_card(x_pre[0])[0]),ranking.split_card(x_pre[0])[1])
x_pre = (0.5*3.14+x_pre)**0.5
print(x_pre)
y_pre = model.predict([[x_pre]])

plt.scatter(x1,x2,s = 2)

print('Rank :',y_pre[0])
print('Accuracy :','{:.2f}'.format(model.score(x_test,y_test)))
plt.show()