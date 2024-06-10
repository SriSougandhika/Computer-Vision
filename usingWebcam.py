import cv2
# the video capture is for access to webcam. 0 sets to default webcam.
c = cv2.VideoCapture(0)
# these are set mode functionalities
# 3 is for (cv2.CAP_PROP_FRAME_WIDTH)
# 4 is for (cv2.CAP_PROP_FRAME_HEIGHT)
# 10 is for (cv2.CAP_PROP_BRIGHTNESS)
c.set(3, 640)
c.set(4, 480)
c.set(10, 100)

# this loop is for the video to remain alive until the user presses q to quit.
while True:
    # this reads each millisecond image and shows it to us
    success, img = c.read()
    cv2.imshow("video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
