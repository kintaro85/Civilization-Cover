from game.block import Block
#from game.world import ToPLayLoop as info
import pygame as pg
from pygame.locals import *
import os
import random
from game.teck import Teck 
import operator
#from world import World as w

class Land():
    def __init__(self, world, camera, x, y,longitude, latitude):
        self.world = world
        self.camera = camera
        #self.w
        self.x = x
        self.y = y
        self.longitude = longitude
        self.latitude = latitude
        
        #self.land_rect = pg.Rect(self.x, self.y, self.width, self.height)
        self.blu = (25, 75, 156)
        self.green = (0, 201, 7)
        self.black = (0,0,0)
        self.brown = (117, 72, 9)
        self.red = (237, 42, 2)
        #self.info_rect = pg.Rect(50 , 500, 92, 122)
        self.info_rect = pg.Rect(self.world.game_width/2-500, 200 , 500, 400)
        self.research_rect = pg.Rect(self.info_rect.x+210, self.info_rect.y+2, 280, 395) # x & y    W & H
    

        self.col = random.choice([self.blu, self.green, self.red])
        
        self.block1 = Block(self, self.world, self.camera,self.info_rect.x+250,self.info_rect.y+180,self.x+122+self.camera.scroll.x,self.y+self.camera.scroll.y)
        self.block2 = Block(self, self.world, self.camera,self.info_rect.x+290,self.info_rect.y+180,self.x+122+40+self.camera.scroll.x,self.y+self.camera.scroll.y)
        self.block3 = Block(self, self.world, self.camera,self.info_rect.x+330,self.info_rect.y+180,self.x+122+80+self.camera.scroll.x,self.y+self.camera.scroll.y)
        self.block4 = Block(self, self.world, self.camera,self.info_rect.x+370,self.info_rect.y+180,self.x+122+120+self.camera.scroll.x,self.y+self.camera.scroll.y)
        self.block5 = Block(self, self.world, self.camera,self.info_rect.x+410,self.info_rect.y+180,self.x+122+160+self.camera.scroll.x,self.y+self.camera.scroll.y)
        
        self.block6 = Block(self, self.world, self.camera,self.info_rect.x+250,self.info_rect.y+220,self.x+122+self.camera.scroll.x,self.y+40+self.camera.scroll.y)
        self.block7 = Block(self, self.world, self.camera,self.info_rect.x+290,self.info_rect.y+220,self.x+122+40+self.camera.scroll.x,self.y+40+self.camera.scroll.y)
        self.block8 = Block(self, self.world, self.camera,self.info_rect.x+330,self.info_rect.y+220,self.x+122+80+self.camera.scroll.x,self.y+40+self.camera.scroll.y)
        self.block9 = Block(self, self.world, self.camera,self.info_rect.x+370,self.info_rect.y+220,self.x+122+120+self.camera.scroll.x,self.y+40+self.camera.scroll.y)
        self.block10 = Block(self, self.world, self.camera,self.info_rect.x+410,self.info_rect.y+220,self.x+122+160+self.camera.scroll.x,self.y+40+self.camera.scroll.y)
        
        self.block11 = Block(self, self.world, self.camera,self.info_rect.x+250,self.info_rect.y+260,self.x+122+self.camera.scroll.x,self.y+80+self.camera.scroll.y)
        self.block12 = Block(self, self.world, self.camera,self.info_rect.x+290,self.info_rect.y+260,self.x+122+40+self.camera.scroll.x,self.y+80+self.camera.scroll.y)
        self.block13 = Block(self, self.world, self.camera,self.info_rect.x+330,self.info_rect.y+260,self.x+122+80+self.camera.scroll.x,self.y+80+self.camera.scroll.y)
        self.block14 = Block(self, self.world, self.camera,self.info_rect.x+370,self.info_rect.y+260,self.x+122+120+self.camera.scroll.x,self.y+80+self.camera.scroll.y)
        self.block15 = Block(self, self.world, self.camera,self.info_rect.x+410,self.info_rect.y+260,self.x+122+160+self.camera.scroll.x,self.y+80+self.camera.scroll.y)
       
        self.block16 = Block(self, self.world, self.camera,self.info_rect.x+250,self.info_rect.y+300,self.x+122+self.camera.scroll.x,self.y+120+self.camera.scroll.y)
        self.block17 = Block(self, self.world, self.camera,self.info_rect.x+290,self.info_rect.y+300,self.x+122+40+self.camera.scroll.x,self.y+120+self.camera.scroll.y)
        self.block18 = Block(self, self.world, self.camera,self.info_rect.x+330,self.info_rect.y+300,self.x+122+80+self.camera.scroll.x,self.y+120+self.camera.scroll.y)
        self.block19 = Block(self, self.world, self.camera,self.info_rect.x+370,self.info_rect.y+300,self.x+122+120+self.camera.scroll.x,self.y+120+self.camera.scroll.y)
        self.block20 = Block(self, self.world, self.camera,self.info_rect.x+410,self.info_rect.y+300,self.x+122+160+self.camera.scroll.x,self.y+120+self.camera.scroll.y)
        
        self.block21 = Block(self, self.world, self.camera,self.info_rect.x+250,self.info_rect.y+340,self.x+122+self.camera.scroll.x,self.y+160+self.camera.scroll.y)
        self.block22 = Block(self, self.world, self.camera,self.info_rect.x+290,self.info_rect.y+340,self.x+122+40+self.camera.scroll.x,self.y+160+self.camera.scroll.y)
        self.block23 = Block(self, self.world, self.camera,self.info_rect.x+330,self.info_rect.y+340,self.x+122+80+self.camera.scroll.x,self.y+160+self.camera.scroll.y)
        self.block24 = Block(self, self.world, self.camera,self.info_rect.x+370,self.info_rect.y+340,self.x+122+120+self.camera.scroll.x,self.y+160+self.camera.scroll.y)
        self.block25 = Block(self, self.world, self.camera,self.info_rect.x+410,self.info_rect.y+340,self.x+122+160+self.camera.scroll.x,self.y+160+self.camera.scroll.y)
        
        self.sciencex = Teck(self)
        
        self.block_list = [self.block1,self.block2,self.block3,self.block4,self.block5,self.block6,
        self.block7,self.block8,self.block9,self.block10,self.block11,self.block12,self.block13,
        self.block14,self.block15,self.block16,self.block17,self.block18,self.block19,self.block20,
        self.block21,self.block22,self.block23,self.block24,self.block25]
        
        self.settling_block = random.choice(self.block_list)
        
        self.rect = pg.Rect((x + self.camera.scroll.x+252) , (y + self.camera.scroll.y), 92, 122)
        #self.info_rect = pg.Rect(50 , 500, 92, 122)
        self.info_click = False

        #self.land_type_list = ["iswoody", "iswet", "isplane"]
        
        #self.info_rect = pg.Rect(self.world.game_width/2-500, 200 , 500, 400)

        

        self.land_info = InfoButt(self,self.world, self.camera, (self.x+122+2), (self.y+2), "I", 15,15)
        self.close_info = CloseInfo(self,self.world, self.camera, self.info_rect.x , self.info_rect.y, "X", 20,20)
        self.research = CloseInfo(self,self.world, self.camera, self.info_rect.x +270 , self.info_rect.y+ 130, "Research", 120,20)
        self.close_reserach_panel = CloseInfo(self,self.world, self.camera, self.research_rect.x , self.research_rect.y, "X", 20,20)
        self.technologies = CloseInfo(self,self.world, self.camera, self.info_rect.x +270 , self.info_rect.y+ 160, "Technologies", 120,20)

        self.land_identity = self.set_land_type()

        self.land_wealth = self.set_land_richness()

        self.isSettled = False

        self.moreWorkers = CloseInfo(self,self.world, self.camera, self.info_rect.x +150, self.info_rect.y+300, "+", 20,20)
        self.moreGurus = CloseInfo(self,self.world, self.camera, self.info_rect.x +150, self.info_rect.y+330, "+", 20,20)
        self.moreTravellers = CloseInfo(self,self.world, self.camera, self.info_rect.x +150, self.info_rect.y+360, "+", 20,20)
        
        self.receiveTravellers = InfoButt(self,self.world, self.camera, self.x+122+100, self.y+100, "+", 20,20)

        self.water = 0
        self.animals = 0
        self.wood = 0
        self.rock = 0
        self.grass = 0
        self.food = 0

        self.new_water = self.water
        self.new_food = self.food
        self.new_wood = self.wood
        self.new_rock = self.rock
        self.new_grass = self.grass

        self.food_regen = 1
        self.water_regen = 1
        self.wood_regen = 1
        self.rock_regen = 1
        self.grass_regen = 1

        self.animals_researchers = 0
        self.water_researchers = 0
        self.trees_researchers = 0
        self.rocks_researchers = 0
        self.grass_researchers = 0

        self.animals_science = 0
        self.water_scince = 0
        self.trees_science = 0
        self.rocks_science = 0
        self.grass_science = 0

        self.all_researchers = 0#self.animals_researchers+self.water_researchers+self.trees_researchers+self.rocks_researchers+self.grass_researchers 

        self.gurus = 0
        self.workers = 0
        self.idle_citizens = 0 
        self.travellers = 0
        self.explorers = 0
        
        self.all_citizens = 0#self.return_tot_civ()#(self.gurus+self.workers+self.idle_citizens+self.travellers+self.explorers)
        
        self.coordinate = [self.longitude,self.latitude]

        self.at_north = [self.longitude,self.latitude+1]
        self.at_south = [self.longitude,self.latitude-1]
        self.at_west = [self.longitude-1,self.latitude]
        self.at_east = [self.longitude+1,self.latitude]

        #self.possible_neibor = [self.at_north,self.at_south,self.at_east,self.at_west]

        self.neighbor = []
        self.number_of_neibor = len(self.neighbor)

        self.explorers_list = []

        self.display_research = False
        self.display_tecks = False
        self.genericFont = pg.font.get_default_font()

        self.water_sub_res_gurus = 0
        self.wood_sub_res_gurus = 0
        self.animal_sub_res_gurus = 0
        self.grass_sub_res_gurus = 0
        self.rock_sub_res_gurus = 0

        self.water_sub_res = []
        self.wood_sub_res = []
        self.rock_sub_res = []
        self.grass_sub_res = []
        self.animals_sub_res = []

        self.mainres1 = "aa"
        self.mainres2 = "bb"
        self.mainres3 = "cc"


    def disply_2_teck_choice(self):
        #self.sub_res_list   or   self.teck
        pass

    def display_discovered_subres(self):
        pass
        

    def calculate_tot_civ(self):
        self.all_citizens = self.idle_citizens+self.gurus+self.explorers+self.travellers+self.workers+self.animals_researchers+self.grass_researchers+self.water_researchers+self.trees_researchers+self.rocks_researchers
        return self.all_citizens    

    def draw_all_res(self):  #LATEST RESAURCES DRAWING METHOD
        #random_x = self.pick_random_x()
        #random_y = self.pick_randowm_y()
        
        self.block1.block_identity_drawing((self.x+122+self.camera.scroll.x), (self.y+self.camera.scroll.y)) # JUST TO REMIND MYSLEF 122 IS THE SIZE OF THE SLAB OF THE MENU 
        self.block2.block_identity_drawing((self.x+122+self.camera.scroll.x+40), (self.y+self.camera.scroll.y))
        self.block3.block_identity_drawing((self.x+122+self.camera.scroll.x+80), (self.y+self.camera.scroll.y))
        self.block4.block_identity_drawing((self.x+122+self.camera.scroll.x+120), (self.y+self.camera.scroll.y))
        self.block5.block_identity_drawing((self.x+122+self.camera.scroll.x+160), (self.y+self.camera.scroll.y))
        
        self.block6.block_identity_drawing((self.x+122+self.camera.scroll.x), (self.y+40+self.camera.scroll.y))
        self.block7.block_identity_drawing((self.x+122+self.camera.scroll.x+40), (self.y+40+self.camera.scroll.y))
        self.block8.block_identity_drawing((self.x+122+self.camera.scroll.x+80), (self.y+40+self.camera.scroll.y))
        self.block9.block_identity_drawing((self.x+122+self.camera.scroll.x+120), (self.y+40+self.camera.scroll.y))
        self.block10.block_identity_drawing((self.x+122+self.camera.scroll.x+160), (self.y+40+self.camera.scroll.y))
        
        self.block11.block_identity_drawing((self.x+122+self.camera.scroll.x), (self.y+80+self.camera.scroll.y))
        self.block12.block_identity_drawing((self.x+122+self.camera.scroll.x+40), (self.y+80+self.camera.scroll.y))
        self.block13.block_identity_drawing((self.x+122+self.camera.scroll.x+80), (self.y+80+self.camera.scroll.y))
        self.block14.block_identity_drawing((self.x+122+self.camera.scroll.x+120), (self.y+80+self.camera.scroll.y))
        self.block15.block_identity_drawing((self.x+122+self.camera.scroll.x+160), (self.y+80+self.camera.scroll.y))
        
        self.block16.block_identity_drawing((self.x+self.camera.scroll.x+122), (self.y+120+self.camera.scroll.y))
        self.block17.block_identity_drawing((self.x+122+self.camera.scroll.x+40), (self.y+120+self.camera.scroll.y))
        self.block18.block_identity_drawing((self.x+122+self.camera.scroll.x+80), (self.y+120+self.camera.scroll.y))
        self.block19.block_identity_drawing((self.x+122+self.camera.scroll.x+120), (self.y+120+self.camera.scroll.y))
        self.block20.block_identity_drawing((self.x+122+self.camera.scroll.x+160), (self.y+120+self.camera.scroll.y))
        
        self.block21.block_identity_drawing((self.x+self.camera.scroll.x+122), (self.y+160+self.camera.scroll.y))
        self.block22.block_identity_drawing((self.x+self.camera.scroll.x+122+40), (self.y+160+self.camera.scroll.y))
        self.block23.block_identity_drawing((self.x+122+self.camera.scroll.x+80), (self.y+160+self.camera.scroll.y))
        self.block24.block_identity_drawing((self.x+122+self.camera.scroll.x+120), (self.y+160+self.camera.scroll.y))
        self.block25.block_identity_drawing((self.x+122+self.camera.scroll.x+160), (self.y+160+self.camera.scroll.y))
        """ for block in self.block_list:
            if block == self.settling_block:
                block.draw_town_hall(random_x,random_y) """
        """ if self.isSettled == True:
            for block in self.block_list:
                if block == self.settling_block: """

    def update_land_values(self):
        self.world.rockKwoledge = self.world.rockKwoledge + (self.rocks_researchers*1.5)
        self.world.treesKwoledge = self.world.treesKwoledge + (self.trees_researchers*1.5)
        self.world.animalsKwoledge = self.world.animalsKwoledge + (self.animals_researchers*1.5)
        self.world.waterKwoledge = self.world.waterKwoledge + (self.water_researchers*1.5)
        self.world.grassKwoledge = self.world.grassKwoledge + (self.grass_researchers*1.5) 
        
       

        
        

        
        
        if self.isSettled == True:
            self.new_food = self.new_food - (self.workers*1.5) - self.idle_citizens + self.food_regen 
            #if self.new_food < self.food:
                #self.new_food = self.new_food - self.all_citizens - self.all_researchers + self.food_regen
            if self.workers > 0:
                self.idle_citizens = self.idle_citizens + (self.workers*1.5) - self.all_citizens

        
        
        
        
        
            
        #self.wood = 
        #self.water = 
        #self.rock =
        #self.grass = 

        # update food
        #food = food - food collected + food regen
        # if food collected < self.allcitizens:
        #    if self.idle > 0:
        #       self.idle =-1
        #    elif slef.idle == 0:
        #       if self.animals_researchers > 0:
                    #self.animals_researchers = -1
                #elif self.water_researchers > 0:
                    #self.water_researchers = -1

        #       
        #   self.trees_researchers = 0
        #   self.rocks_researchers = 0
        #   self.grass_researchers = 0 

        # update science
        # per ogni ricercato in ogni risorsa,
        #   incrementa scinza della rispettiva risorsa
        # se la scienza di una risorsa ranggiunge un certo numero:
        #      sblocca il livello sucessivo di conoscenza di derminata risorsa
        # per ogni risorsa verifica il livello di avanzamento


    def set_all_res(self):  # returned values of block.starting values all added in list to establish startin resaurces
        add_all_wood = []
        add_all_water = []
        add_all_animals = []
        add_all_grass = []
        add_all_rock = []
        add_all_food = []
        all_land_res_list = []
        
        for block in self.block_list:
            all_land_res_list.append(block.starting_values())
        for n in all_land_res_list:
            if n == "w":
                add_all_water.append(n)
                add_all_food.append(n)
            elif n == "t":
                add_all_wood.append(n)
                add_all_food.append(n)
            elif n == "r":
                add_all_rock.append(n)
                
            elif n == "g":
                add_all_grass.append(n)
                add_all_food.append(n)
            else:
                add_all_animals.append(n)
                add_all_food.append(n)
        
        self.animals = len(add_all_animals)*10
        self.wood = len(add_all_wood)*10
        self.water = len(add_all_water)*10
        self.rock = len(add_all_rock)*10
        self.grass = len(add_all_grass)*10
        self.food = len(add_all_food)*10
        
        animal = len(add_all_animals)
        water = len(add_all_water)
        wood = len(add_all_wood)
        grass = len(add_all_grass)
        rock = len(add_all_rock)

        """ if animal > 3:
            self.animals_sub_res.append(self.sciencex.give_random_animal_subres())
        if water > 3:
            self.water_sub_res.append(self.sciencex.give_random_water_subres())
        if grass > 3:
            self.grass_sub_res.append(self.sciencex.give_random_grass_subres())
        if wood > 3:
            self.wood_sub_res.append(self.sciencex.give_random_trees_subres())
        if rock > 3:
            self.rock_sub_res.append(self.sciencex.give_random_rock_subres()) """




        dic = {"animal": animal, "water": water, "wood": wood, "grass": grass, "rock": rock} 
        
        sorteddic = sorted(dic.items(),key=operator.itemgetter(1),reverse=True)
        #keysorteddic = dic.keys()
        mainres1 = str(sorteddic[0])
        mainres2 = str(sorteddic[1])
        mainres3 = str(sorteddic[2])

        """main1 = mainres1
        main2 = mainres2
        main3 = mainres3

        self.rock_sub_res.append(main1)
        self.grass_sub_res.append(main2)
        self.animals_sub_res.append(main3) """

        b = " ,'()0123456789"
        for char in b:
            mainres1 = mainres1.replace(char, "")
            mainres2 = mainres2.replace(char, "")
            mainres3 = mainres3.replace(char, "")

        self.mainres1 = mainres1
        self.mainres2 = mainres2
        self.mainres3 = mainres3

        if self.mainres1 == "animal":
            if self.land_wealth == "rich":
                for n in range(5):
                    self.animals_sub_res.append(self.sciencex.give_random_animal_subres())
                    #for n in self.animals_sub_res:
                        #if n.count() > 1:
                            #self.animals_sub_res.pop()
            if self.land_wealth == "avarege":
                for n in range(4):
                    self.animals_sub_res.append(self.sciencex.give_random_animal_subres())
            if self.land_wealth == "poor":
                for n in range(3):
                    self.animals_sub_res.append(self.sciencex.give_random_animal_subres())
            
        if self.mainres1 == "water":
            if self.land_wealth == "rich":
                for n in range(5):
                    self.water_sub_res.append(self.sciencex.give_random_water_subres())
            if self.land_wealth == "avarege":
                for n in range(4):
                    self.water_sub_res.append(self.sciencex.give_random_water_subres())
            if self.land_wealth == "poor":
                for n in range(3):
                    self.water_sub_res.append(self.sciencex.give_random_water_subres())
        
        if self.mainres1 == "wood":
            if self.land_wealth == "rich":
                for n in range(5):
                    self.wood_sub_res.append(self.sciencex.give_random_trees_subres())
            if self.land_wealth == "avarege":
                for n in range(4):
                    self.wood_sub_res.append(self.sciencex.give_random_trees_subres())
            if self.land_wealth == "poor":
                for n in range(3):
                    self.wood_sub_res.append(self.sciencex.give_random_trees_subres())
        
        if self.mainres1 == "rock":
            if self.land_wealth == "rich":
                for n in range(5):
                    self.rock_sub_res.append(self.sciencex.give_random_rock_subres())
            if self.land_wealth == "avarege":
                for n in range(4):
                    self.rock_sub_res.append(self.sciencex.give_random_rock_subres())
            if self.land_wealth == "poor":
                for n in range(3):
                    self.rock_sub_res.append(self.sciencex.give_random_rock_subres())
        
        if self.mainres1 == "grass":
            if self.land_wealth == "rich":
                for n in range(5):
                    self.grass_sub_res.append(self.sciencex.give_random_grass_subres())
            if self.land_wealth == "avarege":
                for n in range(4):
                    self.grass_sub_res.append(self.sciencex.give_random_grass_subres())
            if self.land_wealth == "poor":
                for n in range(3):
                    self.grass_sub_res.append(self.sciencex.give_random_grass_subres())
            

        """ list = self.sciencex.all_animal_sub_res
        for n in list:
            self.animals_sub_res.append(n) """

        """ if mainres1 == "animal":
            self.animals_sub_res.append(self.sciencex.give_random_animal_subres())
        if mainres1 == "water":
            self.water_sub_res.append(self.sciencex.give_random_water_subres())
        if mainres1 == "grass":
            self.grass_sub_res.append(self.sciencex.give_random_grass_subres())
        if mainres1 == "rock":
            self.rock_sub_res.append(self.sciencex.give_random_rock_subres())
        if mainres1 == "wood":
            self.wood_sub_res.append(self.sciencex.give_random_trees_subres()) """

        """ for n in range(5):
            if mainres1 == "animal":
                self.animals_sub_res.append(self.sciencex.give_random_animal_subres())
            if mainres1 == "water":
                self.water_sub_res.append(self.sciencex.give_random_water_subres())
            if mainres1 == "grass":
                self.grass_sub_res.append(self.sciencex.give_random_grass_subres())
            if mainres1 == "wood":
                self.wood_sub_res.append(self.sciencex.give_random_trees_subres())
            if mainres1 == "rock":
                self.rock_sub_res.append(self.sciencex.give_random_rock_subres()) """

        """ x = [animal,water,wood,grass,rock]
        x.sort(reverse=True)
        for n in x:
            if x[0] == x[1]:
                if n == animal:
                    self.mainres1 = "animal"
                if n == water:
                    self.mainres1 = "water"
                if n == wood:
                    self.mainres1 = "wood"
                if n == grass:
                    self.mainres1 = "grass"
                if n == rock:
                    self.mainres1 = "rock"
            elif x[1] == x[2]:
                if n == animal:
                    self.mainres2 = "animal"
                if n == water:
                    self.mainres2 = "water"
                if n == wood:
                    self.mainres2 = "wood"
                if n == grass:
                    self.mainres2 = "grass"
                if n == rock:
                    self.mainres2 = "rock"
            else:

                if n == x[0]:
                    if n == animal:
                        self.mainres1 = "animal"
                    if n == water:
                        self.mainres1 = "water"
                    if n == wood:
                        self.mainres1 = "wood"
                    if n == grass:
                        self.mainres1 = "grass"
                    if n == rock:
                        self.mainres1 = "rock"
                if n == x[1]:
                    if n == animal:
                        self.mainres2 = "animal"
                    if n == water:
                        self.mainres2 = "water"
                    if n == wood:
                        self.mainres2 = "wood"
                    if n == grass:
                        self.mainres2 = "grass"
                    if n == rock:
                        self.mainres2 = "rock"
                if n == x[2]:
                    if n == animal:
                        self.mainres3 = "animal"
                    if n == water:
                        self.mainres3 = "water"
                    if n == wood:
                        self.mainres3 = "wood"
                    if n == grass:
                        self.mainres3 = "grass"
                    if n == rock:
                        self.mainres3 = "rock" """

        """ if x[0] == animal:
            self.mainres1 = "animal"
        if x[0] == water:
            self.mainres1 = "water"
        if x[0] == grass:
            self.mainres1 = "grass"
        if x[0] == rock:
            self.mainres1 = "rock"
        if x[0] == wood:
            self.mainres1 = "wood"
        
        if x[1] == animal:
            self.mainres2 = "animal"
        if x[1] == water:
            self.mainres2 = "water"
        if x[1] == grass:
            self.mainres2 = "grass"
        if x[1] == rock:
            self.mainres2 = "rock"
        if x[1] == wood:
            self.mainres2 = "wood" """
        #self.mainres1 = x[0]
        #self.mainres2 = x[1]
        #self.mainres3 = x[2]

        self.new_food = self.food
        
        self.travellers = 0
        self.gurus = 0
        self.workers = 0 
        self.idle_citizens = 0
        self.explorers = 0
        self.explorers_list = []
        self.neighbor = []
        self.isSettled = False

        
        
        

    def uncover_fog(self):
        for x in range(len(self.explorers_list)):
            self.size_of_fog.pop() 

        
    def draw_new_fog(self):
        fog_rect1 = pg.Rect((self.x+122+self.camera.scroll.x), (self.y+self.camera.scroll.y), 40, 40)
        fog_rect2 = pg.Rect((self.x+122+40+self.camera.scroll.x), (self.y+self.camera.scroll.y), 40, 40)
        fog_rect3 = pg.Rect((self.x+122+80+self.camera.scroll.x), (self.y+self.camera.scroll.y), 40, 40)
        fog_rect4 = pg.Rect((self.x+122+120+self.camera.scroll.x), (self.y+self.camera.scroll.y), 40, 40)
        fog_rect5 = pg.Rect((self.x+122+160+self.camera.scroll.x), (self.y+self.camera.scroll.y), 40, 40)
        
        fog_rect6 = pg.Rect((self.x+122+self.camera.scroll.x), (self.y+40+self.camera.scroll.y), 40, 40)
        fog_rect7 = pg.Rect((self.x+122+40+self.camera.scroll.x), (self.y+40+self.camera.scroll.y), 40, 40)
        fog_rect8 = pg.Rect((self.x+122+80+self.camera.scroll.x), (self.y+40+self.camera.scroll.y), 40, 40)
        fog_rect9 = pg.Rect((self.x+122+120+self.camera.scroll.x), (self.y+40+self.camera.scroll.y), 40, 40)
        fog_rect10 = pg.Rect((self.x+122+160+self.camera.scroll.x), (self.y+40+self.camera.scroll.y), 40, 40)
        
        fog_rect11 = pg.Rect((self.x+122+self.camera.scroll.x), (self.y+80+self.camera.scroll.y), 40, 40)
        fog_rect12 = pg.Rect((self.x+122+40+self.camera.scroll.x), (self.y+80+self.camera.scroll.y), 40, 40)
        fog_rect13 = pg.Rect((self.x+122+80+self.camera.scroll.x), (self.y+80+self.camera.scroll.y), 40, 40)
        fog_rect14 = pg.Rect((self.x+122+120+self.camera.scroll.x), (self.y+80+self.camera.scroll.y), 40, 40)
        fog_rect15 = pg.Rect((self.x+122+160+self.camera.scroll.x), (self.y+80+self.camera.scroll.y), 40, 40)
        
        fog_rect16 = pg.Rect((self.x+122+self.camera.scroll.x), (self.y+120+self.camera.scroll.y), 40, 40)
        fog_rect17 = pg.Rect((self.x+122+40+self.camera.scroll.x), (self.y+120+self.camera.scroll.y), 40, 40)
        fog_rect18 = pg.Rect((self.x+122+80+self.camera.scroll.x), (self.y+120+self.camera.scroll.y), 40, 40)
        fog_rect19 = pg.Rect((self.x+122+120+self.camera.scroll.x), (self.y+120+self.camera.scroll.y), 40, 40)
        fog_rect20 = pg.Rect((self.x+122+160+self.camera.scroll.x), (self.y+120+self.camera.scroll.y), 40, 40)
        
        fog_rect21 = pg.Rect((self.x+122+self.camera.scroll.x), (self.y+160+self.camera.scroll.y), 40, 40)
        fog_rect22 = pg.Rect((self.x+122+40+self.camera.scroll.x), (self.y+160+self.camera.scroll.y), 40, 40)
        fog_rect23 = pg.Rect((self.x+122+80+self.camera.scroll.x), (self.y+160+self.camera.scroll.y), 40, 40)
        fog_rect24 = pg.Rect((self.x+122+120+self.camera.scroll.x), (self.y+160+self.camera.scroll.y), 40, 40)
        fog_rect25 = pg.Rect((self.x+122+160+self.camera.scroll.x), (self.y+160+self.camera.scroll.y), 40, 40)
        
        size_of_fog = [fog_rect1,fog_rect2,fog_rect3,fog_rect4,fog_rect5,fog_rect6,fog_rect7,fog_rect8,
        fog_rect9,fog_rect10,fog_rect11,fog_rect12,fog_rect13,fog_rect14,fog_rect15,
        fog_rect16,fog_rect17,fog_rect18,fog_rect19, fog_rect20,fog_rect21,
        fog_rect22,fog_rect23,fog_rect24,fog_rect25]
        
        for x in range(len(self.explorers_list)):
            
            size_of_fog.pop()

        
            

        for fog in size_of_fog:
            pg.draw.rect(self.world.screen, self.black, fog)
        
            
    def draw_number_reserachers(self):
        label_font = pg.font.Font(self.world.genericFont, 18)
        
        animals_reaserchers_label = label_font.render("Gurus Studying Animals: " + str(self.animals_researchers), True, (0,0,0))
        water_reaserchers_label = label_font.render("Gurus Studying Water: " + str(self.water_researchers), True, (0,0,0))
        tress_reaserchers_label = label_font.render("Gurus Studying Trees: " + str(self.trees_researchers), True, (0,0,0))
        rocks_reaserchers_label = label_font.render("Gurus Studying Rocks: " + str(self.rocks_researchers), True, (0,0,0))
        grass_reaserchers_label = label_font.render("Gurus Studying Grass: " + str(self.grass_researchers), True, (0,0,0))

        self.world.screen.blit(animals_reaserchers_label, (self.research_rect.x +20, self.info_rect.y + 20))
        self.world.screen.blit(water_reaserchers_label, (self.research_rect.x +20, self.info_rect.y + 40))
        self.world.screen.blit(tress_reaserchers_label, (self.research_rect.x +20, self.info_rect.y + 60))
        self.world.screen.blit(rocks_reaserchers_label, (self.research_rect.x +20, self.info_rect.y + 80))
        self.world.screen.blit(grass_reaserchers_label, (self.research_rect.x +20, self.info_rect.y + 100))

    def draw_tex_resaurce_info(self):  #display text resauces value on slab
        font = pg.font.Font(self.world.genericFont, 18)
        label_font = pg.font.Font(self.world.genericFont, 25)
        
        land_type_label = label_font.render(str(self.land_identity), True, (0,0,0))
        land_wealth_label = label_font.render(str(self.land_wealth), True, (0,0,0))
        res_label = label_font.render("Resaurces: " , True, (0,0,0))
        sub_res_label = label_font.render("Primary Resaurces: " , True, (0,0,0))
        subres1_label = font.render(self.mainres1, True, (0,0,0))
        subres2_label = font.render(self.mainres2, True, (0,0,0))
        subres3_label = font.render(self.mainres3, True, (0,0,0))

        rock_discoverable_label = font.render(str(self.rock_sub_res), True, (0,0,0))
        grass_discoverable_label = font.render(str(self.grass_sub_res), True, (0,0,0))
        animal_discoverable_label = font.render(str(self.animals_sub_res), True, (0,0,0))
        wood_discoverable_label = font.render(str(self.wood_sub_res), True, (0,0,0))
        water_discoverable_label = font.render(str(self.water_sub_res), True, (0,0,0))
        
        animals_img = font.render("Animals: " + str(self.animals), True, (0,0,0))
        wood_img = font.render("Wood: " + str(self.wood), True, (0,0,0))
        water_img = font.render("Water: " + str(self.water), True, (0,0,0))
        rock_img = font.render("Rocks: " + str(self.rock), True, (0,0,0))
        grass_img = font.render("Grass: " + str(self.grass), True, (0,0,0))
        #grass_img = font.render("Grass: " + str(self.grass), True, (0,0,0))
        food_img = font.render("Food: " + str(self.new_food), True, (0,0,0))

        civ_label = label_font.render("Inhabitants: " + str(self.all_citizens), True, (0,0,0))
        
        idles_img = font.render("Idle Citizens: " + str(self.idle_citizens), True, (0,0,0))
        workers_img = font.render("Workers: " + str(self.workers), True, (0,0,0))
        gurus_img = font.render("Gurus: " + str(self.gurus), True, (0,0,0))
        travellers_img = font.render("Travellers: " + str(self.travellers), True, (0,0,0))
        
        display_neibors = len(self.explorers_list)
        #neibor_img = font.render("N of explorers: " + str(display_neibors), True, (0,0,0))
    
        self.world.screen.blit(land_type_label, (self.info_rect.x +30, self.info_rect.y +3))
        self.world.screen.blit(land_wealth_label, (self.info_rect.x +150, self.info_rect.y +3))
        self.world.screen.blit(res_label, (self.info_rect.x +20, self.info_rect.y +30))
        self.world.screen.blit(sub_res_label, (self.info_rect.x +180, self.info_rect.y +30))
        
        self.world.screen.blit(rock_discoverable_label, (self.info_rect.x +200, self.info_rect.y +250))
        self.world.screen.blit(grass_discoverable_label, (self.info_rect.x +200, self.info_rect.y +280))
        self.world.screen.blit(animal_discoverable_label, (self.info_rect.x +200, self.info_rect.y +310))
        self.world.screen.blit(water_discoverable_label, (self.info_rect.x +200, self.info_rect.y +340))
        self.world.screen.blit(wood_discoverable_label, (self.info_rect.x +200, self.info_rect.y +370))

        
        self.world.screen.blit(subres1_label, (self.info_rect.x +210, self.info_rect.y +55))
        self.world.screen.blit(subres2_label, (self.info_rect.x +210, self.info_rect.y +75))
        self.world.screen.blit(subres3_label, (self.info_rect.x +210, self.info_rect.y +95))

        self.world.screen.blit(animals_img, (self.info_rect.x +20, self.info_rect.y +60))
        self.world.screen.blit(wood_img, (self.info_rect.x +20, self.info_rect.y +80))
        self.world.screen.blit(water_img, (self.info_rect.x +20, self.info_rect.y +100))
        self.world.screen.blit(rock_img, (self.info_rect.x +20, self.info_rect.y +120))
        self.world.screen.blit(grass_img, (self.info_rect.x +20, self.info_rect.y +140))
        pg.draw.line(self.world.screen, self.world.black, (self.info_rect.x +20, self.info_rect.y +170), (self.info_rect.x +100, self.info_rect.y +170), 2)
        self.world.screen.blit(food_img, (self.info_rect.x +20, self.info_rect.y +180))

        pg.draw.line(self.world.screen, self.world.black, (self.info_rect.x +20, self.info_rect.y +230), (self.info_rect.x +100, self.info_rect.y +230), 2)

        self.world.screen.blit(civ_label, (self.info_rect.x +20, self.info_rect.y +240))

        self.world.screen.blit(idles_img, (self.info_rect.x +20, self.info_rect.y +280))
        self.world.screen.blit(workers_img, (self.info_rect.x +20, self.info_rect.y +300))
        self.world.screen.blit(gurus_img, (self.info_rect.x +20, self.info_rect.y +330))
        self.world.screen.blit(travellers_img, (self.info_rect.x +20, self.info_rect.y +360))
        #self.world.screen.blit(neibor_img, (self.info_rect.x +20, self.info_rect.y +330))
    
    def set_land_richness(self):
        x = random.randint(1,100)
        if x < 20:
            return "poor"
        elif x < 80:
            return "avarege"
        else:
            return "rich"
    
    
    def set_land_type(self):  # INITIALISE the type of land, wet, plane or woody
        x = random.randint(1,100)
        if x < 15:
            return "ismix"
        elif x < 30:
            return "isrocky"
        elif x < 65:
            return "iswoody"
        else:
            return "isplane"
    
    def display_discovered_teck(self):
        slab_col = (125, 125, 125)

        self.display_tecks = True
        while self.display_tecks:
            pg.draw.rect(self.world.screen, slab_col, self.research_rect)
            self.close_reserach_panel.drawButton()
            font = pg.font.Font(self.world.genericFont, 10)
            self.world.clock.tick(10)
            x = self.research_rect.x + 20
            y = self.research_rect.y + 30

            button_rect = pg.Rect(x, y, 40, 40)
            for n in self.world.learnedTeck:
                #button_rect.x = button_rect.x + 50
                pg.draw.rect(self.world.screen, (255,255,255), button_rect)
                text = n
                abr = text[:4]
                text_img = font.render(abr, True, (0,0,0))
                text_len = text_img.get_width()
                self.world.screen.blit(text_img, (button_rect.x+5, button_rect.y + 5))
                
                
                
                button_rect.x += 50 
                if button_rect.x > self.research_rect.x+235:
                    button_rect.x = self.research_rect.x + 20
                    button_rect.y = button_rect.y + 50
                    if button_rect.x > self.research_rect.x+235:
                        button_rect.x = self.research_rect.x + 20
                        button_rect.y = button_rect.y + 100
                        if button_rect.x > self.research_rect.x+235:
                            button_rect.x = self.research_rect.x + 20
                            button_rect.y = button_rect.y + 150
                #pg.draw.rect(self.world.screen, (255,255,255), button_rect) 
                #text_img = font.render(self.text, True, self.text_col)
                #text_len = text_img.get_width()
                #self.world.screen.blit(text_img, (x + int(self.width /2) -int(text_len /2), y + 5))
                
                #pg.draw.rect(self.world.screen, (255,255,255), button_rect)            
            
            if self.close_reserach_panel.checkifpressed() == True:
                
                self.display_info()
                self.display_tecks = False
            for event in pg.event.get():
            
                if event.type == pg.QUIT:
                    self.display_tecks = False
                    #pg.quit()
        
            pg.display.update()
        pg.quit()

    def display_research_option(self):
        slab_col = (125, 125, 125)
        
        self.display_research = True
        while self.display_research:
            pg.draw.rect(self.world.screen, slab_col, self.research_rect)
            self.close_reserach_panel.drawButton()
            #self.draw_number_reserachers()
            symbolic_list = []
            five_block_list = []
            for block in self.block_list:
                if block.res_identity in symbolic_list:
                    pass
                else:
                    symbolic_list.append(block.res_identity)
                    five_block_list.append(block)
            
            
            for block in five_block_list:
                if block.res_identity == "water":
                    block.block_identity_drawing(self.info_rect.x+250,self.info_rect.y+180)
                    block.drawButton(self.info_rect.x+250,self.info_rect.y+180)
                    if block.checkifpressed(self.info_rect.x+250,self.info_rect.y+180) == True:
                        if self.gurus > 0:
                            #if block.res_identity == "water":
                            self.gurus -= 1
                            self.water_researchers += 1
                    
                elif block.res_identity == "animals":
                    block.block_identity_drawing(self.info_rect.x+330,self.info_rect.y+180)
                    block.drawButton(self.info_rect.x+330,self.info_rect.y+180)
                    if block.checkifpressed(self.info_rect.x+330,self.info_rect.y+180) == True:
                        if self.gurus > 0:
                            #if block.res_identity == "water":
                            self.gurus -= 1
                            self.animals_researchers += 1
                
                elif block.res_identity == "rocks":
                    block.block_identity_drawing(self.info_rect.x+290,self.info_rect.y+220)
                    block.drawButton(self.info_rect.x+290,self.info_rect.y+220)
                    if block.checkifpressed(self.info_rect.x+290,self.info_rect.y+220) == True:
                        if self.gurus > 0:
                            #if block.res_identity == "water":
                            self.gurus -= 1
                            self.rocks_researchers += 1
                    
                elif block.res_identity == "grass":
                    block.block_identity_drawing(self.info_rect.x+250,self.info_rect.y+260)
                    block.drawButton(self.info_rect.x+250,self.info_rect.y+260)
                    if block.checkifpressed(self.info_rect.x+250,self.info_rect.y+260) == True:
                        if self.gurus > 0:
                            #if block.res_identity == "water":
                            self.gurus -= 1
                            self.grass_researchers += 1
                else:
                    block.block_identity_drawing(self.info_rect.x+330,self.info_rect.y+260)
                    block.drawButton(self.info_rect.x+330,self.info_rect.y+260)
                    if block.checkifpressed(self.info_rect.x+330,self.info_rect.y+260) == True:
                        if self.gurus > 0:
                            #if block.res_identity == "water":
                            self.gurus -= 1
                            self.trees_researchers += 1

                #block.drawButton()
            
            """ for block in self.block_list:
                if block.checkifpressed() == True:
                    self.world.thinclick_sound.play()
                    if self.gurus > 0:
                        if block.res_identity == "water":
                            self.gurus -= 1
                            self.water_researchers += 1
                        elif block.res_identity == "animals":
                            self.gurus -= 1
                            self.animals_researchers += 1
                        elif block.res_identity == "rocks":
                            self.gurus -= 1
                            self.rocks_researchers += 1
                        elif block.res_identity == "grass":
                            self.gurus -= 1
                            self.grass_researchers += 1
                        else:
                            self.gurus -= 1
                            self.trees_researchers += 1 """

                    

            self.draw_number_reserachers()

            self.world.clock.tick(10)
            
            if self.close_reserach_panel.checkifpressed() == True:
                
                self.display_info()
                self.display_research = False
            for event in pg.event.get():
            
                if event.type == pg.QUIT:
                    self.display_research = False
                    #pg.quit()
        
            pg.display.update()
        pg.quit()
            
            

            

    
    def display_info(self):
        #label_font2 = pg.font.Font(self.genericFont, 20)
        #score_label = label_font2.render("Score: " + str(self.world.score), True, (0,0,0))
        #pop_label = label_font2.render("Pop: " + str(self.world.clan_population), True, (0,0,0))
        
        slab_col = (74, 74, 74)
        self.world.is_display = True
        while self.world.is_display:
            #self.world.screen.blit(score_label, (10, 200))
            #self.world.screen.blit(pop_label, (10, 250)) 
            pg.draw.rect(self.world.screen, slab_col, self.info_rect)
            #self.world.screen.blit(self.world.game_display, (252,0))
            self.world.draw_shades(self.info_rect.x, self.info_rect.y, 500, 400)
            self.close_info.drawButton()
            self.moreGurus.drawButton()
            self.moreWorkers.drawButton()
            self.moreTravellers.drawButton()
            
            self.research.drawButton()
            self.technologies.drawButton()
                    
            #self.calculate_tot_civ()
            
            self.draw_tex_resaurce_info()
            
            
            if self.research.checkifpressed() == True:
                self.display_research_option()
            
            if self.technologies.checkifpressed() == True:
                self.display_discovered_teck()
                
                #for block in block_list:
                        
                    #block.drawButton()
                    
            
            if self.moreGurus.checkifpressed() == True:
                self.world.thinclick_sound.play()
                self.idle_citizens -= 1
                self.gurus += 1
                
            

            if self.moreWorkers.checkifpressed() == True:
                self.world.thinclick_sound.play()
                self.idle_citizens -=1
                self.workers += 1
                

            if self.moreTravellers.checkifpressed() == True:
                self.world.thinclick_sound.play()
                self.idle_citizens -=1
                self.travellers += 1
                
            
            
            
            

            
            self.world.clock.tick(10)
            
            if self.close_info.checkifpressed() == True:
                self.world.thinclick_sound.play()
                
                self.world.resume_game()
                self.world.is_display = False
            for event in pg.event.get():
            
                if event.type == pg.QUIT:
                    self.is_menu = False
                    #pg.quit()
        
            pg.display.update()
        pg.quit()


