import os
import pickle
import select
import socket
import pygame
import sys
from pygame.locals import *
import random



class Snake():
    def __init__(self,pos,color,screen):
        self.pos = pos
        self.color = color
        self.screen = screen

    def draw_snake(self,):
        global me 
        for us in self.pos:
            me  = pygame.Rect(us[0],us[1],20,20)
            pygame.draw.circle(self.screen,self.color,(us[0],us[1]),10,0)
        return me

    def food(self,x,y,screen):
        food = pygame.Rect(x,y,20,20)
        pygame.draw.circle(screen,'red',(x,y),10,0)
        return food
    


pygame.init()


# variables
Width = 800
height = 500
clock = pygame.time.Clock()
screen  = pygame.display.set_mode((Width,height))
pygame.display.set_caption('snake')
image = pygame.image.load('/Users/kelvinowusu/Desktop/snake project/images.png')
image = pygame.transform.scale(image, (Width, height))
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Press Space To start', True, 'black', )
textRect = text.get_rect()
textRect.center = (Width // 2, height // 1.5)
x1 = 0
y1 = 0
x1_change = 0
y1_change = 0
snake_List = []
Length_of_snake = 1

wall = [pygame.Rect(-10,0,10,500),pygame.Rect(0,500,800,10),pygame.Rect(0,-10,800,10),pygame.Rect(800,0,10,500)]


foodx = round(random.randrange(0,Width-20))
foody = round(random.randrange(0,height-20))

def collidwall_or_self(wall,me):
    global x1,y1
    if me.collidelistall(wall):

        if x1>=Width:
            x1 = 1
        if x1<=0:
            x1 = Width-1
            
        if y1>=height:
            print(y1)
            y1 = 1
            
        if y1<=0:
            y1 = height-1
        print('wall collided')


def game(sound3):
    global x1,y1,x1_change,y1_change,foodx,foody,Length_of_snake
    scores = 0
    
    game_over = False
    while not game_over:
        print(scores)
        score = font.render(f'Score: {scores}', True, 'black', )
        scoreRect = text.get_rect()
        scoreRect.center = (800, 30)
        screen.fill('white')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # game_over = True
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -10
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -10
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = 10
                    x1_change = 0
        x1  = x1 + x1_change
        y1 =  y1 + y1_change
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        
        snake  = Snake(snake_List,'green',screen)
        me = snake.draw_snake()
        food = snake.food(foodx,foody,screen)
        collidwall_or_self(wall,me)
            
        if pygame.Rect.colliderect(me,food):
            foodx = round(random.randrange(0,Width-20))
            foody = round(random.randrange(0,height-20))
            Length_of_snake +=1
            scores +=1
            sound3.play()
           

            print('I have collided') 
        screen.blit(score,scoreRect)

        pygame.display.update()
        clock.tick(24)


def main():
    pygame.mixer.init()
    sound1 = pygame.mixer.Sound('/Users/kelvinowusu/Desktop/snake project/beep-02.wav')
    sound2 = pygame.mixer.Sound('/Users/kelvinowusu/Desktop/snake project/mixkit-arcade-game-opener-222.wav')
    sound3 = pygame.mixer.Sound('/Users/kelvinowusu/Desktop/snake project/mixkit-boxer-getting-hit-2055.wav')
    
    mainpage = False
    while not mainpage:
        screen.fill('red')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # mainpage = True
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    sound1.stop()
                    game(sound3)
        sound2.play()
        screen.blit(image,(0,0,800,500))
        screen.blit(text,textRect)
        pygame.display.update()
        pass

main()
pygame.display.flip()