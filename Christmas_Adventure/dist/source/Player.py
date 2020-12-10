import pygame
import random
import math
from source import Setting
from source import BackDrop


player = pygame.image.load("resources/Girl.png")
playerL_image = pygame.image.load("resources/playerMoveL.png")
playerR_image = pygame.image.load("resources/playerMoveR.png")
player_x = 140  # the initial position of player
player_y = Setting.Height - 80
player_v = 0  # the initial velocity of player

HighScore=0


class CreatePlayr(pygame.sprite.Sprite):#inherit the init of Sprite to create the player
    def __init__(self, screen,image,width,height,columns):
      pygame.sprite.Sprite.__init__(self)#inherit the init of Sprite to create the player
      self.image = None  #set the current frame image
      self.Fullimage = image  #store the full image of animation
      self.rect = None        #set the image position ,width and height
      self.Currentframe = 0   #store the current frame
      self.Preframe = -1      #store the pervious frame
      self.frame_width = width    #store  each frame's width
      self.frame_height = height  #store  each frame's width
      self.first_frame = 0        #store the index of first frame
      self.last_frame = columns-1  #store the index of last frame
      self.columns = columns     #store the columns of animation frams
      self.last_time = 0         #store the last time of animation
      self.Posx=0                #store the x position of player

    def load(self):
        self.rect = self.Posx, Setting.Height - player.get_rect()[3],  self.frame_width, self.frame_height #update the animation's position


    def update(self, current_time, rate=100): #update the animation frame
        if current_time > self.last_time + rate:   # if time beyond the setted period,than change the frame
            self.Currentframe += 1                 # change the frame
            if self.Currentframe > self.last_frame:  # if move to the last frame, move back to the first one
                self.Currentframe = self.first_frame
            self.last_time = current_time          #store the last time

        if self.Currentframe != self.Preframe:     #if index of frame changed
            frame_x = (self.Currentframe % self.columns) * self.frame_width  #store the current frame's positionX in the fullimage
            frame_y = 0  #because player's always same, always set 0
            rect = ( frame_x, 0, self.frame_width, self.frame_height ) #update the current frame's position
            self.image = self.Fullimage.subsurface(rect) #cut the current frame image
            self.Preframe = self.Currentframe #store the current frame




def message_diaplay(text,screen,x,y):
    largeText = pygame.font.Font('resources/font.ttf', 16)
    text=str(text)
    textSurface = largeText.render(text, True, (255,255,255))
    screen.blit(textSurface, (x,y))



class bomb :  # define a class to produce bomb

    def __init__(self):
        self.Img = pygame.image.load("resources/boom.png")
        self.x = random.randint(0, Setting.Width - self.Img.get_rect()[2])    #the position of bomb
        self.y = 5
        self.v = random.randint(1, 3)   #the velocity of bomb,which is a random value


def show_bombs(screen):  # show bombs in the screen
    global  bombs
    if(bombs):
        for b in bombs: #check each bomb to show
            screen.blit(b.Img, (b.x, b.y))
            b.y += b.v  #make the bomb drop


class medicine: #define a class to produce medicine
    def __init__(self):
        self.Img=pygame.image.load("resources/items/power1.png")
        self.Img=pygame.transform.scale(self.Img, (int(Setting.Width * 0.09), int(Setting.Height * 0.06)))
        self.x = random.randint(0, Setting.Width - self.Img.get_rect()[2])  # the position of medicine
        self.y = 5
        self.v = random.randint(2, 4) #the velocity of bomb,which is a random value

def show_medicine(screen):  # show medicines in the screen
    global  medicines
    if(medicines):
        for m in medicines: #check each medicine to show
            screen.blit(m.Img, (m.x, m.y))
            m.y += m.v  #make the medicines drop


def player_move():  # move the player
    global player_x, player_v,player
    player_x += player_v  #update the position by adding the velocity
    if player_x > Setting.Width-player.get_rect()[2]:   # check whether the player is out of screen
        player_x = Setting.Width - player.get_rect()[2]
    if player_x < 0:# check whether the player is out of screen
        player_x = 0


