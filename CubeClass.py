from SortColors import  milieux, coins #, aretes, coins
from NodeClass import A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11


class Cube():
    def __init__(self) -> None:   
        # self.coins = [C1, C2, C3, C4, C5, C6, C7]   
        self.coins = coins #remplacer
        self.aretes = [A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11] # aretes_list = A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12
        self.milieux = milieux # [M1, M2, M3, M4, M5]
        self.blocked_edges = []
        self.solution = ""
    
    def append(self, node):
        self.blocked_edges.append(node)
    
    def get_blocked_edges(self):
        return self.blocked_edges
    
    def get_color_coin(self, num_coin):
        return self.coins[num_coin]
    
    def set_color_coin(self, num_coin, color):
        self.coins[num_coin] = color
    
    def set_solution(self, lettre):
        self.solution += f"{lettre} "

   



    def print_cube(self):
        print(f"""

        {self.coins[4][2]} {self.aretes[11].get_color()[0]} {self.coins[5][1]} 
        {self.aretes[4].get_color()[1]} {self.milieux[4]} {self.aretes[9].get_color()[1]}  
        {self.coins[0][2]} {self.aretes[0].get_color()[1]} {self.coins[1][1]}

{self.coins[4][0]} {self.aretes[4].get_color()[0]} {self.coins[0][1]}   {self.coins[0][0]} {self.aretes[0].get_color()[0]} {self.coins[1][0]}   {self.coins[1][2]} {self.aretes[9].get_color()[0]} {self.coins[5][0]}   {self.coins[5][2]} {self.aretes[11].get_color()[1]} {self.coins[4][1]}
{self.aretes[6].get_color()[0]} {self.milieux[1]} {self.aretes[1].get_color()[1]}   {self.aretes[1].get_color()[0]} {self.milieux[0]} {self.aretes[2].get_color()[0]}   {self.aretes[2].get_color()[1]} {self.milieux[3]} {self.aretes[10].get_color()[0]}   {self.aretes[10].get_color()[1]} {self.milieux[5]} {self.aretes[6].get_color()[1]} 
{self.coins[6][0]} {self.aretes[5].get_color()[0]} {self.coins[2][2]}   {self.coins[2][0]} {self.aretes[3].get_color()[0]} {self.coins[3][0]}   {self.coins[3][1]} {self.aretes[7].get_color()[1]} {self.coins[7][0]}   {self.coins[7][1]} {self.aretes[8].get_color()[1]} {self.coins[6][1]} 

        {self.coins[2][1]} {self.aretes[3].get_color()[1]} {self.coins[3][2]}
        {self.aretes[5].get_color()[1]} {self.milieux[2]} {self.aretes[7].get_color()[0]} 
        {self.coins[6][2]} {self.aretes[8].get_color()[0]} {self.coins[7][2]}

""")
cube = Cube()