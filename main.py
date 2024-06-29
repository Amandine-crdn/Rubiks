from CubeClass import cube
from NodeClass import Node, A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, C0, C1, C2, C3, C4, C5, C6, C7
from Functions import action, optimize_moves
from utils.SolveWhiteCorners import insert_corner, out_corner, swap_corner
from utils.SolveWhiteCross import resolve_cross, backtracking, speeder_path, ft_protection, turn_edge_up, turn_edge_back, turn_edge_left, turn_edge_right
from Rotations import Rien, Right, RightPrime, Left, LeftPrime, Up, UpPrime, Back, BackPrime, Down, DownPrime, Front, FrontPrime, R2, L2, B2, D2, U2, F2
from RotationsStart import action_start, cmd_map
from SecondLayer import edges_from_three_layer, out_edge_back, out_edge_left, out_edge_right, out_edge_up

from SolverRubik import first_layer, second_layer, third_layer

cube.print_cube()
def start_resolve():
        
    first_layer() #40 et 60 mouvements

    #test si faire un U oriente bien les aretes si tout est white, ex R L U pas meme resultat que U R L

    second_layer() # 20 et 30 mouvements
    third_layer()

    cube.print_cube()




    moved = True
    opt_mov = cube.solution.split()
    while moved == True:
        opt_mov, moved = optimize_moves(opt_mov)
    print(len(opt_mov))
    print("Moves:", opt_mov)

    #ft_protection otpimiser ✔️ gain de 10 coups
    #swap_corner otpimiser ✔️ gain de 5 coups

    #remplacer # # if {'W', colors[index_corner][0], colors[index_corner][1]}.issubset(n.get_color())   par exemple, plus claire, check si ça marche bien
    #idem 
                # while {A8.get_color()[0], A8.get_color()[1] }.issubset(color_node) is False: ou meem jsute while {A8.get_color()}.issubset(color_node)??

                #mettre les fonctions de rotations dans la class cube ?


    #-----------------------------------------------------------------------------corners






            #je veux résoudre les 4 coins:
            #je recherche coin par coin
            #je calcule                                                                                                                                                                                         
            #je continue de chercher pour les autres nodes
            #if index >= 0 and index < 4 and index == i_color and 'W' in n.get_color() and color[0] in n.get_color() and color[1] in n.get_color():
            #si la couleur recherchée est entre le CO et le C3 AND qu'il n'est pas sur son bon node:
                #faire sortir le coin:
                #C1: r d r' 
                #C2: l d l' 
                #C3: v


# if __name__ == '__main__':

#     commandes = input("entrez vos commandes: ") # F R U2 B' L' D' => 60 mouvements etages 1 et 2
    
#     split_cmd = commandes.split()
#     if split_cmd:
#         for c in split_cmd: #proteger des commandes inexistantes
#             list_actions = cmd_map.get(c, None)
#             if list_actions is None:
#                 print("Error de parsing\n")
#             else:
#                 for l in list_actions:
#                     action_start(l)()
#                 print("modifier:")
#                 cube.print_cube()
#                 start_resolve()
#     else:
#         print("Veuillez mélanger le cube\n")


commandes = input("entrez vos commandes: ") # F R U2 B' L' D' => 60 mouvements etages 1 et 2
split_cmd = commandes.split()
list_actions = []
if split_cmd:
    for c in split_cmd: #proteger des commandes inexistantes
        acts = cmd_map.get(c, None)
        print(acts)
        if acts is None:
            print("Error de parsing\n")
            list_actions = []
            break
        else:
            list_actions.extend(acts)
    for l in list_actions:
        action_start(l)()
    print("modifier:")
    cube.print_cube()
    if len(list_actions) > 0:
        start_resolve()
    cube.print_cube()
