# Rubiks

## Rotations en speedcubing:

Right -> R, RightPrime -> R', Right x 2 -> R2,
Left -> L, LeftPrime -> L', Left x 2 -> L2,
Front -> F, FrontPrime -> F', Front x 2 -> F2,
Back -> B, BackPrime -> B', Back x 2 -> B2,
Down -> D, DownPrime -> D', Down x 2 -> D2,
Up -> U, upPrime -> U', Up x 2 -> U2,


## Modelisation

         R
      B  W  G  Y
         O


                                            coins[4][2] aretes[11][0] coins[5][1]
                                            aretes[4][1] milieux[4] aretes[9][1]
                                            coins[0][2] aretes[0][1] coins[1][1]

coins[4][0] aretes[4][0] coins[0][1]         coins[0][0] aretes[0][0] coins[1][0]        coins[1][2] aretes[9][0] coins[5][0]       coins[5][2] aretes[11][1] coins[4][1]
aretes[6][0] milieux[1] aretes[1][1]         aretes[1][0] milieux[0] aretes[2][0]        aretes[2][1] milieux[3] aretes[10][0]      aretes[10][1] milieux[5] aretes[6][1] 
coins[6][0] aretes[5][0] coins[2][2]         coins[2][0] aretes[3][0] coins[3][0]        coins[3][1] aretes[7][1] coins[7][0]       coins[7][1] aretes[8][1] coins[6][1] 

                                              coins[2][1] aretes[3][1] coins[3][2]
                                              aretes[5][1] milieux[2] aretes[7][0] 
                                              coins[6][2] aretes[8][0] coins[7][2]

        
## Application

#Création d'une classe Node:
  - l'objet peut-être une arete, un coin ou un milieu
  - chaque noeud est un pointeur définit par sa valeur et ses orientations, seule sera couleur sera changeable
  - les couleurs sont attribuées de manières alétoires en respectant les principes du rubik's cube: les centres sont inchangeables donc fixes, bien intégrer la couleur des coins selon son model
  - Chaque node ne peut avoir que 4 orientations, ex: l'aretes 0 (A0) : A0.setter(u=A1, uprime=A2, b=A9, bprime=A4), cela permet de creér une liste chaînée qui sera la clef de la manipulation du cube, et du moyen de recherche utilisée

#Création d'une classe Cube:
  - contient: tous les objets issu de la classe Node
  - méthodes propres au cube: print_cube, solutions, noeuds verouillés 


## Méthodologie:

**CFOP Speedsolving Method: Cross, First 2 Layers, Orientation, Permutation**


#1ère étape: résoudre la croix blanche
  je veux regarder quelle arete résoudre en premier
  #pour un noeud
      #pour se faire, je vais faire du backtracking pour récolter l'ensemble des chemins possibles pour avoir un W
          #  --> ne pas piocher dans les nodes
  
  
      #une fois la récolte faire, je vais sélectionner le chemin le plus court
  
  #je vais regarder parmis le chemin associé à un noeud lequel est le plus court de tous les noeuds à résoudre
  
  #j'exécute l'action la plus courte
      #je cherche si les nodes bloqué ont changé de place
  
  
  
  
  
      #je retire des noeuds à chercher list_node.pop(node)
      #je l'ajoute au noeud bloquer.
  
  #j'éxecute ces actions tant que les 4 aretes n'ont pas de W


