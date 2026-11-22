import cv2
import mediapipe as mp
from gestures import SwipeDetector

# Initialize mediapipe
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode = False,
    max_num_hands = 1,
    min_detection_confidence = 0.7,
    min_tracking_confidence = 0.7
)

# Initialize the Swipe Detector
swipe_detector = SwipeDetector()

camera = cv2.VideoCapture(0)

while camera.isOpened():
    success, frame = camera.read()

    if not success:
        break

    frame = cv2.flip(frame,  1)

    height, width, _ = frame.shape()

    # convert BGR to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # detect hands
    results = hands.process(rgb_frame)

    gesture = None

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw hand landmarks
            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            # get the palm reference point
            palm = hand_landmarks.landmark[9]

            # Normalized X coordinate (0 to 1)
            x = palm.x

            # Detect swipe
            gesture = swipe_detector.detect(x)

            # draw reference point
            px = int(palm.x * width)
            py = int(palm.y * height)

            cv2.circle(frame, (px, py), 12, (0, 255, 0), -1)

            # display detected gesture
            if gesture:
                cv2.putText(frame, gesture, (50,80), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)
                print('Detected: ', gesture)

    cv2.imshow('Gesture Recognition', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
hands.close()
cv2.destroyAllWindows()