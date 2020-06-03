#Adapted from example at https://docs.python.org/3/library/csv.html
#strftime codes at https://strftime.org/

import csv
import datetime

time_run = 10
now = datetime.datetime.now()
with open('water_log.csv', 'a', newline='') as csvfile:
    logwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    logwriter.writerow([now.strftime("%Y")] + [now.strftime("%d")] + [now.strftime("%m")] + [now.strftime("%H")] + [now.strftime("%M")] + [now.strftime("%S")] + ["Watered for "+str(time_run)+" minutes"])