import cv2
import mediapipe as mp

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

    # Thumbs Up gesture
    if thumb_tip.y < index_finger_tip.y < middle_finger_tip.y < ring_finger_tip.y < pinky_tip.y:
        return 'Thumbs Up'

    # Thumbs Down gesture
    elif thumb_tip.y > index_finger_tip.y > middle_finger_tip.y > ring_finger_tip.y > pinky_tip.y:
        return 'Thumbs Down'

    # OK gesture
    elif middle_finger_tip.y < ring_finger_tip.y < pinky_tip.y < index_finger_tip.y < thumb_tip.y:
        return 'OK'

    # Peace gesture
    elif middle_finger_tip.y < index_finger_tip.y < thumb_tip.y < ring_finger_tip.y < pinky_tip.y:
        return 'Peace'

    # Fist gesture
    elif thumb_tip.y < (index_finger_tip.y and middle_finger_tip.y and ring_finger_tip.y and pinky_tip.y):
        return 'Fist'

    # Greeting gesture
    elif thumb_tip.y > (index_finger_tip.y and middle_finger_tip.y and ring_finger_tip.y and pinky_tip.y):
        return 'Hello'

    return 'Unknown Gesture'


# Initialize video capture
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Recognize gesture
            gesture = recognize_gesture(hand_landmarks.landmark)
            cv2.putText(frame, gesture, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

    # Display the frame
    cv2.imshow('Hand Gesture Recognition', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# cleanup
cap.release()
cv2.destroyAllWindows()