class InfoButt():
    pressed = False
    def __init__(self, land, World, camera, x, y, text, width, height):
        self.world = World
        self.land = land
        self.camera = camera
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

        button_rect = Rect((self.x + self.camera.scroll.x), (self.y+ self.camera.scroll.y), self.width, self.height)

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
        button_rect = pg.Rect((self.x + self.camera.scroll.x), (self.y+ self.camera.scroll.y), self.width, self.height)

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
            
        self.world.draw_shades(self.x + self.camera.scroll.x, self.y + self.camera.scroll.y , self.width, self.height)
        #pg.draw.line(self.world.screen, self.world.white, (self.x, self.y), (self.x + self.width, self.y), 2)
        #pg.draw.line(self.world.screen, self.world.black, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)
        #pg.draw.line(self.world.screen, self.world.black, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
        #pg.draw.line(self.world.screen, self.world.white, (self.x, self.y), (self.x, self.y + self.height), 2)
		
		
		#pg.draw.line(self.world.screen, self.world.black, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)
        
        font = pg.font.Font(self.world.genericFont, 10)
        text_img = font.render(self.text, True, self.text_col)
        text_len = text_img.get_width()
        self.world.screen.blit(text_img, (self.x + int(self.width /2) -int(text_len /2)+ self.camera.scroll.x, self.y + 5+ self.camera.scroll.y))
        return action

class CloseInfo():
    pressed = False
    def __init__(self, land, World, camera, x, y, text, width, height):
        self.world = World
        self.land = land
        self.camera = camera
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
        button_rect = pg.Rect(self.x , self.y, self.width, self.height)

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
            
        self.world.draw_shades(self.x , self.y , self.width, self.height)
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

        
    
   
            
    
    
    
    
    
    

    
     
        
            
        
        
    
              

         
        
    

           
    
   

    