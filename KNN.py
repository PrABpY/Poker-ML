import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.model_selection import train_test_split

df = pd.read_excel('poker.xlsx',sheet_name='dataset')
# df['Rank'] = encode.fit_transform(df['Rank'])

scale = StandardScaler()
x = df[['H1','H2','H3','H4','H5']]
# x = scale.fit_transform(x)
print(x)
y = df[['Rank']]
# y = scale.fit_transform(y)
# print(y)

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state = 42)

K = 4
model = KNeighborsClassifier(n_neighbors = K)
model.fit(x_train,y_train)

x_pre = [['5♠', '5♣', '5♣', '10♦', '7♣']]
x_pre = encode.fit_transform(x_pre[0])
print(x_pre)
y_pre = model.predict([x_pre])
print('Rank :',y_pre[0])
print('Accuracy :','{:.2f}'.format(model.score(x_test,y_test)))