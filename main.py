from CubeClass import cube
from NodeClass import A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11
from Functions import solver_white_edges,turn_edge_up, turn_edge_back, turn_edge_left, turn_edge_right

cube.print_cube()
print("--- INIT ----")

list_whites_nodes = [A6, A8, A10, A11]
functions_turn = [turn_edge_left, turn_edge_up, turn_edge_right, turn_edge_back]
emoji_color = ["🟩", "🟨", "🟪", "🟧"]



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
dico = {}
find = True
i = 0
path = []
nodes_meet = []
node_init = A6

def tracking_node(node, color):
    global i
    global find
    global path
    global nodes_meet
    global dico
    global node_init

    choices = have_tuple(node)
    for k, v in choices.items():
        if color in v.get_color():
            path.append(k)
            dico[i] = path.copy()
            if len(path) != 0:
                path.pop()
            print("💓 FIND ",v.get_color(), i, dico[i])
            i+=1
            #on a enregistrer le chemin mais il continue de checker 
        
        elif v not in nodes_meet and v is not node_init: #avancer: donc ajouter au dico
            nodes_meet.append(v)
            path.append(k)
            dico[i] = path.copy()
            tracking_node(v, color)
            if len(path) != 0:
                path.pop()
   
    return  None
 
node = A6

while node:
    node = tracking_node(node, 'W')

action_temp = dico[0]

for k, v in dico.items():
    if len(v) < len(action_temp):
        action_temp = v
print(action_temp)



# for i, node in enumerate(list_whites_nodes):#
#     if node.get_color()[1] == 'W':  
#         cube.append(node)

#First step: make the white cross
# for i, node in enumerate(list_whites_nodes):
#     print(f"\n{emoji_color[i]} {node.get_color()}")
#     if 'W' not in node.get_color():
#         print(f"{emoji_color[i]} solver {node.get_color()}")
#         tracking_node()
#         solver_white_edges(node)
#         print(f"after cube {emoji_color[i]} {node.get_color()}")
#         cube.print_cube()

#     if node.get_color()[1] != 'W':     #check color orientation edge
#         print(f"\n{emoji_color[i]} solver orientation {node.get_color()}")
#         functions_turn[i]()
#         cube.print_cube()
#     cube.append(node) #only for this function to find an other path
#     print("\n--- NEXT ----\n")


#marche pas tout le temps avec la generation des aretes aléatoires....


















#face blanche: 19 (pas finit)
# D2, L2, U', F', L, F, R, R2, U, F, R', F', F2, F2, U', R', F, R, B'
#remonter les aretes avec centre correspondant
#placer les coins, bonnes orientations