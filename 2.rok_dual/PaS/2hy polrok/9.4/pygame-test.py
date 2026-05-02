#main imports
#boiler plate - potrebny kod kt tam musi byt aby to fungovalo, veci okolo core codu
import pygame
import datetime
import random

#local imports
from pygame_objekty import Hrac

#main 3 phases of game:    (1. input, 2. update) 3. draw

screen_size=(640,640)
game_running = True

pygame.init()
my_screen = pygame.display.set_mode(screen_size)

hrac = Hrac([10,10])

while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("stlacil som space")
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                print("pustil som space")

    #input - check held keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        hrac.suradnice[1] -= hrac.speed
    if keys[pygame.K_DOWN]:
        hrac.suradnice[1] += hrac.speed
    if keys[pygame.K_LEFT]:
        hrac.suradnice[0] -= hrac.speed
    if keys[pygame.K_RIGHT]:
        hrac.suradnice[0] += hrac.speed

    #update
    hrac.update()

    #draw
    my_screen.fill((255,255,255))
    pygame.draw.rect(my_screen, hrac.color, hrac.body)
    pygame.display.update()
    

pygame.quit()