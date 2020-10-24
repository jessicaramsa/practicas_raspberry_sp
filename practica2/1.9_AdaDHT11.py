# Instalación Adafruit DHT11
# sudo apt update && sudo apt install build-essential python-dev
# git clone http://github.com/adafruit/Adafruit_Python_DHT.git
# cd Adafruit_Python_DHT/
# sudo python3 setup.py install
# cd examples
# python3 AdafruitDHT.py 11 2

import Adafruit_DHT
sensor = Adafruit_DHT.DHT11 # set sensor type
gpio = 2 # set GPIO sensor is connected to

# Use read_retry method. This will retry up to 15 times to
# get a sensor reading (waiting 2 seconds between each retry)
while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
    # Reading the DHT11 is very sensitive to timings and occasionally
    # the Pi might fail to get a valid reading. So check if reading are valid.
    if humidity is not None and temperature is not None:
        print('Temperatura = {0:0.1f}*C Humedad = {1:0.1f}%'.format(temperature, humidity))
    else:
        break
