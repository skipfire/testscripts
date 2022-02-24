import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 22

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        temp = temperature * 1.8 + 32
        print("Temp={0:0.1f}°  Humidity={1:0.1f}%".format(temp, humidity))
    else:
        print("Failed to retrieve data from humidity sensor")

