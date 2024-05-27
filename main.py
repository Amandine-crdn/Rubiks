from CubeClass import Cube
from Algorithmes import search_aretes, Right#search_aretes, choice_rotation_arete

print("--- INIT ----")
cube = Cube()
cube.print_cube()


def check_position_color(num_aretes, find_color):
    color = cube.get_color_arete(num_aretes)
    if num_aretes == 9:
        if color[0] == find_color:
            Right(cube)
        else:
            print("B'")

    elif num_aretes == 7:
        if color[0] == find_color:
            Right(cube)
        else:
            print("F'")
    elif num_aretes == 10:
        if color[0] == find_color:
            print("D")
            Right(cube)
        else:
            print("R2")
    elif num_aretes == 2:
        if color[1] == find_color:
            Right(cube)
            print("F'")
        else:
            #au suivant
            pass

white_aretes = search_aretes(cube, 'W')
print(white_aretes)



#remplir ue arete a gauche, une arete a droite, une arete en haut et une arete en bas*
#resoudre une par une les aretes

#placer une a droite:
#check si a droite il y a déjà la présence d'une arete


if 2 in white_aretes: #pour aretes A2
    print("A2 bien placer")
    color = cube.get_color_arete(2)
    print(color[0], color[1])
else:
    check_right = cube.get_right_aretes() #sinon on cherche a en placer une a droite
    color = cube.get_color_arete(2)
    print(color[0], color[1])

if 1 in white_aretes:
    print("A1 bien placer")
else:
    check_left = cube.get_left_aretes() #sinon on cherche a en placer une a droite

#si pas d'arete chercher l'arete
#une fois trouver la placer là et la protéger

#placer une a gauche:
check_right = cube.get_right_aretes() 
for k, v in white_aretes.items():
    if k in check_right and k != 2: #pour face 1 right s'execute si k in []
        print("is on  the right", k, v)
        check_position_color(k, 'W')
    elif k in check_right and k == 2:
        pass
        # passer au coté gauche


# # cube.set_color(face=1, num=2, color='R')
# cube.get_color(face=1, num=2)
# #fonction mouvement R
# C4 = cube.get_color(face=1, num=9)
# A3 = cube.get_color(face=1, num=6)

# C2 = cube.get_color(face=1, num=3)
# C2 = cube.get_color(face=1, num=3)
# C2 = cube.get_color(face=1, num=3)




print("\n--- MODELISATION -----\n")
# modelisation_cube_test()

# modelisation_cube()
# print("\n--- RESOLUTION -----\n")
# print("etape 1: make a cross on the face 1")
# print_face("before: ", face1)


#chercher les aretes blanches 
# aretes = search_aretes('W')
# for a in aretes: #déplacer chaque arete sur la zone attendu face 1 case 2, 4, 6, 8
#     if a.get_numéro_face() == 1:
#         if choice_rotation_arete(a.get_numéro_carré(), a, 2):
#             print("a")





#sur la face  on va prendre les aretes puis faire remonter selon les centre
# print_face("after: ", face1)

# import timeit

# def test(n):
#     return sum(range(n))

# n = 10000
# loop = 1000

# result = timeit.timeit('test(n)', globals=globals(), number=loop) #8.55095e-05
# print(result / loop)
#0.00000855095 avant
#0.00017640929999999998 apres retrait define place new colors
#0.0001437597 apres retrait tri coins aretes
#0.00006746519999999999
#0.0000830519 retrait modelisation explicite