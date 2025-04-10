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
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x >5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 700 - 80:
            self.rect.x += self.speed
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

start = True

while start == True:
    for e in event.get():
        if e.type == QUIT:
            start = False
    display.update()
    clock.tick(FPS)
