import cv2
import numpy as np

# this matrix is for creating a black canvas.
i = np.zeros((512, 512, 3), np.uint8)
print(i.shape)
cv2.imshow("img1", i)
# changing a part of canvas to a different colour
i[300:400] = (255, 234, 21)
cv2.imshow("img2", i)
# draw a line
cv2.line(i,(10,10), (50,50), (255,0,0), 3) # image, start-point, end-point, color, thickness
# draw a rectangle or a square
cv2.rectangle(i, (50,50), (200,100), (0,0,255),cv2.FILLED)
cv2.rectangle(i, (300,300), (100,200), (0,255,0),2)
# draw a circle
cv2.circle(i, (200, 200), 30, (100,300,20), 2)
# put a text
cv2.putText(i, "Sougandhika", (300,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (10,150,10), 1)
# finally show the image
cv2.imshow("img3", i)
cv2.waitKey(0)