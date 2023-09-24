import pygame
from pygame.locals import *

class Widget:
    def __init__(self,master_form,x,y,w,h,color_background):
        self.master_form = master_form
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color_background = color_background

    def render(self):
        pass

    def update(self):
        pass

    def draw(self):
        self.master_form.blit(self.slave_surface,self.slave_rect)

    def get_master(self):
        return self.master_form