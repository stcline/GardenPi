import RPi.GPIO as GPIO
from time import sleep

switchPin = 8

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(switchPin, GPIO.OUT, initial=GPIO.LOW)

# Run a quick test of the switch
print ("The switch is on")
GPIO.output(switchPin, GPIO.HIGH)
sleep (2)
print ("The switch is off")
GPIO.output(switchPin, GPIO.LOW)
