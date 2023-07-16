import pygame
from pygame import mixer
import random

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()

# settings:
screen_size = 1000, 600
velocity=3
direction="r"
direction2="r"
lose=False
flower=False
volume = 1.0 #music volume
font = pygame.font.Font('freesansbold.ttf', 32)

display_surface = pygame.display.set_mode(screen_size)
level = list()
level = [0] * 61
for i in range(61):
    level[i] = [0] * 100
block_size = 10

# TODO: Load a new image for the ground
# TODO: Resize the image to block_size x block_size

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
playing = True

player1_coord = [10,10]
player1_length = 1
player2_coord = [50,50]
player2_length = 1
apple = [11,11]
level[apple[0]][apple[1]]=3
level[player1_coord[1]][player1_coord[0]]=1
level[player2_coord[0]][player2_coord[1]]=2

text = font.render("First player: 0", True, (0, 255, 0), (0, 0, 128))
textRect = text.get_rect()
textRect.center = (150,570)
text2 = font.render("Second player: 0", True, (0, 255, 0), (0, 0, 128))
text2Rect = text.get_rect()
text2Rect.center = (800,570)
#load all sounds
pygame.mixer.music.set_volume(volume)
#background_music = pygame.mixer.music.load("D:\Codes\snake\mus.wav")
#coin_take = pygame.mixer.Sound("D:\Codes\gamedev\coin.wav")
#bonus = pygame.mixer.Sound("D:\Codes\snake\bonus.wav")
#pygame.mixer.music.play(-1)

apples = list()
for i in range(len(level)):
    for j in range(len(level[i])):
        if level[i][j] == 3:
            apples.append(
                pygame.Rect((j * block_size, i * block_size, block_size, block_size)),
            )
