#sudo pip3 install w1thermsensor
import time
from w1thermsensor import W1ThermSensor
sensor = W1ThermSensor()

while True:
    temperature = sensor.get_temperature()
    temperature = temperature * 1.8 + 32
    print("The temperature is {:.2F}°".format(temperature))
    time.sleep(1)
