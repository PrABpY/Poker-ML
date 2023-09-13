import Handing_Flop as ran
import pandas as pd
import xlsxwriter

workbook = xlsxwriter.Workbook('dataset.xlsx')
worksheet = workbook.add_worksheet('dataset')
for num in range(100):
	df = pd.read_excel('poker.xlsx',sheet_name='part').values.tolist()
	card = sum(df,[])
	# print(card)
	Hand = ran.Hand(card)
	print("Hand :",Hand,num)
	for use in Hand : card.remove(use)
	Flop = ran.Flop(card)
	print("Flop :",Flop)
	table = Flop
	for i in Hand : table.append(i)
	print(table)
	for j in range(5):
		worksheet.write(num,j,table[j])
workbook.close()
 