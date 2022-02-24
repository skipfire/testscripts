import RPi.GPIO as GPIO
import time
windIo = 6
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(windIo, GPIO.IN, pull_up_down=GPIO.PUD_UP)
buttonTested = False

def buttonPressed(channel):
    global buttonTested
    print("Wind click", GPIO.input(windIo))

GPIO.add_event_detect(windIo, GPIO.FALLING, callback=buttonPressed)
try:
    while buttonTested == False:
        time.sleep(1)
except KeyboardInterrupt:
    print("KeyboardInterrupt button wait")

GPIO.cleanup() # clean up GPIO on normal exit

print("Done")

