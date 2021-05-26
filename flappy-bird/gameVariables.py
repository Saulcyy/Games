#!/usr/bin/env python
import pygame
from pygame.locals import *

#Variables globales pour le jeu
gameWidth = 300                         #Fenêtre de jeu gameWidth
gameHeight = 500                        #Fenêtre de jeu gameHeight
FPS = 60                                #Images par seconde

birdHeight = 35                              #Hauteur de l'oiseau
birdWidth = 48                               #Largeur de l'oiseau
jumpSteps = 15                               #Pixels à déplacer
jumpPixels = 4                               #Pixels par image
dropPixels = 3                               #Pixels par image

groundHeight = 73                            #Hauteur du sol
pipeWidth = 52                               #Largeur d'un tuyau
pipeHeight = 320                             #Hauteur maximale d'un tuyau
pipesSpace = 4 * birdHeight                  #Largeur maximale d'un tuyau
pipesAddInterval = 2000                      #Millisecondes

pixelsFrame = 2                              #Pixels par image
getNewPipe = USEREVENT + 1                   #Événement personnalisé

pygame.init()                                #Initialiser pygame
screenResolution = pygame.display.Info()     #Obtenir la résolution de l'écran
pygame.quit()                                #Fermer pygame

gameScore = 0                                #Jeu gameScore
waitClick = True                         
