import time
from gpiozero import AngularServo
from gpiozero import LED
from gpiozero import DistanceSensor

GPIO_TRIGGER = 8 # usar pin GPIO 23 como TRIGGER
GPIO_ECHO = 7 # usar ping GPIO 7 como ECHO
gpioservo = 17 # pin que controla el servo
orange = LED(18)
sensor = DistanceSensor(GPIO_ECHO, GPIO_TRIGGER)
sermot = AngularServo(gpioservo)
sermot.angle = 0  # controlar el ángulo del servo

while True:
    espacio = 100 * sensor.distance
    print(espacio)
    time.sleep(1)
    
    if espacio < 15:
        sermot.angle = 90
        orange.on()
        time.sleep(5)
    
    sermot.angle = 0
    orange.off()
