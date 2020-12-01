import sys, csv
from random import *


ligne = randint(0,4)

# open csv file
f = open("button.csv", 'rU')
r = csv.reader(f)
liste = list(r)
couleur = liste[ligne][0].split(";")[0] #premier mot du contenu de la ligne
mot = liste[ligne][0].split(";")[1]
tape = liste[ligne][0].split(";")[2]



print mot
print couleur



#open csv file
ff = open("buttonTape.csv", 'w')
# Write string str to file.
ff.write(tape)
ff.close()
