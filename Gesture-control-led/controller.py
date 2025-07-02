import pyfirmata
# pyfirmata for arduino pin
# pyserial for serial monitor

comport = '/dev/cu.usbmodem101' # Change this to your Arduino's port

board = pyfirmata.Arduino(comport) # Initialize the Arduino board

led_pins = [9, 10, 11, 12, 13] # Define the LED pins
leds = [board.get_pin(f'd:{pin}:o') for pin in led_pins] # Create a list of LED pins as output pins

def reset_leds(): 
    for led in leds:
        led.write(0)


def led(fingerUp):
    # Control the LEDs based on the finger status
    if not isinstance(fingerUp, list) or len(fingerUp) != 5:
        raise ValueError("fingerUp must be a list of 5 elements (0 or 1).")
    for i in range(5): # Iterate through each finger
        leds[i].write(1 if fingerUp[i] else 0)
