import pygame
import time
import random


pygame.init()


display_w=800
display_h=600




black=(0,0,0)
background=(29,148,248)
pink=(190,0,110)
red=(218,59,59)
red1=(251,30,30)
bright_yellow=(255,150,0)
blue=(0,0,200)
green=(0,200,0)
bright_green=(0,255,0)
yellow=(250,242,13)
pink=(241,106,173)
purple=(217,12,210)
orange=(250,153,100)
light_green=(122,243,90)


game=pygame.display.set_mode((display_w,display_h))
pygame.display.set_caption("run minion")

fail_sound = pygame.mixer.Sound("lose-m.wav")
pygame.mixer.music.load("world-m.ogg")
paly_sound=pygame.mixer.Sound("world-m.ogg")
android_img=pygame.image.load("android1.png")
background1=pygame.image.load("tappeh.png")
background3=pygame.image.load("background3.png")
moshak=pygame.image.load("moshak.png")
moshak=pygame.transform.scale(moshak,(200,200))


game.blit(background3,(0,0))
game.blit(background1,(0,0))
clock=pygame.time.Clock()
and_w=40


def android(x,y):
       game.blit(android_img,(x,y))




def stop():
       pygame.mixer.music.stop() 
def play_again():
       pygame.mixer.Sound.play(paly_sound)





def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(game,ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(game,ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    TextSurf,TextRect = text_obj(msg,smallText)
    TextRect.center = ((x+(w/2)),(y + (h/2)))
    game.blit(TextSurf,TextRect)




def quitgame():
    pygame.quit()
    quit()






def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        game.fill(background)
        largeText = pygame.font.Font('freesansbold.ttf',90)
        TextSurf, TextRect = text_obj("are you ready??",largeText)
        TextRect.center = ((display_w/2),(display_h/2))
        game.blit(TextSurf,TextRect)
        button("play",350,450,100,50,green,bright_green,game_loop)
        button("Quit",350,550,100,50,yellow,bright_yellow,quitgame)
        pygame.display.update()





def stuff_dodged(count):
    font = pygame.font.SysFont(None , 25)
    text = font.render("score : "+str(count) , True , red)
    game.blit(text,(0,0))





def stuff(stuffx,stuffy):
    game.blit(background3,(0,0))
    game.blit(background1,(0,0))
    game.blit(moshak,(stuffx,stuffy))






def text_obj(text,font):
    textSurface = font.render(text, True , black)
    return textSurface, textSurface.get_rect()





def message_display(text):
    f = pygame.font.Font('freesansbold.ttf',90)
    TextSurf, TextRect = text_obj(text,f)
    TextRect.center = ((display_w/2),(display_h/2))
    game.blit(TextSurf,TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()




    
def crash(score):
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(fail_sound)
    game.fill(red1)
    file=open("score.txt","a")
    file.write("score:") 
    file.write(str(score))
    file.write("\n")
    file.close()
    largeText = pygame.font.Font('freesansbold.ttf',90)
    TextSurf, TextRect = text_obj("You Crashed",largeText)
    TextRect.center = ((display_w/2),(display_h/2))
    game.blit(TextSurf,TextRect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    

        button("Play!!",350,450,100,50,green,bright_green,game_loop)
        button("Quit",350,550,100,50,yellow,bright_yellow,quitgame)  

        pygame.display.update()





def game_loop():
    pygame.mixer.music.play(-1)

    
    x = (display_w * 0.45)
    y = (display_h * 0.74)   

    x_change = 0
    stuff_startx = random.randrange(0,display_w)
    stuff_starty = -700
    stuff_speed = 3
    stuff_width =120
    stuff_height =170


    score=0
    
    gameExit = False
    while not gameExit:
       for event in pygame.event.get():
              if event.type==pygame.QUIT:
                     pygame.quit()
                     quit()
              if event.type==pygame.KEYDOWN:
                     if event.key==pygame.K_LEFT:
                            x_change=-5
                     elif event.key==pygame.K_RIGHT:
                            x_change=5
              if event.type==pygame.KEYUP:
                     if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                            x_change=0
       x=x+x_change
       
       stuff(stuff_startx,stuff_starty)
       stuff_starty += stuff_speed
       stuff_dodged(score)
       android(x,y)
       button("stop",0,20,45,35,orange,light_green,stop)
       button("play",0,58,45,35,orange,light_green,play_again)
       if x>display_w-and_w or x<0:
              crash(score)
       if stuff_starty > display_h:
            stuff_starty = 0 - stuff_height
            stuff_startx = random.randrange(0,display_w)
            score += 1
            stuff_speed += 1
       if y < stuff_starty + stuff_height:
            if x > stuff_startx and x < stuff_startx + stuff_width or x + and_w > stuff_startx and x + and_w < stuff_startx + stuff_width:
                crash(score)    

       pygame.display.update()
       clock.tick(60)


game_intro()
game_loop()
pygame.quit()
quit()
