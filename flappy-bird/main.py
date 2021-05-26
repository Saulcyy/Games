#!/usr/bin/env python

#Importation de bibliothèques
import os, sys, pygame, random, math
from pygame.locals import *
from gameFunctions import *
from gameClasses import *
import gameVariables

def main():
    #Initialisation de pygame et du mixeur
    screen = initialize_pygame()

    #Mise en place de minuteries 
    clock = pygame.time.Clock()
    pygame.time.set_timer(getNewPipe, pipesAddInterval)
    
    #Chargement des images | Création de l'oiseau | Création du sol | Création de la liste de jeu
    gamePipes = []
    gameBird = Bird()
    gameImages = load_images()
    gameVariables.gameScore = 0
    gameGround = Ground(gameImages['ground'])
      
    #Chargement des sons
    jump_sound = pygame.mixer.Sound('sounds/jump.ogg')
    score_sound = pygame.mixer.Sound('sounds/score.ogg')
    dead_sound = pygame.mixer.Sound('sounds/dead.ogg')

    while(gameVariables.waitClick == True):
        #Dessinez tout et attendez que l'utilisateur clique pour lancer le jeu.
        #Quand on clique quelque part, l'oiseau saute et le jeu commence.
        screen.blit(gameImages['background'], (0, 0))
        draw_text(screen, "Click to start", 285, 20)
        screen.blit(gameImages['ground'], (0, gameHeight - groundHeight))

        #Drawing a "floating" flappy bird
        gameBird.redraw(screen, gameImages['bird'], gameImages['bird2'])

        #Mise à jour de l'écran
        pygame.display.update()

        #Vérifier si l'utilisateur a appuyé sur le clic gauche ou l'espace et lancer (ou non) le jeu.
        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONDOWN or (e.type == pygame.KEYDOWN and e.key == K_SPACE):
                gameBird.steps_to_jump = 15
                gameVariables.waitClick = False
    jump_sound.play()
    
    #Bouclez jusqu'à ce que... nous mourions !
    while True:
        #Dessiner l'arrière-plan
        screen.blit(gameImages['background'], (0, 0))

        #Recevoir les événements de la souris, du clavier ou de l'utilisateur et agir en conséquence
        for e in pygame.event.get():
            if e.type == getNewPipe:
                p = PipePair(gameWidth, False)
                gamePipes.append(p)
            elif e.type == pygame.MOUSEBUTTONDOWN:
                gameBird.steps_to_jump = jumpSteps
                jump_sound.play()
            elif e.type == pygame.KEYDOWN:
                if e.key == K_SPACE:
                    gameBird.steps_to_jump = jumpSteps
                    jump_sound.play()
                elif e.key == K_ESCAPE:
                    exit()

        #Tic ! (nouveau cadre)
        clock.tick(FPS)

        #Mettre à jour la position des gamePipes et les redessiner ; si un pipe n'est plus visible,
        #on le supprime de la liste
        for p in gamePipes:
            p.x -= pixelsFrame
            if p.x <= - pipeWidth:
                gamePipes.remove(p)
            else:
                screen.blit(gameImages['pipe-up'], (p.x, p.toph))
                screen.blit(gameImages['pipe-down'], (p.x, p.bottomh))

        #Redessiner le sol
        gameGround.move_and_redraw(screen)
        
        #Mettre à jour la position de l'oiseau et le redessiner
        gameBird.update_position()
        gameBird.redraw(screen, gameImages['bird'], gameImages['bird2'])

        #Check for any collisions between the gamePipes, bird and/or the lower and the
        #partie supérieure de l'écran
        if any(p.check_collision((gameBird.bird_x, gameBird.bird_y)) for p in gamePipes) or \
               gameBird.bird_y < 0 or \
               gameBird.bird_y + birdHeight > gameHeight - groundHeight:
            dead_sound.play()
            break

        #Il n'y a pas eu de collision si nous avons atterri ici, donc nous vérifions si 
        #l'oiseau a traversé la moitié de la largeur de jeu du tuyau ; si c'est le cas, nous mettons à jour le score du jeu.
        for p in gamePipes:
            if(gameBird.bird_x > p.x and not p.score_counted):
                p.score_counted = True
                gameVariables.gameScore += 1
                score_sound.play()

        #Affiche le score du jeu à l'écran.
        draw_text(screen, gameVariables.gameScore, 50, 35)
        
        #Mise à jour de l'écran
        pygame.display.update()

    #Nous sommes morts maintenant, donc nous faisons "tomber" l'oiseau.
    while(gameBird.bird_y + birdHeight < gameHeight - groundHeight):
        #Redessine l'arrière-plan
        screen.blit(gameImages['background'], (0, 0))

        #Redessiner le gamePipes au même endroit que lorsqu'il est mort
        for p in gamePipes:
            screen.blit(gameImages['pipe-up'], (p.x, p.toph))
            screen.blit(gameImages['pipe-down'], (p.x, p.bottomh))

        #Dessine la pièce au sol pour obtenir l'effet de roulement.
        gameGround.move_and_redraw(screen)

        #Fait tomber l'oiseau et le fait tourner
        gameBird.redraw_dead(screen, gameImages['bird'])

        #Tic !
        clock.tick(FPS * 3)
    
        #Mise à jour de l'ensemble de l'écran
        pygame.display.update()

    #Mettons fin au jeu !
    if not end_the_game(screen, gameScore):
        main()
    else:
        pygame.display.quit()
        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    #- Si ce module avait été importé, __name__ serait 'Flappy Bird' ;
    #sinon, s'il était exécuté (en double-cliquant sur le fichier) nous appellerions main
    main()
