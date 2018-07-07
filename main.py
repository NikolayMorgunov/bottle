import pygame
import time
from pygame import QUIT
from pygame.constants import K_UP, K_DOWN, K_SPACE, K_RETURN
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
    v = random.randint(-7, -5)
    def show(self):
        window.blit(self.bottle_pict, (self.place[0], self.place[1] + 30))

class Dildo:
    place = (0, 0)
    dildo_pict = pygame.image.load("Dildo.png")
    v = 9
    def show(self):
        window.blit(self.dildo_pict, (self.place[0] + 40, self.place[1] + 30))

fps = 0

def draw_all():
    hero.show()
    for i in dildos:
        i.show()
    for i in bottles:
        i.show()
    live = pygame.image.load("Lives.png")
    for i in range(lives):
        window.blit(live, (i * 35, 0))
    podsk = pygame.font.SysFont('Times New Roman', 25)
    nadp = podsk.render(u'Cчёт: ' + str(score), True, (0, 0, 0))
    window.blit(nadp, (580, 20, 200, 200))

    podsk = pygame.font.SysFont('Times New Roman', 25)
    nadp = podsk.render(u'Лучший счёт: ' + str(hi_score), True, (0, 0, 0))
    window.blit(nadp, (540, 60, 200, 200))
FIELD = pygame.image.load("Field.png")
bottles = []
dildos = []
space_pressed = False
menu = True
lost = False
being_lost = False
while True:
    for event in pygame.event.get():
            from pygame import QUIT
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
    if menu:
        pygame.draw.rect(window, (255, 255, 255), (0, 0, 720, 480))
        podsk = pygame.font.SysFont('Times New Roman', 23)
        nadp = podsk.render(u'Управляй Михаилом стрелками (вверх и вниз)', True, (0, 0, 0))
        window.blit(nadp, (140, 20, 200, 200))

        podsk = pygame.font.SysFont('Times New Roman', 23)
        nadp = podsk.render(u'Отстреливайся от бутылок, нажимая на пробел', True, (0, 0, 0))
        window.blit(nadp, (135, 60, 200, 200))

        podsk = pygame.font.SysFont('Times New Roman', 23)
        nadp = podsk.render(u'(Не более 3 "снарядов" одновременно)', True, (0, 0, 0))
        window.blit(nadp, (180, 120, 200, 200))

        podsk = pygame.font.SysFont('Times New Roman', 23)
        nadp = podsk.render(u'Не дай им пройти за чёрную линию', True, (0, 0, 0))
        window.blit(nadp, (185, 180, 200, 200))

        podsk = pygame.font.SysFont('Times New Roman', 23)
        nadp = podsk.render(u'Нажми Enter, тобы начать', True, (0, 0, 0))
        window.blit(nadp, (245, 300, 200, 200))

        if pygame.key.get_pressed()[K_RETURN]:
            menu = False
            lives = 10
            score = 0
            inp = open("hi_score.txt", "r")
            hi_score = int(inp.read())
            inp.close()
    elif lost:
        if score > hi_score:
            outp = open("hi_score.txt", "w")
            outp.write(str(score))
            outp.close()
            hi_score = score
        score = 0
        pygame.draw.rect(window, (255, 255, 255), (0, 0, 720, 480))
        podsk = pygame.font.SysFont('Times New Roman', 23)
        if being_lost:
            phrase = random.choice([u'Ха! Лох проигралъ!!!', u'Ебать ты лох', u'Cнимай штаны, паршня',
                                           u'Фу лох сука тупой', u'Хахаха посмотрите на него!!!',
                                           u'Боже в игру играет умственно отсталый'])
            being_lost = False
        nadp = podsk.render((phrase), True, (0, 0, 0))
        window.blit(nadp, (50, 50, 200, 200))

        podsk = pygame.font.SysFont('Times New Roman', 23)
        nadp = podsk.render(u'Нажми Enter, чтобы попробовать еще раз', True, (0, 0, 0))
        window.blit(nadp, (245, 300, 200, 200))
        if pygame.key.get_pressed()[K_RETURN]:
            lost = False
            lives = 10
            bottles = []
            dildos = []
    else:
    ##################
        window.blit(FIELD, (0, 0))
        draw_all()
        fps += 1
        fps = fps % 60
    #Добавление бутылок
        if not fps:
            if random.choice([True, False]):
                bottles.append(Bottle())
                bottles[-1].place = (720, random.randint(0, 430))
                bottles[-1].v = random.randint(-7, -3)
    #Взаимодействие
        for i in range(len(bottles)):
            for j in range(len(dildos)):
                if bottles[i].place[0] <= dildos[j].place[0] + 30 <= bottles[i].place[0] + 80\
                        and bottles[i].place[1] <= dildos[j].place[1] + 10 <= bottles[i].place[1] + 37:
                    bottles[i].place = (-200, 0)
                    dildos[j].place = (830, 0)
                    score += 1
    #Перемещение бутылок
        for i in range(len(bottles)):
            bottles[i].place = (bottles[i].place[0] + bottles[i].v, bottles[i].place[1])
        bottles = list(filter(lambda x: x.place[0] > -100, bottles))
    #Перемещение дилдо
        dildos = list(filter(lambda x: x.place[0] < 720, dildos))
        for i in range(len(dildos)):
            dildos[i].place = (dildos[i].place[0] + dildos[i].v, dildos[i].place[1])
    #Клава
        pressed = pygame.key.get_pressed()
        if pressed[K_UP]:
            if hero.place[1] > -30:
                hero.place = (hero.place[0], hero.place[1] - hero.v)
        elif pressed[K_DOWN]:
            if hero.place[1] < 415:
                hero.place = (hero.place[0], hero.place[1] + hero.v)
        if pressed[K_SPACE] and not space_pressed and len(dildos) < 3:
            dildos.append(Dildo())
            space_pressed = True
            dildos[-1].place = hero.place
    #Пробел не нажат
        if not pressed[K_SPACE]:
            space_pressed = False
    #Пропущенные бутылки
        for i in range(len(bottles)):
            if bottles[i].place[0] < 175:
                bottles[i].place = (-200, 0)
                lives -= 1
        if not lives:
            being_lost = True
            lost = True
#Апдэйт
    pygame.display.update()
    clock.tick(60)
