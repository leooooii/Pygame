# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame

from source import Setting
from source import Player
from source import BackDrop



pygame.init()
pygame.display.set_mode((Setting.Width, Setting.Height))# set the Width and Height
pygame.display.set_caption("Christmas Adventure")# set the game's name
screen=pygame.display.get_surface()#set the screen

menu=Setting.Menu()


def check_event(screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # check quit
            pygame.quit()
    framerate.tick(100)# set the png play rate,update the png,make the animation
    ticks = pygame.time.get_ticks()#get the time
    for event in pygame.event.get():  #check quit
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == Player.add_bomb: #check the  event to add_bomb(this is a userevent)
            Player.bombs.append(Player.bomb())#if get the event, add bomb in the list of bombs

        if event.type ==Player.add_medicine:#check the  event to add_medicine(this is a userevent)
            Player.medicines.append(Player.medicine())#if get the event, add medicine in the list of medicines

    key = pygame.key.get_pressed()
    group.remove(PlayR, PlayL)#remove moveLeft animation and  moveRight animation

    if key[pygame.K_RIGHT]:
        if (Player.player_v <= 0):
            Player.player_v = 0
        Player.player_v += 0.05 # add the velocity of player
        Player.player_move() #update the player posX
        PlayR.Posx = Player.player_x # let the MoveRight animation on the player position
        PlayR.load() # update the current rect
        group.add(PlayR)  #add the MoveRight animation
    elif key[pygame.K_LEFT]:
        if( Player.player_v>=0):
            Player.player_v=0
        Player.player_v -= 0.05 # minus the velocity of player
        Player.player_move()   # update the player posX
        PlayL.Posx = Player.player_x # let the MoveLeft animation on the player position
        PlayL.load()# update the current rect
        group.add(PlayL) #add the MoveLeft animation
    else:
        screen.blit(Player.player, (Player.player_x, Player.player_y)) #add the stand image of player

    if (group):
        group.update(ticks)  #update the frame
        group.draw(screen) #draw the image





Section=True
while True:

    while(Section):# whether in the first section(menu)

        if(menu.update(screen, Player.HighScore)==False): #update the menu
            Section=False
        pygame.display.flip()


    Player.CreateSanta_Claus(screen)            #Initialize the CreateSanta_Claus
    framerate = pygame.time.Clock()              #Initialize the framerate
    group = pygame.sprite.Group()                #Initialize the sprite Group
    PlayR = Player.CreatePlayr(screen,Player.playerR_image,77.5, 80,4)   #Initialize the MoveRight animation
    PlayL = Player.CreatePlayr(screen,Player.playerL_image,77, 80,4)    #Initialize the MoveLeft animation

    flag=True         #check whether user pause the game
    BackDrop.score=0  #reset the score

    while Section==False: # if in the main game section

        while flag:    #check whether user pause the game

            screen.blit(Setting.img, (0, 0)) #set the backGround
            screen.blit(Setting.Numberscript, (350, 10)) #set the numebr script
            screen.blit(Setting.Backscript, (320, 5))#set the back button
            screen.blit(Setting.Pausescript, (290, 0.8))#set the Pause button
            screen.blit(Setting.Playscript, (260, 0.8))#set the play button

            if(Setting.checkback()!=True): #check whether user back to the menu
                Section=True
                break

            if(Setting.checkpause()!=True):#check whether user pause the game
                flag =False


            if (Player.life == 1):   #if life =1,show one heart
                screen.blit(Setting.Lifescript1, (0, 0))
            if (Player.life == 2): #if life =2,show two heart
                screen.blit(Setting.Lifescript1, (0, 0))
                screen.blit(Setting.Lifescript1, (30, 0))
            if (Player.life == 3): #if life =3,show three heart
                screen.blit(Setting.Lifescript1, (0, 0))
                screen.blit(Setting.Lifescript1, (30, 0))
                screen.blit(Setting.Lifescript1, (60, 0))

            Player.show_bombs(screen)       #show the bombs
            Player.show_medicine(screen)    #show the medicines
            Player.hurt(screen)             #check whether catch the bombs
            Player.addLife(screen)          #check whether catch the medicines
            check_event(screen)             #check player's move
            Player.Santa_Claus.display()    #show the Santa_Claus
            Player.Santa_Claus.move()       #move the Santa_Claus
            Player.Santa_Claus.downgifts()   #Santa_Claus  drops the gifts
            Player.Santa_Claus.count(Player.player_x, Player.player_y) #check whether catch the gifts
            Player.message_diaplay(BackDrop.score, screen, 410, 8.9)   #show the score


            pygame.display.flip()

        while not flag:
            if (Setting.checkback() != True): #check whether user back to the meau
                Section = True
                Setting.mymusic.play()
                break
            if (Setting.checkplay() == False): #check whether recover the game
                flag = True

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()