from CubeClass import cube
from NodeClass import Node, A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, C0, C1, C2, C3, C4, C5, C6, C7
from Functions import action, optimize_moves
from utils.SolveWhiteCorners import insert_corner, out_corner, swap_corner
from utils.SolveWhiteCross import resolve_cross, backtracking, speeder_path, ft_protection, turn_edge_up, turn_edge_back, turn_edge_left, turn_edge_right
from Rotations import Rien, Right, RightPrime, Left, LeftPrime, Up, UpPrime, Back, BackPrime, Down, DownPrime, Front, FrontPrime, R2, L2, B2, D2, U2, F2
from SecondLayer import edges_from_three_layer, out_edge_back, out_edge_left, out_edge_right, out_edge_up
from ThirdLayer import check_cross, make_cross, check_L, check_trait
from RotationsStart import reset, action_start

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


possibility_solutions = [] 
# envoyer l'ordre des nodes_blocked a first layer qui permet un meilleur choix
def return_solution_opti(solution):
    moved = True
    opt_mov = solution.split()
    while moved == True:
        opt_mov, moved = optimize_moves(opt_mov)

    string = ' '.join(opt_mov)
    return string


nodes_blocked = [ #il va tourner 24 fois pour choisir la meilleure option selon l'algo
    {0: None, 1: None, 2: None, 3: None}, {0: None, 1: None, 3: None, 2: None}, {0: None, 2: None, 1: None, 3: None},
    {0: None, 2: None, 3: None, 1: None}, {0: None, 3: None, 1: None, 2: None}, {0: None, 3: None, 2: None, 1: None},
    {1: None, 0: None, 2: None, 3: None}, {1: None, 0: None, 3: None, 2: None}, {1: None, 2: None, 0: None, 3: None},
    {1: None, 2: None, 3: None, 0: None}, {1: None, 3: None, 0: None, 2: None}, {1: None, 3: None, 2: None, 0: None},
    {2: None, 0: None, 1: None, 3: None}, {2: None, 0: None, 3: None, 1: None}, {2: None, 1: None, 0: None, 3: None},
    {2: None, 1: None, 3: None, 0: None}, {2: None, 3: None, 0: None, 1: None}, {2: None, 3: None, 1: None, 0: None},
    {3: None, 0: None, 1: None, 2: None}, {3: None, 0: None, 2: None, 1: None}, {3: None, 1: None, 0: None, 2: None},
    {3: None, 1: None, 2: None, 0: None}, {3: None, 2: None, 0: None, 1: None}, {3: None, 2: None, 1: None, 0: None}
]
map_node = [ #organisé en fonction des nodes_blocked et par rapport à l'algo de resolve cross
    [A0, A1, A2, A3], [A0, A1, A3, A2], [A0, A2, A1, A3],
    [A0, A2, A3, A1], [A0, A3, A1, A2], [A0, A3, A2, A1],
    [A1, A0, A2, A3], [A1, A0, A3, A2], [A1, A2, A0, A3],
    [A1, A2, A3, A0], [A1, A3, A0, A2], [A1, A3, A2, A0],
    [A2, A0, A1, A3], [A2, A0, A3, A1], [A2, A1, A0, A3],
    [A2, A1, A3, A0], [A2, A3, A0, A1], [A2, A3, A1, A0],
    [A3, A0, A1, A2], [A3, A0, A2, A1], [A3, A1, A0, A2],
    [A3, A1, A2, A0], [A3, A2, A0, A1], [A3, A2, A1, A0]
]
nodes_index = [ #organisé en fonction des nodes_blocked et par rapport à l'algo de resolve cross
    [0, 1, 2, 3], [0, 1, 3, 2], [0, 2, 1, 3],
    [0, 2, 3, 1], [0, 3, 1, 2], [0, 3, 2, 1],
    [1, 0, 2, 3], [1, 0, 3, 2], [1, 2, 0, 3],
    [1, 2, 3, 0], [1, 3, 0, 2], [1, 3, 2, 0],
    [2, 0, 1, 3], [2, 0, 3, 1], [2, 1, 0, 3],
    [2, 1, 3, 0], [2, 3, 0, 1], [2, 3, 1, 0],
    [3, 0, 1, 2], [3, 0, 2, 1], [3, 1, 0, 2],
    [3, 1, 2, 0], [3, 2, 0, 1], [3, 2, 1, 0]
]

colors = [
    ['R', 'B', 'G', 'O'], ['R', 'B', 'O', 'G'], ['R', 'G', 'B', 'O'],
    ['R', 'G', 'O', 'B'], ['R', 'O', 'B', 'G'], ['R', 'O', 'G', 'B'],
    ['B', 'R', 'G', 'O'], ['B', 'R', 'O', 'G'], ['B', 'G', 'R', 'O'],
    ['B', 'G', 'O', 'R'], ['B', 'O', 'R', 'G'], ['B', 'O', 'G', 'R'], 
    ['G', 'R', 'B', 'O'], ['G', 'R', 'O', 'B'], ['G', 'B', 'R', 'O'],
    ['G', 'B', 'O', 'R'], ['G', 'O', 'R', 'B'], ['G', 'O', 'B', 'R'],
    ['O', 'R', 'B', 'G'], ['O', 'R', 'G', 'B'], ['O', 'B', 'R', 'G'],
    ['O', 'B', 'G', 'R'], ['O', 'G', 'R', 'B'], ['O', 'G', 'B', 'R']
]

