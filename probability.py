import itertools
import pandas as pd
import xlsxwriter
import ranking
import model
import Handing_Flop as ran
import random

def porb(table):
    df = pd.read_excel('poker.xlsx',sheet_name = 'part').values.tolist()
    data = list(itertools.chain.from_iterable(df))
    # table = ['5♦', '5♥', '5♣', '10♦', '9♦']
    for i in table : data.remove(i)
    all_card = []
    card_type = []
    c_card = []
    # print(len(combo_card))
    if len(table) == 5:
        combo_card = list(itertools.combinations(data,2))
        for i in combo_card :
            tables = table[:]
            tables.append(i[0])
            tables.append(i[1])
            all_card.append(tables)
            # print(tables)
            pre = ranking.get_best_card(tables)
            # c_card.append(pre)
            c_card = all_card
            pre_card = ranking.rank_type(ranking.encode(ranking.split_card(pre)[0]),ranking.split_card(pre)[1])
            # print(tables,pre,pre_card)
            card_type.append(pre_card)

    if len(table) == 4:
        combo_card = list(itertools.combinations(data,1))
        for i in combo_card :
            tables = table[:]
            tables.append(i[0])
            all_card.append(tables)
            # print(tables)
            pre = ranking.get_best_card(tables)
            c_card.append(pre)
            pre_card = ranking.rank_type(ranking.encode(ranking.split_card(pre)[0]),ranking.split_card(pre)[1])
            # print(tables,pre,pre_card)
            card_type.append(pre_card)

    if len(table) == 3:
        combo_card = list(itertools.combinations(data,2))
        for i in combo_card :
            tables = table[:]
            tables.append(i[0])
            tables.append(i[1])
            all_card.append(tables)
            # print(tables)
            pre = ranking.get_best_card(tables)
            c_card.append(pre)
            pre_card = ranking.rank_type(ranking.encode(ranking.split_card(pre)[0]),ranking.split_card(pre)[1])
            # print(tables,pre,pre_card)
            card_type.append(pre_card)

    if len(table) == 2:
        combo_card = list(itertools.combinations(data,3))
        for i in combo_card :
            tables = table[:]
            tables.append(i[0])
            tables.append(i[1])
            tables.append(i[2])
            all_card.append(tables)
            # print(tables)
            pre = ranking.get_best_card(tables)
            c_card.append(pre)
            pre_card = ranking.rank_type(ranking.encode(ranking.split_card(pre)[0]),ranking.split_card(pre)[1])
            # print(tables,pre,pre_card)
            card_type.append(pre_card)

    return card_type,c_card[random.randint(0,len(c_card))]

def status(table):
    if len(table) <= 1 :
        return 0,0,0,0,0,0,0,0,0,0,""
    card_type,pre = porb(table)
    sample = len(card_type)
    Royal_flush = (card_type.count('Royal flush')/sample)*100
    Straight_flush = (card_type.count('Straight flush')/sample)*100
    Straight = (card_type.count('Straight')/sample)*100
    Flush = (card_type.count('Flush')/sample)*100
    Four_of_a_kind = (card_type.count('Four of a kind')/sample)*100
    Full_house = (card_type.count('Full house')/sample)*100
    Three_of_a_kind = (card_type.count('Three of a kind')/sample)*100
    Two_pair = (card_type.count('Two pair')/sample)*100
    One_pair = (card_type.count('One pair')/sample)*100
    High_car = (card_type.count('High card')/sample)*100
    return Royal_flush,Straight_flush,Straight,Flush,Four_of_a_kind,Full_house,Three_of_a_kind,Two_pair,One_pair,High_car,pre

def status_print(table):
    if len(table) == 1 :
        return 0,0,0,0,0,0,0,0,0,0
    card_type = porb(table)
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

# table = ['10♣','10♥']
# status_print(table)
# model.predict(table)