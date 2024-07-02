from CubeClass import cube
from NodeClass import A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, C0, C1, C2, C3, C4, C5, C6, C7

def reset():
    cube.solution = "" #remettre à null
    aretes = ["WR", "WB", "WG", "WO", "BR", "BO", "BY", "OG", "OY", "GR", "GY","RY"] #remettre le cube initial
    coins = ["WBR", "WRG", "WOB","WGO" , "YRB", "YGR", "YBO", "YOG"]
    C0.set_color(coins[0])
    C1.set_color(coins[1])
    C2.set_color(coins[2])
    C3.set_color(coins[3])
    C4.set_color(coins[4])
    C5.set_color(coins[5])
    C6.set_color(coins[6])
    C7.set_color(coins[7])
    A0.set_color(aretes[0])
    A1.set_color(aretes[1])
    A2.set_color(aretes[2])
    A3.set_color(aretes[3])
    A4.set_color(aretes[4])
    A5.set_color(aretes[5])
    A6.set_color(aretes[6])
    A7.set_color(aretes[7])
    A8.set_color(aretes[8])
    A9.set_color(aretes[9])
    A10.set_color(aretes[10])
    A11.set_color(aretes[11])
    
cmd_map = {
    "R": [0],
    "R'": [1],
    "R2": [0, 0],
    "L": [2],
    "L'": [3],
    "L2": [2, 2],
    "F": [4],
    "F'": [5],
    "F2": [4, 4],
    "B": [6],
    "B'": [7],
    "B2": [6, 6],
    "U": [8],
    "U'": [9],
    "U2": [8, 8],
    "D": [10],
    "D'": [11],
    "D2": [10, 10]
}

def action_start(choice: int):
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

def Right():
    # print("🥐Right")
    
    #move corners
    c1 = C1.get_color()
    c3 = C3.get_color()
    c5 = C5.get_color()
    c7 = C7.get_color()

    C1.set_color(c3[2] + c3[0] + c3[1])
    C3.set_color(c7[1] + c7[2] + c7[0])
    C5.set_color(c1[1] + c1[2] + c1[0])
    C7.set_color(c5[2] + c5[0] + c5[1])


    #move edges
    a2 = A2.get_color()[1] + A2.get_color()[0]
    a10 = A10.get_color()[1] + A10.get_color()[0]
    a7 = A7.get_color()
    a9 = A9.get_color()

    A9.set_color(a2)
    A2.set_color(a7)
    A7.set_color(a10)
    A10.set_color(a9)

def RightPrime():
    # print("🥐RightPrime")

    #move corners
    c1 = C1.get_color()
    c3 = C3.get_color()
    c5 = C5.get_color()
    c7 = C7.get_color()

    C1.set_color(c5[2] + c5[0] + c5[1])
    C3.set_color(c1[1] + c1[2] + c1[0])
    C5.set_color(c7[1] + c7[2] + c7[0])
    C7.set_color(c3[2] + c3[0] + c3[1])

    #move edges
    a2 = A2.get_color()
    a10 = A10.get_color()
    a7 = A7.get_color()[1] + A7.get_color()[0]
    a9 =  A9.get_color()[1] + A9.get_color()[0]

    A2.set_color(a9) 
    A7.set_color(a2) 
    A9.set_color(a10) 
    A10.set_color(a7) 

def Left():
    # print("🥐Left")
    
    #move corners
    c0 = C0.get_color()
    c2 = C2.get_color()
    c4 = C4.get_color()
    c6 = C6.get_color()

    C0.set_color(c4[1] + c4[2] + c4[0])
    C2.set_color(c0[2] + c0[0] + c0[1]) 
    C4.set_color(c6[2] + c6[0] + c6[1]) 
    C6.set_color(c2[1] + c2[2] + c2[0]) 

    #move edges
    a1 = A1.get_color()[1] + A1.get_color()[0]
    a4 = A4.get_color()[1] + A4.get_color()[0]
    a6 = A6.get_color()
    a5 = A5.get_color()

    A5.set_color(a1) 
    A1.set_color(a4)
    A4.set_color(a6)
    A6.set_color(a5)
def LeftPrime():
    # print("🥐LeftPrime")

    #move corners
    c0 = C0.get_color()
    c2 = C2.get_color()
    c4 = C4.get_color()
    c6 = C6.get_color()

    C0.set_color(c2[1] + c2[2] + c2[0])
    C2.set_color(c6[2] + c6[0] + c6[1]) 
    C4.set_color(c0[2] + c0[0] + c0[1]) 
    C6.set_color(c4[1] + c4[2] + c4[0])

    #move edges
    a1 = A1.get_color()[1] + A1.get_color()[0]
    a4 = A4.get_color()
    a5 = A5.get_color()[1] + A5.get_color()[0]
    a6 = A6.get_color()

    A1.set_color(a5)
    A4.set_color(a1)
    A5.set_color(a6) 
    A6.set_color(a4)

def Up():
    # print("🥐Up")
    
    #move corners
    c0 = C0.get_color()
    c1 = C1.get_color()
    c2 = C2.get_color()
    c3 = C3.get_color()

    C0.set_color(c2)#✔️
    C1.set_color(c0)#✔️
    C2.set_color(c3)#✔️
    C3.set_color(c1)#✔️

    #move edges
    a0 = A0.get_color()
    a1 = A1.get_color()
    a2 = A2.get_color()
    a3 = A3.get_color()

    A0.set_color(a1) 
    A1.set_color(a3)
    A2.set_color(a0)
    A3.set_color(a2)
