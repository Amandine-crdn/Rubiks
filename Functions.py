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

        
def turn_edge_left():
    L2()
    Down()
    Front()
    LeftPrime()
    FrontPrime()

def turn_edge_right():
    R2()
    DownPrime()
    FrontPrime()
    Right()
    Front()

def turn_edge_up():
    F2()
    Down()
    Right()
    FrontPrime()
    RightPrime()

def turn_edge_back():
    B2()
    DownPrime()
    RightPrime()
    Back()
    Right()