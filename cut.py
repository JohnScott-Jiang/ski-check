import os
import cv2

def calculate(pt):
    x=pt[2].item()-pt[0].item()
    y=pt[3].item()-pt[1].item()
    square=x*y
    return int(square)
def cutpic(xyxy_l,img,num):
    max=[]
    for xyxy in xyxy_l:
        sq=calculate(xyxy)
        if len(max)==0:
            max=xyxy
        elif sq>calculate(max):
            max=xyxy
    final=[int(i.item()) for i in max]
    
    os.makedirs('final',exist_ok=True)
    img=cv2.resize(img[final[1]:final[3],final[0]:final[2]],(96,96))
    cv2.imwrite(os.path.join('final', '%04d.jpg' % num),img)