def simulation(nodes_index, colors, map_node, nodes_blocked):    
    count = 0
    while count != 4:
        list_path_to_resolve_node, nodes_blocked = resolve_cross(nodes_index, colors, map_node, nodes_blocked)
    
        target_path = speeder_path(list_path_to_resolve_node) 
        if target_path : #si l'action existe, l'executer 
            #proteger les nodes_blocked, executer l'action et remettre les nodes_blocked à leur place
            ft_protection(nodes_blocked, target_path)  
            #bloquer le noeud une fois actionS réalisées
            for i in range(0, 4):
                if target_path[0] == i :
                    print("i", i)
                    nodes_blocked[nodes_index[i]] = map_node[nodes_index[i]]
                    print("nodes_blocked[nodes_index[i]] ",nodes_blocked[nodes_index[i]].get_color())
                    print("---> ❎ with action", nodes_blocked[nodes_index[i]].get_color())
                    if nodes_blocked[0]:
                        print("---> 0", nodes_blocked[0].get_color())
                    if nodes_blocked[1]:
                        print("---> 1", nodes_blocked[1].get_color())
                    if nodes_blocked[2]:
                        print("---> 2", nodes_blocked[2].get_color())
                    if nodes_blocked[3]:
                        print("---> 3", nodes_blocked[3].get_color())
            
        count += 1
    #faire le renversement des aretes à la fin du backtracking
    #orienter les aretes vers leur centre
    # print("\n🐋 Cross done :")
    # cube.print_cube()

    # print("\n🐋 Edges'Cross Compass : ")
    # compass_edges()
    # cube.print_cube()


#R U2 F B' L2 R 
def find_best_first_path(list_action): #sans checker le sens des aretes
    #inverser l'ordre des noeuds pour le faire commencer par un autre

    for i in range(0, 2):
        print(f"\n----------------\n🌻 {i}")
        cube.print_cube()
        print(A0.get_color(), A1.get_color(), A2.get_color(), A3.get_color())
        print(nodes_blocked[i])
        print(nodes_index[i])
        # cube.print_cube()
        simulation(nodes_index[i], colors[i], map_node[i], nodes_blocked[i])
        print("solution: ",return_solution_opti(cube.solution))
        possibility_solutions.append((i, cube.solution)) #ajouter l'indice de la solution a choisir et la taille de la solution pour permettre de comaprer apres
        # print(possibility_solutions)
        reset()
        #remettre les mouvements choisi par l'utilisateur
        for l in list_action:
            action_start(l)()
    #une fois finir de faire 'toutes' les possibilités
    #retourner l'odre des noeuds qui permettent la solution la plus courte
    best = possibility_solutions[0]
    index_solution = best[0]
    for p in possibility_solutions:
        index_solution = p[0]
        string = return_solution_opti(p[1])
        len_solution = len(string)

        #s'il trouve solution plus courte
        if len_solution < len(best[1]):
            best = (index_solution, string)
   
    print("solution attendu", best[1])
    #retourner l'index de best pour renvoyer l'ordre
    return index_solution




########################################################################## FIRST LAYER
def first_layer():
    #-----------------------------------------------------------------------------edges
    nodes_blocked = { 0: None, 1: None, 2: None, 3: None }
    # map_node = [ A0, A1, A2, A3 ]
    count = 0
    while count != 4: #mettre 4 pour les 4 aretes
        list_path_to_resolve_node, nodes_blocked = resolve_cross(nodes_blocked)
        target_path = speeder_path(list_path_to_resolve_node) 
        if target_path : #si l'action existe, l'executer 
            #proteger les nodes_blocked, executer l'action et remettre les nodes_blocked à leur place
            ft_protection(nodes_blocked, target_path)  
            #bloquer le noeud une fois actionS réalisées
            for i in range(0, 4):
                if target_path[0] == i:
                    nodes_blocked[i] = map_node[i]
            
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
    #orienter les coins

    compass_corners()
    print("\n🐋 Corners' White Face Cube Done : ")
    cube.print_cube()








########################################################################## SECOND LAYER

def second_layer():

    nodes_blocked = { 0: False, 1: False, 2: False, 3: False }

    colors = ["BR", "BO", "OG", "GR"]
    down_edges = [A6, A8, A10, A11]
    center_edges = [A4, A5, A7, A9]

    #on vient regarder si les aretes sont bien placées
    for index, d in enumerate(center_edges):
        if d.get_color() == colors[index]:
            nodes_blocked[index] = True

    functions_out = [out_edge_back, out_edge_left, out_edge_right, out_edge_up]
    
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


    



 


