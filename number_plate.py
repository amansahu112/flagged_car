import cv2
import numpy as np
import pytesseract

number_plate = cv2.CascadeClassifier('indian_license_plate.xml')

img=cv2.imread('car3.jpg')
plate_rect = np.array([])
i=1
while plate_rect.shape != (1, 4):
    i += 1
    plate_rect = number_plate.detectMultiScale(img, scaleFactor=1.3,
                                            minNeighbors=i)
    plate_rect = np.array(plate_rect)
    if i == 21:
        break
    # print(plate_rect)

x,y,w,h=plate_rect[0][0],plate_rect[0][1],plate_rect[0][2],plate_rect[0][3]
cv2.rectangle(img,(x,y),(x+w,y+h),(250,5,5),1)
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
roi_gray=gray[y:y+h,x:x+w]
#ocr
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
boxes=pytesseract.image_to_data(roi_gray)
print(boxes)
for x,b in enumerate(boxes.splitlines()):
    if x==0:
        continue
    b=b.split()
    if len(b)!=12:
        continue
    print(b)



# print(plate_rect)
cv2.imshow('img',roi_gray)
cv2.waitKey(0)

"""cap=cv2.VideoCapture("resources/Rock on with DJ Chitvan's Mada Faqa [Gouti].mp4")
while True:
    success,img=cap.read()
    cv2.imshow('video',img)
    if cv2.waitKey(30) & 0xFF==ord('q'):
        break """