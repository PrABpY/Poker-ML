from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier,plot_tree
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('poker.xlsx', sheet_name='dataset')

x = df[['H1','H2','H3','H4','H5']]
# x = df[['Encode_sum','Position1','Position2']]
y = df['Rank']
x = x.apply(LabelEncoder().fit_transform)
model = DecisionTreeClassifier(criterion = 'entropy')
model.fit(x,y)
plt.figure(figsize = (16,9))
t = plot_tree(model)
plt.show()