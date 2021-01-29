import pygame as pg
import numpy as np
import random

class Room:

    def __init__(self, x, y):
        self.position = [x, y]
        self.longueur = random.randint(4,8)
        self.largeur = random.randint(4,8)

        if self.position[0] + self.longueur >= 30 :
            d = self.position[0] + self.longueur - 31
            self.position[0] = self.position[0] - d

        if self.position[1] + self.largeur >= 30 :
            d = self.position[1] + self.largeur - 31
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
        liste_mh = []
        for i in range(self.longueur+1):
            liste_mh.append([self.position[0] + i, self.position[1]])
            liste_mh.append([self.position[0] + i, self.position[1] + self.largeur])

        return liste_mh



    def murs_horizontaux(self):
        liste_mv = []
        for i in range(1, self.largeur):
            liste_mv.append([self.position[0],self.position[1]+i])
            liste_mv.append([self.position[0]+self.longueur,self.position[1]+i])

        return liste_mv

    
    def quadrillage_sol(self):
        liste_qs = []
        for i in range(1, self.longueur):
            for j in range(1, self.largeur):
                liste_qs.append([self.position[0]+i, self.position[1]+j])

        return liste_qs




#map1 = Map()
#print(map1.murs_horizontaux(), map1.murs_verticaux(), map1.portes())

class Map(Room) : 
    def __init__(self):
        self.room1 = Room(2, 2)
        self.room2 = Room(12, 20)
        self.porte1 = [self.room1.position[0] + self.room1.largeur, self.room1.position[1]+2]
        self.porte2 = [self.room2.position[0] + 2, self.room2.position[1]]

#"Ahlala qu'est-ce qu'il faut pas faire pour rester éveillés."

    def surface_sol(self):
        sol = self.room1.quadrillage_sol() + self.room2.quadrillage_sol()
        return sol
    
    def prix_au_metre_carre(self):
        return np.random.randint(10000, 15000)

    def prix_total(self):
        return self.surface_sol()*self.prix_au_metre_carre()

    def dim(self):
        return (30, 30)

    def surface_portes(self):
        return self.porte1, self.porte2

    def chemins(self):
        chemin = [self.porte1]

        while chemin[-1][0] < self.porte2[0]:
            x, y = chemin[-1][0], chemin[-1][1]
            chemin.append([x+1, y])
        
        while chemin[-1][1] < self.porte2[1]:
            x, y = chemin[-1][0], chemin[-1][1]
            chemin.append([x, y+1])

        return chemin

    
    



        
            
map1 = Map()
print(map1.chemins(), map1.surface_portes())








        

