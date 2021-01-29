import pygame as pg
import numpy as np
import random

class Room:

    def __init__(self):
        self.position = list(np.random.randint(0, 30, size = 2))
        self.longueur = random.randint(4,10)
        self.largeur = random.randint(4,10)

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

    def portes(self):
        murs = self.murs_horizontaux() + self.murs_verticaux()
        a1 = random.choice(murs)
        a2 = random.choice(murs)
        while a2 == a1:
            a2 = random.choice(murs)
        return a1, a2


#map1 = Map()
#print(map1.murs_horizontaux(), map1.murs_verticaux(), map1.portes())

class Map(Room) : 
    def __init__(self):
        self.room1 = Room()
        self.room2 = Room()

        while abs(room1.depart()[0] - room2.depart()[0]) <= max(room1.Largeur(), room2.Largeur()) + 3
             or abs(room1.depart()[1] - room2.depart()[1]) <= max(room1.Longueur(), room2.Longueur()):
             self.room2 = Room()

#"Ahlala qu'est-ce qu'il faut pas faire pour rester éveillés."

    def surface_sol(self):
        sol = room1.quadrillage_sol() + room2.quadrillage_sol()
        return sol
    
    def prix_au_metre_carre(self):
        return np.random.randint(10000, 15000)

    def prix_total(self):
        return surface_sol()*prix_au_metre_carre()

    def dim(self):
        return (30, 30)

    def surface_portes(self):
        return room1.portes()+room2.portes()

    def chemins(self):
        #on prend la porte 0 d'une room comme sortie et la porte 1 comme entrée
        e1 = room1.portes()[0]
        s1 = room1.portes()[1]
        e2 = room2.portes()[0]
        s2 = room2.portes()[1]

        chemin1 = []
        while e2 not in chemin1 : 






        

