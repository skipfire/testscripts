import RPi.GPIO as GPIO
import time
ioPins = [6,12,13,16,19,20,26,21]
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
for pin in ioPins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

while True:
    for pin in ioPins:
        GPIO.output(pin, GPIO.HIGH)    
        time.sleep(1)
        GPIO.output(pin, GPIO.LOW)    
        
GPIO.cleanup() # clean up GPIO on normal exit

print("Done")

