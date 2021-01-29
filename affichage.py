

def affichage(map1):
    
    n, p = 30,30
    #print(n, p)
    S = [[' ' for j in range(p)] for i in range(n)]
    #print(S)
    for mur_vert in map1.murs_horizontaux():
        i, j = mur_vert
        S[i][j] = '|'

    for mur_hor in map1.murs_verticaux():
        i, j = mur_hor
        S[i][j] = '-'
    
    for sol in map1.quadrillage_sol():
        i, j = sol
        S[i][j] = '.'
    
    print(''.join([''.join(S[i]) + '\n' for i in range(len(S))]))