from typing import Any
import pygame
from CONST import *





class Personaje:
    def __init__(self,x,y,jump,speed) -> None:
        self.position_x = x
        self.position_y = y
        self.is_jump = False
        self.jump = 10
        self.speed = speed

        self.image = pygame.image.load('image/proyectil.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.position_x
        self.rect.y = self.position_y

    def movement_events(self,keys):
        if keys[pygame.K_LEFT] and x > self.speed - self.rect.w:
            self.position_x -= self.speed

        if keys[pygame.K_RIGHT] and x < 500 - self.speed - self.rect.w:
            self.position_x += self.speed

        if not (self.is_jump):  #Mientras no salte
            if keys[pygame.K_SPACE]:
                self.is_jump = True
        else:   #Esto es lo que pasa cuando salta
            if self.jump >= -10:

                print(self.position_y, "=", self.position_y, "- (", self.jump, " * ", abs(self.jump), " )*0.5")
                self.position_y -= (self.jump * abs(self.jump)) * 0.5
                self.jump -= 1

            else:
                print("Y:", y)
                print("Jump Count:", self.jump)

                self.jump = 10
                self.is_jump = False
    
    def update(self):
        self.rect.y = self.position_y
        self.rect.x = self.position_x
    
    def draw(self,screen):
        #self._image = self._animation[self._frame]
        #self._image.set_colorkey(COLORES['VERDE'])
        screen.blit(self.image, self.rect)




pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Jumping")

x = 50
y = 490
width = 5
height = 5
vel = 5

isJump = False
jumpCount = 10

pj = Personaje(x,y,jumpCount,vel)

run = True

while run:

    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    pj.movement_events(keys)
    

    win.fill((0, 0, 255))
    pj.update()
    pj.draw(win)
    #pygame.draw.rect(win, (0, 255, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()