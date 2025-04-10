from pygame import *
from random import randint
from time import time as tm
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,play_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65,65))
        self.speed = play_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y >5:
            self.rect.y-= self.speed
        if keys[K_s] and self.rect.y < height - 80:
            self.rect.y += self.speed
    def update_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y >5:
            self.rect.y-= self.speed
        if keys[K_DOWN] and self.rect.y < height - 80:
            self.rect.y += self.speed
    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.centery,5)
        bullets.add(bullet)
        mixer.music.load('babax.ogg')
        mixer.music.play(-1)

width = 500
height = 500

window = display.set_mode((width,height))
window.fill((0,0,0))
clock = time.Clock()
FPS = 60
player_one = Player('43.jpg', 10, 10, 10)
player_two = Player('1.jpg', width-80, 10, 10)
start = True

while start == True:


    player_one.update_right()
    player_one.reset()

    player_two.update_left()
    player_two.reset()

    for e in event.get():
        if e.type == QUIT:
            start = False
    
    display.update()
    clock.tick(FPS)
