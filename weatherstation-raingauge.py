import RPi.GPIO as GPIO
#import os
#import serial
#import sys
import time
rainIo = 5
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(rainIo, GPIO.IN, pull_up_down=GPIO.PUD_UP)
buttonTested = False

def buttonPressed(channel):
    global buttonTested
    print("Rain change", GPIO.input(rainIo))

GPIO.add_event_detect(rainIo, GPIO.BOTH, callback=buttonPressed)
try:
    while buttonTested == False:
        time.sleep(1)
except KeyboardInterrupt:
    print("KeyboardInterrupt button wait")

GPIO.cleanup() # clean up GPIO on normal exit

print("Done")

