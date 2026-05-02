import pygame

print("importnute")


class Kocka:  # by default velke pismeno prve
    def __init__(self, suradnice=[0, 0], rozmer = [50,50]):  # ma 2 _ -> je to abstrakcia, nechceme aby ostanty vedeli o nej
        self.suradnice = suradnice
        self.color = [255, 100, 3]
        self.width = rozmer[0]
        self.heigth = rozmer[1]
        self.lives = 9

        self.body = pygame.Rect(self.suradnice[0], self.suradnice[1], self.width, self.heigth)
        self.speed = 5
        # hlavna pygame documentacia https://www.pygame.org/docs/

    def update(self):
        self.body = pygame.Rect(self.suradnice[0], self.suradnice[1], self.width, self.heigth)



class EnemyKocka(Kocka):  # by default velke pismeno prve
    def update(self):
        self.body = pygame.Rect(self.suradnice[0], self.suradnice[1], self.width, self.heigth)
        self.chase()

    def chase(self):
        if self.target is not None:
            if self.suradnice[0] < self.target.suradnice[0]:
                self.suradnice[0] += self.speed
            if self.suradnice[0] > self.target.suradnice[0]:
                self.suradnice[0] -= self.speed
            if self.suradnice[1] < self.target.suradnice[1]:
                self.suradnice[1] += self.speed
            if self.suradnice[1] > self.target.suradnice[1]:
                self.suradnice[1] -= self.speed