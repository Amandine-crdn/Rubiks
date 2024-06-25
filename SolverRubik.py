from CubeClass import cube
from NodeClass import Node, A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, C0, C1, C2, C3, C4, C5, C6, C7
from Functions import action, optimize_moves
from utils.SolveWhiteCorners import insert_corner, out_corner, swap_corner
from utils.SolveWhiteCross import resolve_cross, backtracking, speeder_path, ft_protection, turn_edge_up, turn_edge_back, turn_edge_left, turn_edge_right
from Rotations import Rien, Right, RightPrime, Left, LeftPrime, Up, UpPrime, Back, BackPrime, Down, DownPrime, Front, FrontPrime, R2, L2, B2, D2, U2, F2
from SecondLayer import edges_from_three_layer, out_edge_back, out_edge_left, out_edge_right, out_edge_up
from ThirdLayer import to_have_trait, check_L, check_trait

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
    switch_edge = [turn_edge_back, turn_edge_left, turn_edge_right, turn_edge_up] 
    for node_index, n in enumerate(list_whites_nodes, start=0):
        if n.get_color()[0] != 'W':
            switch_edge[node_index]()

########################################################################## FIRST LAYER
def first_layer():
    #-----------------------------------------------------------------------------edges
    nodes_blocked = {
        0: None,
        1: None,
        2: None,
        3: None
    }

    count = 0
    while count != 4: #mettre 4 pour les 4 aretes
        list_path_per_edge, nodes_blocked = resolve_cross(nodes_blocked)
        action_temp = speeder_path(list_path_per_edge) 
        if action_temp : #si l'action existe, l'executer 
            #proteger les nodes_blocked, executer l'action et remettre les nodes_blocked à leur place
            ft_protection(nodes_blocked, action_temp)  
            #bloquer le noeud une fois actionS réalisées
            if action_temp[0] == 0:
                nodes_blocked[0] = A0
            elif action_temp[0] == 1:
                nodes_blocked[1] = A1
            elif action_temp[0] == 2:
                nodes_blocked[2] = A2
            elif action_temp[0] == 3:
                nodes_blocked[3] = A3
        count += 1
    #faire le renversement des aretes à la fin du backtracking
    #orienter les aretes vers leur centre
    print("compass_edge")
    cube.print_cube()
    compass_edges()
    print("compass_edge PARES")

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
    print("compass")
    cube.print_cube()
    #orienter les coins
    compass_corners()







########################################################################## SECOND LAYER

def second_layer():
    print("2eme etage")
    cube.print_cube()

    nodes_blocked = {
        0: False,
        1: False,
        2: False,
        3: False
    }

    colors = ["BR", "BO", "OG", "GR"]
    down_edges = [A6, A8, A10, A11]
    center_edges = [A4, A5, A7, A9]
    #on vient regarder si les aretes sont bien placées
    for index, d in enumerate(center_edges):
        if d.get_color() == colors[index]:
            nodes_blocked[index] = True

    functions_out = [out_edge_back, out_edge_left, out_edge_right, out_edge_up]

    # print("🌴 layer 2")
    # print(nodes_blocked)
    # remplir le 2eme etage par le 3eme, puis checker s'il faut sortir
    all_locked = all(nodes_blocked.values())

    while all_locked is False:
        for i in range(0, 4):
            nodes_blocked = edges_from_three_layer(nodes_blocked)
            if nodes_blocked[i] == False:
                functions_out[i]() #pas tjs tjs vrai !? , boucle infini comme apr haasard number_nodes_locked 2
                                    # number_nodes_locked 3

                                    #number_nodes_locked 2
                                    # 2eme etage, 2eme boucle infini
        all_locked = all(nodes_blocked.values())

    






########################################################################## THIRD LAYER

#etage 3
def third_layer():
    #checker si j'ai un trait:
    print("\n🔻")
    cube.print_cube()

    #si j'ai un trait, etape suivante
    if A6.get_color()[1] == 'Y' and A10.get_color()[1] == 'Y' or A8.get_color()[1] == 'Y' and A11.get_color()[1] == 'Y':
        print("trait deja la")
        return
    #si j'ai un L:
    #le placer grâce à down ou faire 4 algo selon son emplacement pour gagner entre 0 et 3coups
    print("A8, A10", A8.get_color()[1], A10.get_color()[1])
    print("A11, A10", A11.get_color()[1], A10.get_color()[1])
    print("A8, A6", A8.get_color()[1], A6.get_color()[1])
    print("A11, A6", A11.get_color()[1], A6.get_color()[1])

    if check_L() == False:

        while True: #idem pas tjs vrai, boucle infini dangereuse
            print("rien")
            cube.print_cube()
            to_have_trait()
            cube.print_cube()

            #check si ce n'est pas un L
            if check_trait() == False:
                break
            action(11)() #sinon boucle inf
    else:
        print("else")
        check_trait()

    #si 2 aretes opposé bien placer en fonction des milieux:
        #mettre ce trait là face à nous et faire l'algo pour mettre en 2 à coté
        #finir par encore l'algo 
    #si 2 aretes a cote:
        # faire une seule fois l'algo
    #bien placer les coins en fonction de la couleur de ces centres
    #faire le sexy move sur les 4 coins

    #fin... avec je pense 150 coups à la fin

    



 


