import pygame as pg
from pygame.locals import *
import os
import random 
#from world import World as w

class Block():
    def __init__(self, land, world, camera,x,y,gamex,gamey):
        self.world = world
        self.camera = camera
        self.land = land
        #self.w
        self.x = x
        self.y = y
        self.gamex = gamex
        self.gamey = gamey
        self.width = 15
        self.height = 15
        #self.land_rect = pg.Rect(self.x, self.y, self.width, self.height)
        self.blu = (25, 75, 156)
        self.green = (20, 128, 29)
        self.brown = (117, 72, 9)
        self.red = (237, 42, 2)
        self.col = random.choice([self.blu, self.red, self.brown])
        #self.print = self.draw_land(0,0)
        self.water = pg.image.load("water.png")
        self.tree = pg.image.load("tree.png")
        self.food = pg.image.load("cow.png")
        self.food2 = pg.image.load("animals.png")
        self.trees = pg.image.load("trees.png")
        self.house = pg.image.load("house.png")
        self.rocks = pg.image.load("rocks.png")
        self.grass = pg.image.load("grass.png")
        
        
        #self.text = "R"
        #self.width = 40
        #self.height = 40
        
        
        self.play_click = False
        self.button_col = (150, 149, 149)
        self.hover_col = (145, 103, 103)
        self.text_col = (0, 0, 0)
        self.click_col = (74, 74, 74)
        
        self.mistery = random.randint(1,100)

        
        self.res_identity = ""
        self.text = "R"

        self.is_settling_block = False  
        

    

    def draw_town_hall(self,x,y):
        if self.is_settling_block == True:
            if self.land.isSettled:
                self.world.screen.blit(self.house, (x,y))
    
    
    
    def block_identity_drawing(self,x,y):
        """ if self.is_settling_block == True:
            if self.land.isSettled:
                self.world.screen.blit(self.house, (x,y)) """
            
                
        if self.land.land_identity == "ismix":
            if self.mistery < 10:
                self.world.screen.blit(self.water, (x,y))
                self.res_identity = "water"
            elif self.mistery < 20:
                self.world.screen.blit(self.food2, (x,y))
                self.res_identity = "animals"
            elif self.mistery < 40:
                self.world.screen.blit(self.grass, (x,y))
                self.res_identity = "grass"
            elif self.mistery < 60:
                self.world.screen.blit(self.rocks, (x,y))
                self.res_identity = "rocks"
            else:
                self.world.screen.blit(self.tree, (x,y)) or self.world.screen.blit(self.trees, (x,y))
                self.res_identity = "trees"
                    
        elif self.land.land_identity == "isrocky":
            if self.mistery < 5:
                self.world.screen.blit(self.food2, (x,y))
                self.res_identity = "animals"
            elif self.mistery < 20:
                self.world.screen.blit(self.grass, (x,y))
                self.res_identity = "grass"
            elif self.mistery < 45:
                self.world.screen.blit(self.tree, (x,y)) or self.world.screen.blit(self.trees, (x,y))
                self.res_identity = "trees"
            elif self.mistery < 70:
                self.world.screen.blit(self.water, (x,y))
                self.res_identity = "water"
            else:
                self.world.screen.blit(self.rocks, (x,y))
                self.res_identity = "rocks"

        elif self.land.land_identity == "iswoody":
            if self.mistery < 5:
                self.world.screen.blit(self.rocks, (x,y))
                self.res_identity = "rocks"
            elif self.mistery < 15:
                self.world.screen.blit(self.food2, (x,y))
                self.res_identity = "animals"
            elif self.mistery < 25:
                self.world.screen.blit(self.water, (x,y))
                self.res_identity = "water"
            elif self.mistery < 50:
                self.world.screen.blit(self.grass, (x,y))
                self.res_identity = "grass"
            else:
                self.world.screen.blit(self.trees, (x,y))
                self.res_identity = "trees"
        else:
            if self.mistery < 10:
                self.world.screen.blit(self.tree, (x,y)) or self.world.screen.blit(self.trees, (x,y))
                self.res_identity = "trees"
            elif self.mistery < 30:
                self.world.screen.blit(self.water, (x,y))
                self.res_identity = "water"
            elif self.mistery < 55:
                self.world.screen.blit(self.food2, (x,y))
                self.res_identity = "animals"
                
            else:
                self.world.screen.blit(self.grass, (x,y))
                self.res_identity = "grass"
        
        if self.is_settling_block == True:
            if self.land.isSettled:
                self.world.screen.blit(self.house, (x,y))

    def starting_values(self):
        if self.land.land_identity == "ismix":
            if self.mistery < 10:
                return "w"
            elif self.mistery < 20:
                return "a"
            elif self.mistery < 40:
                return "g"
            elif self.mistery < 60:
                return "r"
            else:
                return "t"
                

        elif self.land.land_identity == "iswoody":
            if self.mistery < 5:
                return "r"
            elif self.mistery < 15:
                return "a"
            elif self.mistery < 25:
                return "w"
            elif self.mistery < 50:
                return "g"
            else:
                return "t"
        
        elif self.land.land_identity == "isrocky":
            if self.mistery < 5:
                return "a"
            elif self.mistery < 20:
                return "g"
            elif self.mistery < 45:
                return "t"
            elif self.mistery < 70:
                return "w"
            else:
                return "r"
        
        else:
            if self.mistery < 10:
                return "t"
            elif self.mistery < 30:
                return "w"
            elif self.mistery < 55:
                return "a"
            
            else:
                return "g"
    def checkifpressed(self,x,y):
        global pushed
        global pressed
        #pressed = False
        #action = False
        pos = pg.mouse.get_pos()

        button_rect = Rect(x, y, self.width, self.height)

        #check mouse over event
        if button_rect.collidepoint(pos):
            if pg.mouse.get_pressed()[0] == 1:
                self.pushed = True
                pressed = True
                return True
    
    def drawButton(self,x,y):
        action = False

        #get mouse position
        pos = pg.mouse.get_pos()

        #create pygame .RECT object for the button
        button_rect = pg.Rect(x, y, self.width, self.height)

        #check mouse over event
        if button_rect.collidepoint(pos):
            if pg.mouse.get_pressed()[0] == 1:
                self.play_click = True
                
                pg.draw.rect(self.world.screen, self.click_col, button_rect)
            elif pg.mouse.get_pressed()[0] == 0 and self.play_click == True:
                self.play_click = False
                
                action = True
            else:
                pg.draw.rect(self.world.screen, self.hover_col, button_rect)
        else:
            pg.draw.rect(self.world.screen, self.button_col, button_rect)
            
        self.world.draw_shades(x, y, self.width, self.height)
        #pg.draw.line(self.world.screen, self.world.white, (self.x, self.y), (self.x + self.width, self.y), 2)
        #pg.draw.line(self.world.screen, self.world.black, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)
        #pg.draw.line(self.world.screen, self.world.black, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
        #pg.draw.line(self.world.screen, self.world.white, (self.x, self.y), (self.x, self.y + self.height), 2)
		
		
		#pg.draw.line(self.world.screen, self.world.black, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)
        
        font = pg.font.Font(self.world.genericFont, 10)
        text_img = font.render(self.text, True, self.text_col)
        text_len = text_img.get_width()
        self.world.screen.blit(text_img, (x + int(self.width /2) -int(text_len /2), y + 5))
        return action

