
import pygame as pg
from random import randint

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


def affichage(map1):
    n, p = 30,30
    #print(n, p)
    S = [[' ' for j in range(p)] for i in range(n)]
    #print(S)
    for mur_vert in map1.murs_verticaux():
        i, j = mur_vert
        S[i][j] = '|'

    for mur_hor in map1.murs_horizontaux():
        i, j = mur_hor
        S[i][j] = '-'
    
    for sol in map1.quadrillage_sol():
        i, j = sol
        S[i][j] = '.'
    
    print(''.join([''.join(S[i]) + '\n' for i in range(len(S))]))

def draw_cases(case:np.array, color):
    x,y=case
    x*=width
    y*=width
    rect = pg.Rect(x, y, width, width)
    pg.draw.rect(screen, color, rect)

def pixels(S):
    screen.fill(black)
    for i, ligne in enumerate(S):
        for j, symbol in enumerate(ligne):
            elif symbol == '.':
                draw_cases([i, j], floor)
            elif symbol == '#':
                draw_cases([i, j], orange)
            elif symbol =='+':
                draw_cases([i, j], brown)

pixels()