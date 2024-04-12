#!/usr/bin/env python3

from gpiozero import LED
from time import sleep
import datetime
import csv

start = ["20", "00"]

solenoid = LED(5)
yelLED = LED(27)
time_run = 25
sleep (60)

for x in range(4):
	yelLED.on()
	sleep (.3)
	yelLED.off()
	sleep(.3)

while True:

	now = datetime.datetime.now()

	if now.strftime("%H") == start[0] and now.strftime("%M") == start[1] and now.strftime("%S") == "00":

	# Start watering and print the time to the log
		print ("Water running at ",now)
		yelLED.on()
		solenoid.on()

		with open('/home/pi/GardenPi/water_log.csv', 'a', newline='') as csvfile:
			logwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
			logwriter.writerow([now.strftime("%Y")] + [now.strftime("%d")] + [now.strftime("%m")] + [now.strftime("%H")] + [now.strftime("%M")] + [now.strftime("%S")] + ["Water started for " + str(time_run) + " minutes"])

		sleep(time_run * 60)

		# Stop watering and print the time to the log
		now = datetime.datetime.now()
		print ("Water shut off at ", now)
		yelLED.off()
		solenoid.off()

		with open('/home/pi/GardenPi/water_log.csv', 'a', newline='') as csvfile:
			logwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
			logwriter.writerow([now.strftime("%Y")] + [now.strftime("%d")] + [now.strftime("%m")] + [now.strftime("%H")] + [now.strftime("%M")] + [now.strftime("%S")] + ["Water stopped"])

