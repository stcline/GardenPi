# This script will run the solenoid attached to pin 5 for a given number
# of minutes.  Edit the crontab file to set a time.

from gpiozero import LED
from time import sleep
import datetime

run_min = .5 #minutes solenoid will run
redLED = LED(27)
greenLED = LED(17)
solenoid = LED(5)
x = 1

redLED.off()
greenLED.off()
solenoid.off()

now = datetime.datetime.now()

#x is a proxy for the weather
if x == 1:
    solenoid.on()
    greenLED.on()
    sleep (60*run_min)
    solenoid.off()
    greenLED.off()

    print (now.strftime("%d-%m-%Y"), end = ",")
    print (now.strftime("%H:%M:%M"), end = ",")
    print (run_min)
    
else:
    print ("Rained previous day")
    
#Eventually build a decision in so that it does not run if at least .5 in
#of rain fell the day before.
