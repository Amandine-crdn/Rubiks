from CubeClass import cube
from NodeClass import A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11
from Rotations import Rien, Right, RightPrime, Left, LeftPrime, Up, UpPrime, Back, BackPrime, Down, DownPrime, Front, FrontPrime, R2, L2, B2, D2, U2, F2

print("--- INIT ----")
locked_edge = cube.blocked_edges
# cube.print_cube()

def action(choice: int):
    if choice is None:
        return Rien
    functions = [
        Right, Front, Left, Up, Down, Back, RightPrime, FrontPrime, LeftPrime, DownPrime,  UpPrime, BackPrime, R2, F2, L2, U2, D2, B2
    ]
    return functions[choice]
cube.print_cube()

choice = A10.find_path('W',locked_edge)
action(choice)()
cube.append(A10)

choice2 = A6.find_path('W', locked_edge)
action(choice2)()
cube.append(A6)

choice3 = A8.find_path('W', locked_edge)
action(choice3)()
cube.append(A8)

choice4 = A11.find_path('W', locked_edge)
action(choice4)()
cube.append(A11)

cube.print_cube()

