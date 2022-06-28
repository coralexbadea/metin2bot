import keyboard
import mss
import cv2
import numpy
from time import time, sleep
import pyautogui
import numpy as np
import random


pyautogui.PAUSE = 0

print("Press 's' to start playing.")
print("Once started press 'q' to quit.")
keyboard.wait('s')
found = False

sct = mss.mss()

dimensions = {
    'left': 70,
    'top': 70,
    'width': 900,
    'height': 600
}

fps_time = time()
radius = 250
inner_radius = 55
shift_y = 50
shift_x = -10
shift_click_x = 10
shift_click_y = 10
count = 0
while 1:
    flag = False
    scr = sct.grab(dimensions)
    img = np.array(scr)
    img_hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # lower mask (0-10)
    lower_red = np.array([0,200,200])
    upper_red = np.array([3,255,255])
    mask = cv2.inRange(img_hsv, lower_red, upper_red)
    mask[int(mask.shape[0]/2-inner_radius+shift_y):int(mask.shape[0]/2+inner_radius+shift_y),
           int(mask.shape[1]/2-inner_radius+shift_x):int(mask.shape[1]/2+inner_radius+shift_x)] = 0
    """
    output_img = img.copy()
    output_img[np.where(mask==0)] = 0
    
    cv2.imshow("image", output_img)
    cv2.waitKey(0)
    exit()
    """
    count += 1
    for i in range(int(mask.shape[0]/2-radius),int(mask.shape[0]/2+radius)):
        if(flag): break
        for j in range(int(mask.shape[1]/2-radius),int(mask.shape[1]/2+radius)):
            if(mask[i,j] != 0):
                print("here") 
                pyautogui.moveTo(x=(j+70), y=(i+70+shift_click_y))
                sleep(random.randint(1,2)/10)
                pyautogui.click(clicks=2, interval=random.randint(20,35)/100)              
                flag = True
                count = 0
                break
                
    if(count > 10):
        print("cacat")
        count = 0;
        if(random.randint(1,2) % 2):
            click_y = dimensions['top'] + 120
            click_x = dimensions['left']+20 +dimensions['width']/2
        else:
            click_y = dimensions['top'] + 120 + dimensions['height']/2 + 100
            click_x = dimensions['left']+20 +dimensions['width']/2
        #click_y = (random.randint(dimensions['top']+20, dimensions['top']+dimensions['height']-100))
        #click_x = (random.randint(dimensions['left']+20, dimensions['left']+dimensions['width']-100))  
        pyautogui.moveTo(x=click_x, y=click_y)
        sleep(random.randint(1,2)/10)
        pyautogui.click(clicks=2, interval=random.randint(20,35)/100)
    ##break
    if keyboard.is_pressed('q'):
        break
    print('FPS: {}'.format(1 / (time() - fps_time)))
    fps_time = time()
