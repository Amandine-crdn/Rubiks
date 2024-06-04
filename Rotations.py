from CubeClass import cube
from NodeClass import s_A0, s_A1, s_A2, s_A3, s_A4, s_A5, s_A6, s_A7, s_A8, s_A9, s_A10, s_A11

# from NodeClass import NodeClass


def Right():
    print("🥐 fonction Right\n")
    
    #move corners
    # C1 = cube.get_color_coin(1)
    # C3 = cube.get_color_coin(3)
    # C5 = cube.get_color_coin(5)
    # C7 = cube.get_color_coin(7)

    # cube.set_color_coin(1, C3[2] + C3[0] + C3[1]) #✔️
    # cube.set_color_coin(3, C7[2] + C7[0] + C7[1]) #✔️
    # cube.set_color_coin(5, C1[2] + C1[0] + C1[1]) #✔️
    # cube.set_color_coin(7, C5) #✔️

    #move edges
    a2 = s_A2.get_color()[1] + s_A2.get_color()[0]
    a10 = s_A10.get_color()[1] + s_A10.get_color()[0]
    a7 = s_A7.get_color()
    a9 = s_A9.get_color()

    s_A9.set_color(a2)
    s_A2.set_color(a7)
    s_A7.set_color(a10)
    s_A10.set_color(a9)


def RightPrime():
    print("🥐 fonction RightPrime\n")

    #move corners
    # C1 = cube.get_color_coin(1)
    # C3 = cube.get_color_coin(3)
    # C5 = cube.get_color_coin(5)
    # C7 = cube.get_color_coin(7)

    # cube.set_color_coin(1, C5[1] + C5[2] + C5[0]) #✔️
    # cube.set_color_coin(3, C1[1] + C1[2] + C1[0]) #✔️
    # cube.set_color_coin(5, C7) #✔️
    # cube.set_color_coin(7, C3[1] + C3[2] + C3[0]) #✔️

    #move edges
    a2 = s_A2.get_color()
    a10 = s_A10.get_color()
    a7 = s_A7.get_color()[1] + s_A7.get_color()[0]
    a9 =  s_A9.get_color()[1] + s_A9.get_color()[0]

    s_A2.set_color(a9) 
    s_A7.set_color(a2) 
    s_A9.set_color(a10) 
    s_A10.set_color(a7) 

def Left():
    print("🥐 fonction Left\n")
    
    #move corners
    # C0 = cube.get_color_coin(0)
    # C2 = cube.get_color_coin(2)
    # C4 = cube.get_color_coin(4)
    # C6 = cube.get_color_coin(6)

    # cube.set_color_coin(0, C4[2] + C4[0] + C4[1]) #✔️
    # cube.set_color_coin(2, C0[2] + C0[0] + C0[1]) #✔️
    # cube.set_color_coin(4, C6[0] + C6[2] + C6[1]) #✔️
    # cube.set_color_coin(6, C2[2] + C2[1] + C2[0]) #✔️

    #move edges
    a1 = s_A1.get_color()[1] + s_A1.get_color()[0]
    a4 = s_A4.get_color()[1] + s_A4.get_color()[0]
    a6 = s_A6.get_color()
    a5 = s_A5.get_color()

    s_A5.set_color(a1) 
    s_A1.set_color(a4)
    s_A4.set_color(a6)
    s_A6.set_color(a5)

def LeftPrime():
    print("🥐 fonction LeftPrime\n")

    #move corners
    # C0 = cube.get_color_coin(0)
    # C2 = cube.get_color_coin(2)
    # C4 = cube.get_color_coin(4)
    # C6 = cube.get_color_coin(6)

    # cube.set_color_coin(0, C2[1] + C2[2] + C2[0]) #✔️
    # cube.set_color_coin(2, C6[2] + C6[1] + C6[0]) #✔️
    # cube.set_color_coin(4, C0[1] + C0[2] + C0[0]) #✔️
    # cube.set_color_coin(6, C4[0] + C4[2] + C4[1]) #✔️

    #move edges
    a1 = s_A1.get_color()[1] + s_A1.get_color()[0]
    a4 = s_A4.get_color()
    a5 = s_A5.get_color()[1] + s_A5.get_color()[0]
    a6 = s_A6.get_color()

    s_A1.set_color(a5)
    s_A4.set_color(a1)
    s_A5.set_color(a6) 
    s_A6.set_color(a4)


