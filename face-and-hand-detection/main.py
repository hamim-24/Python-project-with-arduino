import cv2
from cvzone.HandTrackingModule import HandDetector

# mediapipe for landmark of hand or face
# cvzone for face detect

# Init HandDetector and FaceCascade
detector = HandDetector(detectionCon=0.8, maxHands=1)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    frame = cv2.flip(frame, 1)

    hands, frame = detector.findHands(frame, draw=True)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 255), 2)

    if len(faces) > 0:
        print("Face Detected 😎")
    if hands:
        print("Hand Detected 🖐️")
        lmList = hands[0]
        fingerUp = detector.fingersUp(lmList)
        count = sum(fingerUp)
        cv2.putText(frame, f'Finger count: {count}', (0, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)

    cv2.imshow("Face + Hand Detector", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()