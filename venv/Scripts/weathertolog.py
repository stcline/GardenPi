
#!/usr/bin/env python3

import requests
import json
import datetime
from time import sleep
from gpiozero import LED

blueLED = LED(22)

for x in range(4):
    blueLED.on()
    sleep (.3)
    blueLED.off()
    sleep(.3)

settings = {
    'api_key':'eb71c2145016f92a03ebdfff076246e0',
    'zip_code':'80550',
    'country_code':'us',
    'temp_unit':'imperial'} #unit can be metric, imperial, or kelvin

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?appid={0}&zip={1},{2}&units={3}"

while True:
    # Request JSON from OpenWeatherMap
    final_url = BASE_URL.format(settings["api_key"],settings["zip_code"],settings["country_code"],settings["temp_unit"])
    weather_data = requests.get(final_url).json()
    # record date and time
    now = datetime.datetime.now()
    # csv file to store data
    log = open('/home/pi/GardenPi/log.csv', 'a') # On GardenPi
    # TODO: Set these filepaths
    #log = open('/home/pi/GardenPi/log.csv', 'a')  # On PC
    #log = open('/home/pi/GardenPi/log.csv', 'a') # On Linux box
    descriptions = [item['description'] for item in weather_data['weather']] #parse descriptions from weather dictionary
    print ((now.strftime("%d-%m-%Y")) + "," + (now.strftime("%H:%M:%M")) + "," + descriptions[0],file=log) #print timestamp and first description to log
    log.close()
    sleep (300)
