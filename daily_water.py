#!/usr/bin/env python3

from gpiozero import LED
from time import sleep
import datetime

start = ["02","47","00","42"]

solenoid = LED(5)
yelLED = LED(27)
mins = .5
mins2 = .5

sleep (60)

for x in range(4):
    yelLED.on()
    sleep (.3)
    yelLED.off()
    sleep(.3)

while True:
    now = datetime.datetime.now()
    if now.strftime("%H") == start[0] and now.strftime("%M") == start[1] and now.strftime("%S") == "00":
        print ("Time to water!")
        yelLED.on()
        solenoid.on()
        sleep(60*mins)
        print ("All done")
        yelLED.off()
        solenoid.off()
    elif now.strftime("%H") == start[2] and now.strftime("%M") == start[3] and now.strftime("%S") == "00":
        print ("Time to water!")
        yelLED.on()
        solenoid.on()
        sleep(60*mins2)
        print ("All done")
        yelLED.off()
        solenoid.off()