player1 = []
player2 = []
# now, while that variable is still True...
while playing:
    while(not lose):
        # all types of user interaction
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    playing = False
                    lose=True
                    break
                if event.key == pygame.K_UP and direction!="down":
                    direction="up"
                if event.key == pygame.K_RIGHT and direction!="left":
                    direction="right"
                if event.key == pygame.K_LEFT and direction!="right":
                    direction="left"
                if event.key == pygame.K_DOWN and direction!="up":
                    direction="down"


                if event.key == pygame.K_w and direction2!="down":
                    direction2="up"
                if event.key == pygame.K_d and direction2!="left":
                    direction2="right"
                if event.key == pygame.K_a and direction2!="right":
                    direction2="left"
                if event.key == pygame.K_s and direction2!="up":
                    direction2="down"

        pygame.time.wait(int(600/velocity))

        if(player1_coord[0]+1>100 or player1_coord[0]-1<0 or player1_coord[1]+1>60 or player1_coord[1]-1<0):
            lose=True
        if(player2_coord[0]+1>101 or player2_coord[0]-1<0 or player2_coord[1]+1>60 or player2_coord[1]-1<0):#two statements instead of one to increase readability
            lose=True
        

        if(direction=="up"):
            level[player1_coord[1]][player1_coord[0]]=0
            player1_coord[1]=player1_coord[1]-1
        elif(direction=="down"):
            level[player1_coord[1]][player1_coord[0]]=0
            player1_coord[1]=  player1_coord[1]+1
        elif(direction=="left"):
            level[player1_coord[1]][player1_coord[0]]=0
            player1_coord[0]= player1_coord[0]-1
        elif(direction=="right"):
            level[player1_coord[1]][player1_coord[0]]=0
            player1_coord[0]= player1_coord[0]+1
        
        if(direction2=="up"):
            level[player2_coord[1]][player2_coord[0]]=0
            player2_coord[1]=player2_coord[1]-1
        elif(direction2=="down"):
            level[player2_coord[1]][player2_coord[0]]=0
            player2_coord[1]=  player2_coord[1]+1
        elif(direction2=="left"):
            level[player2_coord[1]][player2_coord[0]]=0
            player2_coord[0]= player2_coord[0]-1
        elif(direction2=="right"):
            level[player2_coord[1]][player2_coord[0]]=0
            player2_coord[0]= player2_coord[0]+1
        
        if(player1_coord==apple):
            #coin_take.play()
            velocity=velocity+0.2
            if(flower):
                player1_length=player1_length+3
                flower=False
            else:
                player1_length=player1_length+1
            level[apple[0]][apple[1]]=0
            if(random.randint(1,5)==1):
                flower=True
            apple = [random.randint(1,50),random.randint(1,50)]
        

        if(player2_coord==apple):
            #coin_take.play()
            velocity=velocity+0.2
            if(flower):
                player2_length=player2_length+3
                flower=False
            else:
                player2_length=player2_length+1
            level[apple[0]][apple[1]]=0
            if(random.randint(1,5)==1):
                flower=True
            apple = [random.randint(1,50),random.randint(1,50)]
            
        level[apple[1]][apple[0]]=3

        screen.fill((255, 255, 255))
        
        head=[]
        head2=[]
        head.append(player1_coord[0])
        head.append(player1_coord[1])
        head2.append(player2_coord[0])
        head2.append(player2_coord[1])
        player1.append(head)
        player2.append(head2)
        if len(player1) > player1_length:
                del player1[0]
        if len(player2) > player2_length:
                del player2[0]
        for x in player1[:-1]:
            if x == head:
                lose = True
        for x in player2[:-1]:
            if x == head2:
                lose = True

        for x in player1:
            pygame.draw.rect(screen, (255, 100, 100), [x[0]*block_size, x[1]*block_size, block_size, block_size])
        for x in player2:
            pygame.draw.rect(screen, (0, 255, 0), [x[0]*block_size, x[1]*block_size, block_size, block_size])


        text = font.render("First player: "+str(player1_length), True, (0, 255, 0), (0, 0, 128))
        text2 = font.render("Second player: "+str(player2_length), True, (0, 255, 0), (0, 0, 128))
        display_surface.blit(text, textRect)
        display_surface.blit(text2, text2Rect)
        
        for i in range(len(level)):
            for j in range(len(level[i])):
                if level[i][j] == 1:
                    # TODO: blit the ground at coordinates j*block_size, i*block_size
                    pygame.draw.rect(
                        screen,
                        (255, 100, 100),
                        (j*block_size, i*block_size, block_size, block_size),
                    )
                if level[i][j] == 2:
                    # TODO: blit the ground at coordinates j*block_size, i*block_size
                    pygame.draw.rect(
                        screen,
                        (0, 255, 0),
                        (j*block_size, i*block_size, block_size, block_size),
                    )
                if level[i][j] == 3:
                    # TODO: blit the ground at coordinates j*block_size, i*block_size
                    if(flower):
                        pygame.draw.circle(screen, (255, 200, 0), (j*block_size+5, i*block_size+5), 5)
                    else:
                        pygame.draw.circle(screen, (255, 0, 0), (j*block_size+5, i*block_size+5), 5)

        pygame.display.flip()
        pygame.display.update()
        # wait 1/20 of a second
        clock.tick(20)

    if(player1_length>player2_length):
        text = font.render("Game over first player won! Length: "+str(player1_length), True, (0, 255, 0), (0, 0, 128))
    elif(player1_length<player2_length):
        text = font.render("Game over second player won! Length: "+str(player2_length), True, (0, 255, 0), (0, 0, 128))
    elif(player1_length==player2_length):
        text = font.render("Game over and it is a draw! Length: "+str(player2_length), True, (0, 255, 0), (0, 0, 128))    
    textRect = text.get_rect()
    textRect.center = (screen_size[0]/2,screen_size[1]/2)
    display_surface.blit(text, textRect)
    pygame.display.flip()
    pygame.display.update()
        # wait 1/20 of a second
    clock.tick(20)
    pygame.time.wait(int(2000))
    pygame.quit()

# quit the game when we are out of the cycle
pygame.quit()
