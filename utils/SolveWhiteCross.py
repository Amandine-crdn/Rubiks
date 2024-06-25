from Rotations import Right, RightPrime, Left, LeftPrime, Up, UpPrime, Back, BackPrime, Down, DownPrime, Front, FrontPrime, R2, L2, B2, D2, U2, F2
from NodeClass import Node, A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, C0, C1, C2, C3, C4, C5, C6, C7
from Functions import action
from CubeClass import cube

#rotations #idee a mettre en methode rotation dans cube ?
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

def backtracking(node: Node, old_node: Node, node_init: Node, path: list[int], dico_path: dict[int, list[int]], i: int, color: int, nodes_blocked: dict[int, Node], index: int):
    all_directions = directions(node)
    
    for direction, next_node in all_directions.items():
        
        #unique condition de fermer un chemin
        if 'W' in next_node.get_color() and color in next_node.get_color() and check_is_locked(next_node, nodes_blocked) == False:
            path.append(direction)
            copy_path = path.copy()
            dico_path[i] = copy_path
            path.pop()
            i+=1
        #condition chercher plus loins si la taille du chemin n'excède pas len < 2 #pour optimiser apres on verra
        elif len(path) > 2:
            pass
            # continue
        
        #chercher un autre chemin

        #s'assurer que le noeud suivant n'est pas node_init ou node_bloked ???
        elif next_node != node_init and check_is_locked(next_node, nodes_blocked) == False :
            path.append(direction)
            copy_path = path.copy()
            node, dico_path, path, i = backtracking(next_node, node, node_init, copy_path, dico_path, i, color, nodes_blocked, index)
            if len(path) != 0:
                path.pop() #pour abandonner chemin

    return old_node, dico_path, path, i



def resolve_cross(nodes_blocked: dict[int, Node]):
    nodes = [A0, A1, A2, A3]
    colors = ['R', 'B', 'G', 'O']
    list_path_per_edge = []

    for index, n in enumerate(nodes):
        
        if 'W' in n.get_color() and colors[index] in n.get_color() and nodes_blocked[index] is None:
            nodes_blocked[index] = n
        else:
            path = []
            dico_path = {}
            i = 0
            node = n
            node_init = node
            old_node = None
            while node :
                node, dico_path, path, i = backtracking(node, old_node, node_init, path, dico_path, i, colors[index], nodes_blocked, index)
            action_temp = shorter_path(dico_path, index) #selectionner le chemin le plus court pour le node en cours selon l'ensemble de son dico
            if action_temp:
                list_path_per_edge.append(action_temp)

    return list_path_per_edge, nodes_blocked



def speeder_path(liste: list[tuple]):
    if liste == []:
        return None
    action_temp = liste[0]
    for l in liste:
        if len(l[1]) < len(action_temp[1]):
            action_temp = l
    return action_temp


def shorter_path(dico: dict, index: int):
    if dico == {}:
        return None #pck il est bien placer (le W est bien en haut, sans etre bien orienter ou center pour autant)
    
    action_temp = (index, dico[0])
    for k, v in dico.items():
        if len(v) < len(action_temp):
            action_temp = (index, v)
    return action_temp #retourne le chemin le plus court


def directions(node: Node): #noeud non NULL, renvoie la direction associé au noeud
    if node is None:
        return {}
    dico = {}
    getters = node._getter()
    for k, v in getters:
        if v: #si non NULL l'ajouter au dico
            dico[k] = v
    return dico


def check_is_locked(next_node: Node, nodes_blocked: dict[int, Node]):
    for i in range(0, 4):
        if nodes_blocked[i] and nodes_blocked[i] == next_node:
            return True
    return False


# def ft_protection(nodes_blocked: dict[int, Node], action_temp: tuple[int, list[int]]):
#     # print("\n🐜 -----------------------")
#     # print(action_temp[1])
#     other_protection = []
#     protection = [] #liste car si besoin de protéger les 4 aretes pour un coup
#     once = True
    
#     for index, direction in enumerate(reversed(action_temp[1])):
#         if index > 0 and action_temp[1][index] != action_temp[1][index - 1]:
#             if len(protection) > 0: #tant qu'il n'a pas finit un meme mouvement
#                 for p in protection:
#                     action(p)()
#                 protection = [] #vider la liste
#                 once = True
               
#         if once == True:
#             for k, v in nodes_blocked.items():
#                 #u, u' u2
#                 if v and (direction == 8 or direction == 9): #si none inutile de proteger
                    
#                     if k == 0 and v == A0:
#                         action(6)() #back
#                         action(6)() #back
#                         protection.extend([6, 6]) #b2
#                         once = False
#                     if k == 1 and v == A1:
#                         action(2)() #left
#                         action(2)() #left
#                         protection.extend([2, 2]) #l2
#                         once = False
#                     if k == 2 and v == A2:
#                         action(0)() #right
#                         action(0)() #right
#                         protection.extend([0, 0]) #r2
#                         once = False
#                     if k == 3 and v == A3:
#                         action(4)() #front
#                         action(4)() #front
#                         protection.extend([4, 4]) #f2
#                         once = False
#                     #continuer de boucler car les rotations u peuvent modifier toutes les aretes

