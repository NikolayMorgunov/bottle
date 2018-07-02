import pygame
import time
from pygame import QUIT
from pygame.constants import K_UP, K_DOWN, K_RETURN
from pygame.surface import Surface
import sys
import random
from pygame.time import Clock

pygame.init()
window: Surface = pygame.display.set_mode((720, 480), 0, 32)
pygame.display.set_caption('Michael`s bottles')
clock = Clock()

class Hero:
    place = (95, 215)
    v = 10
    def show(self):
        pygame.draw.ellipse(window, (0, 255, 0), [self.place[0], self.place[1], 25, 25])

class Bottle:
    place = hero.place
    v = random.randint(-30, -10)
    def show(self):
        pygame.draw.rect(window, (255, 0, 0), [self.place[0], self.place[1], 25, 25])

class Dildo:
    place = (95, 215)
    v = 15
    def show(self):
        pygame.draw.rect(window, (255, 255, 0), [self.place[0], self.place[1], 25, 25])

fps = 0
while True:
    for event in pygame.event.get():
        from pygame import QUIT
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    hero = Hero()
    hero.show()
    bottle = Bottle()
    bottle.show()
    fps = fps % 40
    clock.tick(60)
