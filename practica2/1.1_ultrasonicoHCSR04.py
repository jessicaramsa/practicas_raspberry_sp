import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # placa en modo BCM
GPIO_TRIGGER = 8 # usar el pin GPIO 24 como TRIGGER
GPIO_ECHO = 7 # usar el pint GPIO 26 como ECHO

GPIO.setup(GPIO_TRIGGER, GPIO.OUT) # configurar TRIGGER como salida
GPIO.setup(GPIO_ECHO, GPIO.IN) # configurar ECHO como entrada
GPIO.setup(GPIO_TRIGGER, False) # poner el pint 23 como LOW

try:
    while True:
        GPIO.output(GPIO_TRIGGER, True) # enviar pulso de ultrasonidos
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER, False) # apagar pulso
        start = time.time()
        while GPIO.input(GPIO_ECHO) == 0: # mientras el sensor no reciba señal
            start = time.time()
        while GPIO.input(GPIO_ECHO) == 1: # si se recibe señal
            stop = time.time()
        elapsed = stop - start # tiempo transcurrido
        distance = (elapsed * 34300) / 2 # distancia
        print(distance)
        time.sleep(1)
except KeyboardInterrupt:
    print('quit')
    GPIO.cleanup()
