import pygame
import sys
import random
from CONST import *
from player import Player
from plataforma import Plataforma
from enemy import Enemy
from money import Money

screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.init()
clock = pygame.time.Clock()
delta_ms = 0
imagen_fondo1 = pygame.image.load("image/background1.jpg")
imagen_fondo2 = pygame.image.load("image/background2.png")


imagen_fondo1 = pygame.transform.scale(imagen_fondo1,(ANCHO_VENTANA,ALTO_VENTANA))
imagen_fondo2 = pygame.transform.scale(imagen_fondo2,(ANCHO_VENTANA,ALTO_VENTANA))

imagen_fondo2.set_colorkey(COLORES['VERDE'])

plataformas = []
enemys = []
monies = []
#plataformas 1
plataformas.append(Plataforma(500,325,50,50))
plataformas.append(Plataforma(542,325,50,50))
plataformas.append(Plataforma(584,325,50,50))
plataformas.append(Plataforma(628,325,50,50))
#plataformas 2
plataformas.append(Plataforma(100,200,50,50))
plataformas.append(Plataforma(142,200,50,50))
plataformas.append(Plataforma(184,200,50,50))
plataformas.append(Plataforma(228,200,50,50))
#plataformas 3
plataformas.append(Plataforma(400,150,50,50))
plataformas.append(Plataforma(442,150,50,50))
plataformas.append(Plataforma(484,150,50,50))
#Enemigos

enemys.append(Enemy(x=500,y=FLOOR + 15,time_animation=80,speed=5,position_wall_l=500,position_wall_r=700))
enemys.append(Enemy(x=100,y=125,time_animation=80,speed=5,position_wall_l=100,position_wall_r=250))

#Mooney
monies.append(Money(440,FLOOR,0))
monies.append(Money(200,150,1))
monies.append(Money(400,375,2))
monies.append(Money(15,FLOOR,3))
monies.append(Money(600 ,375,4))
#Jugador
player = Player(x=0,y=0,speed=10,gravity=10,jump=20,jump_power=150,jump_height=50)
proyectiles = pygame.sprite.Group()

run = True
while run:

    pygame.time.delay(50) #Normaliza velocidad de juego.

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                player.can_shoot = True
            if event.key == pygame.K_UP:
                player.can_jump = True

    keys = pygame.key.get_pressed()

    
    
    screen.blit(imagen_fondo1,imagen_fondo1.get_rect())
    screen.blit(imagen_fondo2,imagen_fondo2.get_rect())
    
    if player.get_life() == 0:
        screen.fill(COLORES['NEGRO'])
        screen.blit(GAME_OVER,GAME_OVER.get_rect()) #Game Over
    if len(enemys) == 0:
        boss = Enemy(ANCHO_VENTANA,FLOOR,10,10,ANCHO_VENTANA,0,500)
    for plataforma in plataformas:
        plataforma.draw(screen)

    player.events(keys,proyectiles,plataformas)
    player.update(delta_ms,plataformas,enemys,monies)
    proyectiles.update(player,enemys)
    player.draw(screen)
    
    for enemy in enemys:
        enemy.update(delta_ms)
        enemy.draw(screen)
    for proyectil in proyectiles:
        proyectil.draw(screen)

    for money in monies:
        money.draw(screen)


    # enemigos update
    # player dibujarlo
    # dibujar todo el nivel

    pygame.display.flip()
    
    delta_ms += clock.tick(FPS)


    






