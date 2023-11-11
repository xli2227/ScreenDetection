import pyscreenshot as ImageGrab
import pytesseract
import cv2
# import sys
# from PIL import Image
from playsound import playsound


alarm_path = 'assets/attention.mp3'

def detection_and_alarm(x1,y1,x2,y2):
    # get screen shot from a box
    im=ImageGrab.grab(bbox=(x1,y1,x2,y2))
    # test
    # im.show()
    # to file
    im.save('temp-screenshot.png')
    # Load image for detection processing
    image = cv2.imread('temp-screenshot.png')
    # Resize for better detection accuracy
    image = cv2.resize(image, None, fx=2, fy=2)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    config = '--oem 3 --psm %d' % 6
    val_vector = pytesseract.image_to_string(image, config=config)

    val_vector = val_vector.splitlines()

    for val_str in val_vector:
        val = 0
        try:
            val_str = val_str.replace(",", "")
            val_str = val_str.replace(".", "")
            val = float(val_str)
            print('extraced value is ', val_str)
        except:
            print('some value not able to recognize', val_str)
        if val > 10000000:
            # play sound for alarming.
            print('got a big fish here: ', val)
            playsound(alarm_path)

__all__ = ['detection_and_alarm']

