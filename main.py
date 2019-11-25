from directkeys import PressKey, ReleaseKey, STAMINA, HEALTH
import time
from PIL import ImageGrab
import numpy as np
import cv2
import keyboard
from threading import *

run = [True]

keys = []
keys.append('f12')

def listen(key, run):
    while True:
        keyboard.wait(key)
        if run[0] is False:
            run[0] = True
        else:
            run[0] = False
        print("ВКЛ" if run[0] else "ВЫКЛ")

threads = [Thread(target=listen, kwargs={"key": key, "run": run}) for key in keys]
for thread in threads:
    thread.start()

# hsv_min = np.array((100, 100, 100), np.uint8)
# hsv_max = np.array((255, 255, 255), np.uint8)

hsv_stamina_min = np.array((125, 70, 0), np.uint8)
hsv_stamina_max = np.array((220, 255, 100), np.uint8)

hsv_hp_min = np.array((100, 0, 0), np.uint8)
hsv_hp_max = np.array((255, 60, 30), np.uint8)


def select_color(min, max, image_array):
    return cv2.inRange(image_array, min, max)

time.sleep(3)
# 1700 stamina
# 6000 hp num
while True:
    while run[0]:
        image = ImageGrab.grab(bbox=(145, 40, 455, 95))
        image.save('image.png')
        image_np = np.array(image.getdata(), dtype='uint8').reshape(image.size[1], image.size[0], 3)
        stamina = select_color(hsv_stamina_min, hsv_stamina_max, image_np)
        hp = select_color(hsv_hp_min, hsv_hp_max, image_np)
        cv2.imwrite('hp.png', hp)
        cv2.imwrite('stam.png', stamina)
        staminaNum = cv2.countNonZero(stamina)
        hpNum = cv2.countNonZero(hp)

        if hpNum < 5200:
            PressKey(HEALTH)
            time.sleep(.1)
            ReleaseKey(HEALTH)
        if staminaNum <= 1700:
            PressKey(STAMINA)
            time.sleep(.1)
            ReleaseKey(STAMINA)
        time.sleep(.5)
    if run[0] is False:
        time.sleep(4)



