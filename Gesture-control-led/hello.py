import cv2 # for video processing
import controller as cnt # for controlling the LEDs
from cvzone.HandTrackingModule import HandDetector # for hand detection
WIDTH       = 1240
HEIGHT      = 800

def on_mouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"🖱️ Click at: ({x}, {y})")


detector = HandDetector(detectionCon=0.8, maxHands=1) # Initialize hand detector

video = cv2.VideoCapture(0) # Open the webcam

cnt.reset_leds() # Reset the LEDs

while True:
    ret, frame = video.read() # Read a frame from the webcam
    frame = cv2.resize(frame, (WIDTH, HEIGHT)) # Resize the frame
    frame = cv2.flip(frame, 1) # Flip the frame horizontally
    hands, img = detector.findHands(frame) # Detect hands in the frame
    if hands:
        lmList = hands[0] # Get the landmarks of the first detected hand
        fingerUp = detector.fingersUp(lmList) # Check which fingers are up

        print(fingerUp) # Print the status of fingers
        count = 0
        for i in range(0,5): # Count the number of fingers that are up
            if fingerUp[i] == 1:
                count += 1      

        cnt.led(fingerUp) # Control the LEDs based on the finger status
        # Display the count of fingers on the frame
        cv2.putText(frame, f'Finger count: {count}', (0, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)
    
    cv2.imshow("frame", img) # Show the processed frame
    k = cv2.waitKey(1) # Wait for a key press

    if (k == ord("q")) or k == 27: # Exit if 'q' or 'Esc' is pressed
        break


cnt.reset_leds() # Reset the LEDs before exiting
video.release() # Release the webcam
cv2.destroyAllWindows() # Close all OpenCV windows
