import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.decomposition import PCA
from sklearn.metrics import accuracy_score
import find_K
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel('poker.xlsx',sheet_name = 'dataset')

scale = StandardScaler()
encode = LabelEncoder()

X = df[['Position1','Position2']]
y = encode.fit_transform(df['Rank'])

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.5,random_state = 0)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

pca = PCA(n_components = 2)
X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.transform(X_test)

k = 5
knn = KNeighborsClassifier(n_neighbors = k)
knn.fit(X_train_pca, y_train)

y_pred = knn.predict(X_test_pca)

accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy of KNN : {accuracy*100:.4f}%')

k_values,accuracy_scores = find_K.find_k(df)

fig, (ax1, ax2) = plt.subplots(2,1,figsize = (10,8))
fig.suptitle('Horizontally stacked subplots')
a = ax1.scatter(X_test_pca[:,0],X_test_pca[:,1],c = y_test,cmap = 'viridis')
ax1.set_title(f'KNN Prediction (K={k})')
ax1.set_xlabel('Position1')
ax1.set_ylabel('Position2')
fig.colorbar(a,label = 'Target')
ax1.grid(True)

ax2.plot(k_values, accuracy_scores,marker = 'o',linestyle = '-')
ax2.set_xlabel('K Value')
ax2.set_ylabel('Accuracy')
ax2.grid(True)

plt.show()