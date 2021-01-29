import pygame as pg
import numpy as np

# On crée un dictionnaire pour associer les touches appuyées à la commande qu'on veut
# Ex : si on appuie sur la flèche du haut, on voudrait que python comprenne que le personnage veut monter

Touches = {K_LEFT:37, K_UP:38, K_RIGHT:39, K_DOWN:40}

class Character:

    def __init__(self, name:str, position:np.array):
        self.name = name
        self.position = position # un array contenant l'indice des lignes et celui des colonnes
        self.inventaire = {armor:5, arms:10, life:10, gold:50, food:5, water:5}
        self.repr = '@'

    def movement(self, direction:np.array): 
        dx,dy = direction # un tuple qui contient la direction
        self.position[0] += dx
        self.position[1] += dy

        if self.position in quadrillage_sol:
            
            i, j = self.position
            if S[i][j] == 'a':
                self.inventaire(food) += 1
            elif S[i][j] == 'w':
                self.inventaire(water) += 1
            elif S[i][j] == 'A':
                self.inventaire(armor) += 1
            elif S[i][j] == 'T':
                self.inventaire(arms) += 1
            elif S[i][j] == 'o':
                self.inventaire(food) += 5

            elif S[i][j] == 'B':
                win = np.random.randint(1)
                if win == 0:
                    self.inventaire(life) -= 5
                else : 
                    self.inventaire(life) += 5  
            
            S[i][j] = '@'