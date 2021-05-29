import matplotlib.pyplot as plt
import numpy as np
import cv2
from func import get_img, show
import func

RED_GRAY,RED = get_img('red_stop.jpg')
GREEN_GRAY,GREEN = get_img('green_go.jpg')
YELLOW_GRAY,YELLOW = get_img('yellow_wait.jpg')

show(RED)