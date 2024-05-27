
def Right(cube):
    print("\n🥐 fonction Right")
    
    #move corners
    C1 = cube.get_color_coin(1)
    C3 = cube.get_color_coin(3)
    C5 = cube.get_color_coin(5)
    C7 = cube.get_color_coin(7)

    cube.set_color_coin(1, C3[2] + C3[0] + C3[1]) #✔️
    cube.set_color_coin(3, C7[2] + C7[0] + C7[1]) #✔️
    cube.set_color_coin(5, C1[2] + C1[0] + C1[1]) #✔️
    cube.set_color_coin(7, C5) #✔️

    #move edges
    A2 = cube.get_color_arete(2)
    A7 = cube.get_color_arete(7)
    A9 = cube.get_color_arete(9)
    A10 = cube.get_color_arete(10)

    cube.set_color_arete(2, A7) #✔️
    cube.set_color_arete(7, A10[1] + A10[0]) #✔️
    cube.set_color_arete(9, A2[1] + A2[0]) #✔️
    cube.set_color_arete(10, A9) #✔️

def RightPrime(cube):
    print("\n🥐 fonction RightPrime")

    #move corners
    C1 = cube.get_color_coin(1)
    C3 = cube.get_color_coin(3)
    C5 = cube.get_color_coin(5)
    C7 = cube.get_color_coin(7)

    cube.set_color_coin(1, C5[1] + C5[2] + C5[0]) #✔️
    cube.set_color_coin(3, C1[1] + C1[2] + C1[0]) #✔️
    cube.set_color_coin(5, C7) #✔️
    cube.set_color_coin(7, C3[1] + C3[2] + C3[0]) #✔️

    #move edges
    A2 = cube.get_color_arete(2)
    A7 = cube.get_color_arete(7)
    A9 = cube.get_color_arete(9)
    A10 = cube.get_color_arete(10)

    cube.set_color_arete(2, A9[1] + A9[0]) #✔️
    cube.set_color_arete(7, A2) #✔️
    cube.set_color_arete(9, A10) #✔️
    cube.set_color_arete(10, A7[1] + A7[0]) #✔️

def Left(cube):
    print("\n🥐 fonction Left")
    
    #move corners
    C0 = cube.get_color_coin(0)
    C2 = cube.get_color_coin(2)
    C4 = cube.get_color_coin(4)
    C6 = cube.get_color_coin(6)

    cube.set_color_coin(0, C4[2] + C4[0] + C4[1]) #✔️
    cube.set_color_coin(2, C0[2] + C0[0] + C0[1]) #✔️
    cube.set_color_coin(4, C6[0] + C6[2] + C6[1]) #✔️
    cube.set_color_coin(6, C2[2] + C2[1] + C2[0]) #✔️

    #move edges
    A1 = cube.get_color_arete(1)
    A4 = cube.get_color_arete(4)
    A5 = cube.get_color_arete(5)
    A6 = cube.get_color_arete(6)

    cube.set_color_arete(1, A4[1] + A4[0])  #✔️
    cube.set_color_arete(4, A6)  #✔️
    cube.set_color_arete(5, A1[1] + A1[0])  #✔️
    cube.set_color_arete(6, A5)  #✔️

def LeftPrime(cube):
    print("\n🥐 fonction LeftPrime")

    #move corners
    C0 = cube.get_color_coin(0)
    C2 = cube.get_color_coin(2)
    C4 = cube.get_color_coin(4)
    C6 = cube.get_color_coin(6)

    cube.set_color_coin(0, C2[1] + C2[2] + C2[0]) #✔️
    cube.set_color_coin(2, C6[2] + C6[1] + C6[0]) #✔️
    cube.set_color_coin(4, C0[1] + C0[2] + C0[0]) #✔️
    cube.set_color_coin(6, C4[0] + C4[2] + C4[1]) #✔️

    #move edges
    A1 = cube.get_color_arete(1)
    A4 = cube.get_color_arete(4)
    A5 = cube.get_color_arete(5)
    A6 = cube.get_color_arete(6)

    cube.set_color_arete(1, A5[1] + A5[0])#✔️
    cube.set_color_arete(4, A1[1] + A1[0])#✔️
    cube.set_color_arete(5, A6)#✔️
    cube.set_color_arete(6, A4)#✔️


