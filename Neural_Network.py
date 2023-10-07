from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import Handing_Flop as ran
import ranking 

df = pd.read_excel('poker.xlsx', sheet_name='dataset')

x = df[['Encode_sum','Position1','Position2']]
y = df['Rank']

x_train, x_test, y_train, y_test = train_test_split(x, y,test_size = 0.3, random_state=0)

model = MLPClassifier(hidden_layer_sizes=(4, 5),activation='relu',solver='lbfgs',random_state=0)

model.fit(x_train, y_train)
table = ran.table()
x_pre = [table]
x_pre = ranking.rank_number(ranking.encode(ranking.split_card(x_pre[0])[0]),ranking.split_card(x_pre[0])[1])
y_pre = model.predict([[x_pre,x_pre,x_pre]])
print(table)
print(x_pre)
print('Prediction:', y_pre[0])
print('Accuracy :', model.score(x_test, y_test)*100,'%')
# print('weight:')
# print(*model.coefs_, sep='\n')
# print()
# print('bias:')
# print(*model.intercepts_, sep='\n')