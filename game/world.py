
#import land
import pygame as pg
from pygame.locals import *
from game.land import Land
from game.teck import Teck
from .camera import Camera
import os
import random 
import operator

class World():
    def __init__(self):
        pg.init()
        self.screen_width = 1300
        self.screen_height = 680
        self.camera_width = 1000
        self.game_width = 2000
        self.game_height = 770
        self.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
        self.game_display = pg.Surface((self.game_width, self.game_height))
        self.genericFont = pg.font.get_default_font()
        # COLORS:
        self.green = (9, 171, 52)
        self.bgmenu = (200, 200, 200)
        self.bggame = (2, 97, 5)
        self.red = (250, 200, 200)
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.menu_message = "Menu"
        self.game_message = "Play"
        
        self.toplay = ToPLayLoop(self,self.screen_width/2-65,self.screen_height/2,"Resume", 140, 40)
        
        self.topause = ToPLayLoop(self,10,100,"Menu", 90, 40)
        self.nextRound = ToPLayLoop(self,10,150,"Next" ,90, 40)

        #self.new_teck_button_event = ToPLayLoop(self,self.screen_width/2 +50,self.screen_height/2+50,"", 100,100)
        self.close_new_teck_panel = ToPLayLoop(self,self.screen_width/2+125,self.screen_height/2+225,"Continue",150,40)
        self.close_player_name_panel = ToPLayLoop(self,self.screen_width/2+125,self.screen_height/2+225,"Continue",150,40)
        self.back_to_menu = ToPLayLoop(self,self.screen_width/2+100,self.screen_height/2+225,"Back to Menu",230,40)
        
        self.quit = ToPLayLoop(self,self.screen_width/2-40,self.screen_height/2+90,"Quit", 90,40)
        self.newgame = ToPLayLoop(self,self.screen_width/2-85,self.screen_height/2-90,"New Game", 180, 40)
        
        self.is_menu = False
        self.is_game = False
        self.is_display = False
        self.clock = pg.time.Clock()
        self.pushed = False
        #self.land1 = Land(self, , 0, 0, 20, 20)
        self.camera = Camera(self, self.camera_width, self.game_height)
        self.land1 = Land(self, self.camera, 0, 0,1,3)
        self.land2 = Land(self, self.camera, 200, 0,2,3)
        self.land3 = Land(self, self.camera, 400, 0,3,3)
        self.land4 = Land(self, self.camera, 600, 0,4,3)
        self.land5 = Land(self, self.camera, 800, 0,5,3)
        self.land6 = Land(self, self.camera, 1000, 0,6,3)

        self.land7 = Land(self, self.camera, 0, 200,1,2)
        self.land8 = Land(self, self.camera, 200, 200,2,2)
        self.land9 = Land(self, self.camera, 400, 200,3,2)
        self.land10 = Land(self, self.camera, 600, 200,4,2)
        self.land11 = Land(self, self.camera, 800, 200,5,2)
        self.land12 = Land(self, self.camera, 1000, 200,6,2)

        self.land13 = Land(self, self.camera, 0, 400,1,1)
        self.land14 = Land(self, self.camera, 200, 400,2,1)
        self.land15 = Land(self, self.camera, 400, 400,3,1)
        self.land16 = Land(self, self.camera, 600, 400,4,1)
        self.land17 = Land(self, self.camera, 800, 400,5,1)
        self.land18 = Land(self, self.camera, 1000, 400,6,1)

        self.science = Teck(self)

        self.starting_tile = random.choice([self.land1,self.land2,self.land3,self.land4,self.land5,self.land6,
        self.land7,self.land8,self.land9,self.land10,self.land11,self.land12,
        self.land13,self.land14,self.land15,self.land16,self.land17,self.land18])
        

        self.continent = [self.land1,self.land2,self.land3,self.land4,self.land5,self.land6,
        self.land7,self.land8,self.land9,self.land10,self.land11,self.land12,
        self.land13,self.land14,self.land15,self.land16,self.land17,self.land18
        ]
        self.possible_neighbors = self.continent
        self.fatclick_sound = pg.mixer.Sound("click2.ogg")
        self.thinclick_sound = pg.mixer.Sound("sharpclick.ogg")


        self.clan_population = 0#self.land1.all_citizens + self.land2.all_citizens + self.land3.all_citizens +self.land4.all_citizens + self.land5.all_citizens + self.land6.all_citizens + self.land7.all_citizens +self.land8.all_citizens + self.land9.all_citizens + self.land10.all_citizens + self.land11.all_citizens + self.land12.all_citizens + self.land13.all_citizens + self.land14.all_citizens + self.land15.all_citizens +self.land16.all_citizens + self.land17.all_citizens + self.land18.all_citizens
        self.score = 0
        self.round = 30

        self.game_over = False

        self.learnedTeck = []
        
        self.rockKwoledge = 0
        self.treesKwoledge = 0
        self.animalsKwoledge = 0
        self.waterKwoledge = 0
        self.grassKwoledge = 0

        #self.list_of_all_knoledge = [self.treesKwoledge,self.rockKwoledge,self.treesKwoledge,self.animalsKwoledge,self.grassKwoledge]
        
        #self.food_bonus = 1
        #self.rock_bonus = 1
        
        self.addomestication_bonus = False
        self.animal_parts_bonus = False
        self.hunting_bonus = False
        self.selective_breeding_bonus = False

        self.display_new_discovery = False

        #self.discovery_rect = pg.Rect(self.info_rect.x+210, self.info_rect.y+2, 280, 395) # x & y    W & H
        #pg.mixer.music.load("menu.wav")
        #menumusic = pg.mixer.music.load("menu.wav")
        #open_sound = pg.mixer.Sound("sound.ogg")
        #close_sound = pg.mixer.Sound("close.wav")
        #play = pg.mixer.music.play(-1)
        #pause = pg.mixer.music.pause()
        #unpause = pg.mixer.music.unpause()
        #addomestication", "animal parts","hunting","selective breeding

        self.playerName = ""
        self.display_player_name = False
    
    def request_player_name(self):
        label_font = pg.font.Font(self.genericFont, 40)
        a = ToPLayLoop(self,self.screen_width/2-80, self.screen_height/2+100,"a",40,40)
        b = ToPLayLoop(self,self.screen_width/2-40, self.screen_height/2+100,"b",40,40)
        c = ToPLayLoop(self,self.screen_width/2, self.screen_height/2+100,"c",40,40)
        d = ToPLayLoop(self,self.screen_width/2+40, self.screen_height/2+100,"d",40,40)
        e = ToPLayLoop(self,self.screen_width/2+80, self.screen_height/2+100,"e",40,40)
        f = ToPLayLoop(self,self.screen_width/2+120, self.screen_height/2+100,"f",40,40)
        g = ToPLayLoop(self,self.screen_width/2+160, self.screen_height/2+100,"g",40,40)
        h = ToPLayLoop(self,self.screen_width/2+200, self.screen_height/2+100,"h",40,40)
        i = ToPLayLoop(self,self.screen_width/2+240, self.screen_height/2+100,"i",40,40)
        l = ToPLayLoop(self,self.screen_width/2+280, self.screen_height/2+100,"l",40,40)
        m = ToPLayLoop(self,self.screen_width/2+320, self.screen_height/2+100,"m",40,40)
        n = ToPLayLoop(self,self.screen_width/2+360, self.screen_height/2+100,"n",40,40)
        o = ToPLayLoop(self,self.screen_width/2+400, self.screen_height/2+100,"o",40,40)
        p = ToPLayLoop(self,self.screen_width/2+440, self.screen_height/2+100,"p",40,40)
        
        q = ToPLayLoop(self,self.screen_width/2-80, self.screen_height/2+150,"q",40,40)
        r = ToPLayLoop(self,self.screen_width/2-40, self.screen_height/2+150,"r",40,40)
        s = ToPLayLoop(self,self.screen_width/2, self.screen_height/2+150,"s",40,40)
        t = ToPLayLoop(self,self.screen_width/2+40, self.screen_height/2+150,"t",40,40)
        u = ToPLayLoop(self,self.screen_width/2+80, self.screen_height/2+150,"u",40,40)
        v = ToPLayLoop(self,self.screen_width/2+120, self.screen_height/2+150,"v",40,40)
        z = ToPLayLoop(self,self.screen_width/2+160, self.screen_height/2+150,"z",40,40)

        delet = ToPLayLoop(self,self.screen_width/2+240, self.screen_height/2+150,"del",60,40)
        spacex = ToPLayLoop(self,self.screen_width/2+320, self.screen_height/2+150,"space",100,40)
        
        keybord = [a,b,c,d,e,f,g,h,i,l,m,n,o,p,q,r,s,t,u,v,z]
        self.display_player_name = True
        nameList = []
        #name = ("".join(nameList))
        #name = []
        #name[0] = nameList
        #name = '{0}, {1}, {2}'.format(nameList)
        #player_name_string = str(nameList)
        while self.display_player_name:
            #player_name_string = str(nameList)

            self.clock.tick(10)
            self.draw_slab(self.screen_width/2-100, self.screen_height/2, 600,400)
            self.close_player_name_panel.drawButton()
            delet.drawButton()
            spacex.drawButton()
            
            for button in keybord:
                button.drawButton()
            for button in keybord:
                if button.checkifpressed():
                    nameList.append(button.text)
            if delet.checkifpressed():
                nameList.pop()
            if spacex.checkifpressed():
                nameList.append(" ")
            #nameList = []
            #name = nameList
            #a = ToPLayLoop()

            """ for event in pg.event.get():
                if event.type == pg.KEYDOWN or event.type == pg.KEYUP:
                    if pg.key == "K_a":
                        nameList.append("a") """
            """ if a.checkifpressed():
                nameList.append("a")
            if b.checkifpressed():
                nameList.append("b")
            if c.checkifpressed():
                nameList.append("c") """

            listToStr = ''.join([str(element) for element in nameList ]) 
                
            l1_label = label_font.render("Enter Name: " + str(listToStr), True, (0,0,0))
            #l2_label = label_font.render(str(nameList[1]), True, (0,0,0))
            #l3_label = label_font.render(str(nameList[2]), True, (0,0,0))
            #l4_label = label_font.render(str(nameList[3]), True, (0,0,0))

            self.screen.blit(l1_label, (self.screen_width/2-80, self.screen_height/2+30))
            #self.screen.blit(l2_label, (self.screen_width/2-70, self.screen_height/2+15))
            #self.screen.blit(l3_label, (self.screen_width/2-60, self.screen_height/2+15))
            #self.screen.blit(l4_label, (self.screen_width/2-50, self.screen_height/2+15))

            if self.close_player_name_panel.checkifpressed() == True:
                self.playerName = ''.join([str(element) for element in nameList ])
            
                self.resume_game()
                self.display_player_name = False
            for event in pg.event.get():
                
                if event.type == pg.QUIT:
                    self.display_player_name = False
                        #pg.quit()
            
            pg.display.update()
        pg.quit()
            


        


    def update(self):
        self.camera.update()

    def display_discovery(self,teck):
        

        self.display_new_discovery = True
        while self.display_new_discovery:
            
            self.draw_slab(self.screen_width/2-100, self.screen_height/2, 600,400)
            #self.new_teck_button_event.drawButton()
            self.close_new_teck_panel.drawButton()
            self.draw_text("Your Gurus",30,self.screen_width/2+180,self.screen_height/2+50)
            self.draw_text("have discovered: ",30,self.screen_width/2+180,self.screen_height/2+90)
            self.draw_text(teck,50,self.screen_width/2 +180,self.screen_height/2+150)
            
            
            self.clock.tick(10)
            
            
            if self.close_new_teck_panel.checkifpressed() == True:
                for land in self.continent:
                    if teck == "addomestication":
                        land.new_food +=2000
                        self.addomestication_bonus = True
                    if teck == "animal parts":
                        land.wood +=2000
                        self.animal_parts_bonus = True
                    if teck == "hunting":
                        land.rock +=2000
                        self.hunting_bonus = True
                    if teck == "selective breeding":
                        land.grass +=2000
                        self.selective_breeding_bonus = True
                
                self.resume_game()
                self.display_new_discovery = False
            for event in pg.event.get():
            
                if event.type == pg.QUIT:
                    self.display_new_discovery = False
                    #pg.quit()
        
            pg.display.update()
        pg.quit()

    
    def check_for_new_discovery(self):
        mistery = random.randint(1,100)
        knowledge_lenght = len(self.learnedTeck)

        random_animal_teck = self.science.give_random_animal_teck()
        
        if self.animalsKwoledge > 10:
            #mistery = random.randint(1,100)
            if knowledge_lenght == 0:
                if mistery > 20:
                    if random_animal_teck in self.learnedTeck:
                        pass
                    else:
                        self.learnedTeck.append(random_animal_teck)
            if knowledge_lenght == 1:
                if mistery > 80 and mistery < 90:
                    if random_animal_teck in self.learnedTeck:
                        pass
                    else:
                        self.learnedTeck.append(random_animal_teck)
            if knowledge_lenght == 2:
                if mistery >= 90 and mistery <= 95:
                    if random_animal_teck in self.learnedTeck:
                        pass
                    else:
                        self.learnedTeck.append(random_animal_teck)
            if knowledge_lenght == 3:
                if mistery >= 95:
                    if random_animal_teck in self.learnedTeck:
                        pass
                    else:
                        self.learnedTeck.append(random_animal_teck)
        
        if "addomestication" in self.learnedTeck:
            if self.addomestication_bonus == False:
                self.display_discovery("addomestication")
                self.addomestication_bonus = True
            else:
                pass
        if "animal parts" in self.learnedTeck:
            if self.animal_parts_bonus == False:
                self.display_discovery("animal parts")
                self.animal_parts_bonus = True
            else:
                pass
        if "hunting" in self.learnedTeck:
            if self.hunting_bonus == False:
                self.display_discovery("hunting")
                self.hunting_bonus = True
            else:
                pass
        if "selective breeding" in self.learnedTeck:
            if self.selective_breeding_bonus == False:
                self.display_discovery("selective breeding")
                self.selective_breeding_bonus = True
            else:
                pass

    def draw_slab(self, x, y, width, height):
        slab_col = (74, 74, 74)
        menu_slab = pg.Rect(x, y, width, height)
        pg.draw.rect(self.screen, slab_col, menu_slab)
        self.draw_shades(x, y, width, height)

    def draw_shades(self, x, y , width, height):
        pg.draw.line(self.screen, self.white, (x, y), (x + width, y), 2)
        pg.draw.line(self.screen, (46, 45, 42), (x + width, y), (x + width,y + height), 2)
        pg.draw.line(self.screen, (46, 45, 42), (x, y + height), (x + width, y + height), 2)
        pg.draw.line(self.screen, self.white, (x, y), (x, y + height), 2)

    def draw_text(self, text, size, x ,y):
        font = pg.font.Font(self.genericFont, size)
        text_surface = font.render(text, True, self.black)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.screen.blit(text_surface, text_rect)
    
    

    
    
    def calculate_score(self):
        list_of_settled_lands = []
        #settled_land_points = len(list_of_settled_lands)
        for land in self.continent:
            if land.isSettled == True:
                list_of_settled_lands.append(10)                     # point system 10 par settled land
        self.score = sum(list_of_settled_lands) + self.clan_population  # + populations
    
    def calculate_clan_population(self):
        world_census = []
        for land in self.continent:
            if land.isSettled == True:
                world_census.append(land.calculate_tot_civ())


        self.clan_population = sum(world_census)
            #land.all_citizens
    
    def diplay_menu(self):                                     # DSIPLAY THE MAIN MENU
        #pg.mixer.music.load("music.mp3")
        #click_sound = pg.mixer.Sound("click.ogg")
        #pg.mixer.music.play(-1)  
        
        self.is_menu = True
        
        while self.is_menu:
            
            self.clock.tick(15)
            self.screen.fill(self.bgmenu)
            self.display_toolbar()
            self.draw_slab(self.screen_width/2-120, 200, 250, 320)
            self.display_halloffame()
            self.draw_text(self.menu_message, 30, self.screen_width/2, 50)
            self.draw_text(
                "fps={}".format(round(self.clock.get_fps())), 
                25,
                50,
                30
            )
            self.toplay.drawButton()
            self.quit.drawButton()
            self.newgame.drawButton()
            
            if self.newgame.checkifpressed() == True:
                self.thinclick_sound.play()  
                #pg.mixer.music.pause()    
                self.new_game()
                
                self.is_menu = False
                

            
            if self.toplay.checkifpressed() == True:
                #self.thinclick_sound.play()  
                pg.mixer.music.pause()   
                self.resume_game()
                
                self.is_menu = False
            
            if self.quit.checkifpressed() == True:
                
                self.is_menu = False
                pg.quit()

            
            for event in pg.event.get():
            
                if event.type == pg.QUIT:
                    self.is_menu = False
                    
        
            pg.display.update()
        pg.quit()

    def init_all_res(self): # set all the initial value of the resuarces
        for land in self.continent:
            land.set_all_res()
        
    
    def check_all_infobutt_press(self): # check at once if any of the infobutto is clicked and display the relative info
        for lands in self.continent:
            if lands.isSettled == True:
                if lands.land_info.checkifpressed() == True:
                    self.thinclick_sound.play()
                    lands.display_info()
                #lands.drawRESbuttons()

    def check_if_nextround_ispressed(self):
        
        if self.nextRound.checkifpressed() == True:
            self.round -= 1
            #self.thinclick_sound.play()
            self.check_for_new_discovery()
            for land in self.continent:
                land.update_land_values()
            for land in  self.continent:
                for x in range(land.explorers):
                    land.explorers_list.append("a")
                    self.watch_out_for_settled_land() 

    def display_travel_destination(self,land): # CLASS LAND PASSED AS PARAMETER TO DETERMINE TRANSITIONS OF DATA FROM LAND TO LAND
        for element in land.neighbor:
            element.receiveTravellers.drawButton()
            if element.receiveTravellers.checkifpressed() == True:
                #self.thinclick_sound.play()
                self.clock.tick(10)
                if land.travellers >0:
                    if element.isSettled == False:
                        land.travellers -=1
                        element.explorers += 1
                        element.explorers_list.append("a")
                        self.watch_out_for_settled_land()
                    else:
                        land.travellers -=1
                        element.idle_citizens += 1


    
    def establish_starting_land(self):   # SET A RANDOM CHOSED LAND AS THE STARTING SETTLED ONE
        for land in self.continent:
            if land == self.starting_tile:
                land.isSettled = True
                land.idle_citizens = 5
    
    def establish_settling_blocks(self):
        for land in self.continent:
            for block in land.block_list:
                if block == land.settling_block:
                    block.is_settling_block = True

    def watch_out_for_settled_land(self):
        for land in self.continent:
            if len(land.explorers_list) > 24:
                land.idle_citizens = land.explorers
                land.explorers = 0

                land.isSettled = True        
        
    def allocate_neighbors(self,lan):  #DETECT NEIBORING LAND AND ADD IT TO THE LIST OF NEIBORS
        for land in self.continent:
            
            if lan.coordinate == land.at_north:
                land.neighbor.append(lan)
            if lan.coordinate == land.at_south:
                land.neighbor.append(lan)
            if lan.coordinate == land.at_west:
                land.neighbor.append(lan)
            if lan.coordinate == land.at_east:
                land.neighbor.append(lan)
            else:
                continue
    
    def print_list_in_newline(self):
        for n in self.learnedTeck:
            return n

    def display_toolbar(self):
        self.draw_slab(0,0,120,780) # draw mesu slab
        self.topause.drawButton()
        self.nextRound.drawButton()
        label_font = pg.font.Font(self.genericFont, 13)
        #minifont = pg.font.Font(self.genericFont, 8)
        score_label = label_font.render("Score: " + str(self.score), True, (0,0,0))
        pop_label = label_font.render("Pop: " + str(self.clan_population), True, (0,0,0))
        grass_knoledge_label = label_font.render("Grass Teck: " + str(self.grassKwoledge), True, (0,0,0))
        water_knoledge_label = label_font.render("Water Teck: " + str(self.waterKwoledge), True, (0,0,0))
        rock_knoledge_label = label_font.render("Rock Teck: " + str(self.rockKwoledge), True, (0,0,0))
        animals_knoledge_label = label_font.render("Animals Teck: " + str(self.animalsKwoledge), True, (0,0,0))
        trees_knoledge_label = label_font.render("Trees Teck: " + str(self.treesKwoledge), True, (0,0,0))
        number_learned_teck = len(self.learnedTeck)
        number_teck_label = label_font.render("N of Tecks: " + str(number_learned_teck), True, (0,0,0))
        rounds_label1 = label_font.render("Rounds " , True, (0,0,0))
        rounds_label2 = label_font.render("Remaining: " + str(self.round), True, (0,0,0))
        player_name_label1 = label_font.render("Player: " , True, (0,0,0))
        player_name_label2 = label_font.render(str(self.playerName), True, (0,0,0))
        #tecks_label = minifont.render("TEKS " + str(self.learnedTeck[0]), True, (0,0,0))

        self.screen.blit(score_label, (10, 200))
        self.screen.blit(pop_label, (10, 250))
        self.screen.blit(number_teck_label, (10, 300))
        
        self.screen.blit(animals_knoledge_label, (10, 350)) 
        self.screen.blit(water_knoledge_label, (10, 400)) 
        self.screen.blit(trees_knoledge_label, (10, 450)) 
        self.screen.blit(rock_knoledge_label, (10, 500))
        self.screen.blit(grass_knoledge_label, (10, 550))
        self.screen.blit(rounds_label1, (10, 650))
        self.screen.blit(rounds_label2, (10, 670))
        self.screen.blit(player_name_label1, (10, 730))
        self.screen.blit(player_name_label2, (10, 760))
        #self.screen.blit(tecks_label, (10, 650)) 
    
    def display_halloffame(self):
        label_font = pg.font.Font(self.genericFont, 13)
        self.draw_slab(self.screen_width/2-400, 200, 250, 320)
        #alloffameLabel = label_font.render("ALL OF FAME " , True, (0,0,0))
        #leadersLabel = label_font.render("ALL OF FAME " , True, (0,0,0))
        
        top10_dic = {}
        if os.path.isfile('score.txt'):
            writefile = open('score.txt','r')
            for line in writefile:
                #if line == "\n":
                    #continue
                #top10.append(float(line))
                #top10.sort(reverse=True)
                key, value = line.split()
                top10_dic[key] = value
                edited = []
                #d = {"a":1, "b":2, "c":3}
                sortedTop10 = sorted(top10_dic.items(),key=operator.itemgetter(1),reverse=True)
                


        n1 = str(sortedTop10[0])
        n2 = str(sortedTop10[1])
        n3 = str(sortedTop10[2])

        b = "!'@#()$"
        for char in b:
            n1 = n1.replace(char, "")
            n2 = n2.replace(char, "")
            n3 = n3.replace(char, "")
            
        c = ","
        for char in c:
            n1 = n1.replace(char, " :  ")
            n2 = n2.replace(char, " :  ")
            n3 = n3.replace(char, " :  ")
        
        alloffameLabel = label_font.render("ALL OF FAME " , True, (0,0,0))
        #leadersLabel = label_font.render(str(cd), True, (0,0,0))
        
        #pos1label = label_font.render(str(sortedTop10[0]).strip("''()"), True, (0,0,0))
        #pos2label = label_font.render(str(sortedTop10[1]).strip("''()"), True, (0,0,0))
        #pos3label = label_font.render(str(sortedTop10[2]).strip("''()"), True, (0,0,0))

        pos1label = label_font.render(str(n1), True, (0,0,0))
        pos2label = label_font.render(str(n2), True, (0,0,0))
        pos3label = label_font.render(str(n3), True, (0,0,0))
        
        self.screen.blit(alloffameLabel, (self.screen_width/2-380, 210))
        #self.screen.blit(leadersLabel, (self.screen_width/2-380, 230))
        
        self.screen.blit(pos1label, (self.screen_width/2-380, 230))
        self.screen.blit(pos2label, (self.screen_width/2-380, 250))
        self.screen.blit(pos3label, (self.screen_width/2-380, 270))


         
    def display_game_over(self):
        label_font = pg.font.Font(self.genericFont, 13)
        self.game_over = True
        while self.game_over:
            
            self.draw_slab(self.screen_width/2-100, self.screen_height/2, 600,400)
            #self.new_teck_button_event.drawButton()
            self.back_to_menu.drawButton()

            self.draw_text("Game Over!",30,self.screen_width/2+180,self.screen_height/2+50)
            
            rounds_label2 = label_font.render("You Scored: " + str(self.score), True, (0,0,0))
            self.screen.blit(rounds_label2, (self.screen_width/2+140, self.screen_height/2+100))
            
            
            self.clock.tick(10)
            
            
            if self.back_to_menu.checkifpressed() == True:
                if os.path.isfile('highscore.txt'):
                    writefile = open('highscore.txt','a')
                else:
                    writefile = open('highscore.txt','w')
            
                writefile.write("\n"+ str(self.playerName) + " " + str(self.score))
                
                self.round = 7
                self.diplay_menu()
                self.game_over = False
            for event in pg.event.get():
            
                if event.type == pg.QUIT:
                    self.game_over = False
                    #pg.quit()
        
            pg.display.update()
        pg.quit()
            
            
    def new_game(self):
        #pg.mixer.music.load("menu.wav")
        #pg.mixer.music.play(-1)                                      #   MUSIC PLAY IN LOOP WHEN GAME IS STARTED
        #label_font = pg.font.Font(self.genericFont, 20)
        #score_label = label_font.render("Score: " + str(self.score), True, (0,0,0))
        #pop_label = label_font.render("Pop: " + str(self.clan_population), True, (0,0,0))
        #self.world.screen.blit(score_label, (10, 150))
        #self.request_player_name()
        self.is_game = True
        
        self.init_all_res()  # all resurces of each land are set
        self.establish_starting_land()
        self.establish_settling_blocks()
        
        for lanes in self.continent:
            self.allocate_neighbors(lanes)


        self.request_player_name()
        while self.is_game:
                
            self.screen.fill(self.black)
            
            #self.add_teck_bonuses()
            #self.add_teck_bonuses()
            
            #self.draw_slab(0,0,120,780) # draw mesu slab
            self.display_toolbar()
            #self.topause.drawButton() # draw 'menu' button
            #self.nextRound.drawButton() # draw 'next round' button
            #self.clan_population = self.land1.all_citizens + self.land2.all_citizens + self.land3.all_citizens +self.land4.all_citizens + self.land5.all_citizens + self.land6.all_citizens + self.land7.all_citizens +self.land8.all_citizens + self.land9.all_citizens + self.land10.all_citizens + self.land11.all_citizens + self.land12.all_citizens + self.land13.all_citizens + self.land14.all_citizens + self.land15.all_citizens +self.land16.all_citizens + self.land17.all_citizens + self.land18.all_citizens
            self.calculate_clan_population()
            self.calculate_score()
            #self.calculate_teck_progress()
            #self.check_for_new_discovery()
            #self.screen.blit(score_label, (10, 200))
            #self.screen.blit(pop_label, (10, 250))
            
            for land in self.continent:
                land.calculate_tot_civ()
            for land in self.continent:
                land.draw_all_res()
            for land in self.continent:
                if land.isSettled == True:
                    land.land_info.drawButton()

            for land in self.continent:
                if land.isSettled == False:
                    land.draw_new_fog()
            
            
            for land in self.continent:
                while land.travellers > 0:
                    self.display_travel_destination(land)
                    
                    
            self.check_all_infobutt_press()
            
            
            self.check_if_nextround_ispressed()
            

            self.update()

            if self.round == 0:
                self.display_game_over()


            #self.calculate_clan_population()
            #self.calculate_score()
            self.game_display.fill(self.black)
            self.draw_text(
                    "fps={}".format(round(self.clock.get_fps())), 
                    25,
                    50,
                    30
                )
                
            if self.topause.checkifpressed() == True:
                #pg.mixer.music.pause()                        #   MUSIC PAUSE WHEN MESU IS CLICKED
                #self.thinclick_sound.play()
                self.diplay_menu()
                #pg.mixer.music.pause()
                self.is_game = False
            #self.screen.blit(score_label, (10, 200))
            #self.screen.blit(pop_label, (10, 250)) 
            self.clock.tick(10)
            for rounds in range (20):
                pass
            
            for event in pg.event.get():
                
                if event.type == pg.QUIT:
                    self.is_game = False
                    #pg.quit()
                
            pg.display.update()
        pg.quit()
        

        
    def resume_game(self):
        #pg.mixer.music.load("menu.wav")
        #pg.mixer.music.play(-1)         #pg.mixer.music.unpause()     # MUSIC UN-PAUSE WHEN RESUME THE GAME
        label_font = pg.font.Font(self.genericFont, 20)
        score_label = label_font.render("Score: " + str(self.score), True, (0,0,0))
        pop_label = label_font.render("Pop: " + str(self.clan_population), True, (0,0,0))
        self.is_game = True
        
        while self.is_game:
            #self.add_teck_bonuses()
            self.screen.fill(self.black)
            #self.add_teck_bonuses()
            self.display_toolbar()
            #self.draw_slab(0,0,120,780)
            #self.clan_population = self.land1.all_citizens + self.land2.all_citizens + self.land3.all_citizens +self.land4.all_citizens + self.land5.all_citizens + self.land6.all_citizens + self.land7.all_citizens +self.land8.all_citizens + self.land9.all_citizens + self.land10.all_citizens + self.land11.all_citizens + self.land12.all_citizens + self.land13.all_citizens + self.land14.all_citizens + self.land15.all_citizens +self.land16.all_citizens + self.land17.all_citizens + self.land18.all_citizens
            self.calculate_clan_population()
            self.calculate_score()
            #self.calculate_teck_progress()
            #self.check_for_new_discovery()
            #self.screen.blit(score_label, (10, 200))
            #self.screen.blit(pop_label, (10, 250))     
            #self.topause.drawButton()
            #self.nextRound.drawButton()
            
            
            for land in self.continent:
                land.calculate_tot_civ()
            
            for land in self.continent:
                land.draw_all_res()
            
            for land in self.continent:
                if land.isSettled == True:
                    land.land_info.drawButton()

            for land in self.continent:
                if land.isSettled == False:
                    land.draw_new_fog()
            
            for land in self.continent:
                if land.travellers > 0:
                    self.display_travel_destination(land)
                    

            
            
            
            
            self.check_all_infobutt_press()
            
            
            self.check_if_nextround_ispressed()
            
            self.update()

            if self.round == 0:
                self.display_game_over()
            
            
            
            self.game_display.fill(self.black)
            self.draw_text(
                "fps={}".format(round(self.clock.get_fps())), 
                25,
                50,
                30
            )
            
            if self.topause.checkifpressed() == True:
                #pg.mixer.music.pause()                       #  MUSIC PAUSE IF MENU IS CLICKED
                #self.thinclick_sound.play()
                self.diplay_menu()
                self.is_game = False

            #self.screen.blit(score_label, (10, 200))
            #self.screen.blit(pop_label, (10, 250)) 

            self.clock.tick(10)
            for rounds in range (20):
                pass
        
            for event in pg.event.get():
            
                if event.type == pg.QUIT:
                    self.is_game = False
                #pg.quit()
            
            pg.display.update()
        pg.quit()
            
            
        
            
            

