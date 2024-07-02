from Start.CubeClass import cube
from Start.NodeClass import Node, A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, C0, C1, C2, C3, C4, C5, C6, C7
from Utils.Functions import action, optimize_moves
from Layers.SolveWhiteCorners import insert_corner, out_corner, swap_corner
from Layers.SolveWhiteCross import resolve_cross, backtracking, speeder_path, ft_protection, turn_edge_front, turn_edge_back, turn_edge_left, turn_edge_right
from Utils.Rotations import Rien, Right, RightPrime, Left, LeftPrime, Up, UpPrime, Back, BackPrime, Down, DownPrime, Front, FrontPrime, R2, L2, B2, D2, U2, F2
from Start.RotationsStart import action_start, cmd_map
from Layers.SecondLayer import edges_from_three_layer, out_edge_back, out_edge_left, out_edge_right, out_edge_up

from Utils.SolverRubik import second_layer, third_layer
from Layers.FirstLayer import first_layer

import sys

def start_resolve(list_actions):

    first_layer(list_actions) #40 et 60 mouvements  
    # second_layer()
    # third_layer()

    moved = True
    
   
    print("solution",cube.solution)
    opt_mov = cube.solution.split()
    while moved == True:
        opt_mov, moved = optimize_moves(opt_mov)
    print(len(opt_mov))
    print("🏁 Moves:", opt_mov)




print("\n🐋 Start :")
cube.print_cube()
commandes = ' '.join(sys.argv[1::]);
split_cmd = commandes.split()
list_actions = []
if split_cmd:
    for c in split_cmd:
        acts = cmd_map.get(c, None)
        if acts is None:
            list_actions = []
            break
        else:
            list_actions.extend(acts)
    # print("\n🐋 input to shake: ",list_actions)
    for l in list_actions:
        action_start(l)()
    print("\n🐋 State of rubik after shake :")
    cube.print_cube()
    if len(list_actions) > 0:
        start_resolve(list_actions)
