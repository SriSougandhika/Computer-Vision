import cv2
import numpy as np

# first I have captured the color corresponding to my color pen, with which I will be drawing
# captured: (50, 71, 90, 203, 138, 255) as (hmin, hmax, smin, smax, vmin, vmax)
# start the capture
c = cv2.VideoCapture(0)
c.set(3, 640)
c.set(4, 480)

my_color = [[50, 71, 90, 203, 138, 255]]
myPoints = []
myColVal = [0,255,0]

# we can have a line or a circle.
# circle might give out a dotty line due to low quality video.
# then we may use the line. it will help keep a continuous ink on the canvas
def draw(myPts, myColVal):
    for p in myPts:
        cv2.circle(imgRes, (p[0],p[1]), 10, myColVal, cv2.FILLED)

# find where the marker is located
def find_color(img, my_col, colval):
    iHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    newpts = []
    lower = np.array([50,71,90])
    upper = np.array([203,138,255])
    mask = cv2.inRange(iHSV, lower, upper)
    cv2.imshow("mask",mask)
    # this will give coordinates of marker
    x,y = get_contours(mask)
    # create a circle there and append to newpts
    cv2.circle(imgRes,(x,y),10,colval,cv2.FILLED)
    if x!=0 and y!=0:
        newpts.append([x,y])
    return newpts

# it is to give coordinates of contour detected
def get_contours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for c in contours:
        area = cv2.contourArea(c)
        # to remove noise, give threshold to area
        if area > 500:
            cv2.drawContours(imgRes, c, -1, (0,0,255), 3)
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.02*peri, True)
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2, y

# this will continuously read the image and draw on it.
while True:
    success, img = c.read()
    imgRes = img.copy()
    # find wherever the color is detected
    newpts = find_color(img, my_color, myColVal)
    if len(newpts)!=0:
        for n in newpts:
            myPoints.append(n)
    # get the points wherever ink needs to be put
    if len(myPoints)!=0:
        draw(myPoints,myColVal)
    # show the final image on it.
    cv2.imshow("video", imgRes)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

