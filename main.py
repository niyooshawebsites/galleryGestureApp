import cv2

# open the default webcam
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print('Error: Cound not access the webcam')
    exit()

while True:
    success, frame = camera.read()

    if not success:
        print('Failed to capture frame')
        break

    # Mirro the camera feed
    frame = cv2.flip(frame, 1)

    # display webcam feed
    cv2.imshow('Hand Gesture Gallery', frame)

    # pres 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
