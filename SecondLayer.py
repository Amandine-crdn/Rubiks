from NodeClass import Node, A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, C0, C1, C2, C3, C4, C5, C6, C7
from Functions import action

colors = ["BR", "BO", "OG", "GR"]
#on cherche arete par aret en bas d'abord
down_edges = [A6, A8, A10, A11]

def out_edge_back():
    protocole_insertion = [3, 11, 2, 10, 6, 10, 7] # l' d' l d b d b'
    for pi in protocole_insertion:
        action(pi)()
    
def out_edge_left():
    protocole_insertion = [5, 11, 4, 10, 2, 10, 3] # f' d' f d l d l'
    for pi in protocole_insertion:
        action(pi)()
    
def out_edge_right():
    protocole_insertion = [1, 11, 0, 10, 4, 10, 5] # r' d' r d f d f'
    for pi in protocole_insertion:
        action(pi)()

def out_edge_up():
    protocole_insertion = [7, 11, 6, 10, 0, 10, 1] # b' d' b d  r d r'
    for pi in protocole_insertion:
        action(pi)()
    
def reverse_edge(current_edge):
    if current_edge == "OG":
        protocole_insertion = [0, 0, 10, 10, 5, 0, 0, 4, 10, 10, 0, 11, 0] # R2 D2 F' R2 F D2 R D' R"
    elif current_edge == "BO":
        protocole_insertion = [4, 4, 10, 10, 3, 4, 4, 2, 10, 10, 4, 11, 4] # F2 D2 L' F2 L D2 F D' F"
    elif current_edge == "GR":
        protocole_insertion = [6, 6, 10, 10, 1, 6, 6, 0, 10, 10, 6, 11, 6] # B2 D2 R' B2 R D2 B D' B"
    elif current_edge == "BR":
        protocole_insertion = [2, 2, 10, 10, 7, 2, 2, 6, 10, 10, 2, 11, 2] # L2 D2 B' L2 B D2 L D' L"
    for pi in protocole_insertion:
        action(pi)()

   
def edges_from_three_layer(nodes_blocked):

    for i in range(0, 4):
        for d in down_edges:
            color_node = d.get_color()
            protocole_insertion = []
            if 'R' in color_node and 'B' in color_node:
                if color_node[0] == 'R':
                    #le placer sur Vert 
                    while A10.get_color() != "RB" and A10.get_color() != "BR":
                        action(10)()
                    protocole_insertion = [3, 10, 2, 7, 2, 6, 3] #l' d l b' l b l ' 

                elif color_node[0] == 'B':
                    #le placer sur Orange
                    while A8.get_color() != "RB" and A8.get_color() != "BR":
                        action(10)()
                    protocole_insertion = [6, 11, 7, 2, 7, 3, 6] # b d ' b' l  b ' l ' b 
                nodes_blocked[0] = True

            elif 'R' in color_node and 'G' in color_node:
                if color_node[0] == 'R':
                    #le placer sur Bleu
                    while A6.get_color() != "RG" and A6.get_color() != "GR":
                        action(10)()
                    protocole_insertion = [0, 11, 1, 6, 1, 7, 0] # r d' r' b r' b' r 
                
                elif color_node[0] == 'G':
                    # Placer sur Orange
                    while A8.get_color() != "RG" and A8.get_color() != "GR":
                        action(10)()
                    protocole_insertion = [7, 10, 6, 1, 6, 0, 7] # b' d b r' b r b'
                nodes_blocked[3] = True

            elif 'O' in color_node and 'B' in color_node:
                if color_node[0] == 'B':
                    #le placer sur Red
                    while A11.get_color() != "BO" and A11.get_color() != "OB":
                        action(10)()
                    protocole_insertion = [5, 10, 4, 3, 4, 2, 5] # f' d f   l ' f  l f'
                
                elif color_node[0] == 'O':
                    # Placer sur Green 
                    while A10.get_color() != "BO" and A10.get_color() != "OB":
                        action(10)()
                    protocole_insertion = [2, 11, 3, 4, 3, 5, 2] # l d' l' f l' f ' l 
                nodes_blocked[1] = True

            elif 'O' in color_node and 'G' in color_node:
                if color_node[0] == 'G':
                    #le placer sur Red
                    while A11.get_color() != "GO" and A11.get_color() != "OG":
                        action(10)()
                    protocole_insertion = [4, 11, 5, 0, 5, 1, 4] # f d' f' r f' r' f 
                
                elif color_node[0] == 'O':
                    # Placer sur Blue 
                    while A6.get_color() != "GO" and A6.get_color() != "OG":
                        action(10)()
                    protocole_insertion = [1, 10, 0, 5, 0, 4, 1] # r' d r f' r f  r'
                nodes_blocked[2] = True

            for pi in protocole_insertion:
                action(pi)()

    return nodes_blocked
