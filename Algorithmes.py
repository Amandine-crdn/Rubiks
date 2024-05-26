def B():
    pass
def U():
    pass

def D(arete, nb_rotation):
    for _ in range(nb_rotation):
        print("test")
    
def Right(cube):
    print("fonction R")
    print("before")
    C2 = cube.get_color_coin(2)
    C6 = cube.get_color_coin(6)
    C8 = cube.get_color_coin(8)
    C4 = cube.get_color_coin(4)

    A3 = cube.get_color_arete(3)
    A8 = cube.get_color_arete(8)
    A10 = cube.get_color_arete(10)
    A11 = cube.get_color_arete(11)

    print("\nafter")

    cube.set_color_coin(2, C4)
    cube.set_color_coin(4, C8)
    cube.set_color_coin(8, C6)
    cube.set_color_coin(6, C2)

    cube.set_color_arete(3, A8)
    cube.set_color_arete(10, A3)
    cube.set_color_arete(11, A10)
    cube.set_color_arete(8, A11)



    C2 = cube.get_color_coin(2)
    C6 = cube.get_color_coin(6)
    C8 = cube.get_color_coin(8)
    C4 = cube.get_color_coin(4)

    A3 = cube.get_color_arete(3)
    A8 = cube.get_color_arete(8)
    A10 = cube.get_color_arete(10)
    A11 = cube.get_color_arete(11)

    return "R"


#tout reprendre avec les aretes et les coins pour les bouger 

def L(arete, nb_rotation):
    pass
def F(arete, nb_rotation):
    pass

def search_aretes(color: int):
    aretes = []
    for face in faces:
        for num in range(0, 9):
            if face[num].get_color() == color and face[num].get_numéro_carré() % 2 == 0:
                aretes.append(face[num])
    return aretes

def choice_rotation_arete(num_carré_arete: int, arete, nb_rotation):
    if num_carré_arete == 2:
        return D(arete, nb_rotation)
    elif num_carré_arete == 4:
        return L(arete, nb_rotation)
    elif num_carré_arete == 6:
        return R(arete, nb_rotation)
    elif num_carré_arete == 8:
        return F(arete, nb_rotation)
