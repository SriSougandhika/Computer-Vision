import cv2
import numpy as np

# import the image
i = cv2.imread("OshiNoKo3.png")
i = cv2.resize(i, (192*3, 82*3))
kernel = np.ones((5, 5), np.uint8)
# convert the color image to grayscale
iGray = cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)
# blur the image
iBlur = cv2.GaussianBlur(iGray, (7,7), 0)
# detect the edges
iCanny = cv2.Canny(i, 100, 100)
# dilation or filter through kernel defined above
iDil = cv2.dilate(iCanny, kernel, iterations=1)
# erode or make it rough using kernel
iErode = cv2.erode(iDil, kernel, iterations=1)
# cropping an image
iCrop = i[55:150,100:250] # height first then width

# show the images
cv2.imshow("Grayscale", iGray)
cv2.imshow("Blur", iBlur)
cv2.imshow("EdgeDetection", iCanny)
cv2.imshow("Dilation", iDil)
cv2.imshow("Eroded", iErode)
cv2.imshow("Cropped", iCrop)
cv2.waitKey(0)
