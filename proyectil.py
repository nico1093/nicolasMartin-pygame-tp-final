import pygame
from CONST import *

class Proyectil(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self._image = pygame.transform.scale(pygame.image.load('image/proyectil.png'),PROYECTIL_SIZE)
        self._rect = self._image.get_rect()
        self._rect.x = x
        self._rect.y = y
        self._velocidad = 20   # Velocidad de movimiento del proyectil
        self._rect_colition = pygame.Rect(self._rect.x,self._rect.y,self._rect.h-RECT_COLITION,self._rect.h-RECT_COLITION)
        self.damage = 50
       

    def desplazamiento_r(self): 
        self._image = pygame.transform.scale(pygame.image.load('image/proyectil.png'),PROYECTIL_SIZE)
        self._rect.x += self._velocidad  # Mover el proyectil horizontalmente a la derecha
        self._rect_colition.x += self._velocidad
    
    def desplazamiento_l(self):
        self._image = pygame.transform.scale(pygame.transform.flip(self._image,True,False),PROYECTIL_SIZE)
        self._rect.x -= self._velocidad # Mover el proyectil horizontalmente a la izquierda
        self._rect_colition.x -= self._velocidad

    def update(self,player,enemys):
        if player.get_direction() == DERECHA:
            self.desplazamiento_r()
        elif player.get_direction() == IZQUIERDA:
            self.desplazamiento_l()
        if 0 > self._rect.x or self._rect.x > ANCHO_VENTANA:  # Si el proyectil sale de la pantalla, eliminarlo
            self.kill()
        self.kill_enemy(enemys)
        self._image.set_colorkey(AZUL)

    def is_impact_enemy(self,enemy) -> bool:
        return self._rect_colition.colliderect(enemy.get_colition())

    def kill_enemy(self,enemys):
        if len(enemys) > 0:
            for enemy in enemys:
                if self.is_impact_enemy(enemy):
                        self.kill()
                        enemy.damage()
        


    def draw(self,screen):
        if DEBUG:
            pygame.draw.rect(screen, ROJO,self._rect)
            pygame.draw.rect(screen, VERDE, self._rect_colition)
        screen.blit(self._image,self._rect)