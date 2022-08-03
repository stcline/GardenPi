
#!/usr/bin/env python3

from gpiozero import LED
from time import sleep
import datetime

start = ["19","47"]

solenoid = LED(5)
yelLED = LED(27)
mins = 10

sleep (60)

for x in range(4):
    yelLED.on()
    sleep (.3)
    yelLED.off()
    sleep(.3)

while True:
    now = datetime.datetime.now()
    if now.strftime("%H") == start[0] and now.strftime("%M") == start[1] and now.$
        print ("Time to water!")
        yelLED.on()
        solenoid.on()
        sleep(60*mins)
        print ("All done")
        yelLED.off()
        solenoid.off()
