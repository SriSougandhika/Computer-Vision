# Computer-Vision
From basics to projects in computer vision.

## CAVEAT
Tensorflow saved models (.h5 format) are of exceeding size, so you can take a pretrained model instead. 
Also, the images can be personalized. 

## ENVIRONMENT
All codes are executed on Pycharm Community version 2022.3.1
Packages installed  -> numpy, matplotlib, opencv-python, opencv-python-headless, tensorflow. 
Virtual environment created in the project folder itself.

## DETAILS OF ALL CODES
1. usingWebcam.py
This code snippet tells how to use the webcam to get real-time data.

2. imageEditing.py
This code snippet tells how images can be changed to extract features out of them

3. shapesTexts.py
This snippet tells how shapes or text can be inserted on a board or a canvas.

4. warping.py
this snippet is for how to warp an image and also stacking the image into one plot.

5. contoursShapes.py
This snippet tells how to draw the contours using edge detection and guess the shape in the image provided.

6. colorDetection.py
This code uses trackbars to change the Hue, Saturation and Value attributes.

7. faceRecog.py
This snippet recognizes faces in a real time video data, and shows using a bounding box around it.

8. eyeRecog.py
Similar to above code, this one detects eyes. Both this one and above one, use the xml files instead of models. These are pre trained model with the data fed in the xml files.

9. facemesh.py
This one is similar to face recognition, but this creates a mesh on the face, using mediapipe package.

10. emotions.py
This uses a model created by myself, though of low accuracy, predicts the emotion after face recognition. One may use another pre trained model for this. But this snippet provide insight on how to use a self-built model in computer vision for real time detection.

11. project1.py
A simple "draw it" using a color pen, whose HSV values are determined and noted from the colorDetection.py code.

12. project2.py
This is a hand gesture recognition code, it recognizes the hands using mediapipe package. Then based on the landmarks, we can define the gestures. It detects "hello", "ok", "peace", "thumbs up" and "thumbs down" gestures.

13. project3.py
This is a modification to project1 using project2. We use hands to draw. It now has an erase option as well.

## NOTE
I have taken references from a lot of sources including youtube (especially, ). Codes may seem familiar to others' but it is not my intention to plagiarise. I have summarized whatever I have learnt and coded. 
Thanks for reading!

