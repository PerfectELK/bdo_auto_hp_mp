from directkeys import PressKey, ReleaseKey, STAMINA, HEALTH
import time
from PIL import Image, ImageGrab
import numpy as np
import cv2
import json
import pytesseract
import os


dir_ = os.getcwd()
hsv_min = np.array((100, 100, 100), np.uint8)
hsv_max = np.array((255, 255, 255), np.uint8)

time.sleep(3)

while True:
    image = ImageGrab.grab(bbox=(750, 900, 1150, 1025))
    image_np = np.array(image.getdata(), dtype='uint8').reshape(image.size[1], image.size[0], 3)
    thresh = cv2.inRange(image_np, hsv_min, hsv_max)
    cv2.imwrite("in_memory_to_disk.png", thresh)
    thresh = cv2.threshold(thresh, 0, 255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]


    # PressKey(HEALTH)
    # ReleaseKey(HEALTH)
    time.sleep(10)

