from Start.CubeClass import cube
from Utils.Functions import return_solution_opti, optimize_moves


from Start.RotationsStart import action_start, cmd_map

from Utils.SolverRubik import first_layer, second_layer, third_layer

import sys

def start_resolve(list_actions):

    first_layer(list_actions) #40 et 60 mouvements  
    # second_layer()
    # third_layer()

    moved = True
    return_solution_opti(cube.solution)
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
