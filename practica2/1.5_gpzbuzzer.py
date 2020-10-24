from time import sleep
from gpiozero import Buzzer

gpiobuzzer = 16
bz = Buzzer(gpiobuzzer)
bz.on()
sleep(1)
bz.off()
