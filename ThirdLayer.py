from NodeClass import Node, A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, C0, C1, C2, C3, C4, C5, C6, C7
from Functions import action
from CubeClass import cube
from pll import all_pll_binary

def set_binary_face() -> int:
    '''Stocks all yellow boxes in binary'''
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

def convert_moves(moves: list) -> list:
    '''Converts character movements to integer movements'''
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
    '''Make a cross on yellow face'''
    binary_face = set_binary_face()
    instructions = []

    #CROSS
    if (binary_face & 0b00000100011000100000) == 0b00000100011000100000:
        pass

    #POINT
    elif binary_face & 0b01000000100100000010 == 0b01000000100100000010:
        instructions = convert_moves(["F", "L", "D", "L'", "D'", "F'", "B", "D", "R", "D'", "R'", "B'"])

    #NORMAL LINE
    elif binary_face & 0b01000000011000000010 == 0b01000000011000000010:
        instructions = convert_moves(["F", "L", "D", "L'", "D'", "F'"])

    #VERTICAL LINE
    elif binary_face & 0b00000100100100100000 == 0b00000100100100100000:
        instructions = convert_moves(["D", "F", "L", "D", "L'", "D'", "F'"])

    #NORMAL L
    elif binary_face &  0b01000000101000100000 == 0b01000000101000100000:
        instructions = convert_moves(["B", "D", "R", "D'", "R'", "B'"]) 

    #DOWN LEFT L
    elif binary_face &  0b01000000010100100000 == 0b01000000010100100000:
        instructions = convert_moves(["D'", "B", "D", "R", "D'", "R'", "B'"]) 

    #UP RIGHT L
    elif (binary_face & 0b00000100010100000010) == 0b00000100010100000010:
        instructions = convert_moves(["D", "D", "B", "D", "R", "D'", "R'", "B'"]) 

    # UP LEFT L
    elif (binary_face & 0b00000100101000000010) == 0b00000100101000000010:
        instructions = convert_moves(["D", "B", "D", "R", "D'", "R'", "B'"]) 

    for i in instructions:
        action(i)()


def second_step_two_look_oll():
    '''Complete yellow face'''
    binary_face = set_binary_face()
    instructions = []
    #FIG 8
    if (binary_face & 0b00001110011001110000) == 0b00001110011001110000:
        pass

    #FIG 1
    elif (binary_face & 0b10000101011001100001) == 0b10000101011001100001:
        instructions = convert_moves(["L", "D", "L'", "D", "L", "D", "D", "L'"])
    #FIG 1 with D
    elif (binary_face & 0b10000101011010110000) == 0b10000101011010110000:
        instructions = convert_moves(["D", "L", "D", "L'", "D", "L", "D", "D", "L'"])
    #FIG 1 with D'
    elif (binary_face & 0b1101011010100001) == 0b1101011010100001:
        instructions = convert_moves(["D'", "L", "D", "L'", "D", "L", "D", "D", "L'"])
    #FIG 1 with D D
    elif (binary_face & 0b10000110011010100001) == 0b10000110011010100001:
        instructions = convert_moves(["D", "D", "L", "D", "L'", "D", "L", "D", "D", "L'"])

    #FIG 2
    elif (binary_face & 0b10110011000101100) == 0b10110011000101100:
        instructions = convert_moves(["L", "D", "D", "L'", "D'", "L", "D'", "L'"])
    #FIG 2 with D
    elif (binary_face & 0b101100011000101100) == 0b101100011000101100:
        instructions = convert_moves(["D", "L", "D", "D", "L'", "D'", "L", "D'", "L'"])
    #FIG 2 with D'
    elif (binary_face & 0b110100011000110100) == 0b110100011000110100:
        instructions = convert_moves(["D'", "L", "D", "D", "L'", "D'", "L", "D'", "L'"])
    #FIG 2 with D D
    elif (binary_face & 0b110100011001101000) == 0b110100011001101000:
        instructions = convert_moves(["D", "D", "L", "D", "D", "L'", "D'", "L", "D'", "L'"])

    #FIG 3
    elif (binary_face & 0b110100011010100001) == 0b110100011010100001:
        instructions = convert_moves(["L", "D", "D", "L", "L", "D'", "L", "L", "D'", "L", "L", "D", "D", "L"])
    #FIG 3 with D
    elif (binary_face & 0b10101011000100101) == 0b10101011000100101:
        instructions = convert_moves(["D", "L", "D", "D", "L", "L", "D'", "L", "L", "D'", "L", "L", "D", "D", "L"])
    #FIG 3 with D'
    elif (binary_face & 0b10100100011010101000) == 0b10100100011010101000:
        instructions = convert_moves(["D'", "L", "D", "D", "L", "L", "D'", "L", "L", "D'", "L", "L", "D", "D", "L"])
    #FIG 3 with D D
    elif (binary_face & 0b10000101011000101100) == 0b10000101011000101100:
        instructions = convert_moves(["D", "D", "L", "D", "D", "L", "L", "D'", "L", "L", "D'", "L", "L", "D", "D", "L"])

    #FIG 4
    elif (binary_face & 0b10100100011000100101) == 0b10100100011000100101:
        instructions = convert_moves(["F", "L", "D", "L'", "D'", "L", "D", "L'", "D'", "L", "D", "L'", "D'", "F'"])
    #FIG 4 with D
    elif (binary_face & 0b00010101011010101000) == 0b00010101011010101000:
        instructions = convert_moves(["D", "F", "L", "D", "L'", "D'", "L", "D", "L'", "D'", "L", "D", "L'", "D'", "F'"])

    #FIG 5
    elif(binary_face & 0b10000110011000110100) == 0b10000110011000110100:
        instructions = convert_moves(["R", "F", "L'", "F'", "R'", "F", "L", "F'"])
    #FIG 5 with D
    elif(binary_face & 0b00001110011010101000) == 0b00001110011010101000:
        instructions = convert_moves(["D", "R", "F", "L'", "F'", "R'", "F", "L", "F'"])
    #FIG 5 with D'
    elif(binary_face & 0b00010101011001110000) == 0b00010101011001110000:
        instructions = convert_moves(["D'", "R", "F", "L'", "F'", "R'", "F", "L", "F'"])
    #FIG 5 with D D
    elif(binary_face & 0b00101100011001100001) == 0b00101100011001100001:
        instructions = convert_moves(["D", "D", "R", "F", "L'", "F'", "R'", "F", "L", "F'"])

    #FIG 6
    elif(binary_face & 0b10110011001100001) == 0b10110011001100001:
        instructions = convert_moves(["F'", "R", "F", "L'", "F'", "R'", "F", "L"])
    #FIG 6 with D
    elif(binary_face & 0b1101011000110100) == 0b1101011000110100:
        instructions = convert_moves(["D", "F'", "R", "F", "L'", "F'", "R'", "F", "L"])
    #FIG 6 with D'
    elif(binary_face & 0b101100011010110000) == 0b101100011010110000:
        instructions = convert_moves(["D'", "F'", "R", "F", "L'", "F'", "R'", "F", "L"])
    #FIG 6 with D D
    elif(binary_face & 0b10000110011001101000) == 0b10000110011001101000:
        instructions = convert_moves(["D", "D", "F'", "R", "F", "L'", "F'", "R'", "F", "L"])

    #FIG 7
    elif (binary_face & 0b00001110011000100101) == 0b00001110011000100101:
        instructions = convert_moves(["L", "L", "U", "L'", "D", "D", "L", "U'", "L'", "D", "D", "L'"])
    #FIG 7 with D
    elif (binary_face & 0b00001101011001101000) == 0b00001101011001101000:
        instructions = convert_moves(["D", "L", "L", "U", "L'", "D", "D", "L", "U'", "L'", "D", "D", "L'"])
    #FIG 7 with D'
    elif (binary_face & 0b00010110011010110000) == 0b00010110011010110000:
        instructions = convert_moves(["D'", "L", "L", "U", "L'", "D", "D", "L", "U'", "L'", "D", "D", "L'"])
    #FIG 7 with D D
    elif (binary_face & 0b10100100011001110000) == 0b10100100011001110000:
        instructions = convert_moves(["D", "D", "L", "L", "U", "L'", "D", "D", "L", "U'", "L'", "D", "D", "L'"])

    for i in instructions:
        action(i)()

