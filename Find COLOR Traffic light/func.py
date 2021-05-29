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