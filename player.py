import pygame
from others import getSurfaceFromSpriteSheet
from CONST import *
from proyectil import Proyectil
from character import Character


class Player():
    def __init__(self, x, y, speed, gravity, jump, jump_power,jump_height) -> None:
        self._walk_r = getSurfaceFromSpriteSheet('image\charactrer\player.png', 13, 4)[13:22]
        self._walk_l = getSurfaceFromSpriteSheet('image\charactrer\player.png', 13, 4, True)[13:22]
        self._stay_r = getSurfaceFromSpriteSheet('image\charactrer\player.png', 13, 4)[:2]
        self._stay_l = getSurfaceFromSpriteSheet('image\charactrer\player.png', 13, 4, True)[:2]
        self._shoot_r = getSurfaceFromSpriteSheet('image\charactrer\player.png', 13, 4)[26:30]
        self._shoot_l = getSurfaceFromSpriteSheet('image\charactrer\player.png', 13, 4, True)[26:30]
        self._jump_r_up = getSurfaceFromSpriteSheet('image\charactrer\player.png', 13, 4)[39:45]
        self._jump_l_up = getSurfaceFromSpriteSheet('image\charactrer\player.png', 13, 4, True)[39:45]
        self._jump_r_down = getSurfaceFromSpriteSheet('image\charactrer\player.png', 13, 4)[45:48]
        self._jump_l_down = getSurfaceFromSpriteSheet('image\charactrer\player.png', 13, 4, True)[45:48]
        self._score = 0
        self._gravity = gravity
        self._jump = jump
        self._direction = DERECHA
        self._is_jump = False
        self._jump_power = jump_power
        self._y_start_jump = 0
        self.jump_height = jump_height
        self.speed_jump = 5
        self._frame = 0
        self._life = 3
        self._position_x = x
        self._position_y = y
        self._speed = speed
        self._animation = self._stay_r
        self._image = self._animation[self._frame]
        self._rect = self._image.get_rect()

        self._rect_colition = pygame.Rect(self._rect.x + RECT_COLITION, + self._rect.y + RECT_COLITION,self._rect.w -RECT_COLITION_H_W,self._rect.h -RECT_COLITION_H_W)
        self._rect_colition_floor_l = pygame.Rect(self._rect.centerx, self._rect.y + self._rect.h-20,self._rect.w/3,RECT_COLITION)
        self._rect_colition_floor_r = pygame.Rect(self._rect.x + RECT_COLITION, self._rect.y + self._rect.h-20,self._rect.w/3,RECT_COLITION)
        self.can_shoot = True
        self.can_jump = True
    def get_rect_player(self):
        return self._rect

    def get_direction(self):
        return self._direction
    
    def get_life(self):
        return self._life
    
    def set_life(self, life):
        self._life = life


    def caminar(self, direccion,plataformas):
        if self._in_platform(plataformas):
            if self._direction != direccion or (self._animation != self._walk_r and self._animation != self._walk_l):
                self._frame = 0
                self._direction = direccion
                if direccion == DERECHA:
                    self._position_x = self._speed
                    self._animation = self._walk_r
                    self._direction = DERECHA
                else:
                    self._position_x = -self._speed
                    self._animation = self._walk_l
                    self._direction = IZQUIERDA
    

    def saltar(self):#En caso de que no se aplique movimiento salta en el lugar
        if self._is_jump:
            self._y_start_jump = self._rect.y
            if self._rect.x > 0:
                self._position_y -= (self._jump * abs(self._jump)) * 0.5
            if(self._direction == DERECHA):
                self._position_x = self._speed
                self._animation = self._jump_r_up
            else:
                self._position_x = -self._speed
                self._animation = self._jump_l_up
            self._frame = 0
        else:
            self._is_jump = False

            

    def esperar(self):
        if self._animation != self._stay_r and self._animation != self._stay_r:
            if self._direction == DERECHA:
                self._animation = self._stay_r
            else:
                self._animation = self._stay_l
            self._position_x = 0
            self._position_y = 0
            self._frame = 0

    def disparar(self,proyectiles):
            proyectil = Proyectil(self.get_rect_player().centerx, self.get_rect_player().y)
            proyectiles.add(proyectil)
            if self._direction == DERECHA:
                self._animation = self._shoot_r
            else:
                self._animation = self._shoot_l

    def pick_municion(self,municiones):
       for municion in municiones:
            if self._rect_colition.colliderect(municion.get_municion()):
                self._score += 100
                municiones.remove(municion)
        

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

    def _in_platform(self, plataformas) -> bool:
        # Denota verdadero si el personaje se encuentra parado sobre una plataforma adicional
        if self._rect.y >= FLOOR:
            return True
        else:
            if self._direction == DERECHA:
                for plataforma in plataformas:
                    if self._rect_colition_floor_r.colliderect(plataforma.get_colition()):
                        return True
            else:
                for plataforma in plataformas:
                    if self._rect_colition_floor_l.colliderect(plataforma.get_colition()):
                        return True
        return False
    
    def _colition_enemy(self,enemys) -> bool:
        #Denota True si se determina una colision entre el personaje y algun enemigo
        for enemy in enemys:
            if self._rect_colition.colliderect(enemy.get_colition()) and enemy.get_is_a_live():
                return True
        return False

    def _lose_life(self,enemys):
        if self._colition_enemy(enemys):
            self.set_life(self.get_life() - 1)
            #Vuelve a inicio
            self._rect.x = 0
            self._rect.y = 0
            self._rect_colition = pygame.Rect(self._rect.x + RECT_COLITION, + self._rect.y + RECT_COLITION,self._rect.w -RECT_COLITION_H_W,self._rect.h -RECT_COLITION_H_W)
            self._rect_colition_floor_l = pygame.Rect(self._rect.centerx, self._rect.y + self._rect.h-20,self._rect.w/3,RECT_COLITION)
            self._rect_colition_floor_r = pygame.Rect(self._rect.x + RECT_COLITION, self._rect.y + self._rect.h-20,self._rect.w/3,RECT_COLITION)
        
            

    def _player_mover(self):
            if(abs(self._y_start_jump) - abs(self._rect.y) > self.jump_height and self._is_jump):
                self._position_y = 0
            self._desplazamiento_x(self._position_x)
            self._desplazamiento_y(self._position_y)

    def _player_animation(self, plataformas):
        # Manipula la animacion del player
            if (self._frame < len(self._animation) - 1):
                self._frame += 1
            else:
                if self._in_platform(plataformas):
                    self._frame = 0

                    #52418893

    def _player_gravedad(self, plataformas):
        # Se encarga de la gravedad del personaje
        if not(self._in_platform(plataformas)):
            self._desplazamiento_y(self._gravity)
            self._frame = 0
            if self._direction == DERECHA:
                self._animation = self._jump_r_down
            else:
                self._animation = self._jump_l_down

        else:
            self._is_jump = False

    def update(self, delta_ms, plataformas,enemys,municiones):
        self._player_mover()
        self._player_animation(plataformas)
        self._player_gravedad(plataformas)
        self._lose_life(enemys)
        self.pick_municion(municiones)

    def draw(self, screen):
        if DEBUG:
            pygame.draw.rect(screen, COLORES['BLANCO'], self._rect)
            pygame.draw.rect(screen, COLORES['VERDE'], self._rect_colition)
            pygame.draw.rect(screen, COLORES['AZUL'], self._rect_colition_floor_l)
            pygame.draw.rect(screen, COLORES['NEGRO'], self._rect_colition_floor_r)
        self._image = self._animation[self._frame]
        self._image.set_colorkey(COLORES['VERDE'])
        screen.blit(self._image, self._rect)

    def events(self, keys, proyectiles,plataformas):
        if keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and self._rect.x > 0:
            self.caminar(IZQUIERDA,plataformas)
        elif keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT] and self._rect.x < ANCHO_VENTANA - self._rect.w :
            self.caminar(DERECHA,plataformas)
        elif keys[pygame.K_UP] and self._rect.y > 0:
            if self.can_jump and self._in_platform(plataformas):
                self._is_jump = True
                #self.saltar_movimiento(keys)
                self.saltar()
        
        
        else:
             self.esperar()
        if (keys[pygame.K_SPACE]):
            if self.can_shoot:
                self.disparar(proyectiles)
                self.can_shoot = False
        