class ToPLayLoop():
    pressed = False
    def __init__(self, World, x, y, text, width, height):
        self.world = World
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
            
        self.world.draw_shades(self.x, self.y, self.width, self.height)
        #pg.draw.line(self.world.screen, self.world.white, (self.x, self.y), (self.x + self.width, self.y), 2)
        #pg.draw.line(self.world.screen, self.world.black, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)
        #pg.draw.line(self.world.screen, self.world.black, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
        #pg.draw.line(self.world.screen, self.world.white, (self.x, self.y), (self.x, self.y + self.height), 2)
		
		
		#pg.draw.line(self.world.screen, self.world.black, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)
        
        font = pg.font.Font(self.world.genericFont, 30)
        text_img = font.render(self.text, True, self.text_col)
        text_len = text_img.get_width()
        self.world.screen.blit(text_img, (self.x + int(self.width /2) -int(text_len /2), self.y + 5))
        return action

class Pause():
    pressed  = False
    def __init__(self, World, x, y):
        self.world = World
        self.x = x
        self.y = y
        
        
        self.pause_click = False
        self.button_col = (18, 161, 53)
        self.hover_col = (75,225,225)
        self.text_col = (255, 255, 255)
        self.click_col = (50, 150, 255)
        self.width = 180
        self.height = 40
    
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
                self.pause_click = True
                
                pg.draw.rect(self.world.screen, self.click_col, button_rect)
            elif pg.mouse.get_pressed()[0] == 0 and self.pause_click == True:
                self.pause_click = False
                
                action = True
            else:
                pg.draw.rect(self.world.screen, self.hover_col, button_rect)
        else:
            pg.draw.rect(self.world.screen, self.button_col, button_rect)
            

        #text_img = font.render(self.text, True, self.text_col)
        #text_len = text_img.get_width()
        #self.world.screen.blit(text_img, (self.x + int(self.width /2) -int(text_len /2), self.y + 5))
        return action