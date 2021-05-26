#!/usr/bin/env python
import sys, os, random, pygame
from gameVariables import *

def initialize_pygame():
    pygame.init()
    pygame.mixer.init()

    #Ouverture de la fenêtre au centre de l'écran
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % ((screenResolution.current_w - gameWidth) / 2, (screenResolution.current_h - gameHeight) / 2)
    screen = pygame.display.set_mode([gameWidth, gameHeight], pygame.DOUBLEBUF, 32)
    pygame.display.set_icon(pygame.image.load('images/icon.ico'))
    pygame.display.set_caption("Flappy Bird")

    return screen

def load_images():
    #- Chargement de toutes les images requises pour le jeu depuis le dossier images
    #et retourner un dictionnaire de celles-ci comme suit :
       
    #'background_1' : fond du jour
    #'bird' : l'oiseau
    #'bird2' : l'oiseau avec les ailes baissées
    #'pipe-up' : le tuyau pour la partie supérieure
    #'pipe-down' : le tuyau pour la partie inférieure
    #'ground' : le sol

    def load_image(img_file_name):
        #- Recherche d'images dans le dossier images du jeu (./images/)
        #- Chargement de l'image puis conversion de celle-ci, car cela accélère
        #- Chargement de l'image, puis retour de l'image dans le dictionnaire
        #- Pour l'image de fond, nous en chargeons une au hasard, puisque nous avons
        #avons un fond de jour un fond de nuit
        
        file_name = os.path.join('.', 'images', img_file_name)
        img = pygame.image.load(file_name)
        img.convert()
        return img

    return {'background': load_image('background_' + str(random.randint(1, 2)) + '.png'),
            'bird': load_image('bird.png'),
            'bird2': load_image('bird2.png'),    
            'pipe-up': load_image('pipe-up.png'), 
            'pipe-down': load_image('pipe-down.png'),
            'ground': load_image('ground.png')}

def draw_text(screen, text, y_pos, size):
    #Dessiner un texte noir (plus grand) et ensuite un texte blanc, plus petit
    #par-dessus pour obtenir l'effet gameScore désiré.
    font = pygame.font.Font("data/04b_19.TTF", size)
    score_text_b = font.render(str(text), 1, (0, 0, 0))
    score_text_w = font.render(str(text), 1, (255, 255, 255))

    x_pos_b = (gameWidth - score_text_b.get_width()) / 2
    x_pos_w = (gameWidth - score_text_w.get_width()) / 2
    screen.blit(score_text_b, (x_pos_b + 2, y_pos - 1))
    screen.blit(score_text_w, (x_pos_w, y_pos))

def end_the_game(screen, gameScore):
    #Dessine un rectangle, affiche le score du jeu et met à jour le score le plus élevé.
    pygame.draw.rect(screen, (0, 0, 0), (23, gameHeight / 2 - 77, 254, 154))
    pygame.draw.rect(screen, (239, 228, 150), (25, gameHeight / 2 - 75, 250, 150))
    draw_text(screen, "Your Score: " + str(gameScore), 200, 35)
    
    f = open("data/highscore", "r+")
    hs = int(f.readline())
    if(gameScore > hs):
       hs = gameScore
       f.seek(0)
       f.truncate()
       f.write(str(hs))
    f.close()
    
    draw_text(screen, "Highscore: " + str(hs), 250, 35)
    draw_text(screen, "Press space to restart", 335, 20)
    draw_text(screen, "Press esc to exit", 355, 20)
    
    #Mise à jour de l'écran entier pour la dernière fois
    pygame.display.update()

    #Récupère les événements clavier pour voir si l'utilisateur veut redémarrer le jeu.
    while True:
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == K_SPACE:
                    return 0
                elif e.key == K_ESCAPE:
                    return 1