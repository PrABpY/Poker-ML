import pandas as pd
import random

def Hand(card):
	H = random.choices(card,k = 2)
	return H

def Flop(card):
	Flop = random.choices(card,k = 3)
	return Flop

def table():
	df = pd.read_excel('poker.xlsx',sheet_name='part').values.tolist()
	table = random.choices(sum(df,[]),k = 5)
	while True :
		if len(set(table)) == 5 :
			return table
			break

def table_all():
	df = pd.read_excel('poker.xlsx',sheet_name='part').values.tolist()
	table = random.choices(sum(df,[]),k = 7)
	while True :
		if len(set(table)) == 7 :
			return table

if __name__ == '__main__' :
	# df = pd.read_excel('poker.xlsx',sheet_name='part').values.tolist()
	# card = sum(df,[])
	# # print(card)
	# Hand = Hand(card)
	# print("Hand :",Hand)
	# for use in Hand : card.remove(use)
	# Flop = Flop(card)
	print(table())