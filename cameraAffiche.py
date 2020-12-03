import sys, csv
from random import *


ligne = randint(0,3)

# open csv file
f = open("camera.csv", 'rU')
r = csv.reader(f)
liste = list(r)
objet = liste[ligne][0].split(";")[0] #premier mot du contenu de la ligne
couleur = liste[ligne][0].split(";")[1] #deuxième mot du contenu de la ligne



print couleur



#open csv file
ff = open("camera2.csv", 'w')
# Write string str to file.
ff.write(objet)
ff.close()
