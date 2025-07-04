import cv2 # for video processing
from cvzone.HandTrackingModule import HandDetector # for hand detection

# mediapipe for landmark of hand or face
# cvzone for face detect

# Init HandDetector and FaceCascade
detector = HandDetector(detectionCon=0.8, maxHands=1)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

video = cv2.VideoCapture(0) # Open the webcam

while True:
    ret, frame = video.read()  # Read a frame from the webcam
    frame = cv2.flip(frame, 1) # Flip the frame horizontally
    
    hands, frame = detector.findHands(frame, draw=True) # Detect hands in the frame

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Convert the frame to grayscale for face detection
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)  # Detect faces in the frame

    for (x, y, w, h) in faces: # Draw rectangles around detected faces
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 255), 2)

    if len(faces) > 0: # If faces are detected
        print("Face Detected 😎")
    else:
        print("No Face Detected 😢")

    if hands: # If hands are detected
        print("Hand Detected 🖐️")
        lmList = hands[0] # Get the landmarks of the first detected hand
        fingerUp = detector.fingersUp(lmList) # Check which fingers are up
        count = sum(fingerUp) # Count the number of fingers that are up
        cv2.putText(frame, f'Finger count: {count}', (0, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)
    else:
        print("No Hand Detected 🙌")
        count = 0

    cv2.imshow("Face + Hand Detector", frame) # Show the processed frame

    if cv2.waitKey(1) & 0xFF == ord('q'): # Exit if 'q' is pressed
        break


video.release() # Release the webcam
cv2.destroyAllWindows() # Close all OpenCV windows