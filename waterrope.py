#sudo apt install git -y
#git clone https://github.com/doceme/py-spidev
#cd py-spidev
#sudo python3 setup.py install

from spidev import SpiDev
from datetime import datetime



val = adc.read(channel = 1)
if val == 0:
    print("No data read from MCP3008")
else:
    print("Val: {}".format(val))
