import pygame as pg 
import random 
class Teck:
    def __init__(self,world):
        self.world = world
        
        self.allTecks = []
        
        self.grassTeck = []
        self.animalsTeck = []
        self.waterTeck = []
        self.rockTeck = []
        self.treesTeck = []

        self.animals_regen_bonus = 0
        self.trees_regen_bonus = 0
        self.grass_regen_bonus = 0

        self.rock_mining_bonus = 3
        self.food_agricolture_bonus = 1

        #self.bonus_to_foodregen = 1000

        #self.tecknologies = ["agricolture", "mining"]
        #self.choice = random.choice(["agricolture", "mining"])
        
        self.animal_teck_choise = ["addomestication", "animal parts","hunting","selective breeding"]
        self.rock_teck_choise = ["mining", "metal tools","metal chasing","masonary"]
        self.water_teck_choise = ["aquedoct", "irrigation","fishing",""]
        self.trees_teck_choise = ["wooden tools", "wooden construction","",""]
        self.grass_teck_choise = ["agricolture", "","",""]

        self.all_animal_sub_res = ["chicken, pig, cow, horse, sheep"]
        self.all_grass_sub_res = ["wheat", "barley", "corn", "rye", "oats", "quinoa", "rice", "berries"]
        self.all_wood_sub_res = ["apple", "orange", "mango", "pears", "apricot", "coconut", "plum", "almond", "peach", "fig"]
        self.all_water_sub_res = ["fish", "weeds", "crustaceans", "amphibians", "clay"]
        self.all_rock_sub_res = ["salt", "carbon", "chalk", "granite", "salt", "quartz", "marble", "copper", "iron", "oil", "coal"]


        #self.rock_teck_choice = random.choice(["mining","metal tools","masonary","metal chasing"])

        #self.food_bonus_1 = "agricolture"
        #self.rock_bonus_1 = "mining"
    def give_random_animal_subres(self):
        x = random.choice(self.all_animal_sub_res)
        return x
    def give_random_rock_subres(self):
        x = random.choice(self.all_rock_sub_res)
        return x
    def give_random_water_subres(self):
        x = random.choice(self.all_water_sub_res)
        return x
    def give_random_trees_subres(self):
        x = random.choice(self.all_wood_sub_res)
        return x
    def give_random_grass_subres(self):
        x = random.choice(self.all_grass_sub_res)
        return x
    
    
    def give_random_animal_teck(self):
        x = random.choice(self.animal_teck_choise)
        return x
    def give_random_rock_teck(self):
        x = random.choice(self.rock_teck_choise)
        return x
    def give_random_water_teck(self):
        x = random.choice(self.water_teck_choise)
        return x
    def give_random_trees_teck(self):
        x = random.choice(self.trees_teck_choise)
        return x
    def give_random_grass_teck(self):
        x = random.choice(self.grass_teck_choise)
        return x
