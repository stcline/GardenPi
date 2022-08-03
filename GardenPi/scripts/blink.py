from gpiozero import LED
from time import sleep

redLED = LED(27) # Choose the correct pin number
greenLED = LED(17)
solenoid = LED(5)

while True:
    redLED.on()
    greenLED.off()
    solenoid.on()
    sleep(1)
    redLED.off()
    greenLED.on()
    solenoid.off()
    sleep(1)