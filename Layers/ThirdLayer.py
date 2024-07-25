from Start.NodeClass import Node, A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, C0, C1, C2, C3, C4, C5, C6, C7
from Utils.Functions import action
from Start.CubeClass import cube
from Utils.pll import all_pll_binary

 
def set_binary_face() -> int:
    '''Stocks all yellow boxes in binary'''
    binary_buffer = 0
    binary_buffer |= (0<<24)
    binary_buffer |= ((C5.get_color()[2] == 'Y')<<23)
    binary_buffer |= ((A11.get_color()[0] == 'Y')<<22)
    binary_buffer |= ((C4.get_color()[1] == 'Y')<<21)
    binary_buffer |= (0<<20)
    binary_buffer |= ((C5.get_color()[1] == 'Y')<<19)
    binary_buffer |= ((C5.get_color()[0] == 'Y')<<18)
    binary_buffer |= ((A11.get_color()[1] == 'Y')<<17)
    binary_buffer |= ((C4.get_color()[0] == 'Y')<<16)
    binary_buffer |= ((C4.get_color()[2] == 'Y')<<15)
    binary_buffer |= ((A10.get_color()[0] == 'Y')<<14)
    binary_buffer |= ((A10.get_color()[1] == 'Y')<<13)
    binary_buffer |= (0<<12)
    binary_buffer |= ((A6.get_color()[1] == 'Y')<<11)
    binary_buffer |= ((A6.get_color()[0] == 'Y')<<10)
    binary_buffer |= ((C7.get_color()[2] == 'Y')<<9)
    binary_buffer |= ((C7.get_color()[0] == 'Y')<<8)
    binary_buffer |= ((A8.get_color()[1] == 'Y')<<7)
    binary_buffer |= ((C6.get_color()[0] == 'Y')<<6)
    binary_buffer |= ((C6.get_color()[1] == 'Y')<<5)
    binary_buffer |= (0<<4)
    binary_buffer |= ((C7.get_color()[1] == 'Y')<<3)
    binary_buffer |= ((A8.get_color()[0] == 'Y')<<2)
    binary_buffer |= ((C6.get_color()[2] == 'Y')<<1)
    binary_buffer |= (0<<0)
    return binary_buffer

 
def convert_moves(moves: list) -> list:
    '''Converts movement characters into movement code'''
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

 
def rotate_oll(binary_face: list) -> list:
    '''Rotates the binary_face
    ex: 0b0001010100010100110100000 => 0b0001010100010100011001000

    00010      00010
    10100      10100
    01010  =>  01010
    01101      00110
    00000      01000

    '''
    new_binary = 0
    for i in range(0,25):
        new_binary |= (((binary_face & (1<<((((i + 1) * 5) - 1) % 26))) == (1<<((((i + 1) * 5) - 1) % 26)))<<i)
    return new_binary

 
def change_orientation(orientation: int, moves: list) -> list:
    '''Changes moves based rotation (D / D ' / D D'''
    directions = ["L","L'","F","F'","R","R'","B","B'"]
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

 
def first_step_two_look_oll():
    '''Make a cross on the yellow side'''
    binary_face = set_binary_face()
    instructions = []

    for i in range(0,4):
        #CROSS
        if (binary_face & 0b0000000100010100010000000) == 0b0000000100010100010000000:
            break

        #POINT
        elif binary_face & 0b0010000000100010000000100 == 0b0010000000100010000000100:
            instructions = convert_moves(change_orientation(4 - i, ["F","L","D","L'","D'","F'","B","D","R","D'","R'","B'"]))
            break

        #NORMAL LINE
        elif binary_face & 0b0010000000010100000000100 == 0b0010000000010100000000100:
            instructions = convert_moves(change_orientation(4 - i, ["F","L","D","L'","D'","F'"]))
            break

        #NORMAL L
        elif binary_face &  0b0010000000100100010000000 == 0b0010000000100100010000000:
            instructions = convert_moves(change_orientation(4 - i, ["B","D","R","D'","R'","B'"]))
            break
        binary_face = rotate_oll(binary_face)
    for i in instructions:
        action(i)()


def second_step_two_look_oll():
    '''Complete the yellow side'''
    binary_face = set_binary_face()
    instructions = []

    for i in range(0, 4):
        #FIG 8
        if (binary_face & 0b0000001110010100111000000) == 0b0000001110010100111000000:
            break

        #FIG 1
        elif (binary_face & 0b0100000101010100110000010) == 0b0100000101010100110000010:
            instructions = convert_moves(change_orientation(4 - i, ["L","D","L'","D","L","D","D","L'"]))
            break

        #FIG 2
        elif (binary_face & 0b0000010110010100010101000) == 0b0000010110010100010101000:
            instructions = convert_moves(change_orientation(4 - i, ["L","D","D","L'","D'","L","D'","L'"]))
            break

        #FIG 3
        elif (binary_face & 0b0001010100010101010000010) == 0b0001010100010101010000010:
            instructions = convert_moves(change_orientation(4 - i, ["L","D","D","L","L","D'","L","L","D'","L","L","D","D","L"]))
            break

        #FIG 4
        elif (binary_face & 0b0101000100010100010001010) == 0b0101000100010100010001010:
            instructions = convert_moves(change_orientation(4 - i, ["F","L","D","L'","D'","L","D","L'","D'","L","D","L'","D'","F'"]))
            break

        #FIG 5
        elif (binary_face & 0b0100000110010100011001000) == 0b0100000110010100011001000:
            instructions = convert_moves(change_orientation(4 - i, ["R","F","L'","F'","R'","F","L","F'"]))
            break

        #FIG 6
        elif (binary_face & 0b0000010110010100110000010) == 0b0000010110010100110000010:
            instructions = convert_moves(change_orientation(4 - i, ["F'","R","F","L'","F'","R'","F","L"]))
            break

        #FIG 7
        elif (binary_face & 0b0000001110010100010001010) == 0b0000001110010100010001010:
            instructions = convert_moves(change_orientation(4 - i, ["L","L","U","L'","D","D","L","U'","L'","D","D","L'"]))
            break
        binary_face = rotate_oll(binary_face)

    for i in instructions:
        action(i)()

 
def stock_PLL() -> list:
    '''Store all colored boxes in a binary'''
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
    '''Right shift all binary_colors by 3 positions, store the 3 "lost" bits at the beginning'''
    tmp = 0
    for index, b in enumerate(binary_colors):
        tmp = b & 0b000000000111
        binary_colors[index] = (b>>3) | (tmp<<9)
    return binary_colors

 
def PLL():
    '''Swaps edges and corners
    all colors are stored in binary codes: 0b100000000011:   100
                                                            1   0
                                                            1   0
                                                            0   0
                                                             000
    check if the binary colors match with all binary in the all_pll_binary's table
    as long as it's false, it rotates all binary colors: 0b100000000011 => 0b011100000000'''
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
    '''Make movements to align the last layer with the correct color'''
    binary_colors = stock_PLL()
    tmp = 0
    for i in range(0, 4):
        if binary_colors[0] == 0b111000000000:
            match i:
                case 1:
                    action(10)() #D
                case 2:
                    action(10)() #D
                    action(10)() #D
                case 3:
                    action(11)() #D'
        binary_color = turn_binary_colors(binary_colors)
 
 
def resolve_third_layer():
    first_step_two_look_oll()
    second_step_two_look_oll()
    PLL()
    last_rotary()
