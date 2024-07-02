from CubeClass import cube
from NodeClass import Node, A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, C0, C1, C2, C3, C4, C5, C6, C7
from Functions import action
from utils.SolveWhiteCorners import insert_corner, out_corner, swap_corner
from utils.SolveWhiteCross import resolve_cross, backtracking, speeder_path, ft_protection, turn_edge_front, turn_edge_back, turn_edge_left, turn_edge_right
from Rotations import Rien, Right, RightPrime, Left, LeftPrime, Up, UpPrime, Back, BackPrime, Down, DownPrime, Front, FrontPrime, R2, L2, B2, D2, U2, F2
from SecondLayer import edges_from_three_layer, out_edge_back, out_edge_left, out_edge_right, out_edge_up
from ThirdLayer import check_cross, make_cross, check_L, check_trait
from Simulation import nodes_blocked, map_node, nodes_index, colors

def compass_corners():
    final_color = ["WBR", "WRG", "WOB", "WGO"]
    whites_corners = [C0, C1, C2, C3]
    for index, w in enumerate(whites_corners):    
        if w.get_color() == final_color[index]:
            continue
        zone_white = 1 if w.get_color()[1] == 'W' else 2
        swap_corner(index, zone_white)    

def compass_edges():
    list_whites_nodes = [A0, A1, A2, A3]
    switch_edge = [turn_edge_back, turn_edge_left, turn_edge_right, turn_edge_front] 
    for node_index, n in enumerate(list_whites_nodes, start=0):
        if n.get_color()[0] != 'W':
            switch_edge[node_index]()








########################################################################## FIRST LAYER
def first_layer(index):
    print("index ", index)
    from Simulation import nodes_blocked, map_node, nodes_index, colors


    #-----------------------------------------------------------------------------edges
    best_nodes_blocked = nodes_blocked[index]
    for i in range(0, 4):
        best_nodes_blocked[i] = None
    best_map_node = map_node[index]
    best_node_index = nodes_index[index]
    best_colors = colors[index]

    count = 0
    while count != 4: #mettre 4 pour les 4 aretes
        list_path_to_resolve_node, best_n = resolve_cross(best_node_index, best_colors, best_map_node, best_nodes_blocked)
        target_path = speeder_path(list_path_to_resolve_node) 
        if target_path : #si l'action existe, l'executer 
            #proteger les best_n, executer l'action et remettre les best_n à leur place
            ft_protection(best_n, target_path)  
            #bloquer le noeud une fois actionS réalisées
            for i in range(0, 4):
                if target_path[0] == i:
                    best_n[best_node_index[i]] = best_map_node[best_node_index[i]]
            
        count += 1
    #faire le renversement des aretes à la fin du backtracking
    #orienter les aretes vers leur centre
    print("\n🐋 Cross done :")
    cube.print_cube()

    print("\n🐋 Edges'Cross Compass : ")
    compass_edges()
    cube.print_cube()





    #-----------------------------------------------------------------------------corners
    nodes_blocked = {
        0: None,
        1: None,
        2: None,
        3: None
    }

    whites_corners = [C0, C1, C2, C3]
    colors = ['RB', 'RG', 'BO', 'OG']
    nodes = [C0, C1, C2, C3, C4, C5, C6, C7]
    down_corners = [C4, C5, C6, C7]
        
    for index_corner, c in enumerate(whites_corners):
        #pour chaque coin on va chercher sa couleur
        for index_node, n in enumerate(nodes):
            if nodes_blocked[index_corner] is None and {'W', colors[index_corner][0], colors[index_corner][1]}.issubset(n.get_color()) :
            # if 'W' in n.get_color() and colors[index_corner][0] in n.get_color() and colors[index_corner][1] in n.get_color() and nodes_blocked[index_corner] is None : #on choppe le node qu'on veut ramener à c
                #on chercher à savoir c'est quel node:
                if index_node == index_corner: #si le noeud est au bon endroit
                    nodes_blocked[index_corner] = n
                    continue
                elif index_node >= 0 and index_node <= 3: #faire sortir le node recherché pour le placer apres
                    out_corner(index_node)
    
                while True:
                    if 'W' in down_corners[index_corner].get_color() and colors[index_corner][0] in down_corners[index_corner].get_color() and colors[index_corner][1] in down_corners[index_corner].get_color() : #on choppe le node qu'on veut ramener à c
                        break
                    action(10)()
                insert_corner(index_corner)
    print("\n🐋 Corners' Done : ")
    cube.print_cube()
    # orienter les coins

    compass_corners()
    print("\n🐋 Corners' White Face Cube Done : ")
    cube.print_cube()








########################################################################## SECOND LAYER

def second_layer():
    
    nodes_blocked = { 0: False, 1: False, 2: False, 3: False }

    colors = ["BR", "BO", "OG", "GR"]
    # down_edges = [A6, A8, A10, A11]
    center_edges = [A4, A5, A7, A9]
    functions_out = [out_edge_back, out_edge_left, out_edge_right, out_edge_up]

    #on vient regarder si les aretes sont bien placées
    for index, d in enumerate(center_edges):
        if d.get_color() == colors[index]:
            nodes_blocked[index] = True
    
    # remplir le 2eme etage par le 3eme, puis checker s'il faut sortir
    all_locked = all(nodes_blocked.values())
    while all_locked is False:
        for i in range(0, 4):
            nodes_blocked = edges_from_three_layer(nodes_blocked)
            if nodes_blocked[i] == False:
                functions_out[i]()                       
        all_locked = all(nodes_blocked.values())
    
    print("\n🐋 Second Layer Done : ")
    cube.print_cube()
    




########################################################################## THIRD LAYER


#etage 3
def third_layer(): # L R B F R' L' 
    #checker si la cross est deja faite
    print("\n🔻")
    if check_cross() == False:
        print("false")
        check_L()

    cube.print_cube()


    #si 2 aretes opposé bien placer en fonction des milieux:
        #mettre ce trait là face à nous et faire l'algo pour mettre en 2 à coté
        #finir par encore l'algo 
    #si 2 aretes a cote:
        # faire une seule fois l'algo

        # 🍪 r u r' u r u2 r' dans l'aute sens  et replacer avec un down
        # l d l' d l d2 l'
        #liste_actions = [2, 10, 3, 10, 2, 10, 10, 3]



    #bien placer les coins en fonction de la couleur de ces centres
    # 🍪 l' u r  u' l u r' u' à l'envers
    # r' d l' d' r d l' d'
    #liste_actions = [1, 10, 3, 11, 0, 10, 3, 11]


    #faire le sexy move sur les 4 coins
    #🍪 la on est à l'endroit, a faire sur les coins qui faut changer
    #  r u r' u'    #puis down
    #fin... avec je pense 150 coups à la fin

    #

    
#si un motif de rubik est deviné faire son mouvement inverse


    



 


