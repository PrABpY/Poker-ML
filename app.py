import tkinter as tk
from tkinter import *
from itertools import product
from PIL import Image, ImageTk
import model
import ranking 
import probability

def create_deck():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['♥', '♦', '♣', '♠']
    deck = [{'rank': rank, 'suit': suit} for rank, suit in product(ranks, suits)]
    return deck

def show_card(card,bcard,st):
    card_label.config(text=card)
    bast_card.config(text=bcard)
    Royal_flush.config(text = f"{st[0]:.2f}")
    Straight_flush.config(text = f"{st[1]:.2f}")
    Straight.config(text = f"{st[2]:.2f}")
    Flush.config(text = f"{st[3]:.2f}")
    Four_of_a_kind.config(text = f"{st[4]:.2f}")
    Full_house.config(text = f"{st[5]:.2f}")
    Three_of_a_kind.config(text = f"{st[6]:.2f}")
    Two_pair.config(text = f"{st[7]:.2f}")
    One_pair.config(text = f"{st[8]:.2f}")
    High_car.config(text = f"{st[9]:.2f}")
    bast_cards_final.config(text = ' '.join(st[10]))

def deal_specific_card(rank, suit):
    card = next((c for c in deck if c['rank'] == rank and c['suit'] == suit), None)
    c = "".join([card['rank'],card['suit']])
    typec = ""
    if card:
        if c not in a and len(a) < 5:
            # deck.remove(card)
            a.append(c)
            # print(a)
            if len(a) == 1 : typec = 'High card'
            if len(a) == 2 :
                a_c = a[:]
                for g in range(-3,0) : a_c.append(str(g)+'o')
                typec = model.predict(a_c)
            if len(a) == 3 :
                a_c = a[:]
                for g in range(-2,0) : a_c.append(str(g)+'o')
                typec = model.predict(a_c)
            if len(a) == 4 :
                a_c = a[:]
                for g in range(-1,0) : a_c.append(str(g)+'o')
                typec = model.predict(a_c)
            if len(a) == 5 : 
                typec = model.predict(a)
            # print(typec)
            pre_all = probability.status(a)
            print(pre_all)
            show_card(" ".join(a),typec,pre_all)

def reset():
    x = 0
    if len(a) > 1 :
        a.remove(a[-1])
        if len(a) == 1 : typec = 'High card'
        if len(a) == 2 :
            a_c = a[:]
            for g in range(-3,0) : a_c.append(str(g)+'o')
            typec = model.predict(a_c)
        if len(a) == 3 :
            a_c = a[:]
            for g in range(-2,0) : a_c.append(str(g)+'o')
            typec = model.predict(a_c)
        if len(a) == 4 :
            a_c = a[:]
            for g in range(-1,0) : a_c.append(str(g)+'o')
            typec = model.predict(a_c)
        if len(a) == 5 : typec = model.predict(a)
        x = 1
    if len(a) == 1 and x == 0:
        a.remove(a[0])
        typec = " "
    if len(a) == 0 : typec = " "
    pre_all = probability.status(a)
    show_card(" ".join(a),typec,pre_all)

deck = create_deck()
root = tk.Tk()
root.title("Poker Cal")

card = ['A-♠','2-♠','3-♠','4-♠','5-♠','6-♠','7-♠','8-♠','9-♠','10-♠','J-♠','Q-♠','K-♠',
        'A-♣','2-♣','3-♣','4-♣','5-♣','6-♣','7-♣','8-♣','9-♣','10-♣','J-♣','Q-♣','K-♣',
        'A-♥','2-♥','3-♥','4-♥','5-♥','6-♥','7-♥','8-♥','9-♥','10-♥','J-♥','Q-♥','K-♥',
        'A-♦','2-♦','3-♦','4-♦','5-♦','6-♦','7-♦','8-♦','9-♦','10-♦','J-♦','Q-♦','K-♦']

a = []
my_img = []

for i in range(52):
    image = Image.open('PNG-cards-1.3/'+str(i)+'.png')
    img = image.resize((85, 120))
    my_img.append(ImageTk.PhotoImage(img))

left_frame = tk.Frame(root)
left_frame.grid(row = 0,column = 0)

top_frame = tk.Frame(left_frame)
top_frame.grid(row = 0,column = 0)

card_label = tk.Label(top_frame, text="", font=('Helvetica', 65))
card_label.grid(row = 0,column = 0,sticky=W,padx = 20)
space_label = tk.Label(top_frame, text=" ", font=('Helvetica', 1))
space_label.grid(row = 1,column = 0,sticky=W,padx = 530)

button_frame = tk.Frame(left_frame)
button_frame.grid(row = 1,column = 0)

