import cv2
import numpy as np

# this empty function is used in the trackbar creation
def empty(a):
    pass

#create the trackbars having the Hue, Saturation and Value attributes
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 179, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("Val Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)

# run the loop to continuously see the changes being done to the image after toggling with HSV values.
while True:
    # show the image
    i = cv2.imread("OshiNoKo3.png")
    i = cv2.resize(i, (192*2, 82*2))
    # convert to hsv format
    iHSV = cv2.cvtColor(i, cv2.COLOR_BGR2HSV)
    # get the values
    hmin = cv2.getTrackbarPos("Hue Min", "TrackBars")
    hmax = cv2.getTrackbarPos("Hue Max", "TrackBars")
    smin = cv2.getTrackbarPos("Sat Min", "TrackBars")
    smax = cv2.getTrackbarPos("Sat Max", "TrackBars")
    vmin = cv2.getTrackbarPos("Val Min", "TrackBars")
    vmax = cv2.getTrackbarPos("Val Max", "TrackBars")
    print(hmin, hmax, smin, smax, vmin, vmax)
    lower = np.array([hmin, smin, vmin])
    upper = np.array([hmax, smax, vmax])
    # it will filter out colors according to the color range set
    mask = cv2.inRange(iHSV, lower, upper)
    # using the above mask, create a new image:
    iNew = cv2.bitwise_and(i, i, mask=mask)
    # try setting: 0, 179, 0, 124, 111, 221
    final1 = np.hstack((i, iHSV))
    final2 = np.hstack((i, iNew))
    final = np.vstack((final1, final2))
    # stack the images to a single one and then show results
    cv2.imshow("result", final)
    cv2.waitKey(1)
