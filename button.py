import pygame
from pygame.locals import *
from widget import Widget


class Button(Widget):
    def __init__(self,master,x,y,w,h,color_background,on_click,on_click_button,text,font,font_size,font_color):
        super().__init__(master,x,y,w,h,color_background)
        pygame.font.init()
        self.on_click = on_click
        self.on_click_button = on_click_button
        self._text = text
        self.font_sys = pygame.font.Font(font,font_size)
        self.font_color = font_color
        #self.render()
        
    def render(self):
        image_text = self.font_sys.render(self._text,True,self.font_color,self.color_background)
        self.slave_surface = pygame.surface.Surface((self.w,self.h),pygame.SRCALPHA)
        self.slave_rect = self.slave_surface.get_rect()
        self.slave_rect.x = self.x
        self.slave_rect.y = self.y
        #self.slave_rect_collide = pygame.Rect(self.slave_rect)
        #self.slave_rect_collide.x += self.master_form.x
        #self.slave_rect_collide.y += self.master_form.y
        self.slave_surface.fill(self.color_background)
        self.slave_surface.blit(image_text,(5,5))

    def update(self,events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if(self.slave_rect.collidepoint(event.pos)):
                    self.on_click_button = not(self.on_click_button)
                    self.on_click(self.on_click_button)
        self.render()

        