def UpPrime():
    # print("🥐UpPrime")

    #move corners
    c0 = C0.get_color()
    c1 = C1.get_color()
    c2 = C2.get_color()
    c3 = C3.get_color()

    C0.set_color(c1)
    C1.set_color(c3)
    C2.set_color(c0)
    C3.set_color(c2)

    #move edges
    a0 = A0.get_color()
    a1 = A1.get_color()
    a2 = A2.get_color()
    a3 = A3.get_color()

    A0.set_color(a2) 
    A1.set_color(a0)
    A2.set_color(a3)
    A3.set_color(a1)

def Down():
    # print("🥐Down")
    
    #move corners
    c4 = C4.get_color()
    c5 = C5.get_color()
    c6 = C6.get_color()
    c7 = C7.get_color()

    C4.set_color(c5)
    C5.set_color(c7)
    C6.set_color(c4)
    C7.set_color(c6)

    #move edges
    a6 = A6.get_color()
    a8 = A8.get_color()
    a10 = A10.get_color()
    a11 = A11.get_color()

    A6.set_color(a11)
    A8.set_color(a6)
    A10.set_color(a8)
    A11.set_color(a10)
def DownPrime():
    # print("🥐DownPrime")

    #move corners
    c4 = C4.get_color()
    c5 = C5.get_color()
    c6 = C6.get_color()
    c7 = C7.get_color()

    C4.set_color(c6)
    C5.set_color(c4)
    C6.set_color(c7)
    C7.set_color(c5)

    #move edges
    a6 = A6.get_color()
    a8 = A8.get_color()
    a10 = A10.get_color()
    a11 = A11.get_color()

    A6.set_color(a8)
    A8.set_color(a10)
    A10.set_color(a11)
    A11.set_color(a6)

def Front():
    # print("🥐Front")
    
    #move corners
    c2 = C2.get_color()
    c3 = C3.get_color()
    c6 = C6.get_color()
    c7 = C7.get_color()

    C2.set_color(c6[1] + c6[2] + c6[0])
    C3.set_color(c2[2] + c2[0] + c2[1])
    C6.set_color(c7[2] + c7[0] + c7[1])
    C7.set_color(c3[1] + c3[2] + c3[0])


    #move edges
    a3 = A3.get_color()[1] + A3.get_color()[0]
    a5 = A5.get_color()
    a7 = A7.get_color()
    a8 =  A8.get_color()[1] + A8.get_color()[0]

    A3.set_color(a5) 
    A5.set_color(a8)
    A7.set_color(a3)
    A8.set_color(a7)

def FrontPrime():
    # print("🥐FrontPrime")

    #move corners
    c2 = C2.get_color()
    c3 = C3.get_color()
    c6 = C6.get_color()
    c7 = C7.get_color()

    C2.set_color(c3[1] + c3[2] + c3[0])
    C3.set_color(c7[2] + c7[0] + c7[1])
    C6.set_color(c2[2] + c2[0] + c2[1])
    C7.set_color(c6[1] + c6[2] + c6[0])

    #move edges
    a3 = A3.get_color()
    a5 = A5.get_color()[1] + A5.get_color()[0]
    a7 = A7.get_color()[1] + A7.get_color()[0]
    a8 = A8.get_color()

    A3.set_color(a7) 
    A5.set_color(a3)
    A7.set_color(a8)
    A8.set_color(a5)


def Back():
    # print("🥐Back")
    
    #move corners
    c0 = C0.get_color()
    c1 = C1.get_color()
    c4 = C4.get_color()
    c5 = C5.get_color()

    C0.set_color(c1[2] + c1[0] + c1[1])
    C1.set_color(c5[1] + c5[2] + c5[0])
    C4.set_color(c0[1] + c0[2] + c0[0])
    C5.set_color(c4[2] + c4[0] + c4[1])
   
    #move edges
    a0 = A0.get_color()
    a4 = A4.get_color()[1] + A4.get_color()[0]
    a9 = A9.get_color()
    a11 = A11.get_color()[1] + A11.get_color()[0]
    
    A0.set_color(a9) 
    A4.set_color(a0)
    A9.set_color(a11)
    A11.set_color(a4)

def BackPrime():
    # print("🥐BackPrime")

    #move corners
    c0 = C0.get_color()
    c1 = C1.get_color()
    c4 = C4.get_color()
    c5 = C5.get_color()

    C0.set_color(c4[2] + c4[0] + c4[1])
    C1.set_color(c0[1] + c0[2] + c0[0])
    C4.set_color(c5[1] + c5[2] + c5[0])
    C5.set_color(c1[2] + c1[0] + c1[1])

    #move edges
    a0 = A0.get_color()
    a4 = A4.get_color()
    a9 = A9.get_color()[1] + A9.get_color()[0]
    a11 = A11.get_color()[1] + A11.get_color()[0]
    
    A0.set_color(a4)
    A4.set_color(a11)
    A9.set_color(a0)
    A11.set_color(a9)
def R2():
    Right()
    Right()

def F2():
    Front()
    Front()

def L2():
    Left()
    Left()

def U2():
    Up()
    Up()

def D2():
    Down()
    Down()
    
def B2():
    Back()
    Back()

def Rien():
    pass
    