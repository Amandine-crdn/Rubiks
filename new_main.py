from CubeClass import cube
from NodeClass import A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11
from Functions import action, solver_white_edges,turn_edge_up, turn_edge_back, turn_edge_left, turn_edge_right
from Rotations import Rien, Right, RightPrime, Left, LeftPrime, Up, UpPrime, Back, BackPrime, Down, DownPrime, Front, FrontPrime, R2, L2, B2, D2, U2, F2

import copy

cube.print_cube()



def ft_protection(nodes_blocked, action_temp):
    print("\n-----------FT_PROTECTION-------------\nnb action à executer: ",len(action_temp))
    other_protection = -1
    protection = [] #liste car si besoin de protéger les 4 aretes pour un coup
    once = True
    for index, direction in enumerate(reversed(action_temp)):
        if index > 0 and action_temp[index] != action_temp[index - 1]:
            if len(protection) > 0: #tant qu'il n'a pas finit un meme mouvement
                for p in protection:
                    # print("💚")
                    action(p)()
                cube.print_cube()
                protection = [] #vider la liste
                once = True
               
        if once == True:
            for k, v in nodes_blocked.items():
                #u, u' u2
                if v and (direction == 8 or direction == 9): #si none inutile de proteger
                    
                    if k == 0 and v == A0:
                        # print("1 💚")
                        action(6)() #back
                        action(6)() #back
                        # print("1 💚\n")
                        protection.extend([7, 7]) #b'
                        once = False
                    if k == 1 and v == A1:
                        # print("1 💚")
                        action(2)() #left
                        action(2)() #left
                        # print("1 💚\n")
                        protection.extend([3, 3]) #l'
                        once = False
                    if k == 2 and v == A2:
                        # print("1 💚")
                        action(0)() #right
                        action(0)() #right
                        # print("1 💚\n")
                        protection.extend([1, 1]) #r'
                        once = False
                    if k == 3 and v == A3:
                        # print("1 💚")
                        action(4)() #front
                        action(4)() #front
                        protection.extend([5, 5]) #f'
                        # print("1 💚\n")
                        once = False
                    

                #once == True pour pas que les 2 se cumulent
                elif once == True and v == A0 and k == 0 and (direction == 6 or direction == 7):
                    # print("1 🎗️")
                    action(8)() #up
                    other_protection = 9
                    # print("1 🎗️\n")
                    break
                elif once == True and v == A1 and k == 1 and (direction == 2 or direction == 3):
                    # print("1 🎗️")
                    action(8)() #up
                    # print("1 🎗️\n")
                    other_protection = 9
                    break
                elif once == True and v == A2 and k == 2 and (direction == 0 or direction == 1):
                    # print("1 🎗️")
                    action(8)() #up
                    # print("1 🎗️\n")
                    other_protection = 9
                    break
                elif once == True and v == A3 and k == 3 and (direction == 4 or direction == 5):
                    # print("1 🎗️")
                    action(8)() #up
                    # print("1 🎗️\n")
                    other_protection = 9
                    break
                    
                    
        #on fait l'action apres avoir proteger
        print("\n🥐")
        action(direction)()
        print("🥐\n")
        if other_protection != - 1:
            # print("2 🎗️")
            action(other_protection)()
            # print("2 🎗️\n")
            other_protection = -1

    #si programme se finit, terminer  
    if len(protection) > 0:      
        for p in protection:
            # print("2 💚")
            action(p)()
            # print("2 💚\n")


def speeder_path(liste):
    if liste == []:
        return None
    action_temp = liste[0]
    for l in liste:
        if len(l) < len(action_temp):
            action_temp = l
    return action_temp


def shorter_path(dico):
    if dico == {}:
        return None#pck il est bien placer (le W est bien en haut, sans etre bien orienter ou center pour autant)
    action_temp = dico[0]
    for k, v in dico.items():
        if len(v) < len(action_temp):
            action_temp = v
    return action_temp #retourne le chemin le plus court


def directions(node): #noeud non NULL, renvoie la direction associé au noeud
    if node is None:
        return {}
    dico = {}
    getters = node._getter()
    for k, v in getters:
        if v: #si non NULL l'ajouter au dico
            dico[k] = v
    return dico

def check_existing(next_node, nodes_blocked, index):
    if nodes_blocked[index] and nodes_blocked[index]  == next_node:
        return True
    return False
    

