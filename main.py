from CubeClass import cube
from NodeClass import A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11
from Functions import action, solver_white_edges,turn_edge_up, turn_edge_back, turn_edge_left, turn_edge_right
cube.print_cube()
print("--- INIT ----")

list_whites_nodes = [A6, A8, A10, A11]
emoji_color = ["🟩", "🟨", "🟪", "🟧"]
locked_nodes = []



def have_tuple(node):
    if node is None:
        return {}
    dico = {}
    getters = node._getter()
    for k, v in getters:
        if v:
            dico[k] = v
    return dico


#backtracking
def tracking_node(node, color):
    global i
    global path
    global nodes_meet
    global dico
    global node_init
    global locked_nodes

    choices = have_tuple(node)
    for k, v in choices.items():

        if color in v.get_color() and v not in locked_nodes:
            #❌❌❌  checker si l'arete arrive du bon coté sinon continuer de chercher  ❌❌❌
            pass
        if color in v.get_color() and v not in locked_nodes:#ok ne pas aller cherher directement dans les nodes bloqués
            path.append(k)
            dico[i] = path.copy()
            if len(path) != 0:
                path.pop()
            i+=1
            #on a enregistrer le chemin mais il continue de checker 
        
        elif v not in nodes_meet and v is not node_init and v not in locked_nodes: #avancer: donc ajouter au dico
            nodes_meet.append(v)
            path.append(k)
            dico[i] = path.copy() #si false continues de chercher mais ne vas pas plus loin
            tracking_node(v, color)
            if len(path) != 0:
                path.pop()
   
    return  None
 
# def move_locked(path):
#     global locked_nodes
#     # color des locked node avant
#     dico = {
#         0: [A9, A2, A7, A10],
#         1: [A9, A2, A7, A10],
#         2: [A1, A5, A4, A6],
#         3: [A1, A5, A4, A6],
#         4: [A0, A4, A9, A11],
#         5: [A0, A4, A9, A11],
#         6: [A3, A5, A7, A8],
#         7: [A3, A5, A7, A8],
#         8: [A0, A1, A2, A3],
#         9: [A0, A1, A2, A3],
#         10: [A6, A8, A10, A11],
#         11: [A6, A8, A10, A11]
#     }
#     #simulation mouvement
#     for direction in reversed(path):
#         for node in locked_nodes:
#             if node in dico[direction]:
#                 print("False")
#                 #le remettre juste apres
#                 return False
#     return True

def select(node):
    if dico == {}:
        return None
    global locked_nodes
    action_temp = dico[0]
    for k, v in dico.items():
        if len(v) < len(action_temp):
            action_temp = v
    print("💓",action_temp)
    for direction in reversed(action_temp):
        action(direction)()

switch_edge = [turn_edge_left, turn_edge_up, turn_edge_right, turn_edge_back] 

index = 0 #dans le backtracking faire en sorte qu'il check si l'arete va bien tomber ? sinon regarde autre chose
while index != 4: # pour compenser: backtracking ne fait pas toutes les possibilités on dirait
    index_node = 0
    for n in list_whites_nodes:

        dico = {}
        i, index = 0, 0
        path, nodes_meet = [], []
        node_init, node = n, n
        while node:
            if 'W' in node.get_color():
                break
            node = tracking_node(node, 'W')
        select(n)
        #faire le renversement des aretes ici
        locked_nodes.append(n)
  
    for n in list_whites_nodes:
        if 'W' in n.get_color():
            index += 1
cube.print_cube()
    
for node_index, n in enumerate(list_whites_nodes, start=0): #pour compenser le backtracking
    if n.get_color()[1] != 'W':
        print("switch")
        switch_edge[node_index]()

cube.print_cube()
# action_temp()

#idee opti si l l l faire l'



#face blanche: 19 (pas finit)
# D2, L2, U', F', L, F, R, R2, U, F, R', F', F2, F2, U', R', F, R, B'
#remonter les aretes avec centre correspondant
#placer les coins, bonnes orientations