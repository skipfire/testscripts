#sudo apt install git -y
#git clone https://github.com/doceme/py-spidev
#cd py-spidev
#sudo python3 setup.py install

from spidev import SpiDev
from datetime import datetime

voltage = 5.0
multiplier = 1.07 #voltage drifts, this gets really close.

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

val = adc.read(channel = 0)
if val == 0:
    print("No data read from MCP3008")
else:
    print("Val: {}".format(val))
    print("Voltage: {:.2F}".format(val/1024.0*voltage*multiplier))
