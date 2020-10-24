import RPi.GPIO as GPIO
import time
from gpiozero import AngularServo
from gpiozero import LED

GPIO_TRIGGER = 8 # usar pin GPIO 23 como TRIGGER
GPIO_ECHO = 7 # usar pin GPIO 7 como ECHO
gpioservo = 17 # pin que controla el servo
orange = LED(18) # pin que usará el led

GPIO.setmode(GPIO.BCM) # poner placa en modo BCM
GPIO.setup(GPIO_TRIGGER, GPIO.OUT) # configurar TRIGGER como salida
GPIO.setup(GPIO_ECHO, GPIO.IN) # configurar ECHO como entrada
GPIO.output(GPIO_TRIGGER, False) # poner pin 23 como LOW

def distancia():
    GPIO.output(GPIO_TRIGGER, True) # enviar pulso de ultrasonidos
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)  # apagar pulso
    start = time.time()
    while GPIO.input(GPIO_ECHO) == 0: # mientras el sensor no reciba señal
        start = time.time()
    while GPIO.input(GPIO_ECHO) == 1:  # si se recibe señal
        stop = time.time()
    elapsed = stop - start # tiempo transcurrido
    distance = (elapsed * 34300) / 2  # distancia
    return distance

try:
    while True:
        print(distancia())
        time.sleep(1)
except KeyboardInterrupt:
    print('quit')
    GPIO.cleanup()
