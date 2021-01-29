
import pygame as pg
from random import randint

pg.init()
width=35
n,p=20,20
screen = pg.display.set_mode((width*p, width*n))
clock = pg.time.Clock()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

def avance(serpent, direction):
    x,y=serpent[-1]
    dx,dy=direction
    serpent.append((x+dx, y+dy))
    fin=serpent.pop(0)
    return fin

def avance_fruit(serpent, direction):
    x,y=serpent[-1]
    dx,dy=direction
    serpent.append((x+dx, y+dy))
    return fin

def afficher(case, color):
    x,y=case
    x*=width
    y*=width
    rect = pg.Rect(x, y, width, width)
    pg.draw.rect(screen, color, rect)



#affichage initial
screen.fill(white)
x0,y0=n//3,p//2
serpent = [(x0,y0),(x0+1,y0),(x0+2,y0)]
for elem in serpent :
    afficher(elem, black)

direction = (1,0)
dir_fut = direction


score = 0
pg.display.set_caption(f"Score: {score}")
running = True

fruit = (randint(0,p-1), randint(0,n-1))
while fruit in serpent :
    fruit = (randint(0,p-1), randint(0,n-1))
afficher(fruit, red)




while running:

    tete = serpent[-1]


    
        
    if tete in serpent[:-2]:
        running = False
    
    if tete[0]<0 or tete[0]>=p or tete[1]<0 or tete[1]>=n:
        running = False

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                running = False
            elif event.key == pg.K_UP :
                dir_fut=(0,-1)
            elif event.key == pg.K_DOWN :
                dir_fut=(0,1)
            elif event.key == pg.K_RIGHT :
                dir_fut=(1,0)
            elif event.key == pg.K_LEFT :
                dir_fut=(-1,0)
    
            somme = (direction[0]+dir_fut[0],direction[1]+dir_fut[1])
            if somme == (0,0) :
                dir_fut=direction
            else: 
                direction = dir_fut
        
    if tete == fruit:
        fruit = (randint(0,p-1), randint(0,n-1))
        while fruit in serpent :
            fruit = (randint(0,p-1), randint(0,n-1))
        afficher(fruit, red)
        score += 1
        pg.display.set_caption(f"Score: {score}")
        avance_fruit(serpent,direction)
        afficher(serpent[-1],black)
        #afficher(tete,black)
        pg.display.update()
    else:
        fin = avance(serpent, direction)
        afficher(fin, white)
        afficher(serpent[-1],black)
        pg.display.update()

    
    clock.tick(9)
    


pg.quit()
print("Game Over")
print(f"Score : {score}")


