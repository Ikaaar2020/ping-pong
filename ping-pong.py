from pygame import *
from random import randint
from time import sleep

window = display.set_mode((700,500))
display.set_caption('ping-pong')
sps=[-3,3]
class Player:
    def __init__(self,x,y,w,h,im,b_up,b_down):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.im = transform.scale(image.load(im),(w,h))
        self.b_up = b_up
        self.b_down = b_down
        window.blit(self.im,(self.x,self.y))
    def move(self):
        key_buttons=key.get_pressed()
        if self.y > 0 and key_buttons[self.b_up]:
            self.y-=5
        if self.y <500-self.h and key_buttons[self.b_down]:
            self.y+=5
        window.blit(self.im,(self.x,self.y))
class Ball():
    def __init__(self,x,y,w,h,im,speed_y,speed_x):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.speed_y = speed_y
        self.speed_x = speed_x
        self.im = transform.scale(image.load(im),(w,h))
        self.t=True
        window.blit(self.im,(self.x,self.y))
    def move(self, pl:Player,pl1:Player):
        if self.t:
            self.t=False
        if self.collide(pl,pl1):
            self.speed_x*=-1
        if self.y<=0:
            self.speed_y*=-1
        elif self.y>=452:
            self.speed_y*=-1
        self.y+=self.speed_y
        self.x+=self.speed_x
        window.blit(self.im, (self.x,self.y))
    def win_lose(self):
        return self.x<10 or self.x>624
    def collide(self, pl:Player,pl1:Player):
        return Rect(pl.x,pl.y,pl.w,pl.h).colliderect(Rect(self.x,self.y,48,48)) or Rect(pl1.x,pl1.y,pl1.w,pl1.h).colliderect(Rect(self.x,self.y,48,48))

player1=Player(10,200,20,100,"Ping-pong/pl1.png",K_w,K_s)
player2=Player(670,200,20,100,"Ping-pong/pl2.png",K_UP,K_DOWN)
ball=Ball(326,226,48,48,"Ping-pong/ball.png",sps[randint(0,1)],sps[randint(0,1)])

game=True
clock=time.Clock()
while game:
    window.fill((0,80,0))
    for i in event.get():
        if i.type == QUIT:
            game=False
    if not(ball.win_lose()):
        player1.move()
        player2.move()
        ball.move(player1,player2)
    if ball.x<10:
        window.blit(transform.scale(image.load("Ping-pong/LOSE.png"),(700,500)),(0,0))
    elif ball.x>624:
        window.blit(transform.scale(image.load("Ping-pong/Win.png"),(700,500)),(0,0))
    clock.tick(60)
    display.update()