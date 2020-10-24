from gpiozero import DistanceSensor
from time import sleep

GPIO_TRIGGER = 8
GPIO_ECHO = 7
sensor = DistanceSensor(GPIO_ECHO, GPIO_TRIGGER)

while True:
    print('Distance to nearest object is', sensor.distance * 100, 'cm')
    sleep(1)
