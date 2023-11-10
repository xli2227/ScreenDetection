# import pyscreenshot as ImageGrab
import pytesseract
import cv2
# import sys
# from PIL import Image
from playsound import playsound

alarm_path = 'assets/attention.mp3'

# get two points for screenshot boundary
# x1 = sys.argv[1], y1 = sys.argv[2]
# x2 = sys.argv[3], y2 = sys.argv[4]


# Task1: Logic for screenshot, nice to have cursor included
# https://stackoverflow.com/questions/72328718/python-take-screenshot-including-mouse-cursor
# im=ImageGrab.grab(bbox=(x1,y1,x2,y2))
# im.show()
# to file
# ImageGrab.grab_to_file('im.png')

# Load image for detection processing
image = cv2.imread('assets/sample.png')

# Resize for better detection accuracy
image = cv2.resize(image, None, fx=2, fy=2)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Test for best config, after validation set psm to 6
# for psm in range(6,13+1):
#     config = '--oem 3 --psm %d' % psm
#     txt = pytesseract.image_to_string(image, config=config, lang='eng')
#     print('psm ', psm, ':', txt)

config = '--oem 3 --psm %d' % 6
val_vector = pytesseract.image_to_string(image, config=config)

val_vector = val_vector.splitlines()

for val_str in val_vector:
    val = int(val_str)
    if val > 10:
        # play sound for alarming.
        print('got a big fish here: ', val)
        playsound(alarm_path)