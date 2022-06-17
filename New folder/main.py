
import pygame as pg 
from game.world import World

def main():
    running = True
    

    pg.init()
    pg.mixer.init()
    
    w = World()
    

    while running:

        # start menu goes here
        w.diplay_menu()
        
            
            
        

        

if __name__ == "__main__":
    main()