#pip3 install adafruit-circuitpython-ads1x15

import board
import busio
import time
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from datetime import datetime

def findClosest(list, value):
    return list[min(range(len(list)), key = lambda i: abs(list[i]-value))]

d1125 = 0.32 #ESE
d0675 = 0.41 #ENE
d0900 = 0.45 #E
d1575 = 0.62 #SSE
d1350 = 0.90 #SE
d2025 = 1.19 #SSW
d1800 = 1.40 #S
d0225 = 1.98 #NNE
d0450 = 2.25 #NE
d2475 = 2.93 #WSW
d2250 = 3.08 #SW
d3375 = 3.43 #NNW
d0000 = 3.84 #N
d2925 = 4.04 #WNW
d3150 = 4.33 #NW
d2700 = 4.62 #W

voltages = [d0000, d0225, d0450, d0675, d0900, d1125, d1350, d1575, d1800, d2025, d2250, d2475, d2700, d2925, d3150, d3375]

i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
ads.gain = 2/3

try:
    while True:
        chan = AnalogIn(ads, ADS.P0)
        print("ADC CH0: {:>5}\t{:>5.3f}".format(chan.value, chan.voltage))
        voltage = chan.voltage
        closest = findClosest(voltages, voltage)
        if closest == d0000:
            direction = "N"
        elif closest == d0225:
            direction = "NNE"
        elif closest == d0450:
            direction = "NE"
        elif closest == d0675:
            direction = "ENE"
        elif closest == d0900:
            direction = "E"
        elif closest == d1125:
            direction = "ESE"
        elif closest == d1350:
            direction = "SE"
        elif closest == d1575:
            direction = "SSE"
        elif closest == d1800:
            direction = "S"
        elif closest == d2025:
            direction = "SSW"
        elif closest == d2250:
            direction = "SW"
        elif closest == d2475:
            direction = "WSW"
        elif closest == d2700:
            direction = "W"
        elif closest == d2925:
            direction = "WNW"
        elif closest == d3150:
            direction = "NW"
        elif closest == d3375:
            direction = "NNW"
        else:
            direction = "unknown"
        print(direction)
        time.sleep(1)
except KeyboardInterrupt:
    print("KeyboardInterrupt from loop")
