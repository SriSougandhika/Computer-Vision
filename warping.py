import cv2
import numpy as np

# reading an image
i = cv2.imread("OshiNoKo3.png")
# resize the image to new dimensions
i = cv2.resize(i, (192*2, 82*2))
# view the image
cv2.imshow('img', i)

width, height = 250, 350
pts1 = np.float32([[0, 0], [100, 100], [100, 200], [0, 50]])
pts2 = np.float32([[0, 0], [0, height], [width, height], [width, 0]])
# define the pts1 and pts2 to get a warp perspective ends
m = cv2.getPerspectiveTransform(pts1, pts2)

imgNew = cv2.warpPerspective(i, m, (width, height))
cv2.imshow('imgNew', imgNew)

# horizontal stacking of images to view them together
hor = np.hstack((i, i)) # should have same matrix format
cv2.imshow("stacking horizontal", hor)

# vertical stacking of images to view them together
ver = np.vstack((i, i)) # should have same matrix format
cv2.imshow("stacking vertical", ver)

cv2.waitKey(0)