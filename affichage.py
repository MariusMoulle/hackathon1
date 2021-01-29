
import pygame as pg
from random import randint
import numpy as np

pg.init()
width=35
n,p=20,20
screen = pg.display.set_mode((width*p, width*n))
clock = pg.time.Clock()

floor = (225, 206, 154)
wall = (97, 75, 58)
black = (0,0,0)
red = (255,0,0)
orange = (223, 109, 20)
brown = (126, 51, 0)

def draw_cases(case:np.array, color):
    x,y=case
    x*=width
    y*=width
    rect = pg.Rect(x, y, width, width)
    pg.draw.rect(screen, color, rect)

def affiche(S):
    screen.fill(black)
    for i, ligne in enumerate(S):
        for j, symbol in enumerate(ligne):
            if symbol == '.':
                draw_cases([i, j], floor)
            elif symbol == '#':
                draw_cases([i, j], orange)
            elif symbol =='+':
                draw_cases([i, j], brown)
    pg.display.update()