from Start.NodeClass import Node, A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, C0, C1, C2, C3, C4, C5, C6, C7
from Utils.Functions import action
from Start.CubeClass import cube

def set_binary_face(color: str, N1: Node, N2: Node, N3: Node, N4: Node, N5: Node, N6: Node, N7: Node, N8: Node) -> int:
       faces_list = [N1, N2, N3, N4, N5, N6, N7, N8]
       binary_buffer = 0
       current_color = " "
       for index, n in enumerate(faces_list):
           current_color = n.get_color()
           binary_buffer |= (((current_color[1], current_color[0])[len(current_color) == 3] == color[0])<<(len(faces_list) - index - 1))
           print("test", bin(binary_buffer), (current_color[1], current_color[0])[len(current_color) == 3])
       return binary_buffer

def resolve_yellow_cross():
    start = [6] # B
    sexy_move = [0, 10, 1, 11]; # R D R' D'
    end = [7] # B'

    binary_face = set_binary_face('Y', C5, A11, C4, A10, A6, C7, A8, C6)
    print("ROGER WAS HERE", bin(binary_face))
    
    # CROSS PART
    if (binary_face & 0b01011010) == 0b01011010:
        print("cross")
    else:
        print("NO CROSS")

    #LINE PART
    if (binary_face & 0b00011000) == 0b00011000:
        print("horizontal line")
    elif (binary_face & 0b01000010) == 0b01000010:
        print("vertical line")

    else:
        print("NO LINE")


    #L PART
    if (binary_face & 0b01010000) == 0b01010000:
        print ("up left")
    elif (binary_face & 0b01001000) == 0b01001000:
        print ("up right")
    elif (binary_face & 0b00010010) == 0b00010010:
        print ("back left")
    elif (binary_face & 0b00001010) == 0b00001010:
        print ("back right")
    else:
        print("NO CROSS")


def resolve_yellow_face():
    
    # try with python3 main.py "F2 D2 L' F2 L D2 F D' F"
    resolve_yellow_cross();
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
