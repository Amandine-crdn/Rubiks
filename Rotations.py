from CubeClass import cube
from NodeClass import A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11

# from NodeClass import NodeClass


def Right():
    print("🥐Right")
    
    #move corners
    C1 = cube.get_color_coin(1)
    C3 = cube.get_color_coin(3)
    C5 = cube.get_color_coin(5)
    C7 = cube.get_color_coin(7)

    cube.set_color_coin(1, C3[2] + C3[0] + C3[1]) #✔️
    cube.set_color_coin(3, C7[2] + C7[0] + C7[1]) #✔️
    cube.set_color_coin(5, C1[2] + C1[0] + C1[1]) #✔️
    cube.set_color_coin(7, C5) #✔️

    #move edges
    a2 = A2.get_color()[1] + A2.get_color()[0]
    a10 = A10.get_color()[1] + A10.get_color()[0]
    a7 = A7.get_color()
    a9 = A9.get_color()

    A9.set_color(a2)
    A2.set_color(a7)
    A7.set_color(a10)
    A10.set_color(a9)
    cube.set_solution("R")


def RightPrime():
    print("🥐RightPrime")

    #move corners
    C1 = cube.get_color_coin(1)
    C3 = cube.get_color_coin(3)
    C5 = cube.get_color_coin(5)
    C7 = cube.get_color_coin(7)

    cube.set_color_coin(1, C5[1] + C5[2] + C5[0]) #✔️
    cube.set_color_coin(3, C1[1] + C1[2] + C1[0]) #✔️
    cube.set_color_coin(5, C7) #✔️
    cube.set_color_coin(7, C3[1] + C3[2] + C3[0]) #✔️

    #move edges
    a2 = A2.get_color()
    a10 = A10.get_color()
    a7 = A7.get_color()[1] + A7.get_color()[0]
    a9 =  A9.get_color()[1] + A9.get_color()[0]

    A2.set_color(a9) 
    A7.set_color(a2) 
    A9.set_color(a10) 
    A10.set_color(a7) 

    cube.set_solution("R'")

def Left():
    print("🥐Left")
    
    #move corners
    C0 = cube.get_color_coin(0)
    C2 = cube.get_color_coin(2)
    C4 = cube.get_color_coin(4)
    C6 = cube.get_color_coin(6)

    cube.set_color_coin(0, C4[2] + C4[0] + C4[1]) #✔️
    cube.set_color_coin(2, C0[2] + C0[0] + C0[1]) #✔️
    cube.set_color_coin(4, C6[0] + C6[2] + C6[1]) #✔️
    cube.set_color_coin(6, C2[2] + C2[1] + C2[0]) #✔️

    #move edges
    a1 = A1.get_color()[1] + A1.get_color()[0]
    a4 = A4.get_color()[1] + A4.get_color()[0]
    a6 = A6.get_color()
    a5 = A5.get_color()

    A5.set_color(a1) 
    A1.set_color(a4)
    A4.set_color(a6)
    A6.set_color(a5)
    cube.set_solution("L")

def LeftPrime():
    print("🥐LeftPrime")

    #move corners
    C0 = cube.get_color_coin(0)
    C2 = cube.get_color_coin(2)
    C4 = cube.get_color_coin(4)
    C6 = cube.get_color_coin(6)

    cube.set_color_coin(0, C2[1] + C2[2] + C2[0]) #✔️
    cube.set_color_coin(2, C6[2] + C6[1] + C6[0]) #✔️
    cube.set_color_coin(4, C0[1] + C0[2] + C0[0]) #✔️
    cube.set_color_coin(6, C4[0] + C4[2] + C4[1]) #✔️

    #move edges
    a1 = A1.get_color()[1] + A1.get_color()[0]
    a4 = A4.get_color()
    a5 = A5.get_color()[1] + A5.get_color()[0]
    a6 = A6.get_color()

    A1.set_color(a5)
    A4.set_color(a1)
    A5.set_color(a6) 
    A6.set_color(a4)
    cube.set_solution("L'")


def Up():
    print("🥐Up")
    
    #move corners
    C0 = cube.get_color_coin(0)
    C1 = cube.get_color_coin(1)
    C2 = cube.get_color_coin(2)
    C3 = cube.get_color_coin(3)

    cube.set_color_coin(0, C2)#✔️
    cube.set_color_coin(1, C0)#✔️
    cube.set_color_coin(2, C3)#✔️
    cube.set_color_coin(3, C1)#✔️

    #move edges
    a0 = A0.get_color()
    a1 = A1.get_color()
    a2 = A2.get_color()
    a3 = A3.get_color()

    A0.set_color(a1) 
    A1.set_color(a3)
    A2.set_color(a0)
    A3.set_color(a2)
    cube.set_solution("U")

def UpPrime():
    print("🥐UpPrime")

    #move corners
    C0 = cube.get_color_coin(0)
    C1 = cube.get_color_coin(1)
    C2 = cube.get_color_coin(2)
    C3 = cube.get_color_coin(3)

    cube.set_color_coin(0, C1)#✔️
    cube.set_color_coin(1, C3)#✔️
    cube.set_color_coin(2, C0)#✔️
    cube.set_color_coin(3, C2)#✔️

    #move edges
    a0 = A0.get_color()
    a1 = A1.get_color()
    a2 = A2.get_color()
    a3 = A3.get_color()

    A0.set_color(a2) 
    A1.set_color(a0)
    A2.set_color(a3)
    A3.set_color(a1)
    cube.set_solution("U'")


