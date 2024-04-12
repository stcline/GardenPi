from gpiozero import LED
from time import sleep

greenLED = LED(27)
#solenoid = LED(5)

#solenoid.on()
greenLED.on()
sleep (10)
#solenoid.off()
greenLED.off()
