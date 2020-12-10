import pygame
import random
import math
from source import Setting
from source import BackDrop


player = pygame.image.load("resources/Girl.png")

player_x = 140  # the initial position of player
player_y = Setting.Height - 80
player_v = 0  # the initial velocity of player

boom_num = 3
HighScore=0


class MySprite(pygame.sprite.Sprite):
    def __init__(self, target):
      pygame.sprite.Sprite.__init__(self) #基类的init方法
      self.image = None
      self.master_image = None
      self.rect = None
      self.frame = 0
      self.old_frame = -1
      self.frame_width = 1
      self.frame_height = 1
      self.first_frame = 0
      self.last_frame = 0
      self.columns = 1
      self.last_time = 0
      self.Posx=0

    def load(self, filename, width, height, columns):
        self.master_image = pygame.image.load(filename).convert_alpha()
        self.frame_width = width
        self.frame_height = height
        self.rect = self.Posx, Setting.Height - 80, width, height
        self.columns = columns
        rect = self.master_image.get_rect()
        self.last_frame = (rect.width // width) * (rect.height // height) - 1

    def update(self, current_time, rate=100):
     #更新动画帧
        if current_time > self.last_time + rate:
            self.frame += 1
            if self.frame > self.last_frame:
                self.frame = self.first_frame
            self.last_time = current_time

        if self.frame != self.old_frame:
            frame_x = (self.frame % self.columns) * self.frame_width
            frame_y = (self.frame // self.columns) * self.frame_height
            rect = ( frame_x, frame_y, self.frame_width, self.frame_height )
            self.image = self.master_image.subsurface(rect)
            self.old_frame = self.frame




def message_diaplay(text,screen,x,y):
    largeText = pygame.font.Font('resources/font.ttf', 16)
    text=str(text)
    textSurface = largeText.render(text, True, (255,255,255))
    screen.blit(textSurface, (x,y))



class boom :  # define a class to produce boom

    def __init__(self):
        self.Img = pygame.image.load("resources/boom.png")
        self.x = random.randint(0, Setting.Width - self.Img.get_rect()[2])    #the position of boom
        self.y = 5
        self.v = random.randint(1, 3)   #the velocity of boom


def show_booms(screen):  # show booms in the screen
    global  booms
    if(booms):
        for b in booms: #check each boom to show
            screen.blit(b.Img, (b.x, b.y))
            b.y += b.v  #make the boom drop
            if b.y > Setting.Height: # if the boom is out of screen,remove it
                #booms = booms[1:]
                pass

class medicine:
    def __init__(self):
        self.Img=pygame.image.load("resources/items/power1.png")
        self.Img=pygame.transform.scale(self.Img, (int(Setting.Width * 0.09), int(Setting.Height * 0.06)))
        self.x = random.randint(0, Setting.Width - self.Img.get_rect()[2])  # the position of medicine
        self.y = 5
        self.v = random.randint(2, 4)  # the velocity of medicine

def show_medicine(screen):  # show booms in the screen
    global  medicines
    if(medicines):
        for m in medicines: #check each boom to show
            screen.blit(m.Img, (m.x, m.y))
            m.y += m.v  #make the boom drop
            if m.y > Setting.Height: # if the boom is out of screen,remove it
                #booms = booms[1:]
                pass


def player_move():  # move the player
    global player_x, player_v,player
    player_x += player_v
    if player_x > Setting.Width-player.get_rect()[2]:   # check whether the player is out of screen
        player_x = Setting.Width - player.get_rect()[2]
    if player_x < 0:
        player_x = 0



add_boom = pygame.USEREVENT
pygame.time.set_timer(add_boom,800)
booms=[]

add_medicine = pygame.USEREVENT+1
pygame.time.set_timer(add_medicine,2000)
medicines=[]

def collide_check(pla_x,pla_y,boom_x,boom_y,image): #calculate the distance between player and boom
    global player
    pla_x+=player.get_rect()[2]/2
    pla_y += player.get_rect()[3] / 2
    boom_x += image.get_rect()[2] / 2
    boom_y += image.get_rect()[3] / 2
    return int(math.sqrt((pla_x - boom_x)*(pla_x - boom_x)+(pla_y - boom_y)*(pla_y - boom_y)))

life = 3

def addLife(screen):
    global player_x, player_y, life
    for m in medicines:
        m.v+=0.05
        if collide_check(player_x,player_y,m.x,m.y,m.Img) < 30:
            m.x = random.randint(0,360)
            m.y = 5
            m.v = random.randint(1,3)
            Setting.addlifesound()
            if(life<3):
                life += 1

pause=True

def paused(screen):
    global pause,HighScore
    pause = True
    while pause:
        for event in pygame.event.get():
            screen.blit(Setting.img, (0, 0))
            screen.blit(Setting.Playscript, (260, 0.8))
            screen.blit(Setting.Overscript, (Setting.Width / 2 - 80, Setting.Height / 2 - 200))

            screen.blit(Setting.PlayerBoardscript,
                        (Setting.Width / 2 - Setting.PlayerBoardscript.get_rect()[2] / 2, 350))
            largeText = pygame.font.Font('resources/font.ttf', 30)
            text = str(BackDrop.score)
            textSurface = largeText.render(text, True, (0, 0, 0))
            screen.blit(textSurface, (Setting.Width / 2, 420))

            booms.clear()
            medicines.clear()
            Santa_Claus.clear()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if (Setting.checkplay() == False):
                pause=False
            pygame.display.flip()


def hurt(screen): #set the life=3, get boom 1 time then life-1, when time=0, game is over
    global player_x,player_y,life,HighScore,HardMode

    for b in booms:
        b.v +=0.1
        if collide_check(player_x,player_y,b.x,b.y,b.Img) < 30:
            b.x = random.randint(0,360)
            b.y = 5
            b.v = random.randint(1,3)
            life -= 1
            Setting.boomsound()
            if life == 0:
                Setting.diesound()

                if (HighScore < BackDrop.score):
                    HighScore = BackDrop.score
                Setting.mymusic.stop()
                paused(screen)

                BackDrop.score=0
                life=3


class MovePlayer:
    def __init__(self,screen):
        self.PlayR = MySprite(screen)
        self.PlayL = MySprite(screen)
        self.screen=screen


    def update(self):
        self.PlayR = MySprite( self.screen)
        self.PlayR.load("resources/playerMoveR.png", 31, 32, 4)
        self.PlayR.Posx=player_x
        self.PlayL = MySprite( self.screen)
        self.PlayL.load("resources/playerMoveL.png", 31, 32, 4)
        self.PlayL.Posx = player_x




Santa_Claus=[]
def CreateSanta_Claus(screen):
    global Santa_Claus
    Santa_Claus = BackDrop.Santa_Claus(screen)