class ResaurceButton():
    pressed = False
    def __init__(self, land, World, x, y, text, width, height):
        self.world = World
        self.land = land
        
        self.x = x
        self.y = y
        self.text = text
        self.width = width
        self.height = height
        
        
        self.play_click = False
        self.button_col = (150, 149, 149)
        self.hover_col = (145, 103, 103)
        self.text_col = (0, 0, 0)
        self.click_col = (74, 74, 74)
        #self.font = pg.font.get_default_font()
        

    def checkifpressed(self):
        global pushed
        global pressed
        #pressed = False
        #action = False
        pos = pg.mouse.get_pos()

        button_rect = Rect(self.x, self.y, self.width, self.height)

        #check mouse over event
        if button_rect.collidepoint(pos):
            if pg.mouse.get_pressed()[0] == 1:
                self.pushed = True
                pressed = True
                return True
    
    def drawButton(self):
        action = False

        #get mouse position
        pos = pg.mouse.get_pos()

        #create pygame .RECT object for the button
        button_rect = pg.Rect(self.x, self.y, self.width, self.height)

        #check mouse over event
        if button_rect.collidepoint(pos):
            if pg.mouse.get_pressed()[0] == 1:
                self.play_click = True
                
                pg.draw.rect(self.world.screen, self.click_col, button_rect)
            elif pg.mouse.get_pressed()[0] == 0 and self.play_click == True:
                self.play_click = False
                
                action = True
            else:
                pg.draw.rect(self.world.screen, self.hover_col, button_rect)
        else:
            pg.draw.rect(self.world.screen, self.button_col, button_rect)
            
        self.world.draw_shades(self.x, self.y , self.width, self.height)
        #pg.draw.line(self.world.screen, self.world.white, (self.x, self.y), (self.x + self.width, self.y), 2)
        #pg.draw.line(self.world.screen, self.world.black, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)
        #pg.draw.line(self.world.screen, self.world.black, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
        #pg.draw.line(self.world.screen, self.world.white, (self.x, self.y), (self.x, self.y + self.height), 2)
		
		
		#pg.draw.line(self.world.screen, self.world.black, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)
        
        font = pg.font.Font(self.world.genericFont, 10)
        text_img = font.render(self.text, True, self.text_col)
        text_len = text_img.get_width()
        self.world.screen.blit(text_img, (self.x + int(self.width /2) -int(text_len /2), self.y + 5))
        return action