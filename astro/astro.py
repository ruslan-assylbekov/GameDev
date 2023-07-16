#import ast
import pygame
import random
import math
######################   ФУНКЦИИ   ############################
def draw_objects():
    pygame.draw.lines(screen, WHITE, True,[point1, point2,point3])
    pygame.draw.circle(screen,WHITE,asteroid_coordinates,20)
    screen.blit(text.render('angle: '+ str(round(math.cos(angle-math.pi/2),4)),False, WHITE), (500, 520))
    screen.blit(text.render('breaks: '+ breaks,False, WHITE), (520, 560))
    screen.blit(text.render('engines: '+ engines,False, WHITE), (520, 570))
    screen.blit(text.render('velocity: '+str(round(velocity,3)),False, WHITE), (520, 580))
    
def check_collision(point1,point2,radius):
    if (point1[0]-point2[0])*(point1[0]-point2[0])+(point1[1]-point2[1])*(point1[1]-point2[1])<=radius**2:
        return True
######################   ПЕРЕМЕННЫЕ   ############################
pointO = (300,300)
point1 = (200,150)
point2 = (190,210)
point3 = (210,210)

angle=0
angle_velocity=0
velocity=0
fuel = 100

player_velocity=(0,0)
last_player_velocity=(0,0)
final_velocity=(0,0)
directions=(0,1)
last_directions=(0,1)
last_angle=0

asteroid_coordinates=random.randint(100,500),random.randint(100,500)

engines='OFF'
breaks='OFF'
left = False
right = False
forward = False
stop=False
####################   ЦВЕТА   ##############################
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
######################   НАСТРОЙКИ   ############################
pygame.init()
pygame.font.init()
pygame.mixer.init()
text = pygame.font.Font('D:\Codes\Old projects\Python/orange kid.ttf', 15)
fly_sound1 = pygame.mixer.Sound('D:\Codes\Old projects\Python/flying.wav')
fly_sound2 = pygame.mixer.Sound('D:\Codes\Old projects\Python/flying1.wav')
fly_sound1.set_volume(0.5)
screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()
pygame.display.set_caption("Kosmos")
running = True
#######################################################################################
#######################################################################################
#####################                               ###################################
#####################       ОСНОВНОЙ ЦИКЛ ИГРЫ      ###################################
#####################                               ###################################
#######################################################################################
#######################################################################################
while running:
    clock.tick(60)#клок но тут надо разобраться
    screen.blit(text.render('directions: '+ str(round(directions[0],4))+' '+str(round(directions[1],4)*-1),False, WHITE), (400, 540))
    point1 = (pointO[0] + 10 * math.cos(angle-math.pi/2)) , (pointO[1] + 10 * math.sin(angle-math.pi/2))#движение по окружности надо изучить подробно
    point2 = (pointO[0] + 5 * math.cos(angle+math.pi/4)) , (pointO[1] + 5 * math.sin(angle+math.pi/4))
    point3 = (pointO[0] + 5 * math.cos(angle+math.pi-(math.pi/4)) , (pointO[1] + 5 * math.sin(angle+math.pi-(math.pi/4))))

    draw_objects()

    if check_collision(pointO,asteroid_coordinates,20):
        pointO=200,200
        velocity=0
        asteroid_coordinates=random.randint(100,500),random.randint(100,500)
    try:
        x=x/0
    except:
        print('no')
    pointO=(pointO[0]+player_velocity[0]),(pointO[1]+player_velocity[1])
    angle+=angle_velocity
    directions=(1*math.cos(angle-math.pi/2)),(1*math.sin(angle-math.pi/2))
    player_velocity=(velocity*math.cos(last_angle-math.pi/2),velocity*math.sin(last_angle-math.pi/2))
    final_velocity=(player_velocity[0]+last_player_velocity[0]),(player_velocity[1]+last_player_velocity[1])
    for event in pygame.event.get():
        if(event.type == pygame.KEYDOWN):# альтернативный метод проверки зажатия кнопок
            if event.key == pygame.K_a:
                left=True
            if event.key == pygame.K_d:
                right=True
            if event.key == pygame.K_ESCAPE:
                running= False
            if event.key == pygame.K_w:
                forward= True
                engines='ON'
            if event.key == pygame.K_SPACE:
                stop= True
                breaks='ON'
        elif (event.type == pygame.KEYUP):
            if event.key == pygame.K_a:
                left = False
            if event.key == pygame.K_d:
                right = False
            if event.key == pygame.K_w:
                forward= False
                engines='OFF'
            if event.key == pygame.K_SPACE:
                stop= False
                breaks='OFF'
    if abs(angle_velocity)<=0.1:#если он в диапазоне то поворачиваем его куда надо
        if left:
            angle_velocity-=0.001
        elif right:
            angle_velocity+=0.001
    elif angle_velocity>0.1:#выравниваем если вышел за пределы
        angle_velocity=0.1
    else: angle_velocity=-0.1
    if left==False and right==False:
        if angle_velocity!=0:#пока он не равен 0 уменьшаем его до 0
            if angle_velocity>0:
                angle_velocity-=0.001
            elif angle_velocity<0:
                angle_velocity+=0.001
    if stop:
        velocity-=0.01
    elif forward:
        velocity+=0.03
        last_angle=angle
        last_player_velocity=(player_velocity[0],player_velocity[1])
        #fly_sound1.play(fade_ms=25)
    elif forward==False and velocity>0:
        velocity-=0.01
    elif velocity<0:
        velocity=0
    if velocity>2:
        velocity=2
    elif velocity<0:
        velocity=0
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    screen.fill(BLACK)
    # Обновление
    # Визуализация (сборка)