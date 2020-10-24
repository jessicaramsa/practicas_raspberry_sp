from gpiozero import AngularServo

gpioservo = 17
sermotor = AngularServo(gpioservo)
sermotor.angle = 0

try:
    while True:
        angulo = int(input('Introdce el ángulo  '))
        if -90 <= angulo <= 90:
            sermotor.angle = angulo
except KeyboardInterrupt:
    print('fin')
