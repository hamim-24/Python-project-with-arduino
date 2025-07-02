import cv2
#import serial 
import time

# Connect to Arduino (update your port)
arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=9600, timeout=1)
time.sleep(2)  # Give time for Arduino to reboot

# Load OpenCV face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) > 0:
        print("Face Detected 😎")
        arduino.write(b'1')  # Send ON signal
    else:
        print("No Face 😴")
        arduino.write(b'0')  # Send OFF signal

    # Optional: Show webcam feed
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow('Face Detector', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()