# from CubeClass import cube
from Rotations import Rien, Right, RightPrime, Left, LeftPrime, Up, UpPrime, Back, BackPrime, Down, DownPrime, Front, FrontPrime, R2, L2, B2, D2, U2, F2




# def add_path(node, chemin):
#     s_dico = {
#         0: [A2, A9, A10, A7],
#         1: [A2, A9, A10, A7],
#         2: [A1, A4, A6, A5],
#         3: [A1, A4, A6, A5],
#         4: [A3, A8, A7, A5],
#         5: [A3, A8, A7, A5],
#         6: [A0, A4, A11, A9],
#         7: [A0, A4, A11, A9],

#         8: [A0, A1, A2, A3],
#         9: [A0, A1, A2, A3],
#         10: [A6, A8, A10, A11],
#         11: [A6, A8, A10, A11]
#     }
#     new_chemin = []
#     print(chemin[0])
#     if chemin[0] == 0:
#         list_node = s_dico[0]
#         good_path = {
#             0: [9, 7], #u' b'
#             1: [7, 11], #b' d'
#             2: [11, 5], #d' f'
#             3: [5, 9] #f' u'
#         }
#         for index_ln, ln in enumerate(list_node):
#             if ln == node:
#                 new_chemin = good_path[index_ln]

#     elif chemin[0] == 1:
#         list_node = s_dico[1]
#         good_path = {
#             0: [8, 4], #u f 
#             1: [6, 8], #b u
#             2: [10, 6], #d b
#             3: [4, 10] #f d
#         }
#         for index_ln, ln in enumerate(list_node):
#             if ln == node:
#                 new_chemin = good_path[index_ln]


#     elif chemin[0] == 2:
#         list_node = s_dico[2]
#         good_path = {
#             0: [8, 5], #u' f'
#             1: [7, 9], #b' u'
#             2: [10, 7], #d' b'
#             3: [5, 11] #f' d'
#         }
#         for index_ln, ln in enumerate(list_node):
#             if ln == node:
#                 new_chemin = good_path[index_ln]
    
#     elif chemin[0] == 3:
#         list_node = s_dico[3]
#         good_path = {
#             0: [8, 6], #u b
#             1: [6, 10], #b d 
#             2: [10, 4], #d f 
#             3: [4, 8] #f u
#         }
#         for index_ln, ln in enumerate(list_node):
#             if ln == node:
#                 new_chemin = good_path[index_ln]

#     elif chemin[0] == 4:
#         list_node = s_dico[4]
#         good_path = {
#             0: [9, 1], #u' r'
#             1: [1, 11], # r' d'
#             2: [11, 2], # d' l
#             3: [2, 9] # l u'
#         }
#         for index_ln, ln in enumerate(list_node):
#             if ln == node:
#                 new_chemin = good_path[index_ln]
    
#     elif chemin[0] == 5:
#         list_node = s_dico[5]
#         good_path = {
#             0: [8, 2], #u l
#             1: [0, 8], # r u 
#             2: [11, 0], # d' r 
#             3: [2, 11] # l d'
#         }
#         for index_ln, ln in enumerate(list_node):
#             if ln == node:
#                 new_chemin = good_path[index_ln]
    
#     elif chemin[0] == 6:
#         list_node = s_dico[6]
#         good_path = {
#             0: [9, 2], #u' l'
#             1: [3, 10], # l' d
#             2: [10, 1], # d r'
#             3: [1, 9] # r' u'
#         }
#         for index_ln, ln in enumerate(list_node):
#             if ln == node:
#                 new_chemin = good_path[index_ln]
    
#     # faire la suite 
#     #pas finit

#     if new_chemin != []:
#         print("🎀 ",new_chemin)
#     return reversed(new_chemin)


# def ft_simulation(node_init, node, path):
#     if path is None:
#         return path
#     old_path = path.copy()
#     print("----------SIMULATION---------")
#     # print("🎀 avant", sim.get_color()[1])
#     for direction in reversed(old_path):
#         action(direction)()
#     # print("🎀 apres", sim.get_color()[1])
#     #si a la fin des actions l'arete n'est pas bien placé
#     if node_init.get_color()[1] != 'W':
#         print("ADD 🎀")
#         # added = add_path(node, path[:1])
#         # if len(path) != 0:
#         #     path.pop()
#         # path.extend(added)
#     for direction in old_path:
#         action(direction)()
#     #remettre le cube a la normal
#     return path

def action(choice: int):
    if choice is None:
        return Rien

    functions = [
        Right, RightPrime,
        Left,  LeftPrime, 
        Front, FrontPrime,
        Back,  BackPrime, 
        Up, UpPrime, 
        Down, DownPrime
    ]
    #   functions = [
    #     Right, RightPrime, R2,
    #     Left,  LeftPrime, L2,
    #     Front, FrontPrime, F2,
    #     Back,  BackPrime, B2,
    #     Up, UpPrime, U2,
    #     Down, DownPrime, D2
    # ]
    return functions[choice]


def turn_edge_left():
    L2()
    Down()
    Front()
    LeftPrime()
    FrontPrime()

def turn_edge_right():
    R2()
    DownPrime()
    FrontPrime()
    Right()
    Front()

def turn_edge_up():
    F2()
    Down()
    Right()
    FrontPrime()
    RightPrime()

def turn_edge_back():
    B2()
    DownPrime()
    RightPrime()
    Back()
    Right()



def solver_white_edges(goal):
    list_actions = []
    #dabord checker si goal contient pas déjà un W
    dico = goal.find_path('W',cube.blocked_edges)

    init_node = list(dico.keys())[-1]
    init_tuple = list(dico.values())[-1]
    list_actions.append(init_tuple[-1][0]) #ajout de la derniere action

    while True:
        for node, _tuple in dico.items():
            strlen = len(_tuple)
            i = 0
            while i != strlen and strlen != 0:
                print("\tvalue:",_tuple[i][0], _tuple[i][1].get_color())
                if _tuple[i][1] == init_node and _tuple[i][1] != goal:
                    list_actions.append(_tuple[i][0])
                    init_node = node
                    break
                i+=1
        break

    print("actions à réalisé en partant de la fin: ",list_actions)
    for direction in reversed(list_actions):
        action(direction)()
    







# def search_aretes(color: int) : #-> list[NodeClass]:
#     list_aretes = []
#     aretes = cube.get_aretes()
#     for a in aretes:
#         if color in a.get_color():
#             list_aretes.append(a)
#     return list_aretes 

# def search_arete(color1: int, color2: int):
#     aretes = cube.get_aretes()
#     for index, a in enumerate(aretes):
#         if color1 in a and color2 in a :
#             return index
#     return 0
        
    