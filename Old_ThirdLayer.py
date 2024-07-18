from NodeClass import Node, A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, C0, C1, C2, C3, C4, C5, C6, C7
from Functions import action
from CubeClass import cube
from pll import all_pll_binary

#def set_binary_face(color: str, N1: Node, N2: Node, N3: Node, N4: Node, N5: Node, N6: Node, N7: Node, N8: Node) -> int:
def set_binary_face() -> int:
       binary_buffer = 0
       current_color = " "
       binary_buffer |= ((C5.get_color()[2] == 'Y')<<19)
       binary_buffer |= ((A11.get_color()[0] == 'Y')<<18)
       binary_buffer |= ((C4.get_color()[1] == 'Y')<<17)
       binary_buffer |= ((C5.get_color()[1] == 'Y')<<16)
       binary_buffer |= ((C5.get_color()[0] == 'Y')<<15)
       binary_buffer |= ((A11.get_color()[1] == 'Y')<<14)
       binary_buffer |= ((C4.get_color()[0] == 'Y')<<13)
       binary_buffer |= ((C4.get_color()[2] == 'Y')<<12)
       binary_buffer |= ((A10.get_color()[0] == 'Y')<<11)
       binary_buffer |= ((A10.get_color()[1] == 'Y')<<10)
       binary_buffer |= ((A6.get_color()[1] == 'Y')<<9)
       binary_buffer |= ((A6.get_color()[0] == 'Y')<<8)
       binary_buffer |= ((C7.get_color()[2] == 'Y')<<7)
       binary_buffer |= ((C7.get_color()[0] == 'Y')<<6)
       binary_buffer |= ((A8.get_color()[1] == 'Y')<<5)
       binary_buffer |= ((C6.get_color()[0] == 'Y')<<4)
       binary_buffer |= ((C6.get_color()[1] == 'Y')<<3)
       binary_buffer |= ((C7.get_color()[1] == 'Y')<<2)
       binary_buffer |= ((A8.get_color()[0] == 'Y')<<1)
       binary_buffer |= ((C6.get_color()[2] == 'Y')<<0)
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

def convert_moves(moves: list) -> list:
    actions = []

    for m in moves:
        if m[0] == 'R':
            actions.append((0, 1)[len(m) == 2])
        elif m[0] == 'L':
            actions.append((2, 3)[len(m) == 2])
        elif m[0] == 'F':
            actions.append((4, 5)[len(m) == 2])
        elif m[0] == 'B':
            actions.append((6, 7)[len(m) == 2])
        elif m[0] == 'U':
            actions.append((8, 9)[len(m) == 2])
        elif m[0] == 'D':
            actions.append((10, 11)[len(m) == 2])
    return actions

def first_step_two_look_oll():
    print("first step")
    '''Make a cross on yellow face'''
    binary_face = set_binary_face()
    instructions = []
    cube.print_cube()
    if (binary_face & 0b00000100011000100000) == 0b00000100011000100000:
        print("CROSS")
        pass
    elif binary_face & 0b01000000100100000010 == 0b01000000100100000010:
        print("point")
        instructions = convert_moves(["F", "L", "D", "L'", "D'", "F'", "B", "D", "R", "D'", "R'", "B'"])
    elif binary_face & 0b01000000011000000010 == 0b01000000011000000010:
        print("normal line")
        instructions = convert_moves(["F", "L", "D", "L'", "D'", "F'"])
    elif binary_face & 0b00000100100100100000 == 0b00000100100100100000:
        print("vertical line")
        instructions = convert_moves(["D", "F", "L", "D", "L'", "D'", "F'"])
    elif binary_face &  0b01000000101000100000 == 0b01000000101000100000:
        print("normal L")
        instructions = convert_moves(["B", "D", "R", "D'", "R'", "B'"]) 
    elif binary_face &  0b01000000010100100000 == 0b01000000010100100000:
        print("down left L")
        instructions = convert_moves(["D'", "B", "D", "R", "D'", "R'", "B'"]) 
    elif (binary_face & 0b00000100010100000010) == 0b00000100010100000010:
        print("up right L")
        instructions = convert_moves(["D", "D", "B", "D", "R", "D'", "R'", "B'"]) 
    elif (binary_face & 0b00000100101000000010) == 0b00000100101000000010:
        print("up left L")
        instructions = convert_moves(["D", "B", "D", "R", "D'", "R'", "B'"]) 
    for i in instructions:
        action(i)()
    cube.print_cube()


