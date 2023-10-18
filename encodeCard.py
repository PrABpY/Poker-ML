import Handing_Flop as ran
import pandas as pd
import xlsxwriter
import numpy as np
import itertools

def symbol_to_number(csymbol):
	en = {'♠':0.02,'♦':0.03,'♥':0.09,'♣':0.01}
	for i in range(len(csymbol)):
		if csymbol[i] in en :
			csymbol[i] = en[csymbol[i]]
	return sorted(list(csymbol))

def rank_number(number,symbol):
	num_sym = sum(symbol_to_number(symbol))
	if len(number)-1 == max(number)-min(number) and len(set(number)) == len(number):
		if len(set(symbol)) == 1:
			if max(number) == 14:
				return 14.0+num_sym
			return 10.0+num_sym
		return 8.0+num_sym
	if len(set(symbol)) == 1:
		return 6.0+num_sym
	score = float(sum([number.count(i) for i in number]))
	return score+num_sym

def rank_type(number,symbol):
	if len(number)-1 == max(number)-min(number) and len(set(number)) == len(number):
		if len(set(symbol)) == 1:
			if max(number) == 14:
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

def get_best_card(card):
	rank = {'Royal flush':0,
	'Straight flush':1,
	'Straight':2,
	'Flush':3,
	'Four of a kind':4,
	'Full house':5,
	'Three of a kind':6,
	'Two pair':7,
	'One pair':8,
	'High card':9}
	all_hand_combos = list(itertools.combinations(card, 5))
	test_all = []
	for best in range(len(all_hand_combos)):test_all.append(rank[rank_type(encode(split_card(list(all_hand_combos[best]))[0]),split_card(list(all_hand_combos[best]))[1])])
	top_rank = min(test_all)
	for num in range(len(test_all)):
		if test_all[num] == top_rank:
			return list(all_hand_combos[num])

if __name__ == '__main__' :
	workbook = xlsxwriter.Workbook('dataset1.xlsx')
	worksheet = workbook.add_worksheet('dataset')
	row = 0
	rate = 0
	while row <= 20:
		table = ran.table_all()
		# print(table)
		if len(set(table)) == 7 :
			card = get_best_card(table)
			ranking = rank_type(encode(split_card(card)[0]),split_card(card)[1])
			# print(card,ranking)
			if ranking == 'Royal flush':
				print("["+str(rate+1)+"]"+"table :",card,"num =",row)
				for j in range(5):
					worksheet.write(row,j,card[j])
				worksheet.write(row,5,rank_number(encode(split_card(card)[0]),split_card(card)[1]))
				worksheet.write(row,6,ranking)
				row += 1
		rate += 1
	workbook.close()
	# print(get_best_card(ran.table_all()))