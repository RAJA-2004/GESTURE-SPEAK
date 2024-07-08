import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import time

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=2)

imgSize = 300
offset = 20

# storing images
folder = "Data/Z"

counter = 0

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)

    # cropping the image

    if hands:
        hand = hands[0]
        x,y,w,h = hand['bbox'] # bounding box info

        imgWhite = np.ones((imgSize, imgSize, 3),np.uint8)*255
        imgCrop = img[y-offset:y+h+offset,x-offset:x+w+offset]

        imgCropShape = imgCrop.shape # matrix of height width

        aspectRatio = h/w

        if aspectRatio > 1:
            k = imgSize/h   # streching the height
            wCalculated = math.ceil(k*w)    # value will always get higher roundoff
            imgResize = cv2.resize(imgCrop,(wCalculated, imgSize))
            imgResizeShape = imgResize.shape
            wGap = math.ceil((imgSize-wCalculated)/2) # center the image
            imgWhite[:, wGap:wCalculated+wGap] = imgResize

        else:
            k = imgSize / w  # streching the height
            hCalculated = math.ceil(k * h)  # value will always get higher roundoff
            imgResize = cv2.resize(imgCrop, (imgSize, hCalculated))
            imgResizeShape = imgResize.shape
            hGap = math.ceil((imgSize - hCalculated) / 2)  # center the image
            imgWhite[hGap:hCalculated + hGap, :] = imgResize

        cv2.imshow("ImageCrop",imgCrop)
        cv2.imshow("ImageWhite", imgWhite)

    cv2.imshow("Image",img)
    key = cv2.waitKey(1) # makes delay of 1 mili second
    if key == ord("s"):
        counter += 1
        cv2.imwrite(f'{folder}/Image_{time.time()}.jpg',imgWhite)
        print (counter)