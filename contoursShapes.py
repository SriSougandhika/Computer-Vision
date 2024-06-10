import cv2
import numpy as np

# this is for defining the contours in the image input.
def get_contours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for c in contours:
        area = cv2.contourArea(c)
        print(area)
        # to remove noise, give threshold to area
        if area > 500:
            cv2.drawContours(iContour, c, -1, (0,0,255), 3)
            peri = cv2.arcLength(c, True)
            print("perimeter: ", peri, end='\t')
            # find out the corners of contour using area and perimeter
            approx = cv2.approxPolyDP(c, 0.02*peri, True)
            corners = len(approx)
            print("corners: ", corners)
            x, y, w, h = cv2.boundingRect(approx)
            # define the type of shape using corners
            otype=""
            if corners == 3:
                otype = "triangle"
            elif corners == 4:
                aspRatio = w/h
                print("aspect ratio = ",aspRatio)
                if 0.8 < aspRatio < 1.2:
                    otype = "square"
                else:
                    otype = "rectangle"
            elif corners == 5:
                otype = "pentagon"
            elif corners == 6:
                otype = "hexagon"
            else:
                otype = "circle"
            # put the bounding box, with the text / type of image
            cv2.rectangle(iContour, (x,y), (x+w, y+h), (0,255,0), 3)
            cv2.putText(iContour, otype, (x+(w//2)-10, y+(h//2)-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0),1)

# apply the above function after preprocessing image
i = cv2.imread("shapes.png")
i = cv2.resize(i,(750, 600))
iGray = cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)
# we can blur according to our wish, but for this, no blur works well
# iGray = cv2.GaussianBlur(iGray, (7,7), 0)
iNew = cv2.Canny(iGray, 50, 50)
iContour = i.copy()
get_contours(iNew)

# show the results after stacking
final = np.hstack((iGray, iNew))
cv2.imshow("result", final)
cv2.imshow("contours", iContour)
cv2.waitKey(0)