#pip3 install adafruit-circuitpython-ads1x15

from datetime import datetime
from w1thermsensor import W1ThermSensor
import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1015(i2c)
sensor = W1ThermSensor()
while True:
    temperature = sensor.get_temperature()
    temperature = temperature * 1.8 + 32      
    chan = AnalogIn(ads, ADS.P0)
    print("ADC CH0: {:>5}\t{:>5.3f}".format(chan.value, chan.voltage))
    print("Temperature: {:.1F}".format(temperature))
    time.sleep(0.5)
