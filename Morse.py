import RPi.GPIO as GPIO
import sys
import time
from random import *
import sys, argparse, csv

gpio=23
GPIO.setmode(GPIO.BCM) #the number of the gpio
GPIO.setwarnings(False) #to disable warnings

#the lamp is linked to the gpio defined before
LED = int(gpio)
#the gpio is considered as an output
GPIO.setup(LED, GPIO.OUT)


ligne = randint(0,5) #ligne aleatoire du csv

# open csv file
f = open("morse.csv", 'rU')
r = csv.reader(f)
liste = list(r)
frequence = liste[ligne][0].split(";")[0]
print frequence



time.sleep(3)




for i in range(2, len(liste[ligne][0].split(";"))):
	val = liste[ligne][0].split(";")[i]
	print val

	if val == '0' : #espace
		GPIO.output(LED, GPIO.LOW) #the gpio is low (so the led lights off)
		time.sleep(2)

	if val == '1' : #point
		GPIO.output(LED, GPIO.HIGH) #the gpio is high (so the led lights on)
		time.sleep(1)
		GPIO.output(LED, GPIO.LOW)
		time.sleep(1)

	if val == '2' : #trait
		GPIO.output(LED, GPIO.HIGH) #the gpio is high (so the led lights on)
		time.sleep(3)
		GPIO.output(LED, GPIO.LOW)
		time.sleep(1)





GPIO.output(LED, GPIO.LOW)
