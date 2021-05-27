import pygame
from sys import exit

# écouter chaque événement et réagir
def check_events(sqs, status, AI):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            key_down(sqs, event.key, status)
        if event.type == pygame.KEYUP:
            key_up(event.key, status)
    if status.is_AI():
        AI.control(sqs, status)

# traiter les touches qui sont enfoncées
def key_down(sqs, key, status):
    if status.is_game_new():
        status.game_status = status.ACTIVE
    elif status.is_game_over():
        status.game_status = status.RENEW
        status.new_AI = False
    if key == pygame.K_q:   # q stands for quit
        exit()
    if key == pygame.K_DOWN:
        status.down = True
    elif key == pygame.K_LEFT:
        status.left = True
        sqs.clock.update_left_down()
    elif key == pygame.K_RIGHT:
        status.right = True
        sqs.clock.update_right_down()
    elif key == pygame.K_UP:
        status.rotate = True
    elif key == pygame.K_SPACE:
        status.straight_drop = True
    if key == pygame.K_a:
        status.AI = True
        status.new_AI = True
        sqs.st.adjust_for_AI()

# traiter les clés qui sont libérées
def key_up(key, status):
    if key == pygame.K_q:
        exit()
    if key == pygame.K_DOWN:
        status.down = False
    elif key == pygame.K_LEFT:
        status.left = False
    elif key == pygame.K_RIGHT:
        status.right = False
    elif key == pygame.K_UP:
        status.rotate = False
    elif key == pygame.K_SPACE:
        status.straight_drop = False
