

def affichage(map1):
    n, p = map1.dims
    S = [['_' for j in range(p)] for i in range(n)]
    for mur_vert in map1.wall('v'):
        i, j = mur_vert
        S[i][j] = '|'

    for mur_hor in map1.wall('h'):
        i, j = mur_hor
        S[i][j] = '-'
    
    for sol in map.floor():
        i, j = sol
        S[i][j] = '.'
    
    print([S[i].join() + '\n' for i in range(len(S))].join())