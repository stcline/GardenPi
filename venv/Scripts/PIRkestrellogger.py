# Log motion in Kestrel Box every five seconds in a csv file
import RPi.GPIO as GPIO
import time
import datetime
import csv

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(3, GPIO.OUT)         #LED output pin

while True:
        i=GPIO.input(11)
        if i==0:                 #When output from motion sensor is LOW
                print ("No motion",i)
                GPIO.output(3, 0)  #Turn OFF LED
                time.sleep(5)
        elif i==1:               #When output from motion sensor is HIGH
                now = datetime.datetime.now()
                GPIO.output(3, 1)  #Turn ON LED
                with open('bird_log.csv', 'a', newline='') as csvfile:
                        logwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
                        logwriter.writerow([now.strftime("%Y")] + [now.strftime("%d")] + [now.strftime("%m")] + [now.strftime("%H")] + [now.strftime("%M")] + [now.strftime("%S")] + ["motion"])
                print ([now.strftime("%Y")] + [now.strftime("%d")] + [now.strftime("%m")] + [now.strftime("%H")] + [now.strftime("%M")] + [now.strftime("%S")] + [ "motion"])
                time.sleep(5)
