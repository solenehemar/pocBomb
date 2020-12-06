# Ouvrir un terminal et executer la commande ci dessous
# D'apres : https://www.framboise314.fr/i-a-realisez-un-systeme-de-reconnaissance-dobjets-avec-raspberry-pi/
# python3 cameratest.py --prototxt MobileNetSSD_deploy.prototxt --model MobileNetSSD_deploy.caffemodel
 
# importer tout les packages requis
from imutils.video import VideoStream
from imutils.video import FPS
import numpy as np
import argparse
import imutils
import time
import cv2
import sys, csv

 
#variable pour voir si la camera a bien reconnu l'objet
verif=0


#afin de lire le fichier csv et prendre un mot aleatoire
f = open("camera2.csv", 'rU')
r = csv.reader(f)
liste = list(r)
objet = liste[0][0].split(";")[0]
 
# construction des arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--prototxt", required=True,
	help="path to Caffe 'deploy' prototxt file")
ap.add_argument("-m", "--model", required=True,
	help="path to Caffe pre-trained model")
ap.add_argument("-c", "--confidence", type=float, default=0.2,
	help="minimum probability to filter weak detections")

args = vars(ap.parse_args())
 
# initialiser la liste des objets entraines par MobileNet SSD 
# creation du contour de detection avec une couleur attribuee au hasard pour chaque objet
CLASSES = ["arriere-plan", "avion", "velo", "oiseau", "bateau",
	"bouteille", "autobus", "voiture", "chat", "chaise", "vache", "table",
	"chien", "cheval", "moto", "personne", "plante en pot", "mouton",
	"sofa", "train", "moniteur"]


# chargement des fichiers depuis le repertoire de stockage 
net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])
 
# initialiser la camera du pi, attendre 2s pour la mise au point ,
# initialiser le compteur FPS
vs = VideoStream(0).start()
time.sleep(2.0)
fps = FPS().start()
 
# boucle principale du flux video
for i in range (5) :
	# recuperation du flux video, redimension 
	# afin d'afficher au maximum 800 pixels 
	frame = vs.read()
	frame = imutils.resize(frame, width=800)
 
	# recuperation des dimensions et transformation en collection d'images
	(h, w) = frame.shape[:2]
	blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)),
		0.007843, (300, 300), 127.5)
 
	# determiner la detection et la prediction 
	net.setInput(blob)
	detections = net.forward()
 
	# boucle de detection 
	for i in np.arange(0, detections.shape[2]):
		# calcul de la probabilite de l'objet detecte 
		# en fonction de la prediction
		confidence = detections[0, 0, i, 2]
		idx = int(detections[0, 0, i, 1])
		
		# supprimer les detections faibles 
		# inferieures a la probabilite minimale
		if confidence > args["confidence"] and CLASSES[idx] == objet :

			
                        verif=1
	time.sleep(1)
	
print verif