def stock_PLL() -> list:
    '''Stock all colored boxes in a binary'''
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

def turn_binary_colors(binary_colors: list) -> list:
    '''Right shift all binary_colors of 3 positions, stock the 3 "lost" bits at the beginning'''
    tmp = 0
    for index, b in enumerate(binary_colors):
        tmp = b & 0b000000000111
        binary_colors[index] = (b>>3) | (tmp<<9)
    return binary_colors

def change_orientation(orientation: int, moves: list) -> list:
    '''Modif moves depending of rotation (D / D ' / D D'''
    directions = ["L", "L'", "F", "F'", "R", "R'", "B", "B'"]
    for index, m in enumerate(moves):
        if m in directions:
            match orientation:
                case 1:
                    moves[index] = directions[(directions.index(m) - 2) % 8]
                case 2:
                    moves[index] = directions[(directions.index(m) + 4) % 8]
                case 3:
                    moves[index] = directions[(directions.index(m) + 2) % 8]
    return moves

def PLL():
    '''permute edges and corners
    all colors are stock in binary codes: 0b100000000011:    100
                                                            1   0
                                                            1   0
                                                            0   0
                                                             000
    check if the all binary colors match with all binary in the all_pll_binary's tab
    while it's false, it rotate all the binary colors: 0b100000000011 => 0b011100000000'''
    binary_colors = stock_PLL()
    instructions = []
    done = False
    for i in range(0,4):
        for pll in all_pll_binary:
            if binary_colors[0] in pll and binary_colors[1] in pll and binary_colors[2] in pll and binary_colors[3] in pll:
                instructions = (convert_moves(change_orientation(i, pll[5])))
                for a in instructions:
                    action(a)()
                done = True
                break
        if done:
            break
        binary_colors = turn_binary_colors(binary_colors)

def last_rotary():
    '''Makes movements to align the last layer with the good color'''
    binary_colors = stock_PLL()
    i = 0
    tmp = 0;
    while binary_colors[0] != 0b111000000000:
        i = i + 1
        tmp = binary_colors[0] & 0b000000000111
        binary_colors[0] = (binary_colors[0]>>3) | (tmp<<9)
    match i:
        case 1:
            action(10)() #D
        case 2:
            action(10)() #D
            action(10)() #D
        case 3:
            action(11)() #D'
 
def resolve_third_layer():
    # try with python3 main.py "F2 D2 L' F2 L D2 F D' F"
    first_step_two_look_oll()
    second_step_two_look_oll()
    PLL()
    last_rotary()
