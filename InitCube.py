couleurs = ["Blanc"]*9 + ["Bleu"]*9 + ["Orange"]*9+ ["Vert"]*9 + ["Rouge"]*9  + ["Jaune"]*9   

####################### CARRE

class Carré():
    def __init__(self, couleur: str, numéro_face, numéro_carré, id) -> None: #x: int , y: int, 
        self.couleur = couleur
        self.numéro_face = numéro_face
        self.numéro_carré = numéro_carré
        self.id = id

    #getters
    def get_nord(self):
        return self.nord
    
    def get_sud(self):
        return self.sud
    
    def get_ouest(self):
        return self.ouest

    def get_est(self):
        return self.est

    def get_numéro_face(self):
        return self.numéro_face
    
    def get_numéro_carré(self):
        return self.numéro_carré
    
    def get_couleur(self):
        return self.couleur
    
    #setters
    
    def set_nord(self, params : tuple):
        face = params[0]
        case = params[1]
        self.nord = cube._get_by_params(face, case)
    def set_sud(self, params : tuple):
        face = params[0]
        case = params[1]
        self.sud = cube._get_by_params(face, case)

    def set_ouest(self, params : tuple):
        face = params[0]
        case = params[1]
        self.ouest = cube._get_by_params(face, case)
    
    def set_est(self, params : tuple):
        face = params[0]
        case = params[1]
        self.est = cube._get_by_params(face, case)
        
    def set_compass(self, nord: tuple, sud: tuple, ouest: tuple, est: tuple):
        self.set_nord(nord),
        self.set_sud(sud),
        self.set_ouest(ouest),
        self.set_est(est),
    
    
    def print_info_carré(self):
        return print(f"{self.get_around()}\nnuméro carré: {self.get_numéro_carré()}, numéro face: {self.get_numéro_face()}, couleur: {self.get_couleur()}")
    
    def get_around(self):
        dico_coordonnées = {
            'N': self.get_nord().couleur,
            'S': self.get_sud().couleur,
            'O': self.get_ouest().couleur,
            'E': self.get_est().couleur
        }
        return dico_coordonnées
  
def init_cub(couleurs):
    cube = []
    id = 0
    for numéro_face in range(1, 7):
        for numéro_carré in range(1, 10):
            cube.append(Carré(couleurs[id], numéro_face, numéro_carré, id + 1))
            id +=1
    return cube



####################### CUBE
class Cube():
    def __init__(self, cube) -> None:
        self.cube = cube
    
    def _get_all_carrés(self):
        return self.cube
    
    def _get_by_params(self, face, numéro_carré):
        list_carré = self._get_all_carrés()
        for carré in list_carré:
            if carré.numéro_carré == numéro_carré and carré.numéro_face == face:
                return carré
        return None
    
    def get_faces(self):
        all_carrés = self._get_all_carrés()
        list_faces = [
            all_carrés[0:9],
            all_carrés[9:18],
            all_carrés[18:27],
            all_carrés[27:36],
            all_carrés[36:45],
            all_carrés[45:54]
        ]
        return list_faces

    def get_by_id(self, id):
        list_carré = self._get_all_carrés()
        for carré in list_carré:
            if carré.id == id:
                return carré
        return None
     
    def print_info_cube(self):
        faces = cube.get_faces()
        for index, face in enumerate(faces, start=1): # ordre par face
            print("\n🌸 Face ", index)
            for i in range(0, 9):
                print(f"case n°{face[i].get_numéro_carré()} -> {face[i].get_couleur()} {face[i].get_around()}")

print("--- INIT ----")
cube = Cube(init_cub(couleurs))
face1 = cube.get_faces()[0]
face2 = cube.get_faces()[1]
face3 = cube.get_faces()[2]
face4 = cube.get_faces()[3]
face5 = cube.get_faces()[4]
face6 = cube.get_faces()[5]