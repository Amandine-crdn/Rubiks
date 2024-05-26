from SortColors import  milieux, aretes, coins #new_colors
# from Modelisation import creation_faces
####################### CARRE

# class Carré():
#     def __init__(self, couleur: str, numéro_face, numéro_carré, id) -> None:
#         self.couleur = couleur
#         self.numéro_face = numéro_face
#         self.numéro_carré = numéro_carré
#         self.id = id

#     #getters
#     def get_nord(self):
#         return self.nord
    
#     def get_sud(self):
#         return self.sud
    
#     def get_ouest(self):
#         return self.ouest

#     def get_est(self):
#         return self.est

#     def get_numéro_face(self):
#         return self.numéro_face
    
#     def get_numéro_carré(self):
#         return self.numéro_carré
    
#     def get_color(self):
#         return self.couleur
    
#     def get_around(self):
#         dico_coordonnées = {
#             'N': self.get_nord().couleur,
#             'S': self.get_sud().couleur,
#             'O': self.get_ouest().couleur,
#             'E': self.get_est().couleur
#         }
#         return dico_coordonnées
    
#     #setters
    
#     def set_nord(self, params : tuple):
#         face = params[0]
#         case = params[1]
#         self.nord = cube._get_by_params(face, case)
#     def set_sud(self, params : tuple):
#         face = params[0]
#         case = params[1]
#         self.sud = cube._get_by_params(face, case)

#     def set_ouest(self, params : tuple):
#         face = params[0]
#         case = params[1]
#         self.ouest = cube._get_by_params(face, case)
    
#     def set_est(self, params : tuple):
#         face = params[0]
#         case = params[1]
#         self.est = cube._get_by_params(face, case)
        
#     def set_compass(self, nord: tuple, sud: tuple, ouest: tuple, est: tuple):
#         self.set_nord(nord),
#         self.set_sud(sud),
#         self.set_ouest(ouest),
#         self.set_est(est),
    
    
#     def print_info_carré(self):
#         return print(f"{self.get_around()}\nnuméro carré: {self.get_numéro_carré()}, numéro face: {self.get_numéro_face()}, couleur: {self.get_color()}")
    
  

# def print_info_cube():
#     faces = cube.get_faces()
#     for index, face in enumerate(faces, start=1): # ordre par face
#         print("\n🌸 Face ", index)
#         for i in range(0, 9):
#             print(f"case n°{face[i].get_numéro_carré()} -> {face[i].get_color()} {face[i].get_around()}")

# def print_face(word, face):
#     i = 0
#     space = " " * len(word) 
#     return print(f""" 
# {word}  {face[i].get_color()} {face[i+1].get_color()} {face[i+2].get_color()}
# {space}  {face[i+3].get_color()} {face[i+4].get_color()} {face[i+5].get_color()}
# {space}  {face[i+6].get_color()} {face[i+7].get_color()} {face[i+8].get_color()}
# """)


# ####################### CUBE
# class Cube():
#     def __init__(self, cube) -> None:
#         self.cube = cube
    
#     def _get_all_carrés(self):
#         return self.cube
    
#     def _get_by_params(self, face, numéro_carré):
#         list_carré = self._get_all_carrés()
#         for carré in list_carré:
#             if carré.numéro_carré == numéro_carré and carré.numéro_face == face:
#                 return carré
#         return None
    
#     def get_faces(self):
#         all_carrés = self._get_all_carrés()
#         list_faces = [
#             all_carrés[0:9],
#             all_carrés[9:18],
#             all_carrés[18:27],
#             all_carrés[27:36],
#             all_carrés[36:45],
#             all_carrés[45:54]
#         ]
#         return list_faces

#     def get_by_id(self, id):
#         list_carré = self._get_all_carrés()
#         for carré in list_carré:
#             if carré.id == id:
#                 return carré
#         return None
     

    
#     def print_cube(self):
#         faces = self.get_faces()
#         print(f"""                                                                                              
#           {faces[4][8].get_color()} {faces[4][7].get_color()} {faces[4][6].get_color()}                   5
#           {faces[4][5].get_color()} {faces[4][4].get_color()} {faces[4][3].get_color()}                2  1  4  6
#           {faces[4][2].get_color()} {faces[4][1].get_color()} {faces[4][0].get_color()}                   3

# {faces[1][6].get_color()} {faces[1][3].get_color()} {faces[1][0].get_color()}     {faces[0][0].get_color()} {faces[0][1].get_color()} {faces[0][2].get_color()}     {faces[3][2].get_color()} {faces[3][5].get_color()} {faces[3][8].get_color()}     {faces[5][6].get_color()} {faces[5][7].get_color()} {faces[5][8].get_color()}
# {faces[1][7].get_color()} {faces[1][4].get_color()} {faces[1][1].get_color()}     {faces[0][3].get_color()} {faces[0][4].get_color()} {faces[0][5].get_color()}     {faces[3][1].get_color()} {faces[3][4].get_color()} {faces[3][7].get_color()}     {faces[5][3].get_color()} {faces[5][4].get_color()} {faces[5][5].get_color()}
# {faces[1][8].get_color()} {faces[1][5].get_color()} {faces[1][2].get_color()}     {faces[0][6].get_color()} {faces[0][7].get_color()} {faces[0][8].get_color()}     {faces[3][0].get_color()} {faces[3][3].get_color()} {faces[3][6].get_color()}     {faces[5][0].get_color()} {faces[5][1].get_color()} {faces[5][2].get_color()}

