from Start.NodeClass import Node, A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, C0, C1, C2, C3, C4, C5, C6, C7
from Utils.Functions import action
from Start.CubeClass import cube

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