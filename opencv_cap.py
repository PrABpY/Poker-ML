import numpy as np
import cv2
from mss import mss
from PIL import Image
import pandas as pd

card = ['Ap', 'Af', 'Ah', 'As', 
        '2p', '2f', '2h', '2s', 
        '3p', '3f', '3h', '3s', 
        '4p', '4f', '4h', '4s', 
        '5p', '5f', '5h', '5s', 
        '6p', '6f', '6h', '6s', 
        '7p', '7f', '7h', '7s', 
        '8p', '8f', '8h', '8s', 
        '9p', '9f', '9h', '9s', 
        '10p', '10f', '10h', '10s', 
        'Jp', 'Jf', 'Jh', 'Js', 
        'Qp', 'Qf', 'Qh', 'Qs', 
        'Kp', 'Kf', 'Kh', 'Ks']
card_change = {'Ap':'A♠', 'Af':'A♣', 'Ah':'A♥', 'As':'A♦', 
        '2p':'2♠', '2f':'2♣', '2h':'2♥', '2s':'2♦', 
        '3p':'3♠', '3f':'3♣', '3h':'3♥', '3s':'3♦', 
        '4p':'4♠', '4f':'4♣', '4h':'4♥', '4s':'4♦', 
        '5p':'5♠', '5f':'5♣', '5h':'5♥', '5s':'5♦', 
        '6p':'6♠', '6f':'6♣', '6h':'6♥', '6s':'6♦', 
        '7p':'7♠', '7f':'7♣', '7h':'7♥', '7s':'7♦', 
        '8p':'8♠', '8f':'8♣', '8h':'8♥', '8s':'8♦', 
        '9p':'9♠', '9f':'9♣', '9h':'9♥', '9s':'9♦', 
        '10p':'10♠', '10f':'10♣', '10h':'10♥', '10s':'10♦', 
        'Jp':'J♠', 'Jf':'J♣', 'Jh':'J♥', 'Js':'J♦', 
        'Qp':'Q♠', 'Qf':'Q♣', 'Qh':'Q♥', 'Qs':'Q♦', 
        'Kp':'K♠', 'Kf':'K♣', 'Kh':'K♥', 'Ks':'K♦'}

bounding_box = {'top': 400, 'left': 650, 'width': 600, 'height': 180}
sct = mss()
print(card[0])
template = []

for i in card:
    template.append(cv2.imread('cv/img/vertical/'+i+'.png',0))

# print(template)

w, h = (30,60)

while True:
    sct_img = np.array(sct.grab(bounding_box))
    img_gray = cv2.cvtColor(sct_img, cv2.COLOR_BGR2GRAY)

    hand = []
    for i in range(len(template)) :
        res = cv2.matchTemplate(img_gray,template[i],cv2.TM_CCOEFF_NORMED)
        threshold = 0.82
        loc = np.where(res >= threshold)
        # print(len(loc[0]))
        if len(loc[0]) == 1 :
            hand.append(card_change[card[i]])
        for pt in zip(*loc[::-1]):
            cv2.rectangle(sct_img, pt, (pt[0] + w, pt[1] + h), (0,255,0), 3)

    print(hand)
    cv2.imshow('screen', sct_img)

    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        cv2.destroyAllWindows()
        break