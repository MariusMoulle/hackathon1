# from character import Character
import pygame as pg
import affichage as aff
from Map import Map



class Game:

    def __init__(self):
        self.char_name = input("What is your name, Stranger?")
        print(f"Welcome {self.char_name}")
        #self.main_char = Character(self.char_name)
        self.niveau = 1
        self.map = Map()
        self.process()
    
    def affichage(self):
        aff.affichage(self.map)
    
    def process(self):
        self.affichage()

Game()
    
    
    
