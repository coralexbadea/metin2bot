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
        'left': 400,
        'top': 5,
        'width': 500,
        'height': 100
    }
 

health_bar = cv2.imread('./health_bar.png')

fps_time = time()

while 1:

    if not found:
        #random click 
        for x in range(100,900,(50+(random.randint(1, 10)))):
            if found: break
            for y in range(100,600,(50+(random.randint(1, 10)))):
                
                pyautogui.moveTo(x=x, y=y)
                pyautogui.click(button='right')
                sleep(2)
                scr = numpy.array(sct.grab(dimensions))

                # Cut off alpha
                scr_remove = scr[:,:,:3]

                result = cv2.matchTemplate(scr_remove, health_bar, cv2.TM_CCOEFF_NORMED)

                _, max_val, _, max_loc = cv2.minMaxLoc(result)
                print(f"Max Val: {max_val} Max Loc: {max_loc}")

                if max_val > .50:
                    found=True
                    sleep(random.randint(3, 5)/10)
                    pyautogui.click(x=x, y=y)
                    
                    break  
                    
    else:
        scr = numpy.array(sct.grab(dimensions))
        scr_remove = scr[:,:,:3]
        result = cv2.matchTemplate(scr_remove, health_bar, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)
        sleep(random.randint(3, 10)/10)
        if max_val < .50:
            found=False

	
    
    
    ##break
    if keyboard.is_pressed('q'):
        break
    print('FPS: {}'.format(1 / (time() - fps_time)))
    fps_time = time()
