#sudo apt install git -y
#pip3 install adafruit-circuitpython-ads1x15

from datetime import datetime
import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1015(i2c)
while True:
    chan = AnalogIn(ads, ADS.P0)
    print("ADC CH0: {:>5}\t{:>5.3f}".format(chan.value, chan.voltage))
    time.sleep(0.5)
