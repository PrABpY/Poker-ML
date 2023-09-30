import Handing_Flop as ran
import pandas as pd
import xlsxwriter
import numpy as np

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

workbook = xlsxwriter.Workbook('dataset1.xlsx')
worksheet = workbook.add_worksheet('dataset')
row = 1
rate = 0
worksheet.write(0,0,'H')
while row <= 100:
	# print(card)
	table = ran.table()
	if len(set(table)) == 5 :
		ranking = rank_type(encode(split_card(table)[0]),split_card(table)[1])
		if ranking != 'High card' and ranking != 'One pair' and ranking != 'Two pair' and ranking != 'Three of a kind' :
			print("["+str(rate+1)+"]"+"table :",table)
			for j in range(5):
				worksheet.write(row,j,table[j])
			worksheet.write(row,5,rank_number(encode(split_card(table)[0]),split_card(table)[1]))
			worksheet.write(row,6,rank_type(encode(split_card(table)[0]),split_card(table)[1]))
			row += 1
	rate += 1
workbook.close()
 