#                 #once == True pour pas que les 2 se cumulent
#                 elif once == True and v == A0 and k == 0 and (direction == 6 or direction == 7): #back
#                     for k, v in nodes_blocked.items():
#                         if v is None:
#                             if k == 1:
#                                 action(8)() #u
#                                 other_protection.append(9)
#                             elif k == 2:
#                                 action(9)() #u'
#                                 other_protection.append(8)
#                             elif k == 3:
#                                 action(8)() #u
#                                 action(8)() #u
#                                 other_protection.extend([8, 8])
#                             break

#                 elif once == True and v == A1 and k == 1 and (direction == 2 or direction == 3): #left
#                     for k, v in nodes_blocked.items():
#                         if v is None:
#                             if k == 0:
#                                 action(9)() #u'
#                                 other_protection.append(8)
#                             elif k == 2:
#                                 action(8)() #u2
#                                 action(8)() #u2
#                                 other_protection.extend([8, 8])
#                             elif k == 3:
#                                 action(8)() #u
#                                 other_protection.append(9)
#                             break
    
#                 elif once == True and v == A2 and k == 2 and (direction == 0 or direction == 1): #right
#                     for k, v in nodes_blocked.items():
#                         if v is None:
#                             if k == 0:
#                                 action(8)() #u
#                                 other_protection.append(9)
#                             elif k == 1:
#                                 action(8)() #u2
#                                 action(8)() #u2
#                                 other_protection.extend([8, 8])
#                             elif k == 3:
#                                 action(9)() #u'
#                                 other_protection.append(8)
#                             break
                 
#                 elif once == True and v == A3 and k == 3 and (direction == 4 or direction == 5): #front
#                     for k, v in nodes_blocked.items():
#                         if v is None:
#                             if k == 0:
#                                 action(8)() #u2
#                                 action(8)() #u2
#                                 other_protection.extend([8, 8])
#                             elif k == 1:
#                                 action(9)() #u'
#                                 other_protection.append(8)
#                             elif k == 2:
#                                 action(8)() #u
#                                 other_protection.append(9)
#                             break
               
  
#         #on fait l'action apres avoir proteger
#         action(direction)()
#         if len(other_protection) > 0:
#             for op in other_protection:
#                 action(op)()
#             other_protection = []

#     #si programme se finit, terminer  
#     if len(protection) > 0:      
#         for p in protection:
#             action(p)()

def protection_rotation_up(nodes_blocked: dict[int, Node], direction: int):
    #u, u' u2
    protection = []
    number_nodes_locked = get_number_nodes_locked(nodes_blocked)
    # 1 noeuds bloqué: 4 cas
    if number_nodes_locked == 1:
        if nodes_blocked[0]:
            action(6)() #back
            protection.append(7) #b'
        elif nodes_blocked[1]:
            action(2)() #left
            protection.append(3) #l'
        elif nodes_blocked[2]:
            action(0)() #right
            protection.append(1) #r'
        elif nodes_blocked[3]:
            action(4)() #front
            protection.append(5) #f'
        return False, protection


    # 2 noeuds bloqués: 6 cas
    if number_nodes_locked == 2:
        print("number_nodes_locked",number_nodes_locked)
        if nodes_blocked[0] and nodes_blocked[3]:# and nodes_blocked[1] is None and nodes_blocked[2] is None:
            action(6)() #back pour A0
            action(4)() #front pour A3
            protection.extend([7, 5]) #b', f'

        elif nodes_blocked[1] and nodes_blocked[2]:# and nodes_blocked[0] is None and nodes_blocked[3] is None:
            action(2)() #left pour A1
            action(0)() #right pour A2
            protection.extend([3, 1]) #l', r'
        #new
        elif nodes_blocked[0] and nodes_blocked[1]:# and nodes_blocked[0] is None and nodes_blocked[3] is None:
            action(7)() #b' pour A0
            action(2)() #l pour A1
            protection.extend([6, 3]) #b, l'
        elif nodes_blocked[0] and nodes_blocked[2]:# and nodes_blocked[0] is None and nodes_blocked[3] is None:
            action(6)() #b pour A0
            action(1)() #r' pour A2
            protection.extend([7, 0]) #b', r
        elif nodes_blocked[1] and nodes_blocked[3]:# and nodes_blocked[0] is None and nodes_blocked[3] is None:
            action(3)() #l' pour A1
            action(4)() #f pour A3
            protection.extend([2, 5]) #l, f'
        elif nodes_blocked[2] and nodes_blocked[3]:# and nodes_blocked[0] is None and nodes_blocked[3] is None:
            action(0)() #r pour A2
            action(5)() #f' pour A3
            protection.extend([1, 4]) #r', f
        return False, protection

    
    # 3 noeuds bloqués: 4 cas
    if number_nodes_locked == 3:
        print("number_nodes_locked",number_nodes_locked)
        if nodes_blocked[3] and nodes_blocked[2] and nodes_blocked[1] and nodes_blocked[0] is None:
            action(0)() #right
            action(4)() #front
            action(2)() #left
            protection.extend([3, 5, 1]) #l', f', r'
        
        elif nodes_blocked[2] and nodes_blocked[1] and nodes_blocked[0] and nodes_blocked[3] is None:
            action(2)() #left
            action(6)() #back
            action(0)() #right
            protection.extend([1, 7, 3]) #r', b', l'
        
        elif nodes_blocked[1] and nodes_blocked[0] and nodes_blocked[3] and nodes_blocked[2] is None:
            action(4)() #front
            action(2)() #left
            action(6)() #back
            protection.extend([7, 3, 5]) #b', l', f'
        
        elif nodes_blocked[0] and nodes_blocked[3] and nodes_blocked[2] and nodes_blocked[1] is None:
            action(6)() #back
            action(0)() #right
            action(4)() #front
            protection.extend([5, 1, 7]) #f', r', b'
        return False, protection

    return True, protection

