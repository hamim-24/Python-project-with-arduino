# Face Detection with Arduino Control

This project uses OpenCV to detect faces from a webcam feed and communicates with an Arduino to control external devices (like LEDs) based on face detection.

## Features

- Real-time face detection using OpenCV.
- Sends signals to Arduino when a face is detected or not detected.
- Visual feedback with rectangles drawn around detected faces.

## Requirements

- Python 3.x
- cvzone (`cv2`)
- PySerial (`serial`)
- Arduino (connected via USB)
- Webcam

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
   pip install opencv-python pyserial
   pip install cvzone
   ```

4. **Connect your Arduino** and update the serial port in `main.py` if needed:
   ```python
   arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=9600, timeout=1)
   ```
   Change `/dev/ttyUSB0` to your Arduino's port (e.g., `/dev/ttyACM0` or `COM3` on Windows).

5. **Run the script:**
   ```bash
   python main.py
   ```

## How it works

- The script captures video from your webcam.
- If a face is detected, it sends `b'1'` to the Arduino.
- If no face is detected, it sends `b'0'`.
- The Arduino can use this signal to control LEDs or other devices.

## Notes

- Make sure your Arduino is programmed to read serial input and control devices accordingly.
- You may need to install additional drivers for your Arduino board.

## License

This project is licensed under the MIT License.