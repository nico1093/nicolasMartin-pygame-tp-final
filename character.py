import pygame
from others import getSurfaceFromSpriteSheet
from CONST import *

class Character:
    def __init__(self,x,y,speed,animation) -> None:
        self._frame = 0
        self._life = 3
        self._position_x = x
        self._position_y = y
        self._speed = speed
        self._animation = animation
        self._image = self._animation[self._frame]
        self._rect = self._image.get_rect()

    def get_life(self):
        return self._life
    
    def get_position_x(self):
        return self._position_x
    
    def get_position_y(self):
        return self._position_y
    
    def get_animation(self):
        return self._animation
    
    def get_rect(self):
        return self._rect
    
    def _desplazamiento_x(self, desplazamiento):
        self._rect.x += desplazamiento
        self._rect_colition.x += desplazamiento
        self._rect_colition_floor_l.x += desplazamiento
        self._rect_colition_floor_r.x += desplazamiento

    def _desplazamiento_y(self, desplazamiento):
        self._rect.y += desplazamiento
        self._rect_colition.y += desplazamiento
        self._rect_colition_floor_l.y += desplazamiento
        self._rect_colition_floor_r.y += desplazamiento
