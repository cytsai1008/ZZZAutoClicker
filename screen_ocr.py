import pytesseract
from PIL import ImageGrab
from win32gui import FindWindow, GetWindowRect


def screen_ocr():
    img = ImageGrab.grab(bbox=(0, 0, 1920, 1080))
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    text = pytesseract.image_to_string(img, lang='chi_tra+eng')
    print(text)
    return text


def get_window_rect():
    hwnd = FindWindow(None, "ZenlessZoneZero")
    rect = GetWindowRect(hwnd)
    if type(rect) != tuple:
        rect = (0, 0, 1920, 1080)
    return rect
