#sudo apt install -y git python3-setuptools python3-pip libgpiod2
#git clone https://github.com/doceme/py-spidev
#cd py-spidev
#sudo python3 setup.py install
#sudo pip3 install adafruit-circuitpython-bme280 adafruit-circuitpython-dht

import Adafruit_DHT
import RPi.GPIO as GPIO
import sys
import time
from spidev import SpiDev
from datetime import datetime

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 22
rainIo = 5
windIo = 6
baseVoltage = 5.0
multiplier = 1.05 #the voltage is not quite what it should be, this gets really close.

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

class MCP3008:
    def __init__(self, bus = 0, device = 0):
        self.bus, self.device = bus, device
        self.spi = SpiDev()
        self.open()
        self.spi.max_speed_hz = 1000000 # 1MHz

    def open(self):
        self.spi.open(self.bus, self.device)
        self.spi.max_speed_hz = 1000000 # 1MHz

    def read(self, channel = 0):
        adc = self.spi.xfer2([1, (8 + channel) << 4, 0])
        data = ((adc[1] & 3) << 8) + adc[2]
        return data

    def close(self):
        self.spi.close()

adc = MCP3008(bus=1)
adc.open()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(rainIo, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(windIo, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def rainClick(channel):
    print("Rain change", GPIO.input(rainIo))

def windClick(channel):
    print("Wind click", GPIO.input(windIo))

def findClosest(list, value):
    return list[min(range(len(list)), key = lambda i: abs(list[i]-value))]

GPIO.add_event_detect(rainIo, GPIO.FALLING, callback=rainClick)
GPIO.add_event_detect(windIo, GPIO.FALLING, callback=windClick)

try:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        if humidity is not None and temperature is not None:
            temp = temperature * 1.8 + 32
            print("Temp={0:0.1f}°  Humidity={1:0.1f}%".format(temp, humidity))
        else:
            print("Failed to retrieve data from humidity sensor")
        val = adc.read(channel = 0)
        voltage = 0
        if val == 0:
            print("No data read from MCP3008")
        else:
            voltage = val/1024.0*baseVoltage*multiplier
            closest = findClosest(voltages, voltage)
            print("Val: {}".format(val))
            print("Voltage: {:.2F}".format(voltage))
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

GPIO.cleanup() # clean up GPIO on normal exit

print("Done")

#d1125 = 0.32 #ESE
#d0675 = 0.41 #ENE
#d0900 = 0.45 #E
#d1575 = 0.62 #SSE
#d1350 = 0.90 #SE
#d2025 = 1.19 #SSW
#d1800 = 1.40 #S
#d0225 = 1.98 #NNE
#d0450 = 2.25 #NE
#d2475 = 2.93 #WSW
#d2250 = 3.08 #SW
#d3375 = 3.43 #NNW
#d0000 = 3.84 #N
#d2925 = 4.04 #WNW
#d3150 = 4.33 #NW
#d2700 = 4.62 #W

