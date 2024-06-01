from CubeClass import cube
from NodeClass import A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11
from Functions import solver_white_edges,turn_edge_up, turn_edge_back, turn_edge_left, turn_edge_right, locked_edge

print("--- INIT ----")

cube.print_cube()

list_whites_nodes = [A6, A8, A10, A11]
functions_turn = [turn_edge_left, turn_edge_up, turn_edge_right, turn_edge_back]

#First step: make the white cross
for i, node in enumerate(list_whites_nodes):
    if 'W' not in node.get_color():
        solver_white_edges(node)
    if node.get_color()[1] != 'W':     #check color orientation edge
        functions_turn[i]()
    locked_edge.append(node)
    cube.print_cube()


#face blanche: 19 (pas finit)
# D2, L2, U', F', L, F, R, R2, U, F, R', F', F2, F2, U', R', F, R, B'
#remonter les aretes avec centre correspondant
#placer les coins, bonnes orientations