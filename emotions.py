import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

# Load the saved model
model = load_model('emotion_detection_model.h5')
print("model loaded!")
# Emotion labels
labels = ['surprise', 'sad', 'neutral', 'happy', 'fear', 'disgust', 'angry']

# Load OpenCV's pre-trained Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Start webcam video capture
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Loop over the detected faces
    for (x, y, w, h) in faces:
        # Extract the face region
        face = gray[y:y+h, x:x+w]
        face_resized = cv2.resize(face, (48, 48))
        face_expanded = np.expand_dims(face_resized, axis=-1)
        face_expanded = np.expand_dims(face_expanded, axis=0)

        # Predict the emotion of the face
        prediction = model.predict(face_expanded)
        class_index = np.argmax(prediction)
        predicted_emotion = labels[class_index]

        # Draw a rectangle around the face and put the predicted emotion label
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(frame, predicted_emotion, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    # Display the resulting frame
    cv2.imshow('Emotion Detection', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture and close windows
cap.release()
cv2.destroyAllWindows()
