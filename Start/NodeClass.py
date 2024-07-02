from Start.SortColors import aretes, coins

class Node():
    def __init__(self, color: str) -> None:
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

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color


    def setter(self, r=None, rprime=None, f=None, fprime=None, l=None, lprime=None, u=None, uprime=None, d=None, dprime=None, b=None, bprime=None, r2=None,f2=None,l2=None,u2=None,d2=None,b2=None):
        self.r = r
        self.rprime = rprime
        self.l = l
        self.lprime = lprime
        self.f = f
        self.fprime = fprime
        self.b = b
        self.bprime= bprime
        self.u = u
        self.uprime = uprime
        self.d = d
        self.dprime = dprime
    

    
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


A0 = Node(color=aretes[0])
A1 = Node(color=aretes[1])
A2 = Node(color=aretes[2])
A3 = Node(color=aretes[3])
A4 = Node(color=aretes[4])
A5 = Node(color=aretes[5])
A6 = Node(color=aretes[6])
A7 = Node(color=aretes[7])
A8 = Node(color=aretes[8])
A9 = Node(color=aretes[9])
A10 = Node(color=aretes[10])
A11 = Node(color=aretes[11])

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






C0 = Node(color=coins[0])
C1 = Node(color=coins[1])
C2 = Node(color=coins[2])
C3 = Node(color=coins[3])
C4 = Node(color=coins[4])
C5 = Node(color=coins[5])
C6 = Node(color=coins[6])
C7 = Node(color=coins[7])

C0.setter(u=C2, uprime=C1, l=C4, lprime=C2)
C1.setter(u=C0, uprime=C3, r=C3, rprime=C5)
C2.setter(u=C3, uprime=C1, l=C1, lprime=C6)
C3.setter(u=C1, uprime=C2, r=C7, rprime=C2)
C4.setter(d=C5, dprime=C6, l=C6, lprime=C1)
C5.setter(d=C7, dprime=C4, r=C1, rprime=C7)
C6.setter(d=C4, dprime=C7, l=C2, lprime=C4)
C7.setter(d=C6, dprime=C5, r=C5, rprime=C3)