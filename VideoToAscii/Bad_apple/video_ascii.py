import cv2 
import numpy as np
char = "#$@*& "
video_cap = cv2.VideoCapture("Bad_apple.mp4")
font = cv2.FONT_HERSHEY_PLAIN
font_scale = 1
thickness = 1

while True:
    ret , frame = video_cap.read()
    if not ret:
        break
    
    frame = cv2.resize(frame , None , fx= 0.5 , fy= 0.5)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    widths, heights = [], []
    
    for c in char:
        (tw, th), base = cv2.getTextSize(c, font, font_scale, thickness)
        widths.append(tw)
        heights.append(th + base)
        
    avg_w = np.mean(widths); avg_h = np.mean(heights)
    height , width = gray.shape
    scale = 100
    new_wi = scale
    new_hei = int((height / width) * scale * (avg_w / avg_h))
    gray = cv2.resize(gray , (new_wi , new_hei))
    
    ascii_text = ""
    
    for row in gray:
        for pixel in row:
            ascii_text = ascii_text + char[int(pixel / 255 * (len(char) - 1))]
        ascii_text = ascii_text + "\n"
        
    lines = ascii_text.rstrip("\n").rstrip("\n").split("\n")
    
    h = len(lines) * int(avg_h)
    w = max(len(line) for line in lines) * int(avg_w)
    
    frame = np.ones((h , w , 3) , dtype=np.uint8) * 255

    y = 20
    for line in lines :
        cv2.putText(frame, line , (5,y) , cv2.FONT_HERSHEY_PLAIN , 1 , (0,0,0) , 1)
        y += 15
        
    cv2.imshow("test" , frame)
    if cv2.waitKey(13) & 0xFF == ord('q'):
        break

video_cap.release()
cv2.destroyAllWindows
    
    

