from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
import pandas as pd
import ranking 
import encodeCard

def predict(card):
	# card = ['J♦', 'J♥', '8♥', 'Q♦', '9♦']
	print(card)
	x_pre = [card]
	x_pre = ranking.rank_number(ranking.encode(ranking.split_card(x_pre[0])[0]),ranking.split_card(x_pre[0])[1]) + 0.3
	print(x_pre)
	y_pre = voting.predict([[x_pre,x_pre]])
	return y_pre[0]


df = pd.read_excel('poker.xlsx',sheet_name = 'dataset')

X = df[['Position1','Position2']]
y = df['Rank']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.3)

all_model = [('svm',SVC(kernel = 'rbf',gamma = 1)),
			 ('knn',KNeighborsClassifier(n_neighbors = 5)),
			 ('ann',MLPClassifier(hidden_layer_sizes = (4,5),activation = 'relu',solver = 'lbfgs',random_state = 0)),
			 ('baye',GaussianNB())]

voting = VotingClassifier(all_model,voting = 'hard')
voting.fit(X_train,y_train)
score = voting.score(X_test,y_test)
print('Accuracy : '+str(score*100)+'%')