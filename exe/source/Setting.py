import pygame



Width=460
Height=640
Volume=0.3



img = pygame.image.load("resources/merryChristmasBg.png")
img=pygame.transform.scale(img, (int(Width*1.0), int(Height*1)))

MenuBg = pygame.image.load("resources/merryChristmas.png")
MenuBg=pygame.transform.scale(MenuBg, (int(Width), int(Height*1)))

#Title
Titlescript = pygame.image.load("resources/Button/title3.png")
Titlescript=pygame.transform.scale(Titlescript, (int(Width*0.6), int(Height*0.3)))

#icon of StartGame
Startscript1 = pygame.image.load("resources/Button/start1.png")
Startscript1=pygame.transform.scale(Startscript1, (int(Startscript1.get_rect()[2]), int(Startscript1.get_rect()[3])))
Startscript2 = pygame.image.load("resources/Button/start2.png")
Startscript2=pygame.transform.scale(Startscript2, (int(Startscript2.get_rect()[2]), int(Startscript2.get_rect()[3])))
#icon of Score
Scorescript1 = pygame.image.load("resources/Button/score1.png")
Scorescript1=pygame.transform.scale(Scorescript1, (int(Startscript2.get_rect()[2]), int(Startscript2.get_rect()[3])))
Scorescript2 = pygame.image.load("resources/Button/score2.png")
Scorescript2=pygame.transform.scale(Scorescript2, (int(Startscript2.get_rect()[2]), int(Startscript2.get_rect()[3])))

#icon of Exit
Exitscript1 = pygame.image.load("resources/Button/exit1.png")
Exitscript1=pygame.transform.scale(Exitscript1, (int(Exitscript1.get_rect()[2]), int(Exitscript1.get_rect()[3])))
Exitscript2 = pygame.image.load("resources/Button/exit2.png")
Exitscript2=pygame.transform.scale(Exitscript2,  (int(Exitscript2.get_rect()[2]), int(Exitscript2.get_rect()[3])))
#icon of sound
Soundscript1 = pygame.image.load("resources/Button/Louder.png")
Soundscript1=pygame.transform.scale(Soundscript1, (int(Width*0.07), int(Height*0.05)))
Soundscript2 = pygame.image.load("resources/Button/Mute.png")
Soundscript2=pygame.transform.scale(Soundscript2, (int(Width*0.07), int(Height*0.05)))
#icon of life
Lifescript1 = pygame.image.load("resources/items/power1.png")
Lifescript1=pygame.transform.scale(Lifescript1, (int(Width*0.09), int(Height*0.06)))
Lifescript2 = pygame.image.load("resources/items/power2.png")
Lifescript2=pygame.transform.scale(Lifescript2, (int(Width*0.18), int(Height*0.06)))
Lifescript3 = pygame.image.load("resources/items/power3.png")
Lifescript3=pygame.transform.scale(Lifescript3, (int(Width*0.27), int(Height*0.06)))

#icon of gameover
Overscript = pygame.image.load("resources/Button/gameover.png")
Overscript=pygame.transform.scale(Overscript, (int(Width*0.4), int(Height*0.3)))

#icon of Scorenumber
Numberscript = pygame.image.load("resources/items/Score.png")
Numberscript=pygame.transform.scale(Numberscript, (int(Width*0.12), int(Height*0.022)))

#icon of cursor
cursor=pygame.image.load("resources/Button/bell.png")
cursor=pygame.transform.scale(cursor, (int(Width*0.12), int(Height*0.08)))
#icon of back
Backscript=pygame.image.load("resources/Button/back.png")
Backscript=pygame.transform.scale(Backscript, (int(Width*0.06), int(Height*0.04)))
#icon of pause
Pausescript=pygame.image.load("resources/Button/pause.png")
Pausescript=pygame.transform.scale(Pausescript, (int(Width*0.08), int(Height*0.05)))
#icon of play
Playscript=pygame.image.load("resources/Button/play.png")
Playscript=pygame.transform.scale(Playscript, (int(Width*0.08), int(Height*0.05)))
#icon of scoreboard
Boardscript=pygame.image.load("resources/Button/scoreboard.png")
Boardscript=pygame.transform.scale(Boardscript, (int(Boardscript.get_rect()[2]*0.6), int(Boardscript.get_rect()[3]*0.6)))

#icon of playersocer
PlayerBoardscript=pygame.image.load("resources/Button/playersocer.png")
PlayerBoardscript=pygame.transform.scale(PlayerBoardscript, (int(PlayerBoardscript.get_rect()[2]*0.6), int(Boardscript.get_rect()[3]*0.7)))


def buttonsound():
    pygame.mixer.music.load("resources/bgm/buttonsound.mp3")
    pygame.mixer.music.play()

