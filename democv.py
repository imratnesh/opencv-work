# -*- coding: utf-8 -*-
import cv2

filePath = '../videos/Megamind.avi'

imgPath = './images/jpgs/images.jpeg'

image = cv2.imread(imgPath, 1)

# open cascade file
classifier = cv2.CascadeClassifier('./xmls/haarcascade_frontalface_default.xml')

# detect coordinates
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = classifier.detectMultiScale(image, scaleFactor=1.05, minNeighbors=5)

# create rectangle
for x, y , w , h in faces:
    img = cv2.rectangle(image, (x, y), (x+h, y+h), (0,255,0), 2)
    
#print(type(faces), len(faces))
#r_img = cv2.resize(n, (400,400))
cv2.imshow('img', img)

cv2.waitKey(0)

cv2.destroyAllWindows()