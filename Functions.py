from CubeClass import cube
from Rotations import Rien, Right, RightPrime, Left, LeftPrime, Up, UpPrime, Back, BackPrime, Down, DownPrime, Front, FrontPrime, R2, L2, B2, D2, U2, F2
locked_edge = cube.blocked_edges

def action(choice: int):
    if choice is None:
        return Rien
    functions = [
        Right, Front, Left, Up, Down, Back, RightPrime, FrontPrime, LeftPrime, DownPrime,  UpPrime, BackPrime, R2, F2, L2, U2, D2, B2
    ]
    return functions[choice]


def solver_white_edges(goal):
    cube.print_cube()
    list_actions = []
    #dabord checker si goal contient pas déjà un W
    dico = goal.find_path('W',locked_edge)

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
        print(direction)
        action(direction)()
    cube.append(goal)



















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
        
    