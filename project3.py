import cv2
import mediapipe as mp
import numpy as np

# Initialize Mediapipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)


# Gesture recognition function
def recognize_gesture(landmarks):
    thumb_tip = landmarks[mp_hands.HandLandmark.THUMB_TIP]
    index_finger_tip = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    middle_finger_tip = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    ring_finger_tip = landmarks[mp_hands.HandLandmark.RING_FINGER_TIP]
    pinky_tip = landmarks[mp_hands.HandLandmark.PINKY_TIP]
    wrist = landmarks[mp_hands.HandLandmark.WRIST]

    # Two write, index finger up, peace sign to erase, normal hand to do nothing
    if (index_finger_tip.y < thumb_tip.y and
            index_finger_tip.y < middle_finger_tip.y and
            index_finger_tip.y < ring_finger_tip.y and
            index_finger_tip.y < pinky_tip.y):
        return 'write'
    elif middle_finger_tip.y < ring_finger_tip.y < pinky_tip.y < index_finger_tip.y < thumb_tip.y:
        return 'erase'
    else:
        return 'nothing'


# Initialize video capture
cap = cv2.VideoCapture(0)

# Initialize the transparent canvas to draw on
canvas = None
previous_position = None

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    # mirror the frame
    frame = cv2.flip(frame, 1)
    # Convert the frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    # Initialize canvas with transparency
    if canvas is None:
        canvas = np.zeros((frame.shape[0], frame.shape[1], 4), dtype=np.uint8)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Recognize gesture
            gesture = recognize_gesture(hand_landmarks.landmark)
            # Put gesture text on the frame
            cv2.putText(frame, gesture, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

            # Get the coordinates of the index fingertip
            h, w, _ = frame.shape
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            cx, cy = int(index_finger_tip.x * w), int(index_finger_tip.y * h)

            # Perform action based on the gesture
            if gesture == "write":
                if previous_position is not None:
                    cv2.line(canvas, previous_position, (cx, cy), (0, 0, 255, 255), 5)
                previous_position = (cx, cy)
            elif gesture == "erase":
                # Clear the canvas
                canvas = np.zeros((frame.shape[0], frame.shape[1], 4), dtype=np.uint8)
                previous_position = None
            else:
                previous_position = None

    # Combine the frame with the transparent canvas
    combined_frame = cv2.addWeighted(frame, 1.0, canvas[:, :, :3], 0.5, 0)

    # Display the frame
    cv2.imshow('Hand Gesture Recognition', combined_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# cleanup
cap.release()
cv2.destroyAllWindows()
