#main py file

#main imports
import pygame
import datetime
import random

#local imports
#from pygame_game import pygame_objekty
from pygame_objekty import Kocka, EnemyKocka

#main 3 phases of game: input, update, draw

screen_size=(640,440) #je to tuple lebo nase okno size sa nebude menit pocas hry
game_running = True

pygame.init()
my_screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()  ## For syncing the FPS
FPS = 30
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 20)



hrac = Kocka(suradnice=[10,10],rozmer=[30,30])

kocky = []
kocky.append(hrac)

kocky.append(EnemyKocka(suradnice=[screen_size[0] - 10 , screen_size[1] - 10],rozmer=[30,30]))
kocky[-1].color = (0,0,0)
kocky[-1].suradnice[0] -= kocky[-1].width
kocky[-1].suradnice[1] -= kocky[-1].heigth
kocky[-1].target = hrac


while game_running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Stlaceny space")
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                print("Pusteny space")


    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        hrac.suradnice[1] -= hrac.speed
    elif keys[pygame.K_DOWN]:
        hrac.suradnice[1] += hrac.speed
    if keys[pygame.K_LEFT]:
        hrac.suradnice[0] -= hrac.speed
    elif keys[pygame.K_RIGHT]:
        hrac.suradnice[0] += hrac.speed



    #update
    for k in kocky:
        k.update()
        if k.suradnice[0] + k.width >= screen_size[0]:
            k.suradnice[0]  = screen_size[0] - k.width
        elif k.suradnice[0] < 0:
            k.suradnice[0] = 0
        if k.suradnice[1] + k.heigth >= screen_size[1]:
            k.suradnice[1]  = screen_size[1] - k.heigth
        elif k.suradnice[1] < 0:
            k.suradnice[1] = 0


        for j in kocky:
            if j != k:
                if k.body.colliderect(j.body):
                    # print("Kolizia kociek")
                    if k == hrac:
                        hrac.lives -= 1

                    else:
                        x = random.randint(10, screen_size[0] - k.width)
                        y = random.randint(10, screen_size[1] - k.heigth)
                        k.suradnice = [x,y]

    #draw
    my_screen.fill((100,100,100)) #toto je rgb farba

    for k in kocky:
        pygame.draw.rect(my_screen,k.color, k.body)
        if k == hrac:
            my_screen.blit(my_font.render(f'{k.lives}', False, (0, 0, 0)), [k.suradnice[0] + k.width / 4 , k.suradnice[1] + k.heigth / 50])

    pygame.display.update()


pygame.quit()