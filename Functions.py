from Rotations import Rien, Right, RightPrime, Left, LeftPrime, Up, UpPrime, Back, BackPrime, Down, DownPrime, Front, FrontPrime, R2, L2, B2, D2, U2, F2

def action(choice: int):
    if choice is None:
        return Rien

    functions = [
        Right, RightPrime,
        Left,  LeftPrime, 
        Front, FrontPrime,
        Back,  BackPrime, 
        Up, UpPrime, 
        Down, DownPrime
    ]
  
    return functions[choice]

