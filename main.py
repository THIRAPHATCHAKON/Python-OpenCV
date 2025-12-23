import win32gui
import numpy as np
from PIL import Image
import cv2
import dxcam
from time import time
timestamp = time()

def list_keyword(keyword: str):
    
    keyword = keyword.lower()
    serect = []
    def enum_window(hwnd , _):
        if win32gui.IsWindowVisible(hwnd):
            title = win32gui.GetWindowText(hwnd)
            print(f"{hwnd}: {title}")
            if keyword in title.lower():
                serect.append((hwnd , title))
    enum_windows = win32gui.EnumWindows(enum_window , None)
    return serect[0] if serect else None

hwnd = list_keyword("Roblox")
camera = dxcam.create(output_idx=0)


def grab_window(hwnd):
    left, top , right, bottom = win32gui.GetClientRect(hwnd)
    w = right - left
    h = bottom - top
    x0 , y0 = win32gui.ClientToScreen(hwnd , (0 , 0))
    frame = camera.grab()
    if frame is None:
        return None
    frame = frame[y0:h + y0 , x0:w + x0]
    return frame

while True:
    frame = grab_window(hwnd[0])
    if frame is None:
        continue
    print("FPS :", 1 / (time() - timestamp))
    timestamp = time()
    cv2.imshow("Window Capture" , frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break




    

