import pygame
from others import getSurfaceFromSpriteSheet
from CONST import *


class Plataforma:
    def __init__(self,x,y,width,heigth) -> None:
        self._image = getSurfaceFromSpriteSheet('image/plataform/bloks.png',4,4)[7]
        self._image = pygame.transform.scale(self._image,(width,heigth))
        self._rect = self._image.get_rect()
        self._rect.x = x
        self._rect.y = y
        #self._rect_colition = pygame.Rect(self._rect.x,self._rect.y,self._rect.w,self._rect.h)
        self._rect_colition = pygame.Rect(self._rect.x,self._rect.y,self._rect.w,RECT_COLITION)

    def get_colition(self):
        return self._rect_colition
    
    
    def draw(self,screen):
        if DEBUG:
            pygame.draw.rect(screen,COLORES['BLANCO'],self._rect)
            pygame.draw.rect(screen,COLORES['VERDE'],self._rect_colition)
        self._image.set_colorkey(COLORES['BLANCO'])
        screen.blit(self._image,self._rect)
        