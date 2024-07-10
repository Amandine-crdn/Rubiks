from NodeClass import Node, A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, C0, C1, C2, C3, C4, C5, C6, C7
from Functions import action
from CubeClass import cube

#def set_binary_face(color: str, N1: Node, N2: Node, N3: Node, N4: Node, N5: Node, N6: Node, N7: Node, N8: Node) -> int:
def set_binary_face() -> int:
       binary_buffer = 0
       current_color = " "
       binary_buffer |= ((C5.get_color()[2] == 'Y')<<19)
#       print(C5.get_color()[2])
       binary_buffer |= ((A11.get_color()[0] == 'Y')<<18)
#       print(A11.get_color()[0])
       binary_buffer |= ((C4.get_color()[1] == 'Y')<<17)
#       print(C4.get_color()[1])
       binary_buffer |= ((C5.get_color()[1] == 'Y')<<16)
#       print(C5.get_color()[1])
       binary_buffer |= ((C5.get_color()[0] == 'Y')<<15)
#       print(C5.get_color()[0])
       binary_buffer |= ((A11.get_color()[1] == 'Y')<<14)
#       print(A11.get_color()[1])
       binary_buffer |= ((C4.get_color()[0] == 'Y')<<13)
#       print(C4.get_color()[0])
       binary_buffer |= ((C4.get_color()[2] == 'Y')<<12)
#       print(C4.get_color()[2])
       binary_buffer |= ((A10.get_color()[0] == 'Y')<<11)
#       print(A10.get_color()[0])
       binary_buffer |= ((A10.get_color()[1] == 'Y')<<10)
#       print(A10.get_color()[1])
       binary_buffer |= ((A6.get_color()[1] == 'Y')<<9)
#       print(A6.get_color()[1])
       binary_buffer |= ((A6.get_color()[0] == 'Y')<<8)
#       print(A6.get_color()[0])
       binary_buffer |= ((C7.get_color()[2] == 'Y')<<7)
#       print(C7.get_color()[2])
       binary_buffer |= ((C7.get_color()[0] == 'Y')<<6)
#       print(C7.get_color()[0])
       binary_buffer |= ((A8.get_color()[1] == 'Y')<<5)
#       print(A8.get_color()[1])
       binary_buffer |= ((C6.get_color()[0] == 'Y')<<4)
#       print(C6.get_color()[0])
       binary_buffer |= ((C6.get_color()[1] == 'Y')<<3)
#       print(C6.get_color()[1])
       binary_buffer |= ((C7.get_color()[1] == 'Y')<<2)
#       print(C7.get_color()[1])
       binary_buffer |= ((A8.get_color()[0] == 'Y')<<1)
#       print(A8.get_color()[0])
       binary_buffer |= ((C6.get_color()[2] == 'Y')<<0)
#       print(C6.get_color()[2])
#       for index, n in enumerate(faces_list):
#           current_color = n.get_color()
#           binary_buffer |= (((current_color[1], current_color[0])[len(current_color) == 3] == color[0])<<(len(faces_list) - index - 1))
#           print("test", bin(binary_buffer), (current_color[1], current_color[0])[len(current_color) == 3])
       print(bin(binary_buffer))
       return binary_buffer

def resolve_yellow_cross():
    start = [6] # B
    sexy_move = [0, 10, 1, 11]; # R D R' D'
    end = [7] # B'

    binary_face = set_binary_face('Y', C5, A11, C4, A10, A6, C7, A8, C6)

    orientation = 0;

    while((binary_face & 0b01011010) != 0b01011010):
        print("BEGIN")
        #LINE PART
#        if (binary_face & 0b00011000) == 0b00011000:
#            print("horizontal line")
        if (binary_face & 0b01000010) == 0b01000010:
            orientation -= 2
            action(10)() # D
            print("vertical line")
        #L PART
#        elif (binary_face & 0b01010000) == 0b01010000:
#            print ("up left")
        elif (binary_face & 0b01001000) == 0b01001000:
            action(11)() # D'
            print ("up right")
        elif (binary_face & 0b00010010) == 0b00010010:
            print ("back left")
            action(10)() # D
        elif (binary_face & 0b00001010) == 0b00001010:
            action(10)() # D
            action(10)() # D
            print ("back right")
        else:
            for a in start + sexy_move + end :
                action(a)()
        cube.print_cube()
        binary_face = set_binary_face('Y', C5, A11, C4, A10, A6, C7, A8, C6)

