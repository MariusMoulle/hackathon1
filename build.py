from character import Character
import pygame as pg
import affichage as aff
from Map import Map

pg.init()

class Game:

    def __init__(self):
        self.char_name = input("What is your name, Stranger?")
        print(f"Welcome {self.char_name}")
        self.character = Character(self.char_name)
        self.niveau = 1
        self.map = Map()
        self.play()
    
    def affichage(self):
        aff.affichage(self.map)
    
    def play(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_q:
                        running = False
                    elif event.key == pg.K_UP :
                        direction=(0,-1)
                    elif event.key == pg.K_DOWN :
                        direction=(0,1)
                    elif event.key == pg.K_RIGHT :
                        direction=(1,0)
                    elif event.key == pg.K_LEFT :
                        direction=(-1,0)
            
            self.character.movement(direction)
            
            

            

Game()
    
    
    
