#!/usr/bin/env python3

from gpiozero import LED
from time import sleep

solenoid = LED(5)
yelLED = LED(27)
mins = 10

solenoid.on()
print("Water run for "+str(mins)+" minutes.")
sleep(60*mins)
solenoid.off()
