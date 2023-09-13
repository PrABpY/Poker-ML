import pandas as pd
import random

def Hand(card):
	H = random.choices(card,k = 2)
	return H

def Flop(card):
	Flop = random.choices(card,k = 3)
	return Flop

if __name__ == '__main__' :
	df = pd.read_excel('poker.xlsx',sheet_name='part').values.tolist()
	card = sum(df,[])
	# print(card)
	Hand = Hand(card)
	print("Hand :",Hand)
	for use in Hand : card.remove(use)
	Flop = Flop(card)
	print("Flop :",Flop)