def Up(cube):
    print("\n🥐 fonction Up")
    
    #move corners
    C0 = cube.get_color_coin(0)
    C1 = cube.get_color_coin(1)
    C2 = cube.get_color_coin(2)
    C3 = cube.get_color_coin(3)
    cube.set_color_coin(0, C2)#✔️
    cube.set_color_coin(1, C0)#✔️
    cube.set_color_coin(2, C3)#✔️
    cube.set_color_coin(3, C1)#✔️

    #move edges
    A0 = cube.get_color_arete(0)
    A1 = cube.get_color_arete(1)
    A2 = cube.get_color_arete(2)
    A3 = cube.get_color_arete(3)

    cube.set_color_arete(0, A1)#✔️
    cube.set_color_arete(1, A3)#✔️
    cube.set_color_arete(2, A0)#✔️
    cube.set_color_arete(3, A2)#✔️

def UpPrime(cube):
    print("\n🥐 fonction UpPrime")

    #move corners
    C0 = cube.get_color_coin(0)
    C1 = cube.get_color_coin(1)
    C2 = cube.get_color_coin(2)
    C3 = cube.get_color_coin(3)

    cube.set_color_coin(0, C1)#✔️
    cube.set_color_coin(1, C3)#✔️
    cube.set_color_coin(2, C0)#✔️
    cube.set_color_coin(3, C2)#✔️

    #move edges
    A0 = cube.get_color_arete(0)
    A1 = cube.get_color_arete(1)
    A2 = cube.get_color_arete(2)
    A3 = cube.get_color_arete(3)

    cube.set_color_arete(0, A2)#✔️
    cube.set_color_arete(1, A0)#✔️
    cube.set_color_arete(2, A3)#✔️
    cube.set_color_arete(3, A1)#✔️

def Down(cube):
    print("\n🥐 fonction Down")
    
    #move corners
    C4 = cube.get_color_coin(4)
    C5 = cube.get_color_coin(5)
    C6 = cube.get_color_coin(6)
    C7 = cube.get_color_coin(7)

    cube.set_color_coin(4, C5[1] + C5[2] + C5[0]) #✔️
    cube.set_color_coin(5, C7[2] + C7[0] + C7[1]) #✔️
    cube.set_color_coin(6, C4[1] + C4[2] + C4[0]) #✔️
    cube.set_color_coin(7, C6[2] + C6[1] + C6[0]) #✔️

    #move edges
    A6 = cube.get_color_arete(6)
    A8 = cube.get_color_arete(8)
    A10 = cube.get_color_arete(10)
    A11 = cube.get_color_arete(11)

    cube.set_color_arete(6, A11)#✔️
    cube.set_color_arete(8, A6)#✔️
    cube.set_color_arete(10, A8)#✔️
    cube.set_color_arete(11, A10)#✔️

def DownPrime(cube):
    print("\n🥐 fonction DownPrime")

    #move corners
    C4 = cube.get_color_coin(4)
    C5 = cube.get_color_coin(5)
    C6 = cube.get_color_coin(6)
    C7 = cube.get_color_coin(7)

    cube.set_color_coin(4, C6[2] + C6[1] + C6[0])#✔️
    cube.set_color_coin(5, C4[2] + C4[0] + C4[1])#✔️
    cube.set_color_coin(6, C7[2] + C7[1] + C7[0])#✔️
    cube.set_color_coin(7, C5[1] + C5[2] + C5[0])#✔️

    #move edges
    A6 = cube.get_color_arete(6)#✔️
    A8 = cube.get_color_arete(8)#✔️
    A10 = cube.get_color_arete(10)
    A11 = cube.get_color_arete(11)#✔️

    cube.set_color_arete(6, A8)
    cube.set_color_arete(8, A10)
    cube.set_color_arete(10, A11)
    cube.set_color_arete(11, A6)