def protection_other_rotations(nodes_blocked: dict[int, Node], direction: int):
    other_protection = []
    for k, v in nodes_blocked.items():
        #si une méthode de protection faire, return pour ne pas continuer de boucler sur d'autres protections (gain de temps)
        #but: chercher le noeud None volontairement pour justement le placer à l'endroit de la rotation, car si sa valeur change ça ne casse pas les bons emplacements
        
        #backs rotation
        if v and k == 0 and (direction == 6 or direction == 7):
            for k, v in nodes_blocked.items():
                if v is None: #ici on cherche le v none contrairement à protection_rotation_up
                    if k == 1:
                        action(8)() #u
                        other_protection.append(9)
                    elif k == 2:
                        action(9)() #u'
                        other_protection.append(8)
                    elif k == 3:
                        action(8)() #u
                        action(8)() #u
                        other_protection.extend([8, 8])
                    return other_protection
        
        #lefts rotation
        elif v and k == 1 and (direction == 2 or direction == 3):
            for k, v in nodes_blocked.items():
                if v is None:
                    if k == 0:
                        action(9)() #u'
                        other_protection.append(8)
                    elif k == 2:
                        action(8)() #u2
                        action(8)() #u2
                        other_protection.extend([8, 8])
                    elif k == 3:
                        action(8)() #u
                        other_protection.append(9)
                    return other_protection
        
        #rights rotation
        elif v and k == 2 and (direction == 0 or direction == 1): 
            for k, v in nodes_blocked.items():
                if v is None:
                    if k == 0:
                        action(8)() #u
                        other_protection.append(9)
                    elif k == 1:
                        action(8)() #u2
                        action(8)() #u2
                        other_protection.extend([8, 8])
                    elif k == 3:
                        action(9)() #u'
                        other_protection.append(8)
                    return other_protection

        #fronts rotation
        elif v and k == 3 and (direction == 4 or direction == 5): 
            for k, v in nodes_blocked.items():
                if v is None:
                    if k == 0:
                        action(8)() #u2
                        action(8)() #u2
                        other_protection.extend([8, 8])
                    elif k == 1:
                        action(9)() #u'
                        other_protection.append(8)
                    elif k == 2:
                        action(8)() #u
                        other_protection.append(9)
                    return other_protection

    return  other_protection
    
def get_number_nodes_locked(nodes_blocked: dict[int, Node]):
    number_nodes_locked = 0
    for k, v in nodes_blocked.items():
        if v: 
            number_nodes_locked += 1
    return number_nodes_locked

def ft_protection(nodes_blocked: dict[int, Node], action_temp: tuple[int, list[int]]):
    other_protection = []
    protection = [] #liste car si besoin de protéger les 4 aretes pour un coup
    once = True

    for index, direction in enumerate(reversed(action_temp[1])):
        if index > 0 and action_temp[1][index] != action_temp[1][index - 1]:
            if len(protection) > 0: #tant qu'il n'a pas finit un meme mouvement
                for p in protection:
                    action(p)()
                protection = [] #vider la liste
                once1 = True
            
               
        if once == True and (direction == 8 or direction == 9) :
            once, protection = protection_rotation_up(nodes_blocked, direction) #retourne once = False s'il a fait une méthode de protection
        if once == True: #once == True pour pas que les 2 se cumulent
            other_protection = protection_other_rotations(nodes_blocked, direction)
        #on fait l'action apres avoir proteger
        action(direction)()
        if len(other_protection) > 0:
            for op in other_protection:
                action(op)()
            other_protection = [] #on vide la liste

        #on effectue ici la rotation de autre protection inverse pour remettre le noeud bloquer à sa place
        

    #si programme se finit, terminer les actions de protection
    if len(protection) > 0:      
        for p in protection:
            action(p)()
