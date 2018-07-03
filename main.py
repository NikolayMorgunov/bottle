import pygame
import time
from pygame import QUIT
from pygame.constants import K_UP, K_DOWN, K_SPACE
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
    v = 7
    face = pygame.image.load("Michael.png")
    def show(self):
        window.blit(self.face, self.place)

hero = Hero()
class Bottle:
    global hero
    place = hero.place
    v = random.randint(-10, -3)
    def show(self):
        pygame.draw.rect(window, (255, 0, 0), [self.place[0], self.place[1], 25, 25])

class Dildo:
    place = hero.place
    dildo_pict = pygame.image.load("Dildo.png")
    v = 9
    def show(self):
        window.blit(self.dildo_pict, (self.place[0], self.place[1] + 30))

fps = 0

def draw_all():
    hero.show()
    for i in dildos:
        i.show()


FIELD = pygame.image.load("Field.png")
bottles = []
dildos = []
while True:
    space_pressed = False
    for event in pygame.event.get():
        from pygame import QUIT
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    window.blit(FIELD, (0, 0))
    draw_all()
    fps = fps % 40
    fps += 1

    if not fps:
        if random.choice([True, False]):
            bottles.append(Bottle())
    for i in range(len(bottles)):
        bottles[i].place[0] += bottles[i].v
    for i in range(len(dildos)):
        dildos[i].place = (dildos[i].place[0] + dildos[i].v, dildos[i].place[1])

    pressed = pygame.key.get_pressed()
    if pressed[K_UP]:
        if hero.place[1] > 0:
            hero.place = (hero.place[0], hero.place[1] - hero.v)
    elif pressed[K_DOWN]:
        if hero.place[1] < 415:
            hero.place = (hero.place[0], hero.place[1] + hero.v)
    elif pressed[K_SPACE] and not space_pressed:
        dildos.append(Dildo())
        space_pressed = True

    if not pressed[K_SPACE]:
        space_pressed = False

    pygame.display.update()
    clock.tick(60)
