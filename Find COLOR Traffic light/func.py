import matplotlib.pyplot as plt
import numpy as np
import cv2

# utility 
def show(img,s=8,b=False):
    '''
    img: image
    return: None
    '''
    plt.figure(figsize=(s,s))
    plt.imshow(img,cmap='gray')
    plt.grid(alpha=.2)
    plt.grid(b)
    plt.show()

def get_img(name):
    '''
    name: image name
    return: grayscale image
    '''
    img = cv2.imread(name)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img = cv2.blur(img,(12,12))
    gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    return gray,img

def get_mask(img):
    mask = np.zeros(img.shape,dtype=np.uint8)
    mask = cv2.rectangle(mask,(180,180),(600,1400),color=(255,255,255),thickness=-1)
    return mask

def get_ROI(img,mask):
    ROI_img = cv2.bitwise_and(img,mask)
    ROI_img = cv2.cvtColor(ROI_img,cv2.COLOR_RGB2GRAY)
    return ROI_img

def kernal(x,y):
    k = np.ones((x,y),dtype=np.uint8)
    return k

def filters_img(ROI_img,start_color,stop_color,kernal):
    img = cv2.inRange(ROI_img,start_color,stop_color)
    opening = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernal(20,20))
    dilation = cv2.dilate(opening,kernal(18,18))
    return dilation