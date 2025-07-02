import pyfirmata
# pyfirmata for arduino pin
# pyserial for serial monitor

comport = '/dev/cu.usbmodem101'

board = pyfirmata.Arduino(comport)

led_pins = [9, 10, 11, 12, 13]
leds = [board.get_pin(f'd:{pin}:o') for pin in led_pins]

def reset_leds():
    for led in leds:
        led.write(0)


def led(fingerUp):
    if not isinstance(fingerUp, list) or len(fingerUp) != 5:
        raise ValueError("fingerUp must be a list of 5 elements (0 or 1).")
    for i in range(5):
        leds[i].write(1 if fingerUp[i] else 0)
