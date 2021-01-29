import pygame as pg
import numpy as np
import random

class Map:

    def __init__(self):
        self.position = list(np.random.randint(0, 30, size = 2))
        self.longueur = random.randint(4,10)
        self.largeur = random.randint(4,10)

        if self.position[0] + self.longueur > 30 :
            d = self.position[0] + self.longueur - 30
            self.position[0] = self.position[0] - d

        if self.position[1] + self.largeur > 30 :
            d = self.position[1] + self.largeur - 30
            self.position[1] = self.position[1] - d

    def taille(self):
        return [self.longueur, self.largeur]

    def Longueur(self):
        return self.longueur

    def Largeur(self):
        return self.largeur

    def depart(self):
        return self.position

    def murs_verticaux(self):
        liste_mv = []
        for i in range(self.largeur):
            liste_mv.append([self.position[0],self.position[1]+i])
            liste_mv.append([self.position[0]+self.longueur,self.position[1]+i])

        return liste_mv

    def murs_horizontaux(self):
        liste_mh = []
        for i in range(self.longueur):
            liste_mh.append([self.position[0] + i, self.position[1]])
            liste_mh.append([self.position[0] + i, self.position[1] + self.largeur])

        return liste_mh

    
    def quadrillage_sol(self):
        liste_qs = []
        for i in range(1, self.longueur - 1):
            for j in range(1, self.largeur - 1):
                liste_qs.append([self.position[0]+i, self.position[1]+j])

        return liste_qs
