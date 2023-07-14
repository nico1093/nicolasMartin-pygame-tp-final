import pygame 

ANCHO_VENTANA = 900
ALTO_VENTANA = 600

#Direcciones
DERECHA = 1
IZQUIERDA = 0
MUERTE = -1

#Personaje
JUMP_HEIGTH = 150
GRAVEDAD = 0.02 
SALTO_VELOCIDAD = 10
MAX_SALTOS = 2
#
COLORES = {
    'VERDE': (0,255,0),
    'BLANCO': (255,255,255),
    'ROJO': (255, 0, 0),
    'AZUL' :  (0, 0, 255),
    'NEGRO': (0,0,0)
    }
#Proyectiles
PROYECTIL_SIZE = (50,80)
DEBUG = True  
DUPLICATE  = 2

FLOOR = 365
RECT_COLITION = 5
RECT_COLITION_H_W = 20
#PANTALLAS SCREEN
GAME_OVER = pygame.transform.scale(pygame.image.load("image/gameover.jpg"),(ANCHO_VENTANA,ALTO_VENTANA))



FPS = 60
FPS_PLAYER = 10
FPS_ENEMY = 120