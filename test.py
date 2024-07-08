import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=2)
classifier = Classifier("Model/keras_model.h5","Model/labels.txt")

imgSize = 300
offset = 20

# storing images
folder = "Data/C"

counter = 0

labels = ["A","B","C","D","E","F","G","H","HELLO","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

while True:
    success, img = cap.read()
    imgOutput = img.copy()
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
            prediction, index = classifier.getPrediction(imgWhite, draw = False)
            print(prediction,index)

        else:
            k = imgSize / w  # streching the height
            hCalculated = math.ceil(k * h)  # value will always get higher roundoff
            imgResize = cv2.resize(imgCrop, (imgSize, hCalculated))
            imgResizeShape = imgResize.shape
            hGap = math.ceil((imgSize - hCalculated) / 2)  # center the image
            imgWhite[hGap:hCalculated + hGap, :] = imgResize
            prediction, index = classifier.getPrediction(imgWhite, draw = False)

        #cv2.rectangle(imgOutput, (x - offset, y - offset-50), (x-offset+90, y-offset-50+50), (255, 0, 255))
        text_size = cv2.getTextSize(labels[index], cv2.FONT_HERSHEY_COMPLEX, 1.7, 2)[0]
        text_x = x + int((w - text_size[0]) / 2)
        cv2.putText(imgOutput, labels[index], (text_x, y-26), cv2.FONT_HERSHEY_COMPLEX, 1.7,(255,255,255),2)
        cv2.rectangle(imgOutput,(x-offset,y-offset),(x+w+offset,y+h+offset),(255,0,255),4)

        #cv2.imshow("ImageCrop",imgCrop)
        cv2.imshow("ImageWhite", imgWhite)

    cv2.imshow("Image",imgOutput)
    cv2.waitKey(1) # makes delay of 1 mili second