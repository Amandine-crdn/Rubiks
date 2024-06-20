from Functions import action


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