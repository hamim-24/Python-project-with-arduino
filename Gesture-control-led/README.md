# Hand Gesture LED Controller

A real-time hand gesture recognition system that controls Arduino LEDs based on finger counting using computer vision and PyFirmata.

## Overview

This project uses your webcam to detect hand gestures and count the number of fingers held up, then controls corresponding LEDs connected to an Arduino board. Each finger corresponds to a specific LED, creating an interactive visual feedback system.

## Features

- **Real-time hand detection** using MediaPipe and CVZone
- **Finger counting** (0-5 fingers)
- **Arduino LED control** via PyFirmata
- **Visual feedback** with on-screen finger count display
- **Automatic LED reset** when no hand is detected

## Hardware Requirements

- Arduino board (Uno, Nano, etc.)
- 5 LEDs
- 5 resistors (220Ω recommended)
- Breadboard and jumper wires
- USB cable to connect Arduino to computer
- Webcam

## Circuit Setup

Connect LEDs to the following Arduino pins:
- LED 1: Pin 9
- LED 2: Pin 10
- LED 3: Pin 11
- LED 4: Pin 12
- LED 5: Pin 13

Each LED should be connected with a current-limiting resistor (220Ω) between the Arduino pin and the LED's anode, with the cathode connected to ground.

## Software Requirements

- Python 3.7+(python3.10)
- Arduino IDE (for initial setup)
- Webcam drivers

## Installation

1. **Clone or download the project files**

2. **Install Python3.10**
    ```bash
    brew install python@3.10
    ```

3. **Make Python Environment**
    ```bash
    python3.10 -m venv .venv
    ```
4. **Active Environment**
    ```bash
    source .venv/bin/active
    ```

5. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

6. **Set up Arduino**
   - Connect your Arduino to your computer
   - Upload the StandardFirmata sketch to your Arduino:
     - Open Arduino IDE
     - Go to File → Examples → Firmata → StandardFirmata
     - Upload the sketch to your Arduino

7. **Update the COM port**
   - Find your Arduino's COM port (check Device Manager on Windows or use `ls /dev/cu.*` on macOS)
   - You can find it in the Arduino Ide also
   - Update the `comport` variable in `controller.py` with your Arduino's port
    ```py
    comport = '' # past here
    ```

## Usage

1. **Connect your Arduino** with the LED circuit
2. **Run the main program**
   ```bash
   python hello.py
   ```
3. **Position your hand** in front of the webcam
4. **Hold up fingers** (1-5) to see corresponding LEDs light up
5. **Press 'q' or ESC** to quit the program

## How It Works

### Hand Detection
- Uses MediaPipe through CVZone for robust hand landmark detection
- Processes webcam feed in real-time at 1040x600 resolution
- Detects up to 1 hand with 80% confidence threshold

### Finger Counting
The system recognizes these finger patterns:
- **0 fingers**: `[0, 0, 0, 0, 0]` - All LEDs off
- **1 finger**: `[0, 1, 0, 0, 0]` - Index finger up
- **2 fingers**: `[0, 1, 1, 0, 0]` - Index and middle fingers up
- **3 fingers**: `[0, 1, 1, 1, 0]` - Index, middle, and ring fingers up
- **4 fingers**: `[0, 1, 1, 1, 1]` - All fingers except thumb up
- **5 fingers**: `[1, 1, 1, 1, 1]` - All fingers up

### Arduino Control
- Uses PyFirmata to communicate with Arduino over serial
- Controls 5 digital output pins (9-13) for LED control
- Automatically resets all LEDs when no hand is detected

## File Structure

```
project/
├── hello.py              # Main application file
├── controller.py         # Arduino LED controller module
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Troubleshooting

### Common Issues

**"Serial port not found" error**
- Check if Arduino is properly connected
- Verify the COM port in `controller.py`
- Ensure StandardFirmata is uploaded to Arduino

**Hand detection not working**
- Check webcam permissions
- Ensure good lighting conditions
- Keep hand within camera frame
- Try adjusting `detectionCon` parameter in `hello.py`

**LEDs not responding**
- Verify circuit connections
- Check if LEDs are connected with correct polarity
- Test LEDs individually with a simple Arduino sketch

### Performance Tips

- Ensure good lighting for better hand detection
- Keep background simple and uncluttered
- Position hand 1-2 feet from camera
- Avoid rapid hand movements

## Dependencies

Key libraries used:
- **OpenCV**: Computer vision and webcam handling
- **CVZone**: Simplified hand tracking interface
- **PyFirmata**: Arduino communication
- **MediaPipe**: Hand landmark detection (via CVZone)

## Contributing

Feel free to fork this project and submit pull requests for improvements such as:
- Additional gesture recognition
- More LED patterns
- GUI interface
- Gesture-based commands

## License

This project is open source. Feel free to use and modify as needed.

## Acknowledgments

- MediaPipe team for hand tracking technology
- CVZone for simplified computer vision interface
- PyFirmata for Arduino-Python communication

---

