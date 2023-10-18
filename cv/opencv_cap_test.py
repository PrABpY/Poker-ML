import numpy as np
import cv2
from mss import mss
from PIL import Image
import pandas as pd

df = pd.read_excel('poker.xlsx',sheet_name='part').values.tolist()
card = sum(df,[])

bounding_box = {'top': 500, 'left': 750, 'width': 300, 'height': 300}

sct = mss()
template = []

for i in card:
    template.append(cv2.imread('img/vertical'+i+'.png',0))

w, h = (30,30)
cla = {0:'♠',1:'♠'}

while True:
    sct_img = np.array(sct.grab(bounding_box))
    img_gray = cv2.cvtColor(sct_img, cv2.COLOR_BGR2GRAY)

    hand = []
    for i in range(len(template)) :
        res = cv2.matchTemplate(img_gray,template[i],cv2.TM_CCOEFF_NORMED)
        threshold = 0.95
        loc = np.where(res >= threshold)
        # print(len(loc[0]))
        if len(loc[0]) == 1 :
            hand.append(cla[i])
        for pt in zip(*loc[::-1]):
            cv2.rectangle(sct_img, pt, (pt[0] + w, pt[1] + h), (255,0,0), 1)

    print(hand)
    cv2.imshow('screen', sct_img)

    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        cv2.destroyAllWindows()
        break