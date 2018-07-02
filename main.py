import pygame
import time
from pygame import QUIT
#from pygame.constants import K_LEFT, K_RIGHT, K_UP, K_SPACE, K_k, K_m
from pygame.surface import Surface
import sys
import random
from pygame.time import Clock

pygame.init()
window: Surface = pygame.display.set_mode((720, 480), 0, 32)
pygame.display.set_caption('Michael`s bottles')
clock = Clock()

class Hero:
    place = (120, 240)
    def show(self):
        pygame.draw.ellipse(window, (0, 255, 0), [self.place[0], self.place[1], 25, 25])


while True:
    for event in pygame.event.get():
        from pygame import QUIT
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    hero = Hero()
    hero.show()

    clock.tick(60)
