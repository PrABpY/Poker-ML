import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.decomposition import PCA
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel('poker.xlsx', sheet_name='dataset')

scale = StandardScaler()
encode = LabelEncoder()

X = df[['Position1','Position2']]
y = encode.fit_transform(df['Rank'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

pca = PCA(n_components=2)
X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.transform(X_test)

k = 2 
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train_pca, y_train)

y_pred = knn.predict(X_test_pca)

accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy of KNN with {k} neighbors: {accuracy:.2f}')

plt.figure(figsize=(10, 6))
plt.scatter(X_test_pca[:, 0], X_test_pca[:, 1], c=y_test, cmap='viridis')
plt.title(f'KNN Prediction (K={k})')
plt.xlabel('Position1')
plt.ylabel('Position2')
plt.colorbar(label='Target')
plt.grid(True)
plt.show()