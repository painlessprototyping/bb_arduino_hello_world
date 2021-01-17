"""
Button Board Hello World
by Travis Bumgarner
Revision 1.0
Date 11-21-2016
This sketch is for the Button Board V1.2. It will display a message
via the terminal for each button press.
"""

#Imports
"""
First import allows Python to control the GPIO Pins and the second
Allows for using time delays.
"""
import RPi.GPIO as GPIO
import time

# Inputs
"""
I found it best the use the SparkFun Pi Wedge which makes the GPIO
much easier to access on the breadboard. Pins 16 and 17 are on
the left side of the board and the remaining pins are on the right side.
"""
s1 = 16
s2 = 17
s3 = 18
s4 = 19
s5 = 20
s6 = 21
s7 = 22
s8 = 23
s9 = 24
s10 = 25
s11 = 26
s12 = 27

#Setup
"""
The following code sets each of the 12 pins as inputs to the Raspberry Pi
"""
GPIO.setmode(GPIO.BCM)
GPIO.setup(s1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(s2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(s3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(s4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(s5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(s6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(s7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(s8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(s9, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(s10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(s11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(s12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#Loop
"""
This loop will run forever until Ctrl+C is pressed. It will loop through and
check if any of the 12 buttons are pressed, if so, it triggers the print
statement.
"""
print("Press CTRL+C to exit")
try:
    while True:
        time.sleep(0.075)
        if GPIO.input(s1):
            print("Button S1 is down")
        elif GPIO.input(s2):
            print("Button S2 is down")
        elif GPIO.input(s3):
            print("Button S3 is down")
        elif GPIO.input(s4):
            print("Button S4 is down")
        elif GPIO.input(s5):
            print("Button S5 is down")
        elif GPIO.input(s6):
            print("Button S6 is down")
        elif GPIO.input(s7):
            print("Button S7 is down")
        elif GPIO.input(s8):
            print("Button S8 is down")
        elif GPIO.input(s9):
            print("Button S9 is down")
        elif GPIO.input(s10):
            print("Button S10 is down")
        elif GPIO.input(s11):
            print("Button S11 is down")
        elif GPIO.input(s12):
            print("Button S12 is down")
except KeyboardInterrupt:
    GPIO.cleanup()