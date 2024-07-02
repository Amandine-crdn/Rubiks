from Start.NodeClass import A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, C0, C1, C2, C3, C4, C5, C6, C7
from Start.CubeClass import cube
from Utils.Functions import return_solution_opti
from Start.RotationsStart import reset

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


def simulation(nodes_index, colors, map_node, nodes_blocked):    
    from Layers.SolveWhiteCross import resolve_cross, ft_protection, speeder_path

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
                    nodes_blocked[nodes_index[i]] = map_node[nodes_index[i]]
                    print(nodes_blocked[nodes_index[i]].get_color())
        count += 1
    


#R U2 F B' L2 R 
def best_cross(list_action): #sans checker le sens des aretes

    possibility_solutions = [] 
    #inverser l'ordre des noeuds pour le faire commencer par un autre
  
    # for i in range(0, 24):
    for i in range(0, 1):
        simulation(nodes_index[i], colors[i], map_node[i], nodes_blocked[i])
        possibility_solutions.append((i, cube.solution)) #ajouter l'indice de la solution a choisir et la taille de la solution pour permettre de comaprer apres
        #remettre les mouvements choisi par l'utilisateur
        reset(list_action)
        
        if i == 0:
            best = possibility_solutions[0]
            index_solution = best[0]
            string_solution = best[1]
            cube.set_solution(string_solution)
    #une fois finir de faire 'toutes' les possibilités
    #retourner l'odre des noeuds qui permettent la solution la plus courte
        
    for p in possibility_solutions:
        opt_mov = return_solution_opti(p[1])
        string = ' '.join(opt_mov)
        len_solution = len(string)

        #s'il trouve solution plus courte
        if len_solution < len(best[1]):
            index_solution = p[0]
            string_solution = p[1]
            best = (index_solution, string)

    cube.set_solution(string_solution)


#R U2 F B' L2 R 
def find_orientation_edge_white(node_init, path, direction, index, map_node, nodes_index, color):
    from Start.RotationsStart import action_start
    # print(colors[nodes_index[index]])
    copy_path = path.copy()
    copy_path.append(direction)
    for p in copy_path:
        action_start(p)()
    
    if node_init.get_color() != "W" + color:
        for p in reversed(copy_path):
            action_start(p)()
        copy_path.pop()
        
        return False
    print("🎍 find ", node_init.get_color())

    for p in reversed(copy_path):
        action_start(p)()

    copy_path.pop()
    return True