for i in range(len(card)):
    # print(card[i].split('-'))
    r = card[i].split('-')
    button = tk.Button(button_frame, text=card[i],image = my_img[i],borderwidth = 0, command=lambda r=r[0], s=r[1]: deal_specific_card(r, s))
    button.grid(row=i // 13, column=i % 13,padx = 3,pady = 3)

image = Image.open('ui/backspace.png')
img = image.resize((120, 100))
bb = ImageTk.PhotoImage(img)
reset = tk.Button(top_frame, text="reset",image = bb,borderwidth = 0, command=reset)
reset.grid(row = 0,column = 1,sticky=E)

status_frame = tk.Frame(root)
status_frame.grid(row = 0,column = 1,sticky=N,pady = 20)

status_frame_top = tk.Frame(status_frame)
status_frame_top.grid(row = 0,column = 0,sticky=N,pady = 5)

tk.Label(status_frame_top, text="Best Card :", font=('Helvetica', 16)).grid(row = 0,column = 0,sticky=W,padx = 20)
bast_card = tk.Label(status_frame_top, text="", font=('Helvetica', 25))
bast_card.grid(row = 1,column = 0,sticky=W,padx = 20)
tk.Label(status_frame_top, text="_________________________", font=('Helvetica', 16)).grid(row = 2,column = 0,sticky=W,padx = 20)

status_frame_bottom = tk.Frame(status_frame)
status_frame_bottom.grid(row = 1,column = 0,sticky=N,pady = 10)

tk.Label(status_frame_bottom, text="Royal flush :", font=('Helvetica', 15)).grid(row = 0,column = 0,sticky=W,padx = 20)
Royal_flush = tk.Label(status_frame_bottom, text="0.00", font=('Helvetica', 15))
Royal_flush.grid(row = 0,column = 1,sticky=W,padx = 20)
tk.Label(status_frame_bottom, text="Straight flush :", font=('Helvetica', 15)).grid(row = 1,column = 0,sticky=W,padx = 20)
Straight_flush = tk.Label(status_frame_bottom, text="0.00", font=('Helvetica', 15))
Straight_flush.grid(row = 1,column = 1,sticky=W,padx = 20)
tk.Label(status_frame_bottom, text="Straight :", font=('Helvetica', 15)).grid(row = 2,column = 0,sticky=W,padx = 20)
Straight = tk.Label(status_frame_bottom, text="0.00", font=('Helvetica', 15))
Straight.grid(row = 2,column = 1,sticky=W,padx = 20)
tk.Label(status_frame_bottom, text="Flush :", font=('Helvetica', 15)).grid(row = 3,column = 0,sticky=W,padx = 20)
Flush = tk.Label(status_frame_bottom, text="0.00", font=('Helvetica', 15))
Flush.grid(row = 3,column = 1,sticky=W,padx = 20)
tk.Label(status_frame_bottom, text="Four of a kind :", font=('Helvetica', 15)).grid(row = 4,column = 0,sticky=W,padx = 20)
Four_of_a_kind = tk.Label(status_frame_bottom, text="0.00", font=('Helvetica', 15))
Four_of_a_kind.grid(row = 4,column = 1,sticky=W,padx = 20)
tk.Label(status_frame_bottom, text="Full house :", font=('Helvetica', 15)).grid(row = 5,column = 0,sticky=W,padx = 20)
Full_house = tk.Label(status_frame_bottom, text="0.00", font=('Helvetica', 15))
Full_house.grid(row = 5,column = 1,sticky=W,padx = 20)
tk.Label(status_frame_bottom, text="Three of a kind :", font=('Helvetica', 15)).grid(row = 6,column = 0,sticky=W,padx = 20)
Three_of_a_kind = tk.Label(status_frame_bottom, text="0.00", font=('Helvetica', 15))
Three_of_a_kind.grid(row = 6,column = 1,sticky=W,padx = 20)
tk.Label(status_frame_bottom, text="Two pair :", font=('Helvetica', 15)).grid(row = 7,column = 0,sticky=W,padx = 20)
Two_pair = tk.Label(status_frame_bottom, text="0.00", font=('Helvetica', 15))
Two_pair.grid(row = 7,column = 1,sticky=W,padx = 20)
tk.Label(status_frame_bottom, text="One pair :", font=('Helvetica', 15)).grid(row = 8,column = 0,sticky=W,padx = 20)
One_pair = tk.Label(status_frame_bottom, text="0.00", font=('Helvetica', 15))
One_pair.grid(row = 8,column = 1,sticky=W,padx = 20)
tk.Label(status_frame_bottom, text="High card :", font=('Helvetica', 15)).grid(row = 9,column = 0,sticky=W,padx = 20)
High_car = tk.Label(status_frame_bottom, text="0.00", font=('Helvetica', 15))
High_car.grid(row = 9,column = 1,sticky=W,padx = 20)
for i in range(10):
    tk.Label(status_frame_bottom, text="%", font=('Helvetica', 15)).grid(row = i,column = 2,sticky=N,padx = 20)
tk.Label(status_frame_bottom, text=" ").grid(row = 10,column = 1,sticky=N,padx = 50)

status_frame_bottoms = tk.Frame(status_frame)
status_frame_bottoms.grid(row = 2,column = 0,sticky=N)

tk.Label(status_frame_bottoms, text="Final Rank", font=('Helvetica', 16)).grid(row = 0,column = 0,padx = 20)
bast_cards = tk.Label(status_frame_bottoms, text="", font=('Helvetica', 10))
bast_cards.grid(row = 1,column = 0,padx = 20)
tk.Label(status_frame_bottoms, text="_________________________", font=('Mitr', 16)).grid(row = 3,column = 0,sticky=N)
bast_cards_final = tk.Label(status_frame_bottoms, text="", font=('Helvetica', 25))
bast_cards_final.grid(row = 2,column = 0,padx = 20)

root.mainloop()
