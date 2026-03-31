import os
from PIL import Image
import cv2
import numpy as np
from .check_leaf import *

def isCorrupted(file):
    try:
        img = Image.open(file)
        img.verify()
        return False
    except:
        return True
def check_image_quality(image_path):
    img = Image.open(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if is_blurry(grey=gray):
        return False
    if isDarkOrBright(gray):
        return False
    return True
def isDarkOrBright(gray):
    brightness = np.mean(gray)
    if brightness < 40:
        return True
    elif brightness > 200:
        return True
    else:
       return False


def is_blurry(image_path=None,grey=None ,threshold=100):
    gray = None
    if image_path != None:
        img = cv2.imread(image_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    elif grey != None:
        gray = grey
    if gray is not  None:
        variance = cv2.Laplacian(gray, cv2.CV_64F).var()
        print("Sharpness value:", variance)
        if variance < threshold:
            return True   # blurry
        else:
            return False  # clear
    return False
def isvalidImage(image_path):
    if not isCorrupted(image_path): return False
    if not is_blurry(image_path): return False
    if not check_image_quality(image_path): return False
    return True
if __name__ == "__main__": 
    im="blur.jpg"
    if isvalidImage(im):print("valid")
    else:print("not valid")