def second_step_two_look_oll():
    print("second_step")
    cube.print_cube()
    binary_face = set_binary_face()
    instructions = []
    #fig 2
    # L D2 L' D' L' D' L'

    #fig 3
    # L D2 L2 D' L2 D' L2 D2 L
    print(bin(binary_face))
    #FIG 8
    if (binary_face & 0b00001110011001110000) == 0b00001110011001110000:
        print("Yellow face ok");
        pass

    #FIG 1
    elif (binary_face & 0b10000101011001100001) == 0b10000101011001100001:
        print("Fig 1")
        instructions = convert_moves(["L", "D", "L'", "D", "L", "D", "D", "L'"])
    elif (binary_face & 0b10000101011010110000) == 0b10000101011010110000:
        print("Fig 1 with D")
        instructions = convert_moves(["D", "L", "D", "L'", "D", "L", "D", "D", "L'"])
    elif (binary_face & 0b1101011010100001) == 0b1101011010100001:
        print("Fig 1 with D'")
        instructions = convert_moves(["D'", "L", "D", "L'", "D", "L", "D", "D", "L'"])
    elif (binary_face & 0b10000110011010100001) == 0b10000110011010100001:
        print("Fig 1 with D D")
        instructions = convert_moves(["D", "D", "L", "D", "L'", "D", "L", "D", "D", "L'"])

    #FIG 2
    elif (binary_face & 0b10110011000101100) == 0b10110011000101100:
        print("Fig 2")
        instructions = convert_moves(["L", "D", "D", "L'", "D'", "L", "D'", "L'"])
    elif (binary_face & 0b101100011000101100) == 0b101100011000101100:
        print("Fig 2 with D")
        instructions = convert_moves(["D", "L", "D", "D", "L'", "D'", "L", "D'", "L'"])
    elif (binary_face & 0b110100011000110100) == 0b110100011000110100:
        print("Fig 2 with D'")
        instructions = convert_moves(["D'", "L", "D", "D", "L'", "D'", "L", "D'", "L'"])
    elif (binary_face & 0b110100011001101000) == 0b110100011001101000:
        print("Fig 2 with D D")
        instructions = convert_moves(["D", "D", "L", "D", "D", "L'", "D'", "L", "D'", "L'"])

    #FIG 3
    elif (binary_face & 0b110100011010100001) == 0b110100011010100001:
        print("Fig 3")
        instructions = convert_moves(["L", "D", "D", "L", "L", "D'", "L", "L", "D'", "L", "L", "D", "D", "L"])
    elif (binary_face & 0b10101011000100101) == 0b10101011000100101:
        print("Fig 3 with D")
        instructions = convert_moves(["D", "L", "D", "D", "L", "L", "D'", "L", "L", "D'", "L", "L", "D", "D", "L"])
    elif (binary_face & 0b10100100011010101000) == 0b10100100011010101000:
        print("Fig 3 with D'")
        instructions = convert_moves(["D'", "L", "D", "D", "L", "L", "D'", "L", "L", "D'", "L", "L", "D", "D", "L"])
    elif (binary_face & 0b10000101011000101100) == 0b10000101011000101100:
        print("Fig 3 with D D")
        instructions = convert_moves(["D", "D", "L", "D", "D", "L", "L", "D'", "L", "L", "D'", "L", "L", "D", "D", "L"])

    #FIG 4
    elif (binary_face & 0b10100100011000100101) == 0b10100100011000100101:
        print("Fig 4")
        instructions = convert_moves(["F", "L", "D", "L'", "D'", "L", "D", "L'", "D'", "L", "D", "L'", "D'", "F'"])
    elif (binary_face & 0b00010101011010101000) == 0b00010101011010101000:
        print("Fig 4 with D")
        instructions = convert_moves(["D", "F", "L", "D", "L'", "D'", "L", "D", "L'", "D'", "L", "D", "L'", "D'", "F'"])

    #FIG 5
    elif(binary_face & 0b10000110011000110100) == 0b10000110011000110100:
        print("Fig 5")
        instructions = convert_moves(["R", "F", "L'", "F'", "R'", "F", "L", "F'"])
    elif(binary_face & 0b00001110011010101000) == 0b00001110011010101000:
        print("Fig 5 with D")
        instructions = convert_moves(["D", "R", "F", "L'", "F'", "R'", "F", "L", "F'"])
    elif(binary_face & 0b00010101011001110000) == 0b00010101011001110000:
        print("Fig 5 with D'")
        instructions = convert_moves(["D'", "R", "F", "L'", "F'", "R'", "F", "L", "F'"])
    elif(binary_face & 0b00101100011001100001) == 0b00101100011001100001:
        print("Fig 5 with D2")
        instructions = convert_moves(["D", "D", "R", "F", "L'", "F'", "R'", "F", "L", "F'"])

    #FIG 6
    elif(binary_face & 0b10110011001100001) == 0b10110011001100001:
        print("Fig 6")
        instructions = convert_moves(["F'", "R", "F", "L'", "F'", "R'", "F", "L"])
    elif(binary_face & 0b1101011000110100) == 0b1101011000110100:
        print("Fig 6 with D")
        instructions = convert_moves(["D", "F'", "R", "F", "L'", "F'", "R'", "F", "L"])
    elif(binary_face & 0b101100011010110000) == 0b101100011010110000:
        print("Fig 6 with D'")
        instructions = convert_moves(["D'", "F'", "R", "F", "L'", "F'", "R'", "F", "L"])
    elif(binary_face & 0b10000110011001101000) == 0b10000110011001101000:
        print("Fig 6 with D D")
        instructions = convert_moves(["D", "D", "F'", "R", "F", "L'", "F'", "R'", "F", "L"])

    #FIG 7
    elif (binary_face & 0b00001110011000100101) == 0b00001110011000100101:
        print("Fig 7")
        instructions = convert_moves(["L", "L", "U", "L'", "D", "D", "L", "U'", "L'", "D", "D", "L'"])
    elif (binary_face & 0b00010110011010110000) == 0b00010110011010110000:
        print("Fig 7 with D'")
        instructions = convert_moves(["D'", "L", "L", "U", "L'", "D", "D", "L", "U'", "L'", "D", "D", "L'"])
    elif (binary_face & 0b00001101011001101000) == 0b00001101011001101000:
        print("Fig 7 with D")
        instructions = convert_moves(["D", "L", "L", "U", "L'", "D", "D", "L", "U'", "L'", "D", "D", "L'"])
    elif (binary_face & 0b10100100011001110000) == 0b10100100011001110000:
        print("Fig 7 with D2")
        instructions = convert_moves(["D", "D", "L", "L", "U", "L'", "D", "D", "L", "U'", "L'", "D", "D", "L'"])

    for i in instructions:
        action(i)()
    cube.print_cube()

