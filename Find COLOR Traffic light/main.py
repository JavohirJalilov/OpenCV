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


colorname_red = func.find_color(red_filter)
bbox_red = func.bbox_img(red_filter)

colorname_green = func.find_color(green_filter)
bbox_green = func.bbox_img(green_filter)

colorname_yellow = func.find_color(yellow_filter)
bbox_yellow = func.bbox_img(yellow_filter)

red_final = func.draw_bbox(RED,bbox_red,colorname_red)
green_final = func.draw_bbox(GREEN,bbox_green,colorname_green)
yellow_final = func.draw_bbox(YELLOW,bbox_yellow,colorname_yellow)

final_img = np.hstack((red_final,green_final,yellow_final))
final_img = cv2.cvtColor(final_img,cv2.COLOR_RGB2BGR)

cv2.imwrite('final_img.jpg',final_img)
show(final_img)