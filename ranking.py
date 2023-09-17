import pandas as pd
import numpy as np
import xlsxwriter

def rank(number,symbol):
	if len(number) == max(number)-min(number) and len(set(number)) == len(number):
		if len(set(symbol)) == 1:
			if max(ranks) == 14:
				return 'Royal flush'
			return 'Straight flush'
		return 'Straight'
	if len(set(symbol)) == 1:
		return 'Flush'
	score = sum([number.count(i) for i in number])
	hand_names = {
        17: 'Four of a kind',
        13: 'Full house',
        11: 'Three of a kind',
        9: 'Two pair',
        7: 'One pair',
        5: 'High card'
        }
	return hand_names[score]

def encode(cnumber):
	en = {'J':11,'Q':12,'K':13,'A':14}
	for i in range(len(cnumber)):
		if cnumber[i] in en :
			cnumber[i] = en[cnumber[i]]
	return sorted(list(map(int,cnumber)))

def split_card(card):
	card = card[0:5]
	# print(card)
	number = []
	symbol = []
	for i in card:
		symbol.append(i[-1])
		number.append(i.replace(i[-1],""))
	return number,symbol

workbook = xlsxwriter.Workbook('dataset1.xlsx')
worksheet = workbook.add_worksheet('dataset')
df = pd.read_excel('poker.xlsx',sheet_name='dataset').values.tolist()
row = 0
col = 0
for card in df :
	print(rank(encode(split_card(card)[0]),split_card(card)[1]))
	worksheet.write(row,0,rank(encode(split_card(card)[0]),split_card(card)[1]))
	row += 1
workbook.close()