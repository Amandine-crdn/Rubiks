# import random

# def get_random_colors():
#     #sous forme de liste pour melanger aleatoirement avec random shuffle
#     aretes = [['O','B'], ['O','W'], ['O','G'], ['O','Y'], ['G','W'], ['G','R'], ['G','Y'], ['R','W'], ['R','B'], ['R','Y'], ['B','W'], ['B','Y']]
#     for a in aretes:
#         random.shuffle(a)
#     new_aretes = []
#     for a in aretes:
#         new_aretes.append(a[0] + a[1])
#     random.shuffle(new_aretes)
    
#     coins = [['WRG', 'RGW', 'GWR'], ['WBR', 'RWB', 'BRW'], ['WOB', 'BWO', 'OBW'], ['WGO', 'GOW', 'OWG'], ['BYR', 'YRB', 'RBY'], ['BOY', 'OYB', 'YBO'], ['GRY', 'RYG', 'YGR'], ['YOG', 'GYO', 'OGY']]
#     for c in coins:
#         random.shuffle(c)
    
#     new_coins = []
#     for c in coins:
#         new_coins.append(c[0])
#     random.shuffle(new_coins)
#     #les milieux doivent respecter la coherence du rubikscub
#     milieu = ['W', 'B', 'O', 'G', 'R', 'Y'] #definit la dimension du cube dans l'espace car après ne bougera pas

#     return milieu, new_aretes, new_coins

# milieux, aretes, coins = get_random_colors()

milieux = ['W', 'B', 'O', 'G', 'R', 'Y'] #definit la dimension du cube dans l'espace car après ne bougera pas

#retirer lignes en dessous
aretes = ["WR", "WB", "WG", "WO", "BR", "BO", "BY", "OG", "OY", "GR", "GY","RY"]
# aretes = ["BO", "BY", "WR", "BR", "OG", "OY", "GR", "WB","GY", "WG", "WO", "RY"]
coins = ["WBR", "WRG", "WOB","WGO" , "BYR", "GRY", "BYO", "GYO"]