#use a set_timer function to show bombs/medicine every once in a while
add_bomb = pygame.USEREVENT #add the event of add_bomb
pygame.time.set_timer(add_bomb,800)#set the time
bombs=[]

add_medicine = pygame.USEREVENT+1# the same way to show medicine
pygame.time.set_timer(add_medicine,2000)#set the time,the time is longer than add_bomb,becaure we don't want to many medicines
medicines=[]

def collide_check(pla_x,pla_y,bomb_x,bomb_y,image): #calculate the distance between player and bomb
    global player
    pla_x+=player.get_rect()[2]/2       #calculate the player's center point of the x-axis
    pla_y += player.get_rect()[3] / 2   #calculate the player's center point of the y-axis
    bomb_x += image.get_rect()[2] / 2   #calculate the object's center point of the x-axis
    bomb_y += image.get_rect()[3] / 2   #calculate the object's center point of the x-axis
    return int(math.sqrt((pla_x - bomb_x)*(pla_x - bomb_x)+(pla_y - bomb_y)*(pla_y - bomb_y)))
    #use a mathematical formula to calculate the distance of center point between player and object

life = 3  #the value of life



pause=True

def paused(screen):# if game over stop the game
    global pause,HighScore
    pause = True
    while pause:
        for event in pygame.event.get():
            screen.blit(Setting.img, (0, 0))
            screen.blit(Setting.Playscript, (260, 0.8))#reset the backGround
            screen.blit(Setting.Overscript, (Setting.Width / 2 - 80, Setting.Height / 2 - 200)) #show the title of game over

            screen.blit(Setting.PlayerBoardscript,
                        (Setting.Width / 2 - Setting.PlayerBoardscript.get_rect()[2] / 2, 350))#show the score board
            largeText = pygame.font.Font('resources/font.ttf', 30)
            text = str(BackDrop.score)
            textSurface = largeText.render(text, True, (0, 0, 0))
            screen.blit(textSurface, (Setting.Width / 2, 420))  #show the score

            bombs.clear()  #clear the bomb
            medicines.clear() #clear the medicines
            Santa_Claus.clear() #clear gifts
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if (Setting.checkplay() == False): #RESTART the game
                pause=False
            pygame.display.flip()


def addLife(screen): #life =3 , if catch bomb than life -1
    global player_x, player_y, life
    for m in medicines:
        m.v+=0.02
        if collide_check(player_x,player_y,m.x,m.y,m.Img) < 30:#if the distance between the player and medicine <30, the program regard as the player catch the medicine
            m.x = random.randint(0,360) #reset the medicine
            m.y = 5
            m.v = random.randint(1,3)
            Setting.addlifesound() #play the sound
            if(life<3): # the life won't >3
                life += 1


def hurt(screen): #set the life=3, get bomb 1 time then life-1, when life=0, game is over
    global player_x,player_y,life,HighScore,HardMode

    for b in bombs:
        b.v +=0.05
        if collide_check(player_x,player_y,b.x,b.y,b.Img) < 30: #if the distance between the player and bomb <30, the program regard as the player catch the bomb
            b.x = random.randint(0,360) #reset the bomb
            b.y = 5
            b.v = random.randint(1,3)
            life -= 1
            Setting.bombsound()#play the bombsound
            if life == 0:
                Setting.diesound()#play the game over sound
                if (HighScore < BackDrop.score):#store the highest score
                    HighScore = BackDrop.score
                Setting.mymusic.stop() #stop the music
                paused(screen)   #stop the game
                BackDrop.score=0 #reset the score
                life=3  #reset the life




Santa_Claus=[]
def CreateSanta_Claus(screen):  #Create the Santa_Claus to drop things
    global Santa_Claus
    Santa_Claus = BackDrop.Santa_Claus(screen)