def giftsound():
    pygame.mixer.music.load("resources/bgm/coinsound.mp3")
    pygame.mixer.music.play()

def diesound():
    pygame.mixer.music.load("resources/bgm/diesound.mp3")
    pygame.mixer.music.play()

def boomsound():
    pygame.mixer.music.load("resources/bgm/boomsound.mp3")
    pygame.mixer.music.play()

def addlifesound():
    pygame.mixer.music.load("resources/bgm/addlife.mp3")
    pygame.mixer.music.play()

pygame.mixer.init()
pygame.mixer.music.set_volume(Volume)  # 设置音量的大小

mymusic = pygame.mixer.Sound("resources/bgm/Christmas.mp3")  # 加载音频文件
mymusic.set_volume(0.5)  # 加载的音量大小
mymusic.play(-1)  # 循环播放


def checkback():
    mouse_pos = pygame.mouse.get_pos()
    buttons = pygame.mouse.get_pressed()
    if mouse_pos[0] >= 321 and mouse_pos[0] <= 344 :
        if mouse_pos[1] >= 5 and mouse_pos[1] <= 26:
            if buttons[0]:
                print('s')
                return False

    return True



def checkpause():
    mouse_pos = pygame.mouse.get_pos()
    buttons = pygame.mouse.get_pressed()
    if mouse_pos[0] >= 293 and mouse_pos[0] <= 320 :
        if mouse_pos[1] >= 5 and mouse_pos[1] <= 27:
            if buttons[0]:
                mymusic.stop()
                return False
    return True




def checkplay():
    mouse_pos = pygame.mouse.get_pos()
    buttons = pygame.mouse.get_pressed()
    if mouse_pos[0] >= 263 and mouse_pos[0] <= 290 :
        if mouse_pos[1] >= 5 and mouse_pos[1] <= 27:
            if buttons[0]:
                mymusic.play(-1)
                return False
    return True




BoardPrint=True

class Menu:
    global Boardscript
    def __init__(self):
        self.setup_background()
        self.count=0
        self.volume=0.3


    def setup_background(self):
        self.background=pygame.transform.scale(MenuBg, (int(Width), int(Height*1)))


    def update(self,surface,Highscore):
        surface.blit(MenuBg, (0, 0))
        mouse_pos = pygame.mouse.get_pos()
        buttons = pygame.mouse.get_pressed()
        surface.blit(Titlescript, (90, 150))
        surface.blit(Startscript1, (130, 415))
        surface.blit(Scorescript1, (130, 460))
        surface.blit(Exitscript1, (130, 505))
        surface.blit(Soundscript1, (380, 10))
        surface.blit(Soundscript2, (420, 10))

        BoardPrint=True

        if mouse_pos[0] >= 130 and mouse_pos[0] <= 330 :
            if mouse_pos[1] >= 419 and mouse_pos[1] <= 457:
                surface.blit(Startscript2, (130, 415))
                scriptPose = Startscript2.get_rect()

                surface.blit(Scorescript1, (130, 460))
                surface.blit(Exitscript1, (130, 505))
                surface.blit(cursor, (85, 412))

                if buttons[0]:

                    buttonsound()
                    self.count = 1
                    return False

            elif  mouse_pos[1] >= 465 and mouse_pos[1] <= 503:
                surface.blit(Startscript1, (130, 415))
                scriptPose = Startscript2.get_rect()

                surface.blit(Boardscript, (Width/2-Boardscript.get_rect()[2]/2, 350))
                BoardPrint=False
                largeText = pygame.font.Font('resources/font.ttf', 30)
                text = str(Highscore)
                textSurface = largeText.render(text, True, (0, 0, 0))
                surface.blit(textSurface, (Width / 2, 460))

                if buttons[0]:
                    buttonsound()
                    self.count = 2
                    return False

            elif  mouse_pos[1] >= 511 and mouse_pos[1] <= 546:
                surface.blit(Startscript1, (130, 415))
                scriptPose = Startscript2.get_rect()

                surface.blit(Scorescript1, (130, 460))
                surface.blit(Exitscript2, (130, 505))
                surface.blit(cursor, (85, 502))

                if buttons[0]:
                    pygame.quit()
                    exit()

        if mouse_pos[1] >= 10 and mouse_pos[1] <= 45:
            if mouse_pos[0] >= 378 and mouse_pos[0] <= 411:
                if buttons[0]:
                    self.volume =0.5
                    mymusic.set_volume(self.volume)

            elif mouse_pos[0] >= 418 and mouse_pos[0] <= 451:
                if buttons[0]:
                    self.volume=0
                    mymusic.set_volume(self.volume)


        for newEvent in pygame.event.get():
            if newEvent.type == pygame.QUIT:
                pygame.quit()  # 卸载所有pygame模块
                exit()

        pygame.display.flip()



