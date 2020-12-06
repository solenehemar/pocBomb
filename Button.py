import RPi.GPIO as GPIO
import time
import sys, csv
from datetime import datetime, timedelta


button=24
count=0

GPIO.setmode(GPIO.BCM)
GPIO.setup(button,GPIO.IN)


value=GPIO.input(button)


# open csv file
f = open("buttonTape.csv", 'rU')
r = csv.reader(f)
liste = list(r)
tape = int(liste[0][0].split(";")[0]) #premier mot de la seule ligne du fichier



while value == 0:
        value = (GPIO.input(button))
        time.sleep(0.2)


if value == 1:
        count = count + 1
        now = datetime.now()
        date = now.strftime("%d/%m/%Y %H:%M:%S")
        seconds_to_add = 3
        datetime_new = now + timedelta(seconds = seconds_to_add)


        while datetime.now() < datetime_new:
                value = (GPIO.input(button))

                if value == 1:
                         count = count + 1
                         now = datetime.now()
                         date = now.strftime("%d/%m/%Y %H:%M:%S")
                         seconds_to_add = 3
                         datetime_new = now + timedelta(seconds = seconds_to_add)
                         time.sleep(0.2)




if count==tape:
	print 1
else:
	print 0
