#!/usr/bin/env python3

from gpiozero import LED
from time import sleep
import datetime
import csv

solenoid = LED(5)
redLED = LED(17)
mins = .25

now = datetime.datetime.now()

with open('/home/pi/GardenPi/water_log.csv', 'a', newline='') as csvfile:
                        logwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                        logwriter.writerow([now.strftime("%Y")] + [now.strftime("%d")] + [now.strftime("%m")] + [now.strftime("%H")] + [now.strftime("%M")] + [now.strftime("%S")] + ["Startup"])

redLED.on()
solenoid.off()
sleep (60 * mins)
redLED.off()
