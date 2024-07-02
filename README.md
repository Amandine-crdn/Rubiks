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


                                                      coins[4][1] aretes[11][0] coins[5][2]
                                                      aretes[4][1] milieux[4] aretes[9][1]
                                                      coins[0][2] aretes[0][1] coins[1][1]

         coins[4][2] aretes[4][0] coins[0][1]         coins[0][0] aretes[0][0] coins[1][0]        coins[1][2] aretes[9][0] coins[5][1]       coins[5][0] aretes[11][1] coins[4][0]
         aretes[6][0] milieux[1] aretes[1][1]         aretes[1][0] milieux[0] aretes[2][0]        aretes[2][1] milieux[3] aretes[10][0]      aretes[10][1] milieux[5] aretes[6][1] 
         coins[6][1] aretes[5][0] coins[2][2]         coins[2][0] aretes[3][0] coins[3][0]        coins[3][1] aretes[7][1] coins[7][2]       coins[7][0] aretes[8][1] coins[6][0] 

                                                      coins[2][1] aretes[3][1] coins[3][2]
                                                      aretes[5][1] milieux[2] aretes[7][0] 
                                                      coins[6][2] aretes[8][0] coins[7][1]


Je fais correspondre un int à chaque rotation pour les besoins de mon algorithme:
0: Right, 1: RightPrime, 2: Left, 3: LeftPrime, 4: Front, 5: FrontPrime, 6: Back, 7: BackPrime, 8: Up, 9: UpPrime, 10: Down, 11: DownPrime

## Application

**Création d'une classe Node:**
  - l'objet peut-être une arete, un coin ou un milieu
  - chaque noeud est un pointeur définit par sa valeur et ses orientations, seule sera couleur sera changeable
  - les couleurs sont attribuées de manières alétoires en respectant les principes du rubik's cube: les centres sont inchangeables donc fixes, bien intégrer la couleur des coins selon son model
  - Chaque node ne peut avoir que 4 orientations, ex: l'aretes 0 (A0) :

             A0.setter(u=A1, uprime=A2, b=A9, bprime=A4)
    
    Cela permet de creér une liste chaînée qui sera la clef de la manipulation du cube, et du moyen de recherche utilisée

**Création d'une classe Cube:**
  - contient: tous les objets issu de la classe Node
  - méthodes propres au cube: print_cube, solutions, noeuds verouillés 


## Méthodologie:

***CFOP Speedsolving Method: Cross, First 2 Layers, Orientation, Permutation***

##1ère étape: résoudre la croix blanche
## Outils
- path: variable de type list qui va ajouter petit à petit les mouvements de rotations à effectuer pour aller jusqu'au noeud souhaité. Ex : path = [1, 2, 8, 5]
- dico_path: variable de type dictionnaire qui va ajouter les différents path possibles par noeud
- nodes_blocked: variable de type list et de taille max 4 qui va ajouter les nodes bien placer et les nodes ajoutés par la suite à protéger de autres mouvements de résolutions d'autres nodes 
## Backtracking
- va sélectionner tous les chemins possibles pour apporter le node souhaité à l'endroit désiré
- condition d'arrêt: longueur du chemin
- conditino d'ajout du chemin: la couleur (2 couleurs pour une arete) a été trouvé
- sinon continuer la recherche
## Actions
- si un noeud est déjà bien placé, l'insérer dans la liste locked_edges
- je veux regarder quel noeud résoudre en premier: je selectionne le chemin le plus court par noeud, et sélectionner le chemin le plus courts parmis les 4 noeuds à résoudre
- avant d'éxécuter les actions, je dois m'assurer pour chaque rotations que les noeuds bloqués ne sont pas déplacé, je créer donc une fonction spéciale qui va anticiper les actions et protéger les noeuds
- je peux enfin ajouter le noeud à la liste des noeuds bloqués car le programme s'est exécuté avec succès
## Nb de coups
*optimisation pour le cas où la fin d'une rotation d'un chemin précédent + le début d'un chemin suivant sont:*
- si deux rotations sont égales la transformer en une, ex: [0, 0], correspondant à Right Right, et donc cela devient R2 dans la solution, je gagne 1 coup.
- si deux rotations sont opposées (la fin d'une rotation d'un chemin précédent + le début d'un cehmin suivant à faire), j'annule les coups, je gagne 2 coups.
- si trois rotations égales: faire la rotation inverse, ex : r r r -> r' 





















