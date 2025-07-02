import cv2
import controller as cnt
from cvzone.HandTrackingModule import HandDetector
WIDTH       = 1040
HEIGHT      = 600
def on_mouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"🖱️ Click at: ({x}, {y})")


detector = HandDetector(detectionCon=0.8, maxHands=1)

video = cv2.VideoCapture(0)

cnt.reset_leds()

while True:
    ret, frame = video.read()
    frame = cv2.resize(frame, (WIDTH, HEIGHT))
    frame = cv2.flip(frame, 1)
    hands, img = detector.findHands(frame)
    if hands:
        lmList = hands[0]
        fingerUp = detector.fingersUp(lmList)

        print(fingerUp)
        count = 0
        for i in range(0,5):
            if fingerUp[i] == 1:
                count += 1      

        cnt.led(fingerUp)
        cv2.putText(frame, f'Finger count: {count}', (0, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
        
        cnt.reset_leds()

    cv2.imshow("frame", img)
    k = cv2.waitKey(1)

    if (k == ord("q")) or k == 27:
        break

video.release()
cv2.destroyAllWindows()