def backtracking(node, old_node, node_init, path, dico_path, i, color, nodes_blocked, index):
    all_directions = directions(node)
    
    for direction, next_node in all_directions.items():
        
        #unique condition de fermer un chemin
        #  next_node not in nodes_blocked pour pas lui piquer son voisin
        if 'W' in next_node.get_color() and color in next_node.get_color():# and check_existing(next_node, nodes_blocked, index) == False:
            path.append(direction)
            copy_path = path.copy()
            print(copy_path)
            dico_path[i] = copy_path
            path.pop()
            i+=1
        #condition chercher plus loins si la taille du chemin n'excède pas len < 2 #pour optimiser apres on verrra
        elif len(path) > 2:
            pass
        #chercher un autre chemin
        #s'assurer que le noeud suivant n'est pas node_init ou node_bloked
        elif next_node != node_init:
            path.append(direction)
            copy_path = path.copy()
            node, dico_path, path = backtracking(next_node, node, node_init, copy_path, dico_path, i, color, nodes_blocked, index)
            if len(path) != 0:
                path.pop()

    return old_node, dico_path, path



def resolve_cross(nodes_blocked):
    nodes = [A0, A1, A2, A3]
    colors = ['R', 'B', 'G', 'O']
    list_path_per_edge = []

    for index, n in enumerate(nodes):
        
        # nodes_blocked, is_locked = locker(colors[index], nodes_blocked, n)
        if 'W' in n.get_color() and colors[index] in n.get_color() and nodes_blocked[index] is None:
            nodes_blocked[index] = n
        else:
        # if is_locked == False:
            path = []
            dico_path = {}
            i = 0
            node = n
            node_init = node
            old_node = None
            while node :
                node, dico_path, path = backtracking(node, old_node, node_init, path, dico_path, i, colors[index], nodes_blocked, index)
            action_temp = shorter_path(dico_path)
            if action_temp:
                list_path_per_edge.append(action_temp)
        # nodes_blocked, is_locked = locker(colors[index], nodes_blocked, n)
        if 'W' in n.get_color() and colors[index] in n.get_color() and nodes_blocked[index] is None:
            nodes_blocked[index] = n

    
    return list_path_per_edge, nodes_blocked




def calc_len_locked(nodes_blocked):
    calc = 0
    for k, v in nodes_blocked.items():
        if v:
            calc += 1
    return calc


nodes_blocked = {
    0: None,
    1: None,
    2: None,
    3: None
}

count = 0
start = 0

while count != 4: #mettre 4 pour les 4 aretes

    list_path_per_edge, nodes_blocked = resolve_cross(nodes_blocked)
    start += 1

    for i in range(0, 4):
        if nodes_blocked[i]:
            print("❌",nodes_blocked[i].get_color())

    action_temp = speeder_path(list_path_per_edge) 
    

    if action_temp : #si l'action existe, l'executer 
        #proteger les nodes_blocked, executer l'action et remettre les nodes_blocked à leur place
        ft_protection(nodes_blocked, action_temp)  
    
    # if start != calc_len_locked(nodes_blocked):
    #     print(action_temp, "🎵🎵🎵🎵🎵🎵🎵")
    #     pass
    # else:
    count += 1

    cube.print_cube() 
            
    
cube.print_cube()





#je veux regarder quelle arete résoudre en premier
#pour un noeud
    #pour se faire, je vais faire du backtracking pour récolter l'ensemble des chemins possibles pour avoir un W
        #  --> ne pas piocher dans les nodes


    #une fois la récolte faire, je vais sélectionner le chemin le plus court

#je vais regarder parmis le chemin associé à un noeud lequel est le plus court de tous les noeuds à résoudre

#j'exécute l'action la plus courte
    #je cherche si les nodes bloqué ont changé de place





    #je retire des noeuds à chercher list_node.pop(node)
    #je l'ajoute au noeud bloquer.

#j'éxecute ces actions tant que les 4 aretes n'ont pas de W



#transformer les 3 l en l'
#transformer les 2 u en u2
#annuler les coups opposés

# def shorter_solution(solver):
#     solution = solver.split()
#     print(len(solution))
#     new_solution = ""
#     to_pass = -1
#     for index, s in enumerate(solution):
       
#         if index == to_pass:
#             pass
#         elif index < len(solution) - 1 and solution[index] == solution[index + 1]: # s'ils sont egaux ex: u u mettre u2
#             new_solution += f"{s[0]}2 "
#             to_pass = index + 1
#         elif index < len(solution) - 1 and solution[index][0] == solution[index + 1][0]: # s'ils sont opposé ex: u u' annuler
#             to_pass = index + 1
#         else:
#             new_solution += f"{s} "

#     return new_solution


# new_solution = shorter_solution(cube.solution)
# new_solution = shorter_solution(new_solution)
# new_solution = new_solution.split()
# print(len(new_solution))
# print(new_solution)


# print(cube.solution)