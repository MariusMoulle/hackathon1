from character import Character
import pygame as pg
import affichage as aff
from Map import Map
import numpy as np

pg.init()

class Game:

    def __init__(self):
        self.char_name = input("What is your name, Stranger? ")
        print(f"Welcome {self.char_name}")
        self.map = Map()
        depart = self.map.surface_sol()[0]
        self.character = Character(self.char_name, self, depart)
        self.play()
        

    def affiche(self):
        S = self.grille
        aff.affichage(S)
    
    def combine(self):
        n, p = self.map.dim()
        S = [[' ' for j in range(p)] for i in range(n)]
        for sol in self.map.surface_sol():
            i, j = sol
            S[i][j] = '.'

        # for chemin in self.map.chemins():
        #     i, j = chemin
        #     S[i][j] = '#'
        
        # for porte in self.map.portes():
        #     i, j = porte
        #     S[i][j] = '+'
        
        i, j = self.character.position
        S[i][j] = '@'

        # for objet in self.map.objets():
        #     if objet.position == self.character.position:
        #         self.map.remove(objet)
        #         self.character.inventaire[objet.type] += objet.valeur
        #     i, j = objet.position
        #     S[i][j] = objet.repr
        
        self.grille = S

    def play(self):
        running = True
        while running:
            direction = (0,0)
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
            self.combine()
            self.affiche()


            

            

Game()
    
    
    
