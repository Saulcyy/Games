#!/usr/bin/env python

import pygame, math, random
from gameVariables import *

class Bird:
    #- La classe pour l'oiseau ; la position x est toujours la même, on ne fait que
    #mise à jour de la position y uniquement lorsque nous tombons ou sautons, en se basant sur une formule
    def __init__(self):
        self.bird_x = gameWidth / 2 - birdWidth
        self.bird_y = gameHeight / 2 - birdHeight / 2
        self.steps_to_jump = 0

    #La formule utilisée permet de tout faire bouger "en douceur".
    def update_position(self):
        if self.steps_to_jump > 0:
            self.bird_y -= (1 - math.cos((jumpSteps - self.steps_to_jump) * math.pi)) * jumpPixels 
            #self.bird_y -= jumpPixels * (jumpSteps - self.steps_to_jump) / 5 ;
            self.steps_to_jump -= 1
        else:
            self.bird_y += dropPixels

    #- Quand on redessine l'oiseau sur l'écran de jeu, on dessine l'image de l'aile en haut ou de l'aile en bas.
    #l'image de l'aile en bas, pour créer l'effet de "battement".
    def redraw(self, screen, image_1, image_2):
        if pygame.time.get_ticks() % 500 >= 250 :
            screen.blit(image_1, (self.bird_x, self.bird_y))
        else:
            screen.blit(image_2, (self.bird_x, self.bird_y))

    #Rotation de l'oiseau pour créer l'effet de chute
    def redraw_dead(self, screen, image):
        self.bird_y += dropPixels
        bird_rot = pygame.transform.rotate(image, gameHeight / 2 - self.bird_y)
        screen.blit(bird_rot, (self.bird_x, self.bird_y))

class PipePair:
    #- La classe pour les tuyaux ; la position x d'origine est la marge de la fenêtre de jeu.
    #fenêtre de jeu ; les tuyaux se déplacent pixelsFrame / FPS
    #- A chaque fois, nous générons deux hauteurs : une pour le tuyau supérieur
    #et une pour le tuyau inférieur, avec le même espace exact entre les deux.
    #alors, pipesSpace
    #- score_counted nous dit si nous sommes passés par les tuyaux avec succès et
    #nous avons reçu les points
    
    def __init__(self, x, score_counted):
        self.x = gameWidth
        self.toph = random.randint(50, 250) - pipeHeight
        self.bottomh = self.toph + pipeHeight + pipesSpace
        self.score_counted = score_counted

    #Vérifie la collision avec l'oiseau et renvoie 1 ou 0 (1 = collision, 0 = pas de collision).
    def check_collision(self, bird_position):
        bx, by = bird_position
        in_x_range = bx + birdWidth > self.x and bx < self.x + pipeWidth
        in_y_range = by > self.toph + pipeHeight and by + birdHeight < self.toph + pipeHeight + pipesSpace
        return in_x_range and not in_y_range

class Ground:
    #- Une petite classe pour le sol qui semble rouler vers la gauche
    #- C'est juste une image qui a deux fois la largeur de l'écran du jeu,
    #mais quand elle arrive à sa fin, on la réinitialise
    
    def __init__(self, image):
        self.x = 0
        self.y = gameHeight - groundHeight
        self.image = image

    def move_and_redraw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        self.x -= pixelsFrame
        if(self.x < - gameWidth):
            self.x = 0