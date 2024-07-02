from Utils.Functions import action

def insert_corner(index):
    list_out = []
    if index == 0:
        list_out = [6, 10, 7] #C0: b d b'
    elif index == 1:
        list_out = [7, 11, 6] #C1: b' d' b 
    elif index == 2:
        list_out = [5, 11, 4] #C2: f' d' f
    elif index == 3:
        list_out = [4, 10, 5] #C3: f d f'

    for o in list_out:
        action(o)()

def out_corner(index):
    list_out = []
    if index == 0:
        list_out = [3, 10, 2] #C0: l' d l 
    elif index == 1:
        list_out = [0, 10, 1] #C1: r d r' 
    elif index == 2:
        list_out = [2, 10, 3] #C2: l d l' 
    elif index == 3:
        list_out = [1, 10, 0] #C3: r' d r
    
    for o in list_out:
        action(o)()
    
def swap_corner(index, zone_white): # 7 coups : sexys mooves
    list_out = []
    if index == 0:
        if zone_white == 2:
            #si le blanc est sur le cote 1
            list_out = [3, 10, 2, 6, 10, 7] # l' d l b d  b'
        elif zone_white == 1:
            #si le blanc est sur le cote 2
            list_out = [3, 11, 2, 10, 3, 11, 2] # l' d' l d l'  d' l

    elif index == 1:
        if zone_white == 1:
            #si le blanc est sur le cote 1
            list_out = [0, 11, 1, 7, 11, 6] # r d' r' b' d' b
        elif zone_white == 2:
            #si le blanc est sur le cote 2
            list_out = [0, 10, 1, 11, 0, 10, 1] # r d r' d' r  d r'

    elif index == 2:
        if zone_white == 1:
            #si le blanc est sur le cote 1
            list_out = [2, 11, 3, 5, 11, 4] # l d' l' f' d' f
        elif zone_white == 2:
            #si le blanc est sur le cote 2
            list_out = [2, 10, 3, 11, 2, 10, 3] # l d l' d' l  d l'

    elif index == 3:
        if zone_white == 1:
            #si le blanc est sur le cote 1
            list_out = [1, 11, 0, 10, 1, 11, 0] # r' d' r d r'  d' r
        if zone_white == 2:
            #si le blanc est sur le cote 2
            list_out = [1, 10, 0, 4, 10, 5] # r' d r f d f'




    for o in list_out:
        action(o)()
