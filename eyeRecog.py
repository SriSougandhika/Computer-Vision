import cv2

# this is the xml file decoder using the xml from the open source.
eyeCascade = cv2.CascadeClassifier("haarcascade_eye.xml")

# start the video capture
c = cv2.VideoCapture(0)
c.set(3, 640)
c.set(4, 480)
c.set(10, 100)

# start loop to keep on detecting eyes real-time
while True:
    # take the image from a timestamp
    success, img = c.read()
    # convert to grayscale
    iGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # detect the eye
    eyes = eyeCascade.detectMultiScale(iGray,1.1,4)
    # show the bounding box around it
    for (x, y, w, h) in eyes:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    # show the images
    cv2.imshow("eyes-recognizer", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