def Front(cube):
    print("\n🥐 fonction Front")
    
    #move corners
    C2 = cube.get_color_coin(2)
    C3 = cube.get_color_coin(3)
    C6 = cube.get_color_coin(6)
    C7 = cube.get_color_coin(7)

    cube.set_color_coin(2, C6[0] + C6[2] + C6[1])#✔️
    cube.set_color_coin(3, C2[2] + C2[0] + C2[1])#✔️
    cube.set_color_coin(6, C7[1] + C7[0] + C7[2])#✔️
    cube.set_color_coin(7, C3) #✔️
    #move edges
    A3 = cube.get_color_arete(3)
    A5 = cube.get_color_arete(5)
    A7 = cube.get_color_arete(7)
    A8 = cube.get_color_arete(8)

    cube.set_color_arete(3, A5)#✔️
    cube.set_color_arete(5, A8[1] + A8[0])#✔️
    cube.set_color_arete(7, A3[1] + A3[0])#✔️
    cube.set_color_arete(8, A7)#✔️

def FrontPrime(cube):
    print("\n🥐 fonction FrontPrime")

    #move corners
    C2 = cube.get_color_coin(2)
    C3 = cube.get_color_coin(3)
    C6 = cube.get_color_coin(6)
    C7 = cube.get_color_coin(7)

    cube.set_color_coin(2, C3[1] + C3[2] + C3[0])#✔️
    cube.set_color_coin(3, C7)#✔️
    cube.set_color_coin(6, C2[0] + C2[2] + C2[1])#✔️
    cube.set_color_coin(7, C6[1] + C6[0] + C6[2])#✔️

    #move edges
    A3 = cube.get_color_arete(3)
    A5 = cube.get_color_arete(5)
    A7 = cube.get_color_arete(7)
    A8 = cube.get_color_arete(8)

    cube.set_color_arete(3, A7[1] + A7[0])#✔️
    cube.set_color_arete(5, A3)#✔️
    cube.set_color_arete(7, A8)#✔️
    cube.set_color_arete(8, A5[1] + A5[0])#✔️

def Back(cube):
    print("\n🥐 fonction Back")
    
    #move corners
    C0 = cube.get_color_coin(0)
    C1 = cube.get_color_coin(1)
    C4 = cube.get_color_coin(4)
    C5 = cube.get_color_coin(5)
    cube.set_color_coin(0, C1[2] + C1[0] + C1[1])#✔️
    cube.set_color_coin(1, C5)#✔️
    cube.set_color_coin(4, C0)#✔️
    cube.set_color_coin(5, C4[1] + C4[2] + C4[0])#✔️
    #move edges
    A0 = cube.get_color_arete(0)
    A4 = cube.get_color_arete(4)
    A9 = cube.get_color_arete(9)
    A11 = cube.get_color_arete(11)

    cube.set_color_arete(0, A9)#✔️
    cube.set_color_arete(4, A0)#✔️
    cube.set_color_arete(9, A11[1] + A11[0])#✔️
    cube.set_color_arete(11, A4[1] + A4[0])#✔️

def BackPrime(cube):
    print("\n🥐 fonction BackPrime")

    #move corners
    C0 = cube.get_color_coin(0)
    C1 = cube.get_color_coin(1)
    C4 = cube.get_color_coin(4)
    C5 = cube.get_color_coin(5)

    cube.set_color_coin(0, C4)#✔️
    cube.set_color_coin(1, C0[1] + C0[2] + C0[0])#✔️
    cube.set_color_coin(4, C5[2] + C5[0] + C5[1])#✔️
    cube.set_color_coin(5, C1)#✔️
    #move edges
    A0 = cube.get_color_arete(0)
    A4 = cube.get_color_arete(4)
    A9 = cube.get_color_arete(9)
    A11 = cube.get_color_arete(11)

    cube.set_color_arete(0, A4)#✔️
    cube.set_color_arete(4, A11[1] + A11[0])#✔️
    cube.set_color_arete(9, A0)#✔️
    cube.set_color_arete(11, A9[1] + A9[0])#✔️
    

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
            

# def choice_rotation_arete(num_carré_arete: int, arete, nb_rotation):
#     if num_carré_arete == 2:
#         return D(arete, nb_rotation)
#     elif num_carré_arete == 4:
#         return L(arete, nb_rotation)
#     elif num_carré_arete == 6:
#         return R(arete, nb_rotation)
#     elif num_carré_arete == 8:
#         return F(arete, nb_rotation)
