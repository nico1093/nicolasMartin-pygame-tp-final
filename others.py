import pygame
from CONST import *


def getSurfaceFromSpriteSheet(path,columnas,filas,flip=False,size = None,step = 1):
        lista = []
        surface_imagen = pygame.image.load(path).convert()
        fotograma_ancho = int(surface_imagen.get_width()/columnas)
        fotograma_alto = int(surface_imagen.get_height()/filas)
        x = 0
        for fila in range(filas):
            for columna in range(0,columnas,step):
                x = columna * fotograma_ancho
                y = fila * fotograma_alto
                surface_fotograma = surface_imagen.subsurface(x,y,fotograma_ancho,fotograma_alto)
                if(flip):
                    surface_fotograma = pygame.transform.flip(surface_fotograma,True,False)
                if size == None:
                    surface_fotograma = pygame.transform.scale(surface_fotograma,(surface_fotograma.get_width() * DUPLICATE, 
                                                                                surface_fotograma.get_height() * DUPLICATE))
                else:
                    surface_fotograma = pygame.transform.scale(surface_fotograma,(size[0],size[1]))
                
                lista.append(surface_fotograma)
        return lista