def Up():
    print("🥐 fonction Up\n")
    
    #move corners
    # C0 = cube.get_color_coin(0)
    # C1 = cube.get_color_coin(1)
    # C2 = cube.get_color_coin(2)
    # C3 = cube.get_color_coin(3)

    # cube.set_color_coin(0, C2)#✔️
    # cube.set_color_coin(1, C0)#✔️
    # cube.set_color_coin(2, C3)#✔️
    # cube.set_color_coin(3, C1)#✔️

    #move edges
    a0 = s_A0.get_color()
    a1 = s_A1.get_color()
    a2 = s_A2.get_color()
    a3 = s_A3.get_color()

    s_A0.set_color(a1) 
    s_A1.set_color(a3)
    s_A2.set_color(a0)
    s_A3.set_color(a2)

def UpPrime():
    print("🥐 fonction UpPrime\n")

    #move corners
    # C0 = cube.get_color_coin(0)
    # C1 = cube.get_color_coin(1)
    # C2 = cube.get_color_coin(2)
    # C3 = cube.get_color_coin(3)

    # cube.set_color_coin(0, C1)#✔️
    # cube.set_color_coin(1, C3)#✔️
    # cube.set_color_coin(2, C0)#✔️
    # cube.set_color_coin(3, C2)#✔️

    #move edges
    a0 = s_A0.get_color()
    a1 = s_A1.get_color()
    a2 = s_A2.get_color()
    a3 = s_A3.get_color()

    s_A0.set_color(a2) 
    s_A1.set_color(a0)
    s_A2.set_color(a3)
    s_A3.set_color(a1)


def Down():
    print("🥐 fonction Down\n")
    
    #move corners
    # C4 = cube.get_color_coin(4)
    # C5 = cube.get_color_coin(5)
    # C6 = cube.get_color_coin(6)
    # C7 = cube.get_color_coin(7)

    # cube.set_color_coin(4, C5[1] + C5[2] + C5[0]) #✔️
    # cube.set_color_coin(5, C7[2] + C7[0] + C7[1]) #✔️
    # cube.set_color_coin(6, C4[1] + C4[2] + C4[0]) #✔️
    # cube.set_color_coin(7, C6[2] + C6[1] + C6[0]) #✔️

    #move edges
    a6 = s_A6.get_color()
    a8 = s_A8.get_color()
    a10 = s_A10.get_color()
    a11 = s_A11.get_color()

    s_A6.set_color(a11)
    s_A8.set_color(a6)
    s_A10.set_color(a8)
    s_A11.set_color(a10)

def DownPrime():
    print("🥐 fonction DownPrime\n")

    #move corners
    # C4 = cube.get_color_coin(4)
    # C5 = cube.get_color_coin(5)
    # C6 = cube.get_color_coin(6)
    # C7 = cube.get_color_coin(7)

    # cube.set_color_coin(4, C6[2] + C6[1] + C6[0])#✔️
    # cube.set_color_coin(5, C4[2] + C4[0] + C4[1])#✔️
    # cube.set_color_coin(6, C7[2] + C7[1] + C7[0])#✔️
    # cube.set_color_coin(7, C5[1] + C5[2] + C5[0])#✔️

    #move edges
    a6 = s_A6.get_color()
    a8 = s_A8.get_color()
    a10 = s_A10.get_color()
    a11 = s_A11.get_color()

    s_A6.set_color(a8)
    s_A8.set_color(a10)
    s_A10.set_color(a11)
    s_A11.set_color(a6)

