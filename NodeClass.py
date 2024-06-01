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
        # to_init = [
        #     self.r, self.f, self.l, self.u, self.d, self.b, self.rprime, self.fprime, self.lprime, self.dprime, self.uprime, self.bprime, self.r2, self.f2, self.l2, self.u2, self.d2, self.b2
        # ]
        # value_input = [
        #     r, f, l, u, d, b, rprime, fprime, lprime, dprime, uprime, bprime, r2, f2, l2, u2, d2, b2
        # ]
        # for i in range(0, len(value_input) - 1):
        #     to_init[i] = value_input[i]
        self.r = r
        self.f = f
        self.l = l
        self.u = u
        self.d = d
        self.b = b
        self.rprime = rprime
        self.fprime = fprime
        self.lprime = lprime
        self.dprime = dprime
        self.uprime = uprime
        self.bprime= bprime
        self.r2 = r2
        self.f2 = f2
        self.l2 = l2
        self.u2 = u2
        self.d2 = d2
        self.b2 = b2
    

    
    def _getter(self):
        dico = {}

        keys = [
            'r', 'f', 'l', 'u', 'd', 'b', 'rprime', 'fprime', 'lprime', 'dprime', 'uprime', 'bprime', 'r2', 'f2', 'l2', 'u2', 'd2', 'b2'
        ]

        list_attributs = [
            self.r, self.f, self.l, self.u, self.d, self.b, self.rprime, self.fprime, self.lprime, self.dprime, self.uprime, self.bprime, self.r2, self.f2, self.l2, self.u2, self.d2, self.b2
        ]

        for i in range(0, len(keys)):
            dico[i] = list_attributs[i]
        return dico



    #return le chemin le plus rapide
    def find_path(self, color: int, locked_edge): 
        print("\n")
        if self.get_color() in color:
            return None

        temp_node = [self]
        new_list = []
        dico_node = {}
        while True:
            print("💮💮💮 TEMP NODE",len(temp_node))
            
            for tmp in temp_node:
                dico_node[(tmp)] = []
                print("💮", tmp.get_color())
                new_list.clear()
                for k, v in tmp._getter().items():
                    if v:
                        new_list.append(v)
                        if v not in locked_edge: # contourner le noeud ?
                            dico_node[tmp].append((k, v))
                    if v and color in v.get_color() and v not in locked_edge:
                        print("✔️",k, v.get_color())
                        return dico_node
             
            if len(new_list) == 0:
                print("🚩None")
                break
            temp_node = new_list
        return {}



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



#premonition mouvement

A0.setter(u=A1, uprime=A2, u2=A3, b=A9, bprime=A4, b2=A11)
A1.setter(l=A5, lprime=A4, l2=A6, u=A3, uprime=A0, u2=A2)
A2.setter(r=A7, rprime=A9, r2=A10, u=A0, uprime=A3, u2=A1)
A3.setter(f=A4, fprime=A5, f2=A6, u=A2, uprime=A1, u2=A0)
A4.setter(l=A6, lprime=A1, l2=A5, b=A0, bprime=A11, b2=A9)
A5.setter(l=A1, lprime=A6, l2=A4, f=A8, fprime=A3, f2=A7)
A6.setter(l=A5, lprime=A4, l2=A1, d=A11, dprime=A8, d2=A10)
A7.setter(r=A10, rprime=A2, r2=A9, f=A3, fprime=A8, f2=A5)
A8.setter(d=A6, dprime=A10, d2=A11, f=A7, fprime=A6, f2=A3)
A9.setter(r=A2, rprime=A10, r2=A7, b=A11, bprime=A0, b2=A4)
A10.setter(r=A9, rprime=A7, r2=A2, d=A8, dprime=A11, d2=A6)
A11.setter(b=A4, bprime=A9, b2=A0, d=A10, dprime=A6, d2=A8)



