import cv2

# this is cascade, or the decoded xml file for detect the faces. This is available on for free use.
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# start video capture
c = cv2.VideoCapture(0)
c.set(3, 640)
c.set(4, 480)
c.set(10, 100)

# start loop to continuously show the faces real-time
while True:
    success, img = c.read()
    # read img from a timestamp, convert to grayscale
    iGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # then detect using the xml file cascade
    faces = faceCascade.detectMultiScale(iGray,1.1,4)
    # draw a bounding box wherever the match is found
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)

    # show the image mask
    cv2.imshow("faces-recognizer", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
