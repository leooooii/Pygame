import pygame
import random
import pygame.font
from pygame.locals import *
from source import Player
from source import Setting


score = 0


class Santa_Claus:
    def __init__(self, screen):
        # set the direction of Santa_Claus
        self.direction = 'right'
        # reset the position of Santa_Claus
        self.x = 0
        self.y = 0
        self.screen = screen
        self.ImageName = "resources/leftM.png"
        self.image = pygame.image.load(self.ImageName)
        self.image = pygame.transform.scale(self.image, (int(Setting.Width * 0.4), int(Setting.Height * 0.22)))

        # store the gifts
        self.giftslist = []

    def display(self):
        # show the gifts
        self.screen.blit(self.image, (self.x, self.y))
        giftsDelList = []
        #  go through the list
        for i in giftsDelList:
            self.giftslist.remove(i)
            pass
        for coin in self.giftslist:
            coin.display()  # show the gifts
            coin.move()

    def downgifts(self):
        num = random.randint(1, 100)
        if num == 3:
            newgifts = Gift(self.x, self.y, self.screen)
            self.giftslist.append(newgifts) #add the gifts

    def move(self):
        if self.direction == 'right':
            self.x += 1 #update the position of Santa_Claus,move right

        elif self.direction == 'left':
            self.x -= 1#update the position of Santa_Claus,move left

        if self.x > Setting.Width-self.image.get_rect()[2]:
            self.direction = 'left'
            self.image = pygame.image.load("resources/rightM.png")#if change the direction, change the image
            self.image = pygame.transform.scale(self.image, (int(Setting.Width * 0.4), int(Setting.Height * 0.22)))
        elif self.x < 0:
            self.direction = 'right'
            self.image = pygame.image.load("resources/leftM.png")#if change the direction, change the image
            self.image = pygame.transform.scale(self.image, (int(Setting.Width * 0.4), int(Setting.Height * 0.22)))

    def count(self, player_x, player_y):
        global score
        for c in self.giftslist:
            if Player.collide_check(player_x, player_y, c.x, c.y, c.Giftimage) < 30: #check whether player catch the gifts
                Setting.giftsound()
                score += 1 #if catch the gifts, add the score
                c.x = self.x
                c.y = self.y

    def clear(self):
        self.giftslist.clear()  #clear the list


class Gift(object):
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y +  random.randint(25, 35) #radomly set the gifts' position Y,
        self.screen = screen
        self.Giftimage = pygame.image.load("resources/gift.png")#load the gift image
        self.Giftimage = pygame.transform.scale(self.Giftimage, (int(Setting.Width * 0.07), int(Setting.Height * 0.05)))

    def display(self):
        self.screen.blit(self.Giftimage, (self.x, self.y)) #show the gifts

    def move(self):  #update the position of gifts
        self.y += 2
