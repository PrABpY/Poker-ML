import Handing_Flop as ran
import pandas as pd
import xlsxwriter

workbook = xlsxwriter.Workbook('dataset1.xlsx')
worksheet = workbook.add_worksheet('dataset')
row = 1
worksheet.write(0,0,'H')
for num in range(700):
	# print(card)
	table = ran.table()
	if len(set(table)) == 5 :
		print("["+str(row+1)+"]"+"table :",table)
		for j in range(5):
			worksheet.write(row,j,table[j])
		row += 1
workbook.close()
 