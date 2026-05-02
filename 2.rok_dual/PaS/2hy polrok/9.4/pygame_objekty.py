import pygame
print("triedy importovane")

class Hrac:
    def __init__(self, suradnice = [0,0]):
        self.suradnice = suradnice
        self.color = [216, 0, 116]
        self.height = 100
        self.width = 100
        self.body = pygame.Rect(self.suradnice[0], self.suradnice[1], self.width, self.height)
        self.speed = 0.2

    def update(self):
        self.body = pygame.Rect(self.suradnice[0], self.suradnice[1], self.width, self.height)