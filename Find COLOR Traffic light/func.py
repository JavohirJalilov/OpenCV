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