from InitCube import cube, face1, face2, face3, face4, face5, face6
from Modelisation import algo_face1, algo_face2, algo_face3, algo_face4, algo_face5, algo_face6
#faire rentrer en input les couleurs



# cube.modelisation_cube()

# cube.print_info_cube()


#Face 1:
#   case 1 -> (N:Face 5 case 3, S: Face 1 case 4, O: Face 2 case 1, E: Face 1 Case 2)
#   case 2 -> (N:Face 5 case 2, S: Face 1 case 5, O: Face 1 case 1, E: Face 1 Case 3)
#   case 3 -> (N:Face 5 case 1, S: Face 1 case 6, O: Face 1 case 2, E: Face 4 Case 3)

#   case 4 -> (N:Face 1 case 1, S: Face 1 case 7, O: Face 2 case 2, E: Face 1 Case 5)
#   case 5 -> (N:Face 1 case 2, S: Face 1 case 8, O: Face 1 case 4, E: Face 1 Case 6)
#   case 6 -> (N:Face 1 case 3, S: Face 1 case 9, O: Face 1 case 5, E: Face 4 Case 2)

#   case 7 -> (N:Face 1 case 4, S: Face 3 case 1, O: Face 2 case 3, E: Face 1 Case 8)
#   case 8 -> (N:Face 1 case 5, S: Face 3 case 2, O: Face 1 case 7, E: Face 1 Case 9)
#   case 9 -> (N:Face 1 case 6, S: Face 3 case 3, O: Face 1 case 8, E: Face 4 Case 1)

#Face 2:
#   case 1 -> (N:Face 1 case 1, S: Face 2 case 4, O: Face 5 case 3, E: Face 2 Case 2)
#   case 2 -> (N:Face 1 case 4, S: Face 2 case 5, O: Face 2 case 1, E: Face 2 Case 3)
#   case 3 -> (N:Face 1 case 7, S: Face 2 case 6, O: Face 2 case 2, E: Face 3 Case 1)

#   case 4 -> (N:Face 2 case 1, S: Face 2 case 7, O: Face 5 case 6, E: Face 2 Case 5)
#   case 5 -> (N:Face 2 case 2, S: Face 2 case 8, O: Face 1 case 4, E: Face 2 Case 6)
#   case 6 -> (N:Face 2 case 3, S: Face 2 case 9, O: Face 1 case 5, E: Face 3 Case 4)

#   case 7 -> (N:Face 2 case 4, S: Face 6 case 7, O: Face 5 case 9, E: Face 2 Case 8)
#   case 8 -> (N:Face 2 case 5, S: Face 6 case 4, O: Face 2 case 7, E: Face 2 Case 9)
#   case 9 -> (N:Face 2 case 6, S: Face 6 case 1, O: Face 2 case 8, E: Face 3 Case 7)
#



algo_remplissage = [algo_face1(), algo_face2(), algo_face3(), algo_face4(),algo_face5(), algo_face6()]

def modelisation_cube():
    # faces = cube.get_faces()

    for face in range(0, 6): # ordre par face
        algo_remplissage[face]

        # for i in range(0, 9):
        #     print(face[i].get_couleur())
        
            # algo_face1(c)
            # c.print_info_carré()

print("--- MODELISATION ----")
modelisation_cube()
cube.print_info_cube()

#MODELISATION CUBE
#Case 1 son Nord
# Face 1: Face 5 case 3
# Face 2: Face 1 case 1
# Face 3: Face 1 case 7
# Face 4: Face 1 case 9
# Face 5: Face 1 case 3
# Face 6: Face 3 case 7

#Case 1 son Sud
# Face 1: Face 1 case 4
# Face 2: Face 1 case 1
# Face 3: Face 1 case 7
# Face 4: Face 1 case 9
# Face 5: Face 1 case 3
# Face 6: Face 3 (sud) case 7


# one_carré = cube.get_one_carré_by_numéro(44)
# whatis = cube.get_one_carré_from_face_and_case(1, 9)
# print(whatis.couleur)
    
    
    

    