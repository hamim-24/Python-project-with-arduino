# Face and Hand Detection

This project uses OpenCV and cvzone to detect faces and hands in real-time from a webcam feed.

## Features

- **Face Detection:** Uses OpenCV's Haar Cascade to detect faces.
- **Hand Detection:** Uses cvzone's HandTrackingModule for hand and finger detection.
- **Finger Counting:** Counts and displays the number of fingers held up.
- **Visual Feedback:** Draws rectangles around faces and displays finger count on the video feed.

## Requirements

- Python 3.x
- OpenCV (`opencv-python`)
- cvzone
- (Optional) mediapipe

## Setup

1. **Install python3.10:**
   ```bash
   brew install python@3.10
   ```

2. **Create and active environment :**
    ```bash
    python3.10 -m venv .venv
    source .venv/bin/activate 
    ```

3. **Install dependencies:**
   ```bash
   pip install cvzone
   pip install mediapipe
   ```

## Usage

Run the main script:
```bash
python main.py
```

- Press `q` to quit the application.

## How it Works

- The webcam feed is processed frame by frame.
- Faces are detected and highlighted with rectangles.
- Hands are detected, and the number of fingers up is counted and displayed.
- Console output indicates when a face or hand is detected.

## License

This project is licensed under the MIT