def first_step_two_look_oll():
    binary_face = set_binary_face()
    instructions = []
    cube.print_cube()
    if (binary_face & 0b00000100011000100000) == 0b00000100011000100000:
        print("CROSS")
        pass
    elif binary_face & ((1<<1) | (1<<8) | (1<<11) | (1<<18)) == ((1<<1) | (1<<8) | (1<<11) | (1<<18)):
        print("point")
        instructions = [4, 2, 10, 3, 11, 5, 6, 10, 0, 11, 1, 7]# F L D L' D' F' B D R D' R' B'
    elif binary_face & ((1<<1) | (1<<9) | (1<<10) | (1<<18)) == ((1<<1) | (1<<9) | (1<<10) | (1<<18)):
        print("normal line")
        instructions = [4, 2, 10, 3, 11, 5]# F L D L' D' F'
    elif binary_face & ((1<<5) | (1<<8) | (1<<11) | (1<<14)) == ((1<<5) | (1<<8) | (1<<11) | (1<<14)):
        print("vertical line")
        instructions = [10, 4, 2, 10, 3, 11, 5]# D F L D L' D' F'
    elif binary_face &  0b01000000101000100000 == 0b01000000101000100000:
        print("normal L")
        instructions = [6, 10, 0, 11, 1, 7] # B D R D' R' B' 
    elif binary_face &  0b01000000010100100000 == 0b01000000010100100000:
        print("down left L")
        instructions = [11, 6, 10, 0, 11, 1, 7] # D' B D R D' R' B' 
    elif (binary_face & 0b00000100010100000010) == 0b00000100010100000010:
        print("up right L")
        instructions = [10, 10, 6, 10, 0, 11, 1, 7] # DD  B D R D' R' B' 
    elif (binary_face & 0b00000100101000000010) == 0b00000100101000000010:
        print("up left L")
        instructions = [10, 6, 10, 0, 11, 1, 7] # D B D R D' R' B' 
    for i in instructions:
        action(i)()
    cube.print_cube()


def resolve_yellow_face():
    
    # try with python3 main.py "F2 D2 L' F2 L D2 F D' F"
    first_step_two_look_oll()
#    resolve_yellow_cross();
#       yellow_faces_list = [C5, A11, C4, A10, A6, C7, A8, C6]
#       binary_yellow = 0
#       current_color = " "
#       for index, n in enumerate(yellow_faces_list):
#           current_color = n.get_color()
#           print("test", (current_color[1], current_color[0])[len(current_color) == 3])
#           binary_yellow |= (((current_color[1], current_color[0])[len(current_color) == 3] == 'Y')<<(len(yellow_faces_list) - index))
#       print(bin(binary_yellow))


def check_cross():
        #a11
    #a6     a10
        #a8
    print(A8.get_color()[1], A6.get_color()[1], A10.get_color()[1], A11.get_color()[1])
    if A8.get_color()[1] == 'Y' and A10.get_color()[1] == 'Y' and A11.get_color()[1] == 'Y' and A6.get_color()[1] == 'Y':
        return True
    elif A10.get_color()[1] == 'Y' and A6.get_color()[1] == 'Y':
        make_cross()
        print("1")
    elif A11.get_color()[1] == 'Y' and A8.get_color()[1] == 'Y':
        action(11)
        make_cross()
        print("2")
    else:
        return False
    return True
    
def make_cross():
    protocole_list = [4, 2, 10, 3, 11, 5] # f l d l' d' f'
    for p in protocole_list:
        action(p)()
    
def check_L():
    if A8.get_color()[1] == 'Y' and A10.get_color()[1] == 'Y':
        action(10)() #d
        make_cross()
        make_cross()
    elif A11.get_color()[1] == 'Y' and A10.get_color()[1] == 'Y':
        make_cross()
        make_cross()
    elif A8.get_color()[1] == 'Y' and A6.get_color()[1] == 'Y':
        action(10)() #d
        action(10)() #d
        make_cross()
        make_cross()
    elif A11.get_color()[1] == 'Y' and A6.get_color()[1] == 'Y':
        action(11)() #d'
        make_cross()
        make_cross()
   

def check_trait():
    if (A8.get_color()[1] == 'Y' and A10.get_color()[1] == 'Y') or\
        (A11.get_color()[1] == 'Y' and A10.get_color()[1] == 'Y') or\
        (A8.get_color()[1] == 'Y' and A6.get_color()[1] == 'Y') or\
        (A11.get_color()[1] == 'Y' and A6.get_color()[1] == 'Y'):
        return True
    return False
