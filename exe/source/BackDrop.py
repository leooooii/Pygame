import pygame
import random
import pygame.font
from pygame.locals import *
from source import Player
from source import Setting


score = 0


class Santa_Claus:
    def __init__(self, screen):
        # 设置云朵的方向
        self.direction = 'right'
        # 云朵的默认位置
        self.x = 0
        self.y = 0
        self.screen = screen
        self.ImageName = "resources/leftM.png"
        self.image = pygame.image.load(self.ImageName)
        self.image = pygame.transform.scale(self.image, (int(Setting.Width * 0.4), int(Setting.Height * 0.22)))

        # 存放金币的信息
        self.giftslist = []

    def display(self):
        # 显示云朵的信息
        self.screen.blit(self.image, (self.x, self.y))
        # 金币的展示模式（掉落消失）
        giftsDelList = []
        for item in self.giftslist:
            if item.judge():
               # giftsDelList.append(item)
                pass
            pass
        # 重新遍历一次
        for i in giftsDelList:
            self.giftslist.remove(i)
            pass
        for coin in self.giftslist:
            coin.display()  # 显示金币的位置
            coin.move()

    def downgifts(self):
        num = random.randint(1, 100)
        if num == 3:
            newgifts = Gift(self.x, self.y, self.screen)
            self.giftslist.append(newgifts)

    def move(self):
        if self.direction == 'right':
            self.x += 1

        elif self.direction == 'left':
            self.x -= 1

        if self.x > Setting.Width-self.image.get_rect()[2]:
            self.direction = 'left'
            self.image = pygame.image.load("resources/rightM.png")
            self.image = pygame.transform.scale(self.image, (int(Setting.Width * 0.4), int(Setting.Height * 0.22)))
        elif self.x < 0:
            self.direction = 'right'
            self.image = pygame.image.load("resources/leftM.png")
            self.image = pygame.transform.scale(self.image, (int(Setting.Width * 0.4), int(Setting.Height * 0.22)))

    def count(self, player_x, player_y):
        global score
        for c in self.giftslist:
            if Player.collide_check(player_x, player_y, c.x, c.y, c.Giftimage) < 30:
                Setting.giftsound()
                score += 1
                #self.giftslist = self.giftslist[1:]
                c.x = self.x
                c.y = self.y

    def clear(self):
        self.giftslist.clear()


class Gift(object):
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y + 10
        self.screen = screen
        self.Giftimage = pygame.image.load("resources/gift.png")
        self.Giftimage = pygame.transform.scale(self.Giftimage, (int(Setting.Width * 0.07), int(Setting.Height * 0.05)))
        pass

    def display(self):
        self.screen.blit(self.Giftimage, (self.x, self.y))
        pass

    def move(self):
        self.y += 2
        pass

    def judge(self):
        if self.y > Setting.Height:
            return True
        else:
            return False
        pass

    pass





