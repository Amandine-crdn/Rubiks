from SortColors import aretes, coins, milieux

class Node():
    def __init__(self, value: int, color: str) -> None:
        self.value = value
        self.color = color
        self.r = None
        self.f = None
        self.l = None
        self.u = None
        self.d = None
        self.b = None
        self.rprime = None
        self.fprime = None
        self.lprime = None
        self.uprime = None
        self.dprime = None
        self.bprime= None
        self.r2 = None
        self.f2 = None
        self.l2 = None
        self.u2 = None
        self.d2 = None
        self.b2 = None
        
      

    def get_value(self):
        return self.value

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color


    def setter(self, r=None, rprime=None, f=None, fprime=None, l=None, lprime=None, u=None, uprime=None, d=None, dprime=None, b=None, bprime=None, r2=None,f2=None,l2=None,u2=None,d2=None,b2=None):
        self.r = r
        self.rprime = rprime
        self.r2 = r2

        self.l = l
        self.lprime = lprime
        self.l2 = l2

        self.f = f
        self.fprime = fprime
        self.f2 = f2
        
        self.b = b
        self.bprime= bprime
        self.b2 = b2
        
        self.u = u
        self.uprime = uprime
        self.u2 = u2
        
        self.d = d
        self.dprime = dprime
        self.d2 = d2

    
    def _getter(self):

        list_tuple = []
        keys = [
            'r', 'rprime', 
            'l', 'lprime', 
            'f', 'fprime',
            'b', 'bprime',
            'u', 'uprime', 
            'd', 'dprime'
        ]

        list_attributs = [
            self.r, self.rprime, 
            self.l, self.lprime,
            self.f, self.fprime, 
            self.b, self.bprime, 
            self.u, self.uprime, 
            self.d, self.dprime
        ]

        for i in range(0, len(keys)):
            list_tuple.append((i, list_attributs[i]))

        return list_tuple


A0 = Node(value=0, color=aretes[0])
A1 = Node(value=1, color=aretes[1])
A2 = Node(value=2, color=aretes[2])
A3 = Node(value=3, color=aretes[3])
A4 = Node(value=4, color=aretes[4])
A5 = Node(value=5, color=aretes[5])
A6 = Node(value=6, color=aretes[6])
A7 = Node(value=7, color=aretes[7])
A8 = Node(value=8, color=aretes[8])
A9 = Node(value=9, color=aretes[9])
A10 = Node(value=10, color=aretes[10])
A11 = Node(value=11, color=aretes[11])

C0 = Node(value=0, color=coins[0])
C1 = Node(value=1, color=coins[1])
C2 = Node(value=2, color=coins[2])
C3 = Node(value=3, color=coins[3])
C4 = Node(value=4, color=coins[4])
C5 = Node(value=5, color=coins[5])
C6 = Node(value=6, color=coins[6])
C7 = Node(value=7, color=coins[7])

A0.setter(u=A1, uprime=A2, b=A9, bprime=A4)
A1.setter(l=A4, lprime=A5, u=A3, uprime=A0)
A2.setter(r=A7, rprime=A9,  u=A0, uprime=A3)
A3.setter(f=A5, fprime=A7,  u=A2, uprime=A1)
A4.setter(l=A6, lprime=A1,  b=A0, bprime=A11)
A5.setter(l=A1, lprime=A6,  f=A8, fprime=A3)
A6.setter(l=A5, lprime=A4,  d=A11, dprime=A8)
A7.setter(r=A10, rprime=A2,  f=A3, fprime=A8)
A8.setter(d=A6, dprime=A10, f=A7, fprime=A5)
A9.setter(r=A2, rprime=A10, b=A11, bprime=A0)
A10.setter(r=A9, rprime=A7, d=A8, dprime=A11)
A11.setter(b=A4, bprime=A9, d=A10, dprime=A6)