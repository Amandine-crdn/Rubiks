from Rotations import Rien, Right, RightPrime, Left, LeftPrime, Up, UpPrime, Back, BackPrime, Down, DownPrime, Front, FrontPrime, R2, L2, B2, D2, U2, F2

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

