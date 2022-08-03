# This script will run the solenoid attached to pin 5 for 30 minutes

from gpiozero import LED
from time import sleep

redLED = LED(27)
greenLED = LED(17)
solenoid = LED(5)

solenoid.on()
greenLED.on()
print ("Solenoid Valve On")
sleep(1800)
solenoid.off()
greenLED.off()
print ("Solenoid Valve Off")
