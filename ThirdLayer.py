from NodeClass import Node, A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, C0, C1, C2, C3, C4, C5, C6, C7
from Functions import action
from CubeClass import cube

def to_have_trait():
    print("procotocole")
    protocole_list = [4, 2, 10, 3, 11, 5] # f l d l' d' f'
    for p in protocole_list:
        action(p)()
    
def check_L():
    if A8.get_color()[1] == 'Y' and A10.get_color()[1] == 'Y':
        action(10)() #d
        to_have_trait()
    elif A11.get_color()[1] == 'Y' and A10.get_color()[1] == 'Y':
        to_have_trait()
    elif A8.get_color()[1] == 'Y' and A6.get_color()[1] == 'Y':
        action(10)() #d
        action(10)() #d
        to_have_trait()
    elif A11.get_color()[1] == 'Y' and A6.get_color()[1] == 'Y':
        action(11)() #d'
        to_have_trait()
    else:
        return False

    return True

def check_trait():
    if (A8.get_color()[1] == 'Y' and A10.get_color()[1] == 'Y') or\
        (A11.get_color()[1] == 'Y' and A10.get_color()[1] == 'Y') or\
        (A8.get_color()[1] == 'Y' and A6.get_color()[1] == 'Y') or\
        (A11.get_color()[1] == 'Y' and A6.get_color()[1] == 'Y'):
        return True
    return False