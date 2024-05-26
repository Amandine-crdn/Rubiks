def B():
    pass
def U():
    pass

def D(arete, nb_rotation):
    for _ in range(nb_rotation):
        print("test")
    
def Right(cube):
    print("\nfonction R")
    print("before\n")
    C2 = cube.get_color_coin(1)
    C6 = cube.get_color_coin(5)
    C8 = cube.get_color_coin(7)
    C4 = cube.get_color_coin(3)

    A3 = cube.get_color_arete(2)
    A8 = cube.get_color_arete(7)
    A10 = cube.get_color_arete(9)
    A11 = cube.get_color_arete(10)

    print("\nafter\n")

    cube.set_color_coin(1, C4)
    cube.set_color_coin(3, C8)
    cube.set_color_coin(7, C6)
    cube.set_color_coin(5, C2)

    cube.set_color_arete(2, A8)
    cube.set_color_arete(9, A3)
    cube.set_color_arete(10, A10)
    cube.set_color_arete(7, A11)



    C2 = cube.get_color_coin(1)
    C6 = cube.get_color_coin(5)
    C8 = cube.get_color_coin(7)
    C4 = cube.get_color_coin(3)

    A3 = cube.get_color_arete(2)
    A8 = cube.get_color_arete(7)
    A10 = cube.get_color_arete(9)
    A11 = cube.get_color_arete(10)

def search_arete (cube, color1: int, color2: int):
    aretes = cube.get_aretes()
    for index, a in enumerate(aretes):
        if color1 in a and color2 in a:
            print(a, index)
            return index
        
def search_aretes(cube, color: int):
    dico = {}
    aretes = cube.get_aretes()
    for index, a in enumerate(aretes):
        if color in a :
            dico[index] = a
    return dico
            

#tout reprendre avec les aretes et les coins pour les bouger 

def L(arete, nb_rotation):
    pass
def F(arete, nb_rotation):
    pass

# def search_aretes(color: int):
#     aretes = []
#     for face in faces:
#         for num in range(0, 9):
#             if face[num].get_color() == color and face[num].get_numéro_carré() % 2 == 0:
#                 aretes.append(face[num])
#     return aretes

def choice_rotation_arete(num_carré_arete: int, arete, nb_rotation):
    if num_carré_arete == 2:
        return D(arete, nb_rotation)
    elif num_carré_arete == 4:
        return L(arete, nb_rotation)
    elif num_carré_arete == 6:
        return R(arete, nb_rotation)
    elif num_carré_arete == 8:
        return F(arete, nb_rotation)