def stock_PLL():
    binary_colors = [0, 0, 0, 0]
    all_colors = []
    all_colors.append(C5.get_color()[2])
    all_colors.append(A11.get_color()[0])
    all_colors.append(C4.get_color()[1])

    all_colors.append(C4.get_color()[2])
    all_colors.append(A6.get_color()[0])
    all_colors.append(C6.get_color()[1])

    all_colors.append(C6.get_color()[2])
    all_colors.append(A8.get_color()[0])
    all_colors.append(C7.get_color()[1])

    all_colors.append(C7.get_color()[2])
    all_colors.append(A10.get_color()[0])
    all_colors.append(C5.get_color()[1])



    for index, c in enumerate(all_colors):
        binary_colors[0] |= ((c == 'R')<<(len(all_colors) - index - 1))
    for index, c in enumerate(all_colors):
        binary_colors[1] |= ((c == 'G')<<(len(all_colors) - index - 1))
    for index, c in enumerate(all_colors):
        binary_colors[2] |= ((c == 'B')<<(len(all_colors) - index - 1))
    for index, c in enumerate(all_colors):
        binary_colors[3] |= ((c == 'O')<<(len(all_colors) - index - 1))
    return binary_colors

def turn_pll_binary(copy_all_pll_binary):
    tmp = 0
    for c_index,c in enumerate(copy_all_pll_binary):
