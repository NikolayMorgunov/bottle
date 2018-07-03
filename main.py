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
    v = 9
    face = pygame.image.load("Michael.png")
    def show(self):
        window.blit(self.face, self.place)

hero = Hero()
class Bottle:
    global hero
    bottle_pict = pygame.image.load("Bottle.png")
    place = (720, random.randint(0, 430))
    v = random.randint(-10, -3)
    def show(self):
        window.blit(self.bottle_pict, (self.place[0], self.place[1] + 30))

class Dildo:
    place = (0, 0)
    dildo_pict = pygame.image.load("Dildo.png")
    v = 9
    def show(self):
        window.blit(self.dildo_pict, (self.place[0], self.place[1] + 30))

fps = 0

def draw_all():
    hero.show()
    for i in dildos:
        i.show()
    for i in bottles:
        i.show()


FIELD = pygame.image.load("Field.png")
bottles = []
dildos = []
space_pressed = False
while True:
    for event in pygame.event.get():
        from pygame import QUIT
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    window.blit(FIELD, (0, 0))
    draw_all()
    fps += 1
    fps = fps % 60

    if not fps:
        if random.choice([True, False]):
            bottles.append(Bottle())
            bottles[-1].place = (720, random.randint(0, 430))
            bottles[-1].v = random.randint(-7, -3)
    for i in range(len(bottles)):
        bottles[i].place = (bottles[i].place[0] + bottles[i].v, bottles[i].place[1])

    bottles = list(filter(lambda x: x.place[0] > -100, bottles))
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
        dildos[-1].place = hero.place

    dildos = list(filter(lambda x: x.place[0] < 720, dildos))
    if not pressed[K_SPACE]:
        space_pressed = False

    pygame.display.update()
    clock.tick(60)