def Down():
    print("🥐Down")
    
    #move corners
    C4 = cube.get_color_coin(4)
    C5 = cube.get_color_coin(5)
    C6 = cube.get_color_coin(6)
    C7 = cube.get_color_coin(7)

    cube.set_color_coin(4, C5[1] + C5[2] + C5[0]) #✔️
    cube.set_color_coin(5, C7[2] + C7[0] + C7[1]) #✔️
    cube.set_color_coin(6, C4[1] + C4[2] + C4[0]) #✔️
    cube.set_color_coin(7, C6[2] + C6[1] + C6[0]) #✔️

    #move edges
    a6 = A6.get_color()
    a8 = A8.get_color()
    a10 = A10.get_color()
    a11 = A11.get_color()

    A6.set_color(a11)
    A8.set_color(a6)
    A10.set_color(a8)
    A11.set_color(a10)
    cube.set_solution("D")

def DownPrime():
    print("🥐DownPrime")

    #move corners
    C4 = cube.get_color_coin(4)
    C5 = cube.get_color_coin(5)
    C6 = cube.get_color_coin(6)
    C7 = cube.get_color_coin(7)

    cube.set_color_coin(4, C6[2] + C6[1] + C6[0])#✔️
    cube.set_color_coin(5, C4[2] + C4[0] + C4[1])#✔️
    cube.set_color_coin(6, C7[2] + C7[1] + C7[0])#✔️
    cube.set_color_coin(7, C5[1] + C5[2] + C5[0])#✔️

    #move edges
    a6 = A6.get_color()
    a8 = A8.get_color()
    a10 = A10.get_color()
    a11 = A11.get_color()

    A6.set_color(a8)
    A8.set_color(a10)
    A10.set_color(a11)
    A11.set_color(a6)

    cube.set_solution("D'")

def Front():
    print("🥐Front")
    
    #move corners
    C2 = cube.get_color_coin(2)
    C3 = cube.get_color_coin(3)
    C6 = cube.get_color_coin(6)
    C7 = cube.get_color_coin(7)

    cube.set_color_coin(2, C6[0] + C6[2] + C6[1])#✔️
    cube.set_color_coin(3, C2[2] + C2[0] + C2[1])#✔️
    cube.set_color_coin(6, C7[1] + C7[0] + C7[2])#✔️
    cube.set_color_coin(7, C3) #✔️

    #move edges
    a3 = A3.get_color()[1] + A3.get_color()[0]
    a5 = A5.get_color()
    a7 = A7.get_color()
    a8 =  A8.get_color()[1] + A8.get_color()[0]

    A3.set_color(a5) 
    A5.set_color(a8)
    A7.set_color(a3)
    A8.set_color(a7)

    cube.set_solution("F")

def FrontPrime():
    print("🥐FrontPrime")

    #move corners
    C2 = cube.get_color_coin(2)
    C3 = cube.get_color_coin(3)
    C6 = cube.get_color_coin(6)
    C7 = cube.get_color_coin(7)

    cube.set_color_coin(2, C3[1] + C3[2] + C3[0])#✔️
    cube.set_color_coin(3, C7)#✔️
    cube.set_color_coin(6, C2[0] + C2[2] + C2[1])#✔️
    cube.set_color_coin(7, C6[1] + C6[0] + C6[2])#✔️

    #move edges
    a3 = A3.get_color()
    a5 = A5.get_color()[1] + A5.get_color()[0]
    a7 = A7.get_color()[1] + A7.get_color()[0]
    a8 = A8.get_color()

    A3.set_color(a7) 
    A5.set_color(a3)
    A7.set_color(a8)
    A8.set_color(a5)

    cube.set_solution("F'")


def Back():
    print("🥐Back")
    
    #move corners
    C0 = cube.get_color_coin(0)
    C1 = cube.get_color_coin(1)
    C4 = cube.get_color_coin(4)
    C5 = cube.get_color_coin(5)

    cube.set_color_coin(0, C1[2] + C1[0] + C1[1])#✔️
    cube.set_color_coin(1, C5)#✔️
    cube.set_color_coin(4, C0)#✔️
    cube.set_color_coin(5, C4[1] + C4[2] + C4[0])#✔️
   
    #move edges
    a0 = A0.get_color()
    a4 = A4.get_color()[1] + A4.get_color()[0]
    a9 = A9.get_color()
    a11 = A11.get_color()[1] + A11.get_color()[0]
    
    A0.set_color(a9) 
    A4.set_color(a0)
    A9.set_color(a11)
    A11.set_color(a4)

    cube.set_solution("B")

def BackPrime():
    print("🥐BackPrime")

    #move corners
    C0 = cube.get_color_coin(0)
    C1 = cube.get_color_coin(1)
    C4 = cube.get_color_coin(4)
    C5 = cube.get_color_coin(5)

    cube.set_color_coin(0, C4)#✔️
    cube.set_color_coin(1, C0[1] + C0[2] + C0[0])#✔️
    cube.set_color_coin(4, C5[2] + C5[0] + C5[1])#✔️
    cube.set_color_coin(5, C1)#✔️

    #move edges
    a0 = A0.get_color()
    a4 = A4.get_color()
    a9 = A9.get_color()[1] + A9.get_color()[0]
    a11 = A11.get_color()[1] + A11.get_color()[0]
    
    A0.set_color(a4) 
    A4.set_color(a11)
    A9.set_color(a0)
    A11.set_color(a9)
    cube.set_solution("B'")

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