#        print(c, ' ')
        for b_index, b in enumerate(c):
            if b_index == 0 or b_index == 5:
                continue
#            print(bin(b), ' ')
            tmp = b & 0b000000000111
            b = (b>>3) | (tmp<<9)
            copy_all_pll_binary[c_index][b_index] = b
#            print(bin(b), '\n')
#        print(c, '\n')
    return copy_all_pll_binary

def change_orientation(orientation, moves):
    directions = ["L", "L'", "F", "F'", "R", "R'", "B", "B'"]
    for index, m in enumerate(moves):
        if m in directions:
            match orientation:
                case 1:
                    moves[index] = directions[(directions.index(m) + 2) % 8]
                case 2:
                    moves[index] = directions[(directions.index(m) + 4) % 8]
                case 3:
                    moves[index] = directions[(directions.index(m) - 2) % 8]
    print("change orientation: ", moves)
    return moves

def PLL():
    binary_colors = stock_PLL()
    instructions = []
    print("R", bin(binary_colors[0]), binary_colors[0])
    print("G", bin(binary_colors[1]), binary_colors[1])
    print("B", bin(binary_colors[2]), binary_colors[2])
    print("O", bin(binary_colors[3]), binary_colors[3])
    copy_all_pll_binary = all_pll_binary
    print(copy_all_pll_binary, "\n")
    done = False
    for i in range(0,4):
        print(i)
        for pll in copy_all_pll_binary:
            if binary_colors[0] in pll and binary_colors[1] in pll and binary_colors[2] in pll and binary_colors[3] in pll:
                print("PLL: ",pll[0], pll[5], '\n')
#                match i:
#                    case 1:
#                        instructions = convert_moves(["D'"])
#                    case 2:
#                        instructions = convert_moves(["D", "D"])
#                    case 3:
#                        instructions = convert_moves(["D"])
                instructions = (convert_moves(change_orientation(i, pll[5])))
#                print("INSTRUCTIONS      : ", pll[5])
#                print("MODIF INSTRUCTIONS: ", change_orientation(i, pll[5]))
                for a in instructions:
                    action(a)()
                done = True
                break
        if done:
            break
        copy_all_pll_binay = turn_pll_binary(copy_all_pll_binary)

def last_rotary():
    binary_colors = stock_PLL()
    i = 0
    tmp = 0;
    while binary_colors[0] != 0b111000000000:
        i = i + 1
        tmp = binary_colors[0] & 0b000000000111
        binary_colors[0] = (binary_colors[0]>>3) | (tmp<<9)
    match i:
        case 1:
            action(10)()
        case 2:
            action(10)()
            action(10)()
        case 3:
            action(11)()
    print("i", i)

def resolve_yellow_face():
    # try with python3 main.py "F2 D2 L' F2 L D2 F D' F"
    first_step_two_look_oll()
    second_step_two_look_oll()
    PLL()
    last_rotary()
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