#           {faces[2][0].get_color()} {faces[2][1].get_color()} {faces[2][2].get_color()}
#           {faces[2][3].get_color()} {faces[2][4].get_color()} {faces[2][5].get_color()}
#           {faces[2][6].get_color()} {faces[2][7].get_color()} {faces[2][8].get_color()}

# """)
             
# def init_cub(couleurs):
#     # print(couleurs)
#     cube = []
#     id = 0
#     for numéro_face in range(1, 7):
#         for numéro_carré in range(1, 10):
#             cube.append(Carré(couleurs[id], numéro_face, numéro_carré, id + 1))
#             id +=1
#     return cube 


####################### CUBE TEST


class CubeTest():
    def __init__(self, faces) -> None:
        self.faces = faces
        self.coins = coins
        self.aretes = aretes
        self.milieux = milieux
        self.right_aretes = [2, 7, 9, 10]
        self.right_coins = [1, 3, 5, 7]
        # coins_list = C1, C2, C3, C4, C5, C6, C7, C8
        # aretes_list = A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12
        # milieu_list = M1, M2, M3, M4, M5
    
    
    # def get_color(self, face, num):
    #     print(f"Face {face} Num {num} :",self.faces[((face-1)*9 + num)-1])
    #     return self.faces[((face-1)*9 + num)-1]
    # def set_color(self, face, num, color):
    #     self.faces[((face-1)*9 + num)-1] = color

    def get_coins(self):
        return self.coins
    
    def get_right_coins(self):
        return self.right_coins
    
    def get_right_aretes(self):
        return self.right_aretes
    
    def get_color_coin(self, num_coin):
        print(self.coins[num_coin])
        return self.coins[num_coin]
    
    def set_color_coin(self, num_coin, color):
        self.coins[num_coin] = color

    def get_aretes(self):
        return self.aretes
    
    def get_color_arete(self, num_arete):
        print(self.aretes[num_arete])
        return self.aretes[num_arete]
    
    def set_color_arete(self, num_arete, color):
        self.aretes[num_arete] = color
    

    def print_cube(self): # a verifier
        print(f"""


        {self.coins[4][1]} {self.aretes[3][1]} {self.coins[3][2]}
        {self.aretes[5][1]} {self.milieux[2]} {self.aretes[7][0]} 
        {self.coins[6][1]} {self.aretes[8][0]} {self.coins[7][0]}

{self.coins[4][0]} {self.aretes[4][0]} {self.coins[0][1]}   {self.coins[0][0]} {self.aretes[0][0]} {self.coins[1][0]}   {self.coins[1][2]} {self.aretes[9][0]} {self.coins[5][0]}   {self.coins[1][1]} {self.aretes[0][1]} {self.coins[0][2]}
{self.aretes[6][0]} {self.milieux[1]} {self.aretes[1][1]}   {self.aretes[1][0]} {self.milieux[0]} {self.aretes[2][0]}   {self.aretes[2][1]} {self.milieux[3]} {self.aretes[10][0]}   {self.aretes[9][1]} {self.milieux[4]} {self.aretes[4][1]} 
{self.coins[6][0]} {self.aretes[5][0]} {self.coins[2][2]}   {self.coins[2][0]} {self.aretes[3][0]} {self.coins[3][0]}   {self.coins[3][1]} {self.aretes[7][1]} {self.coins[7][1]}   {self.coins[5][1]} {self.aretes[11][0]} {self.coins[7][1]} 

        {self.coins[4][1]} {self.aretes[3][1]} {self.coins[3][2]}
        {self.aretes[5][1]} {self.milieux[2]} {self.aretes[7][0]} 
        {self.coins[6][1]} {self.aretes[8][0]} {self.coins[7][0]}
""")
        pass

    # def get_aretes(self):
    #     return self.aretes
    # def get_milieux(self):
    #     return self.milieux

def init_cub_test(faces):
    return CubeTest(faces)
    

# color = cube.get_color(1, 1)
# print(color)

# cube = Cube(init_cub(new_colors))
# cube.print_cube()

# face1 = cube.get_faces()[0]
# face2 = cube.get_faces()[1]
# face3 = cube.get_faces()[2]
# face4 = cube.get_faces()[3]
# face5 = cube.get_faces()[4]
# face6 = cube.get_faces()[5]
# faces = face1, face2,face3, face4, face5, face6