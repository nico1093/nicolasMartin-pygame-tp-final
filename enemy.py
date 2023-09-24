import pygame
from CONST import *
from others import getSurfaceFromSpriteSheet
from player import Player

class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y,time_animation,speed, position_wall_l,position_wall_r) -> None:
        self._move_l = getSurfaceFromSpriteSheet('image/charactrer/soldier.png',12,4,False)[12:24]
        self._move_r = getSurfaceFromSpriteSheet('image/charactrer/soldier.png',12,4,True)[12:24]
        self._frame = 0
        self._animation = self._move_r 
        self._image = self._animation[self._frame]
        self._rect = self._image.get_rect()
        self._rect.x = x
        self._rect.y = y
        self._speed = speed
        self._direction = IZQUIERDA
        self._health = 2

        self._time_animation = time_animation
        self._current_time = 0
        self._rect_colition = pygame.Rect(self._rect.x+ RECT_COLITION_H_W,self._rect.y,self._rect.w - RECT_COLITION_H_W,self._rect.h - RECT_COLITION_H_W)
        self._rect_limit_move_r = pygame.Rect(position_wall_l,0,RECT_COLITION,ALTO_VENTANA)
        self._rect_limit_move_l = pygame.Rect(position_wall_r,0,RECT_COLITION,ALTO_VENTANA)
        self._is_a_live = True


    def get_is_a_live(self):
        return self._is_a_live

    def damage(self):
        sound = pygame.mixer.Sound('music/grito_dead.mp3')
        self._health -= 1
        if self._health == 0:
            self._is_a_live = False
            Player.score += 500
            sound.play()

    def get_colition(self):
        return self._rect_colition   

    def movement(self):
        if self._rect_colition.colliderect(self._rect_limit_move_l) or self._rect_colition.colliderect(self._rect_limit_move_r):
            if self._direction == DERECHA:
                self._direction = IZQUIERDA
                self._animation = self._move_r
            elif self._direction == IZQUIERDA:
                self._direction = DERECHA
                self._animation = self._move_l
            else:
                self._animation = self._dead
            self._speed *= -1
    
    def _enemy_animation(self):
        if  self._direction == MUERTE:
            if(self._frame < len(self._animation) - 1):
                self._frame += 1 
            else:
                self.kill()
        else: 
            if(self._frame < len(self._animation) - 1):
                self._frame += 1 
            else:
                self._frame = 0
        self._image = self._animation[self._frame]
    
    def desplazamiento(self):
        self._rect.x += self._speed
        self._rect_colition.x += self._speed


    def update(self):
        self._enemy_animation()
        self.movement()
        self.desplazamiento()
        

    def draw(self,screen):
        if DEBUG:
            pygame.draw.rect(screen,BLANCO,self._rect)
            pygame.draw.rect(screen,VERDE,self._rect_colition) 
            pygame.draw.rect(screen,AZUL,self._rect_limit_move_r)
            pygame.draw.rect(screen,AZUL,self._rect_limit_move_l)
        if self._health > 0:
            self._image = self._animation[self._frame]
            self._image.set_colorkey(NEGRO)
            screen.blit(self._image,self._rect)
        

        
