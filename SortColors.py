import random

#faire rentrer en input les couleurs
    # face 1
    # coin, arete, coin,
    # arete, milieu, arete,
    # coin, arete, coin

    # face 2
    # x x x
    # arrete, milieu, arete
    # coin, arete, coin

    # face 3
    # x x x
    # x, milieu, arete
    # x, arete, coin

    # face 4
    # x x x
    # x milieu aretes
    # x arete coin

    # face 5
    # x x x
    # x milieu x
    # x arete x

    # face 6
    # x x x
    # x milieu x
    # x x x

def define_place(milieu, aretes, coins):
    face1, face2,face3, face4, face5, face6  = {}, {}, {}, {}, {}, {}
    new_colors = []
    #coin
    face1[1] = coins[0][0]
    face2[1] = coins[0][1]
    face5[3] = coins[0][2]
    #arete
    face1[2] = aretes[0][0]
    face5[2] = aretes[0][1] 
    #coin
    face1[3] = coins[1][0]
    face5[1] = coins[1][1]
    face4[3] = coins[1][2]

    #arete
    face1[4] = aretes[1][0]
    face2[2] = aretes[1][1] 
    #milieu
    face1[5] = milieu[0]
    #arete
    face1[6] = aretes[2][0]
    face4[2] = aretes[2][1]

    #coin
    face1[7] = coins[2][0]
    face3[1] = coins[2][1]
    face2[3] = coins[2][2]
    #arete
    face1[8] = aretes[3][0]
    face3[2] = aretes[3][1] 
    #coin
    face1[9] = coins[3][0]
    face4[1] = coins[3][1] 
    face3[3] = coins[3][2] 

    #arete
    face2[4] = aretes[4][0]
    face5[6] = aretes[4][1] 
    #milieu
    face2[5] = milieu[1]
    #arete
    face2[6] = aretes[5][0]
    face3[4] = aretes[5][1]

    #coin
    face2[7] = coins[4][0]
    face6[7] = coins[4][1]
    face5[9] = coins[4][2]
    #arete
    face2[8] = aretes[6][0]
    face6[4] = aretes[6][1] 
    #coin
    face2[9] = coins[5][0]
    face3[7] = coins[5][1]
    face6[1] = coins[5][2]

    #milieu
    face3[5] = milieu[2]
    #arete
    face3[6] = aretes[7][0]
    face4[4] = aretes[7][1]

    #arete
    face3[8] = aretes[8][0]
    face6[2] = aretes[8][1] 
    #coin
    face3[9] = coins[6][0]
    face4[7] = coins[6][1]
    face6[3] = coins[6][2]

    #milieu
    face4[5] = milieu[3]
    #arete
    face4[6] = aretes[9][0]
    face5[4] = aretes[9][1]

    #arete
    face4[8] = aretes[10][0]
    face6[6] = aretes[10][1] 
    #coin
    face4[9] = coins[7][0]
    face5[7] = coins[7][1]
    face6[9] = coins[7][2]

    #milieu
    face5[5] = milieu[4]

    #arete
    face5[8] = aretes[11][0]
    face6[8] = aretes[11][1] 

    #milieu
    face6[5] = milieu[5]

    #trier selon le numero de case
    faces = [face1, face2, face3, face4, face5, face6]
    for f in faces:
        for i in range(1, 10):
            new_colors.append(f[i])
    
    return new_colors



def get_random_colors_test():
    #sous forme de liste pour melanger aleatoirement avec random shuffle
    aretes = [['O','B'], ['O','W'], ['O','G'], ['O','Y'], ['G','W'], ['G','R'], ['G','Y'], ['R','W'], ['R','B'], ['R','Y'], ['B','W'], ['B','Y']]
    for a in aretes:
        random.shuffle(a)
    new_aretes = []
    for a in aretes:
        new_aretes.append(a[0] + a[1])
    random.shuffle(new_aretes)
    
    coins = [['WRG', 'RGW', 'GWR'], ['WBR', 'RWB', 'BRW'], ['WOB', 'BWO', 'OBW'], ['WGO', 'GOW', 'OWG'], ['BYR', 'YRB', 'RBY'], ['BOY', 'OYB', 'YBO'], ['GRY', 'RYG', 'YGR'], ['YOG', 'GYO', 'OGY']]
    for c in coins:
        random.shuffle(c)
    
    new_coins = []
    for c in coins:
        new_coins.append(c[0])
    random.shuffle(new_coins)
    #les milieux doivent respecter la coherence du rubikscub
    milieu = ['W', 'B', 'O', 'G', 'R', 'Y'] #definit la dimension du cube dans l'espace car après ne bougera pas

    return milieu, new_aretes, new_coins

def get_random_colors():
    colors = []
    #sous forme de liste pour melanger aleatoirement avec random shuffle
    aretes = [['O','B'], ['O','W'], ['O','G'], ['O','Y'], ['G','W'], ['G','R'], ['G','Y'], ['R','W'], ['R','B'], ['R','Y'], ['B','W'], ['B','Y']]
    for a in aretes:
        random.shuffle(a)
    
    coins = [['WRG', 'RGW', 'GWR'], ['WBR', 'RWB', 'BRW'], ['WOB', 'BWO', 'OBW'], ['WGO', 'GOW', 'OWG'], ['BYR', 'YRB', 'RBY'], ['BOY', 'OYB', 'YBO'], ['GRY', 'RYG', 'YGR'], ['YOG', 'GYO', 'OGY']]
    for c in coins:
        random.shuffle(c)
    
    milieu = ['W', 'B', 'O', 'G', 'R', 'Y'] #definit la dimension du cube dans l'espace car après ne bougera pas
  
    new_coins = []
    for c in coins:
        new_coins.append(c[0])
    colors.extend(aretes)
    colors.extend(new_coins)
    random.shuffle(colors)
    colors.extend(milieu) #les milieux doivent respecter la coherence du rubikscub

    return colors


def sort_colors(colors):
    milieu = []
    aretes = []
    coins = []
    for c in colors:
        milieu.append(c) if len(c) == 1 else aretes.append(c) if len(c) == 2 else coins.append(c)
    return milieu, aretes, coins

milieux, aretes, coins = get_random_colors_test()
# colors = get_random_colors()
# milieu, aretes, coins = sort_colors(colors)
# new_colors = define_place(milieu, aretes, coins)


