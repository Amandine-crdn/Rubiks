from CubeClass import cube
from NodeClass import A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11
from Functions import action, solver_white_edges,turn_edge_up, turn_edge_back, turn_edge_left, turn_edge_right
from Rotations import Rien, Right, RightPrime, Left, LeftPrime, Up, UpPrime, Back, BackPrime, Down, DownPrime, Front, FrontPrime, R2, L2, B2, D2, U2, F2

cube.print_cube()

print("--- INIT ----")

emoji_color = ["🟩", "🟨", "🟪", "🟧"]
locked_nodes = []


def have_tuple(node): #noeud non NULL, renvoie la direction associé au noeud
    if node is None:
        return {}
    dico = {}
    getters = node._getter()
    for k, v in getters:
        if v:
            dico[k] = v
    return dico

def check_path(k):
    copy_path = path.copy()
    copy_path.append(k)
    for a, micro_path in dico.items():
        if copy_path == micro_path:
            return False
    return True

#backtracking
def tracking_node(new_node, old_node, color):
    global i
    global path
    global dico
    global node_init
    global locked_nodes
    choices = have_tuple(new_node)

    for k, v in choices.items():

        if color in v.get_color() and v not in locked_nodes:
            path.append(k)
            dico[i] = path.copy()
            i+=1
            if len(path) != 0:
                path.pop()
            #on a enregistrer le chemin mais il continue de checker 
        elif check_path(k) == False or len(path) > 4: #si chemin déjà rencontré
            pass
        elif v not in locked_nodes and v is not node_init: #avancer:continues de chercher donc ajouter au dico
            path.append(k)
            dico[i] = path.copy()
            new_node = tracking_node(v, new_node, color)
            if len(path) != 0:
                path.pop()

    return old_node, dico


def select(node, dico):
    if dico == {}:
        return #pck il est bien placer (le W est bien en haut, sans etre bien orienter ou center pour autant)
    action_temp = dico[0]
    for k, v in dico.items():
        if len(v) < len(action_temp):
            action_temp = v
    # for direction in reversed(action_temp):
    #     action(direction)()
    return action_temp #new, a delete et remettre au dessus

list_whites_nodes = [A0, A1, A2, A3]
index = 0


path = []
dico = {}
i = 0
node_init = None
#pour chaque noeud recuperer le chemin le plus court:

def best_choice(node):
    i = 0
    dico = {}
    path = []
    node_init = node
    while node:
        if 'W' in node.get_color():
            break
        node, dico = tracking_node(node, None, 'W')
    return select(node_init, dico)

# while index != 4: #possible boucle infinie
#     for y, n in enumerate(list_whites_nodes):
#         i = 0
#         dico = {}
#         path = []
#         node_init = n
#         node = n
#         while node:
#             if 'W' in node.get_color():
#                 break
#             node = tracking_node(node, None, 'W')
#         # select(n)
#         locked_nodes.append(n)
#         index = 0
#         for n in list_whites_nodes:
#             if 'W' in n.get_color():
#                 index += 1

locked_nodes = {
    0: None,
    1: None,
    2: None,
    3: None 
}
count = 0
while count != 4:

    list_choice = []

    for n in list_whites_nodes:
        print("search for", n.get_color())
        #pour chaque noeud
        find = False
        #sil fait parti des noeuds bloqués
        for k, v in locked_nodes.items():
            if n is not None and n == v:
                #lajouter None a la suite de choix a faire
                list_choice.append(None)
                find = True
        #si ce n'est pas un noeud bloquer, chercher la meilleure solution
        if find == False:
            list_choice.append(best_choice(n))
    
    print("--- best choice ---")
    for index, choice in enumerate(list_choice):
        print(f"{index} - {list_whites_nodes[index].get_color()} {choice}")
   
    action_temp = None
    find = False
    #on va chercher a executer le plus petit chemin
    for index, choice in enumerate(list_choice):
        print("---> ",choice)
        #si un chemin et None et qu'il  n'est pas dans les noeud bloquer
        # le bloquer et passer au noeud suivant
        if choice is None and list_whites_nodes[index] != locked_nodes[index]:
            find = True
            locked_nodes[index] = list_whites_nodes[index]
            print("🔞ajout de noeud")
            break   
        #s'il est None et qu'il est dans le noeud bloquer
        if choice is None:
            #regarder la suite des chemins sans en tenir compte
            pass
        #choisir la derniere action
        elif find == False:
            action_temp = choice
   
    #si l'action est faisable
    if action_temp is not None: 
        print("action faisable",action_temp)
        for v in list_choice:
            if v and len(v) < len(action_temp):
                action_temp = v
        for direction in reversed(action_temp):
            action(direction)()

    count = 0
    for k, v in locked_nodes.items():
        if v:
            print(v.get_color())
            count +=1
    print("count", count)

cube.print_cube()


# print("----- SWITCH ----")
# #faire le renversement des aretes à la fin du backtracking
# switch_edge = [turn_edge_back, turn_edge_left, turn_edge_right, turn_edge_up] 
# for node_index, n in enumerate(list_whites_nodes, start=0):
#     if n.get_color()[0] != 'W':
#         switch_edge[node_index]()
# cube.print_cube()


# color = ["WR", "WB", "WG", "WO"]
# action_center = [B2, L2, R2, F2]

# #tourner la face sur le carré s'il correspond
# #avec u trouver le milieu correspondant puis rabaisser l'arete sur la face

# print("----- CENTER ----")
# count = 0
# while count != 4 :
#     for y, n in enumerate(list_whites_nodes):
#         if color[y] == n.get_color() :
#             action_center[y]()
#             count +=1
#     Up()
# for y in range(0,4):
#     action_center[y]()

# cube.print_cube()



# #idee opti si l l l faire l'


# #placer les coins, bonnes orientations