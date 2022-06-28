import keyboard
import mss
import cv2
from time import time, sleep
import pyautogui
import numpy as np

pyautogui.PAUSE = 0
sct = mss.mss()

"""
dimensions = {
        'left': 600,
        'top': 530,
        'width': 155,
        'height': 220
    }
scr = sct.grab(dimensions)
img = np.array(scr)
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.imwrite("./screen_left.png", img)
q

dimensions = {
		'left': 600,
        'top': 530 ,
        'width': 155,
        'height': 35
    }
scr = sct.grab(dimensions)
img = np.array(scr)
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.imwrite("./wood_left.png", img)
"""
if __name__ == "__main__":

    dimensions = {
        'left': 70,
        'top': 70,
        'width': 900,
        'height': 600
    }
    
    scr = sct.grab(dimensions)
    img = np.array(scr)
    
    img_hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # lower mask (0-10)
    lower_red = np.array([0,50,50])
    upper_red = np.array([3,255,255])
    mask0 = cv2.inRange(img_hsv, lower_red, upper_red)

    # join my masks
    mask = mask0
    print(mask.shape[0])
    print(mask.shape[1])
    # set my output img to zero everywhere except my mask
    output_img = img.copy()
    output_img[np.where(mask==0)] = 0
    
    cv2.imshow("image", output_img)
    cv2.waitKey(0)


    #cv2.imwrite("./health_bar.png", img)

