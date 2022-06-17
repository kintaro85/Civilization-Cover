import pygame as pg 

class Camera:

    def __init__(self,world,width,height):

        self.width = width 
        self.height = height
        self.world = world
        self.scroll = pg.Vector2(0,0)
        self.dx = 0 # direction of camera movement on the x axis 
        self.dy = 0 # direction of camera movement on the y axis
        self.speed = 25  #speed of camera movement in pixel(25)
        
    def update(self):
        
        mouse_pos = pg.mouse.get_pos()
        rect = pg.Rect(122 + self.scroll.x, 0, 250, 780)

        # movement on the x axis
        
        if mouse_pos[0] > self.width * 0.97 and rect.x >= 125:  #if we are in the far right of the screen 
            #if rect.x >= 250:                                     #self.world.test_collide() == True:
            self.dx = -self.speed 
        elif mouse_pos[0] < self.width * 0.03: #if we are on the far left
            self.dx = self.speed
        else:
            self.dx = 0
        
        # movement on the y axis

        if mouse_pos[1] > self.height * 0.97:  #if we are in the far bottom of the screen 
            self.dy = -self.speed 
        elif mouse_pos[1] < self.width * 0.03: 
            self.dy = self.speed
        else:
            self.dy = 0

        # update camera scroll

        self.scroll.x += self.dx
        self.scroll.y += self.dy
