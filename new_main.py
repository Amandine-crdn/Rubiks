from CubeClass import cube
from NodeClass import Node, A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, C0, C1, C2, C3, C4, C5, C6, C7
from Functions import action
from utils.SolveWhiteCorners import insert_corner, out_corner, swap_corner
from utils.SolveWhiteCross import resolve_cross, backtracking, speeder_path, ft_protection, turn_edge_up, turn_edge_back, turn_edge_left, turn_edge_right
from Rotations import Rien, Right, RightPrime, Left, LeftPrime, Up, UpPrime, Back, BackPrime, Down, DownPrime, Front, FrontPrime, R2, L2, B2, D2, U2, F2

cmd_map = {
    "R": [0],
    "R'": [1],
    "R2": [0, 0],
    "L": [2],
    "L'": [3],
    "L2": [2, 2],
    "F": [4],
    "F'": [5],
    "F2": [4, 4],
    "B": [6],
    "B'": [7],
    "B2": [6, 6],
    "U": [8],
    "U'": [9],
    "U2": [8, 8],
    "D": [10],
    "D'": [11],
    "D2": [10, 10]
}
commandes = input("entrez vos commandes: ")
split_cmd = commandes.split()
for c in split_cmd: #proteger des commandes inexistantes
    list_actions = cmd_map[c]
    for l in list_actions:
        action(l)()
print("modifier:")
cube.print_cube()


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
list_whites_nodes = [A0, A1, A2, A3]
switch_edge = [turn_edge_back, turn_edge_left, turn_edge_right, turn_edge_up] 
for node_index, n in enumerate(list_whites_nodes, start=0):
    if n.get_color()[0] != 'W':
        switch_edge[node_index]()








#-----------------------------------------------------------------------------corners






    #je veux résoudre les 4 coins:
    #je recherche coin par coin
    #je calcule quel coin a le chemin le plus court
    #j'execute l'action 
    #je bloque le node
    #je continue de chercher pour les autres nodes
    #if index >= 0 and index < 4 and index == i_color and 'W' in n.get_color() and color[0] in n.get_color() and color[1] in n.get_color():
    #si la couleur recherchée est entre le CO et le C3 AND qu'il n'est pas sur son bon node:
        #faire sortir le coin:
        #C1: r d r' 
        #C2: l d l' 
        #C3: v

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
        if 'W' in n.get_color() and colors[index_corner][0] in n.get_color() and colors[index_corner][1] in n.get_color() : #on choppe le node qu'on veut ramener à c
            #on chercher à savoir c'est quel node:
            if nodes_blocked[index_corner] is None and index_node == index_corner: #si le noeud est au bon endroit
                nodes_blocked[index_corner] = n
            elif nodes_blocked[index_corner] is None:
                if index_node >= 0 and index_node <= 3: #faire sortir le node recherché pour le placer apres
                    out_corner(index_node)
                    while True:
                        if 'W' in down_corners[index_corner].get_color() and colors[index_corner][0] in down_corners[index_corner].get_color() and colors[index_corner][1] in down_corners[index_corner].get_color() : #on choppe le node qu'on veut ramener à c
                            break
                        action(10)() # le placer "en face"
                    #plus qu'à insérer
                    insert_corner(index_corner)
                    break
    
                elif index_node >= 4 and index_node <= 7:
                    while True:
                        if 'W' in down_corners[index_corner].get_color() and colors[index_corner][0] in down_corners[index_corner].get_color() and colors[index_corner][1] in down_corners[index_corner].get_color() : #on choppe le node qu'on veut ramener à c
                            break
                        action(10)()
                    insert_corner(index_corner)
                    break

final_color = ["WBR", "WRG", "WOB", "WGO"]
# final_color = ["WRB", "WRG", "WOB", "WOG"]
whites_corners = [C0, C1, C2, C3]
cube.print_cube()
def compass_corners():
    for index, w in enumerate(whites_corners):
        
        while True:
            if w.get_color() == final_color[index]:
                break
            swap_corner(index)
            

compass_corners()# F R U2 B' L' D'


#2eme etage:

#reperer 





def shorter_solution(solver):
    solution = solver.split()
    new_solution = ""
    for index, s in enumerate(solution):

        if index < len(solution) - 1 and solution[index] == solution[index + 1]: # s'ils sont egaux ex: u u mettre u2
            new_solution += f"{s[0]}2 "
            to_pass = index + 1
        elif index < len(solution) - 1 and solution[index][0] == solution[index + 1][0]: # s'ils sont opposé ex: u u' annuler
            to_pass = index + 1
        else:
            new_solution += f"{s} "

    return new_solution

# print(cube.solution)
new_solution = shorter_solution(cube.solution)
# new_solution = shorter_solution(new_solution)
new_solution = new_solution.split()
print(len(new_solution))
print(new_solution)

cube.print_cube()


# print(cube.solution)



#opti dans le cross -> dans les protections
#opti dans le corner -> swap

# : R R R -> R').
#transformer les 3 l en l'
#transformer les 2 u en u2
#annuler les coups opposés
#voir pour reduite d'avance les couprs avec l'affichage duc hemin qui va etre executer, car êut entrainer des surprotection dans ft protect


