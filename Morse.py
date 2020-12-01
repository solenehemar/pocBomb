import RPi.GPIO as GPIO
import sys
import time
from random import *
import sys, argparse, csv

gpio=24
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
mot = liste[ligne][0].split(";")[1] #premier mot du contenu de la ligne numero "ligne" (car la ligne numero "ligne" est un tableau contenant un string)

frequence = liste[ligne][0].split(";")[0]
print frequence



time.sleep(3)




for i in range(2, len(liste[ligne][0].split(";"))):
	val = liste[ligne][0].split(";")[i]
	print val

	if val == '0' : #espace dans csv
		GPIO.output(LED, GPIO.LOW) #the gpio is low (so the led light off)
		time.sleep(2)

	if val == '1' : #point dans csv
		GPIO.output(LED, GPIO.HIGH) #the gpio is high (so the led light on)
		time.sleep(1)
		GPIO.output(LED, GPIO.LOW)
		time.sleep(1)

	if val == '2' : #trait dans csv
		GPIO.output(LED, GPIO.HIGH) #the gpio is high (so the led light on)
		time.sleep(3)
		GPIO.output(LED, GPIO.LOW)
		time.sleep(1)





GPIO.output(LED, GPIO.LOW)
