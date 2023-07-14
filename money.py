import pygame
from others import getSurfaceFromSpriteSheet
from CONST import *

class Money(pygame.sprite.Sprite):
    def __init__(self,x,y,position) -> None:
        self._image = getSurfaceFromSpriteSheet('image/Money.png',5,1,False,(40,40))[position]
        self._rect = self._image.get_rect()
        self._rect.x = x
        self._rect.y = y
        self._rect_colition = pygame.Rect(self._rect.centerx,self._rect.centery,self._rect.w,self._rect.h)

    def get_municion(self):
        return self._rect_colition
    
    def total_moneys(self):
        return len(getSurfaceFromSpriteSheet('image/Money.png',5,1,False,(40,40)))

    
    def draw(self,screen):
        if DEBUG:
            pygame.draw.rect(screen,COLORES['ROJO'],self._rect)
        self._image.set_colorkey(COLORES['NEGRO'])            
        screen.blit(self._image,self._rect)
    