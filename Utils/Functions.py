from Utils.Rotations import Rien, Right, RightPrime, Left, LeftPrime, Up, UpPrime, Back, BackPrime, Down, DownPrime, Front, FrontPrime, R2, L2, B2, D2, U2, F2

def action(choice: int):
    if choice is None:
        return Rien
    #mapper les indices en fonctions des rotations
    functions = [
        Right, RightPrime, #0 1
        Left,  LeftPrime, # 2 3
        Front, FrontPrime, # 4 5
        Back,  BackPrime, # 6 7
        Up, UpPrime, # 8 9
        Down, DownPrime #10 11
    ]
  
    return functions[choice]



# 📽️ corriger "R'2" => R2



def optimize_moves(moves):
    i = 0
    moved = False
    new_str = []
    while i < len(moves): 
        if i < len(moves) - 3 and (moves[i] == moves[i + 1] == moves[i + 2] == moves[i + 3]):
            i+=4 #"l l l l"   ou  "l' l' l' l' " annule 4
            moved = True
        elif i < len(moves) - 2 and len(moves[i]) == 1 and (moves[i] == moves[i + 1] == moves[i + 2]):
            new_str.append(f"{moves[i]}'")
            i+=3 #"l l l " => l'
            moved = True

        elif i < len(moves) - 2 and len(moves[i]) == 2 and (moves[i] == moves[i + 1] == moves[i + 2]):
            new_str.append(moves[i][0])
            i+=3 # ou  "l' l' l' " => l
            moved = True
        
        elif i < len(moves) - 1 and len(moves[i]) > 2 and moves[i] == moves[i + 1]: #pour eviter B'2
            new_str.append(f"{moves[i][0]}2")
            print("here")
            i+=2 # si 2 egaux dire 2
            moved = True
            
        elif i < len(moves) - 1 and moves[i] == moves[i + 1]:
            new_str.append(f"{moves[i]}2")
            i+=2 # si 2 egaux dire 2
            moved = True


        elif i < len(moves) - 1 and (moves[i] == f"{moves[i + 1]}'" or f"{moves[i]}'" == moves[i+1]): 
            i+=2 #pour les l' l et l l' annule 2 opposé
            moved = True

        elif i < len(moves) - 1 and (moves[i][0] == moves[i + 1][0] and  '2' in moves[i] and '2' in moves[i + 1]):
            i+=2 #annule 2 D
            moved = True
            
        elif i < len(moves) - 1 and  moves[i + 1][0] == moves[i][0] and (\
        ('2' in moves[i] and len(moves[i + 1]) == 1) or\
        ('2' in moves[i + 1] and len(moves[i]) == 1 )):
            new_str.append(f"{moves[i][0]}'")
            i+=2 #si D2 et d => d'   ou d D2 => d'   
            moved = True
                             
        elif i < len(moves) - 1 and  moves[i + 1][0] == moves[i][0] and (\
        ('2' in moves[i] and len(moves[i + 1]) == 2 and moves[i + 1][1] == "'") or\
        ('2' in moves[i + 1] and len(moves[i]) == 2 and moves[i][1] == "'")):
            new_str.append(f"{moves[i][0]}")
            i+=2  #si D2 et d' => d ou d'D2 => d
            moved = True
        

        else:
            new_str.append(moves[i])
            i+=1
        #annuler les l l' l2 l2 l' l   
    return new_str, moved
    