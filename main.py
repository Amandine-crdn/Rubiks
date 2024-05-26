from InitCube import init_cub_test#, print_info_cube, print_face, cube#, faces, face1, face2, face3, face4, face5, face6
from Modelisation import creation_faces#modelisation_cube_test#modelisation_cube, algo_face1, algo_face2, algo_face3, algo_face4, algo_face5, algo_face6
from Algorithmes import Right#search_aretes, choice_rotation_arete

# cube.print_cube()

# print_info_cube()
print("--- INIT ----")
cube = init_cub_test(creation_faces())
movements = ""
movements += Right(cube)
print(movements)


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
#6.746519999999999e-05