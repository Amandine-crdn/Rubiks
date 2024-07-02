from NodeClass import Node, A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, C0, C1, C2, C3, C4, C5, C6, C7
from CubeClass import cube


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

# envoyer l'ordre des nodes_blocked a first layer qui permet un meilleur choix
def return_solution_opti(solution):
    from Functions import optimize_moves
    moved = True
    opt_mov = solution.split()
    while moved == True:
        opt_mov, moved = optimize_moves(opt_mov)

    string = ' '.join(opt_mov)
    return string



def simulation(nodes_index, colors, map_node, nodes_blocked):    
    from utils.SolveWhiteCross import resolve_cross, ft_protection, speeder_path

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
                    # print("i", i)
                    nodes_blocked[nodes_index[i]] = map_node[nodes_index[i]]    
        count += 1
    


#R U2 F B' L2 R 
def find_best_first_path(list_action): #sans checker le sens des aretes
    from RotationsStart import reset, action_start

    possibility_solutions = [] 
    #inverser l'ordre des noeuds pour le faire commencer par un autre

    for i in range(0, 24):
        simulation(nodes_index[i], colors[i], map_node[i], nodes_blocked[i])
        possibility_solutions.append((i, cube.solution)) #ajouter l'indice de la solution a choisir et la taille de la solution pour permettre de comaprer apres
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



def ft_solver_sim(node_init, path, direction, index, map_node, nodes_index):
    from RotationsStart import reset, action_start
    # print("START ", node.get_color())
    # print("START ", map_node[nodes_index[index]].get_color())
    # print(nodes_index)
    path.append(direction)
    copy_path = path.copy()
    for p in copy_path:
        action_start(p)()
    # print("END ", node.get_color())
    # print("index", index)
    # print("nodes_index", nodes_index)
    # print("map_node", map_node)
    if node_init.get_color()[0] != 'W':
        for p in reversed(copy_path):
            action_start(p)()
        path.pop()
        
        return False
    print("END ", nodes_index[index], node_init.get_color())
    for p in copy_path:
        action_start(p)()
    path.pop()
    return True