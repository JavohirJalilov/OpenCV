import matplotlib.pyplot as plt
import numpy as np
import cv2
from func import get_img, show
import func

RED_GRAY,RED = get_img('red_stop.jpg')
GREEN_GRAY,GREEN = get_img('green_go.jpg')
YELLOW_GRAY,YELLOW = get_img('yellow_wait.jpg')

red_mask = func.get_mask(RED)
green_mask = func.get_mask(GREEN)
yellow_mask = func.get_mask(YELLOW)

red_ROI = func.get_ROI(RED,red_mask)
green_ROI = func.get_ROI(GREEN,green_mask)
yellow_ROI = func.get_ROI(YELLOW,yellow_mask)

red_filter = func.filters_img(red_ROI,87,140,func.kernal)
green_filter = func.filters_img(green_ROI,120,255,func.kernal)
yellow_filter = func.filters_img(yellow_ROI,120,255,func.kernal)

show(red_filter)