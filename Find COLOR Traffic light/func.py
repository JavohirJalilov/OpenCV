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

def find_color(img):
    H,W = img.shape
    h = H//3
    red = img[:h,:]
    yellow = img[h:h*2,:]
    green = img[h*2:h*3,:]
    
    count_red = len(red[red == 0])
    count_yellow = len(yellow[yellow == 0])
    count_green = len(green[green == 0])
    min_color_black = min(count_red,count_yellow,count_green)
    color = ''
    if count_red == min_color_black:
        color = 'RED'
    elif count_yellow == min_color_black:
        color = 'YELLOW'
    elif count_green == min_color_black:
        color = 'GREEN'

    return color

def bbox_img(img_mask):
    # contours,_ = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHANIN_APPROX_SIMPLE)
    box = cv2.boundingRect(img_mask)
    x,y,w,h = box
    start_point = (x,y)
    end_point = (x+w,y+h)
    return start_point,end_point

def draw_bbox(img,bbox,colorname):
    start_point,end_point = bbox

    rect_img = cv2.rectangle(img,start_point,end_point,color=(255,0,0),thickness=5)
    cv2.putText(rect_img,colorname,(start_point[0],start_point[1]-10),5,2.0,color=(255,0,0),thickness=2)
    return rect_img