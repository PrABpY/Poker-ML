import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

def find_k(df):
    scale = StandardScaler()

    X = df[['Position1','Position2']]
    y = df[['Rank']]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)

    k_values = list(range(1, 21))
    accuracy_scores = []

    for k in k_values:
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(X_train, y_train.values.ravel())
        accuracy = knn.score(X_test, y_test)
        accuracy_scores.append(accuracy)

    return k_values,accuracy_scores

if __name__ == '__main__' :
    df = pd.read_excel('poker.xlsx', sheet_name='dataset')
    k_values,accuracy_scores = find_k(df)
    plt.figure(figsize=(10, 6))
    plt.plot(k_values, accuracy_scores, marker='o', linestyle='-')
    plt.title('Accuracy vs. K Value for KNN')
    plt.xlabel('K Value')
    plt.ylabel('Accuracy')
    plt.grid(True)
    plt.show()