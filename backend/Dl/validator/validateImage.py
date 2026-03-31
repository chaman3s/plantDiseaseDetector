from PIL import Image
import cv2
import numpy as np
import io


def isCorrupted(file_bytes):
    try:
        img = Image.open(io.BytesIO(file_bytes))
        img.verify()
        return False
    except:
        return True


def load_gray(file_bytes):
    img = np.frombuffer(file_bytes, np.uint8)
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)
    if img is None:
        return None
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray
def is_blurry(gray, threshold=100):
    variance = cv2.Laplacian(gray, cv2.CV_64F).var()
    print("Sharpness:", variance)
    return variance < threshold
def isDarkOrBright(gray):
    brightness = np.mean(gray)
    print("Brightness:", brightness)
    return brightness < 40 or brightness > 200
def isvalidImage(file_bytes):
    # 1. corrupted
    if isCorrupted(file_bytes):
        return False, "Corrupted image"
    # 2. load
    gray = load_gray(file_bytes)
    if gray is None:
        return False, "Cannot read image"
    # 3. blur
    if is_blurry(gray):
        return False, "Image is blurry"

    # 4. brightness
    if isDarkOrBright(gray):
        return False, "Image too dark or too bright"
    return True, "Valid"