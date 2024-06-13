from CubeClass import cube
from NodeClass import A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11
from Functions import action, solver_white_edges,turn_edge_up, turn_edge_back, turn_edge_left, turn_edge_right
from Rotations import Rien, Right, RightPrime, Left, LeftPrime, Up, UpPrime, Back, BackPrime, Down, DownPrime, Front, FrontPrime, R2, L2, B2, D2, U2, F2

import copy
#3 ans possible ?
#d'autres master ?
#condition à remplir admin
#contrat pro
#statut et salaire 


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


def existing_path(direction, path, dico_path):
    path.append(direction)
    for a, _p in dico_path.items():
        if path == _p:
            return True
    return False

#revient bien en arriere ✔️
def backtracking(node, old_node, node_init, path, dico_path, i, color):
    global nodes_blocked
    all_directions = directions(node)
    # if len(path) > 10:
    #     return old_node, dico_path, path
    

    for direction, next_node in all_directions.items():
        #condition de retour
        #arreter la recherche
        
        #unique condition de fermer un chemin
        #si le chemin souhaiter n'a pas déjà été trouvé et si W 
        #  next_node not in nodes_blocked pour pas lui piquer son voisin
        if 'W' in next_node.get_color() and color in next_node.get_color() and next_node not in nodes_blocked.values() :# and existing_path(direction, path, dico_path) == False:                    
            path.append(direction)
            copy_path = path.copy()
            dico_path[i] = copy_path
            path.pop()
            i+=1
        elif len(path) > 2:
            pass
        #chercher un autre chemin
        #s'assurer que le noeud suivant n'est pas node_init ou node_bloked
        #si W est dans le node 
        #condition chercher plus loins si la taille du chemin n'excède pas len < 4 #pour optimiser apres on verrra
        elif next_node != node_init:
            path.append(direction)
            copy_path = path.copy()
            node, dico_path, path = backtracking(next_node, node, node_init, copy_path, dico_path, i, color)
            if len(path) != 0:
                path.pop()
    return old_node, dico_path, path



cube.print_cube()

def resolve_cross():
    global nodes_blocked
    nodes = [A0, A1, A2, A3]
    colors = ['R', 'B', 'G', 'O']
    list_path_per_edge = []

    for index, n in enumerate(nodes):
        if 'W' in n.get_color() and colors[index] in n.get_color() and nodes_blocked[n] is None:
            nodes_blocked[n] = n
        else:
            path = []
            dico_path = {}
            i = 0
            node = n
            node_init = node
            old_node = None
            while node :
                node, dico_path, path = backtracking(node, old_node, node_init, path, dico_path, i, colors[index])
            action_temp = shorter_path(dico_path)
            if action_temp:
                list_path_per_edge.append(action_temp)

    return list_path_per_edge

def is_moved(before, after):
    nodes = [A0, A1, A2, A3]
    nodes_w = ['A0', 'A1', 'A2', 'A3']
    for index, n in enumerate(nodes):
        if after[n] and before[n] and before[n].get_color() != after[n].get_color():
            print("❌",nodes_w[index], ": ", before[n].get_color(), " -> ",  after[n].get_color())
            
            # return True
    return False



def ft_protection(nodes_blocked, action_temp):
    print("\n-----------FT_PROTECTION-------------\nnb action à executer: ",len(action_temp))

    protection = []
    other_protection = []
    once = True
    for index, direction in enumerate(reversed(action_temp)):
        if index > 0:
            if action_temp[index] != action_temp[index - 1] and len(protection) > 0: #tant qu'il n'a pas finit un meme mouvement
                print("💚")
                for p in protection:
                    action(p)()
                print("END")
                cube.print_cube()
                protection = [] #vider la liste
                once = True
               
        if once == True:
            for k, v in nodes_blocked.items():
                #u, u' u2
                if v and (direction == 8 or direction == 9): #si none inutile de proteger
                    if k == A0:
                        action(6)() #back
                        protection.append(7) #b'
                    if k == A1:
                        action(2)() #left
                        protection.append(3) #l'
                    if k == A2:
                        action(0)() #right
                        protection.append(1) #r'
                    if k == A3:
                        action(4)() #front
                        protection.append(5) #f'
                    once = False

                #r, r', r2
                # elif v and k == A2 and (direction == 0 or direction == 1): #seulement A2 qui est impliqué
                #     #ça depend du prochain coup
                #     if index < len(action_temp) - 1 and direction[index] == direction[index + 1]
                        
                #         #si next_direction = r
                #         if direction == 0:
                #             action(6)() # back
                #             other_protection.append(7) #b'

                #         #si next_direction = r'
                #         if direction == 1:
                #             action(4)() # front
                #             other_protection.append(5) #f'
                    
                    
                    



        #on fait l'action apres avoir proteger
        action(direction)()
        if len(other_protection) > 0:
            print("💚other protec")
            for p in other_protection:
                action(p)()

    #si programme se finit, terminer  
    if len(protection) > 0:      
        print("💚")
        for p in protection:
            action(p)()
        print("END")                
            
    
    # elif direction == 6 or direction == 7 #b
    #si A0 et que action back,  faire action suivant et back'
    #si A1 et que action left, faire action suivant et left'
    #si A2 et que action right, faire action suivant et right'
    #si A3 et que action front, faire action suivant et front'



nodes_blocked = {
    A0: None,
    A1: None,
    A2: None,
    A3: None
}
count = 0
while count != 4: #mettre 4 pour les 4 aretes
    nodes = [A0, A1, A2, A3]
    nodes_w = ['A0', 'A1', 'A2', 'A3']

    list_path_per_edge = resolve_cross()
    action_temp = speeder_path(list_path_per_edge)

    if action_temp : #si l'action existe, l'executer 
        
        #proteger les nodes_blocked, executer l'action et remettre les nodes_blocked à leur place
        ft_protection(nodes_blocked, action_temp)
            
            #si autre action refaire la premiere? action à l'envers
            # moove = is_moved(state_before, nodes_blocked)
            
         
                
        

    count += 1
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
def shorter_solution():
    solution = cube.solution.split()
    new_solution = ""
    to_pass = -1
    for index, s in enumerate(solution):
       
        if index == to_pass:
            pass
        elif index < len(solution) - 1 and solution[index] == solution[index + 1]: # s'ils sont egaux ex: u u mettre u2
            new_solution += f"{s[0]}2 "
            to_pass = index + 1
        elif index < len(solution) - 1 and solution[index][0] == solution[index + 1][0]: # s'ils sont opposé ex: u u' annuler
            to_pass = index + 1
        else:
            new_solution += f"{s} "

    return new_solution


new_solution = shorter_solution()
print(new_solution)
new_solution = new_solution.split()
print(new_solution)
print(len(new_solution))


# print(cube.solution)