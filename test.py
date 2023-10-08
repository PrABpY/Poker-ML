import itertools
import pandas as pd
import xlsxwriter
import ranking

df = pd.read_excel('poker.xlsx',sheet_name = 'part').values.tolist()
data = list(itertools.chain.from_iterable(df))
table = ['A♦', '7♠', '10♠', '5♣', '2♥']
for i in table : data.remove(i)
combo_card = list(itertools.combinations(data,2))
all_card = []
card_type = []
for i in combo_card :
    table = ['A♦', '7♠', '10♠', '5♣', '2♥']
    table.append(i[0])
    table.append(i[1])
    all_card.append(table)
    # print(table)
    pre = ranking.get_best_card(table)
    pre_card = ranking.rank_type(ranking.encode(ranking.split_card(pre)[0]),ranking.split_card(pre)[1])
    print(table,pre,pre_card)
    card_type.append(pre_card)

sample = len(card_type)
Royal_flush = card_type.count('Royal flush')
Straight_flush = card_type.count('Straight flush')
Straight = card_type.count('Straight')
Flush = card_type.count('Flush')
Four_of_a_kind = card_type.count('Four of a kind')
Full_house = card_type.count('Full house')
Three_of_a_kind = card_type.count('Three of a kind')
Two_pair = card_type.count('Two pair')
One_pair = card_type.count('One pair')
High_car = card_type.count('High card')

print(f'Royal flush : {(Royal_flush/sample)*100:.2f}'.format(),"%")
print(f'Straight flush : {(Straight_flush/sample)*100:.2f}'.format(),"%")
print(f'Straight : {(Straight/sample)*100:.2f}'.format(),"%")
print(f'Flush : {(Flush/sample)*100:.2f}'.format(),"%")
print(f'Four of a kind : {(Four_of_a_kind/sample)*100:.2f}'.format(),"%")
print(f'Full house : {(Full_house/sample)*100:.2f}'.format(),"%")
print(f'Three of a kind : {(Three_of_a_kind/sample)*100:.2f}'.format(),"%")
print(f'Two pair : {(Two_pair/sample)*100:.2f}'.format(),"%")
print(f'One pair : {(One_pair/sample)*100:.2f}'.format(),"%")
print(f'High card : {(High_car/sample)*100:.2f}'.format(),"%")