def Front():
    print("🥐 fonction Front\n")
    
    #move corners
    # C2 = cube.get_color_coin(2)
    # C3 = cube.get_color_coin(3)
    # C6 = cube.get_color_coin(6)
    # C7 = cube.get_color_coin(7)

    # cube.set_color_coin(2, C6[0] + C6[2] + C6[1])#✔️
    # cube.set_color_coin(3, C2[2] + C2[0] + C2[1])#✔️
    # cube.set_color_coin(6, C7[1] + C7[0] + C7[2])#✔️
    # cube.set_color_coin(7, C3) #✔️

    #move edges
    a3 = s_A3.get_color()[1] + s_A3.get_color()[0]
    a5 = s_A5.get_color()
    a7 = s_A7.get_color()
    a8 =  s_A8.get_color()[1] + s_A8.get_color()[0]

    s_A3.set_color(a5) 
    s_A5.set_color(a8)
    s_A7.set_color(a3)
    s_A8.set_color(a7)

def FrontPrime():
    print("🥐 fonction FrontPrime\n")

    #move corners
    # C2 = cube.get_color_coin(2)
    # C3 = cube.get_color_coin(3)
    # C6 = cube.get_color_coin(6)
    # C7 = cube.get_color_coin(7)

    # cube.set_color_coin(2, C3[1] + C3[2] + C3[0])#✔️
    # cube.set_color_coin(3, C7)#✔️
    # cube.set_color_coin(6, C2[0] + C2[2] + C2[1])#✔️
    # cube.set_color_coin(7, C6[1] + C6[0] + C6[2])#✔️

    #move edges
    a3 = s_A3.get_color()
    a5 = s_A5.get_color()[1] + s_A5.get_color()[0]
    a7 = s_A7.get_color()[1] + s_A7.get_color()[0]
    a8 = s_A8.get_color()

    s_A3.set_color(a7) 
    s_A5.set_color(a3)
    s_A7.set_color(a8)
    s_A8.set_color(a5)


def Back():
    print("🥐 fonction Back\n")
    
    #move corners
    # C0 = cube.get_color_coin(0)
    # C1 = cube.get_color_coin(1)
    # C4 = cube.get_color_coin(4)
    # C5 = cube.get_color_coin(5)

    # cube.set_color_coin(0, C1[2] + C1[0] + C1[1])#✔️
    # cube.set_color_coin(1, C5)#✔️
    # cube.set_color_coin(4, C0)#✔️
    # cube.set_color_coin(5, C4[1] + C4[2] + C4[0])#✔️
   
    #move edges
    a0 = s_A0.get_color()
    a4 = s_A4.get_color()[1] + s_A4.get_color()[0]
    a9 = s_A9.get_color()
    a11 = s_A11.get_color()[1] + s_A11.get_color()[0]
    
    s_A0.set_color(a9) 
    s_A4.set_color(a0)
    s_A9.set_color(a11)
    s_A11.set_color(a4)

def BackPrime():
    print("🥐 fonction BackPrime\n")

    #move corners
    # C0 = cube.get_color_coin(0)
    # C1 = cube.get_color_coin(1)
    # C4 = cube.get_color_coin(4)
    # C5 = cube.get_color_coin(5)

    # cube.set_color_coin(0, C4)#✔️
    # cube.set_color_coin(1, C0[1] + C0[2] + C0[0])#✔️
    # cube.set_color_coin(4, C5[2] + C5[0] + C5[1])#✔️
    # cube.set_color_coin(5, C1)#✔️

    #move edges
    a0 = s_A0.get_color()
    a4 = s_A4.get_color()
    a9 = s_A9.get_color()[1] + s_A9.get_color()[0]
    a11 = s_A11.get_color()[1] + s_A11.get_color()[0]
    
    s_A0.set_color(a4) 
    s_A4.set_color(a11)
    s_A9.set_color(a0)
    s_A11.set_color(a9)


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